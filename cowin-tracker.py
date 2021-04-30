#Importing the required libraries
import requests

#Setting up the parameters that need to be passed
parameters = {
    "header":"hi_IN",
    "pincode":"412307",
    "date":"01-05-2021"
}
#Hitting the COWIN Public API  
res  = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin",params=parameters)

print(res.status_code)

