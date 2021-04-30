# cowin-tracker
Open Source Script that can be run on a CRON job so that you can be updated by email of any changes to the Cowin Vaccination Portal 

# How to Run
Install requests from PyPi into your dev env.\
Clone this repository and take the cowin-tracker.py file \
Go to your gmail account and create an App Password if you have Two Factor Authentication (Which you should by the way). \
Create a new file called creds.py into the same directory as cowin-tracker.py script and add two variables in it :\
emails = 'yourEmailHere'\
pws = 'theGoogleGeneratedPasswordHere'\
Tip: Use the code that has been commented out in the script if you do not know what your state_id is \
> Replace the state_id parameter value in the Parameters Dictionary to change the script to run for your particular state.\

![image](https://user-images.githubusercontent.com/37734939/116748223-beb0dc00-aa1c-11eb-8ee1-326d280a15c4.png)
