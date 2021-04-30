'''
Creating a simple script to track changes in the Cowin Portal and send you an email when there is a slot available

'''

import requests

#Hitting the COWIN Public API  
res  = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?header=hi_IN&pincode=412307&date=01-05-2021")
