#Importing the required libraries
import requests
import json

#Function that converts json object in Human Readable Form
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Setting up the parameters that need to be passed
parameters = {
    "header":"hi_IN",
    # "pincode":"412307",
    "date":"01-05-2021",
    "district_id":"17", #683

}

#Code that can be used to generate the State ID's
# for i in range(1,40):
#     res  = requests.get(f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{i}")

#     print(res.status_code)

#     jprint(res.json())

# For our purposes. state_id = 17 is what we want to generate the 

#Hitting the COWIN Public API  
res  = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict",params=parameters)

print(res.status_code)

jprint(res.json())