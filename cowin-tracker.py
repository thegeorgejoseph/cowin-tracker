#Importing the required libraries
import requests
import json
import smtplib
import os
from creds import emails,pws

#Code that can be used to generate the State ID's
# for i in range(1,40):
#     res  = requests.get(f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{i}")

#     print(res.status_code)

#     jprint(res.json())

# For our purposes. state_id = 17 is what we want to generate the 


#Setting up the parameters that need to be passed
parameters = {
    "header":"hi_IN",
    "date":"01-05-2021",
    "district_id":"108",

}


#Hitting the COWIN Public API  
res  = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict",params=parameters)

if res.status_code == 200:
    data = res.json()
    result_obj = {}
    key=0
    for obj in data['centers']:
        name = obj["name"]
        district_name = obj["district_name"]
        block_name = obj["block_name"]
        pincode = obj["pincode"]
        sessions = []
        for i in range(len(obj["sessions"])):
            sessions.append(obj["sessions"][i]["date"])
            sessions.append(obj["sessions"][i]["available_capacity"])
            sessions.append(obj["sessions"][i]["vaccine"])
        result_obj[key] = {"name" : name,"district_name" : district_name,"block_name" : block_name, "pincode" : pincode, "date_availability_vaccine-brand" : sessions}
        key = key + 1

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(emails,pws)
        subject = 'YOU HAVE AN UPDATE FROM COWIN TRACKER'
        body = ''
        for k,v in result_obj.items():
            body = body + json.dumps(v,indent=3) + '\n'
        msg = f"Subject:{subject}\n\n\n{body}"

        if result_obj:
            smtp.sendmail(emails,emails,msg) #Sender,Receiver,Message
else:
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(emails,pws)
        subject = 'COWIN TRACKER CRASHED'
        body = 'There was an error with accessing the API'
        msg = f"Subject:{subject}\n\n\n{body}"

        if result_obj:
            smtp.sendmail(emails,emails,msg) 

