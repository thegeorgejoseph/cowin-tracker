# cowin-tracker
Open Source Script to run a CRON job on so that you are updated by email of any changes to the Cowin Vaccination Portal 

# How to Run
Install requests from PyPi into your dev env.\
Clone this repository and take the cowin-tracker.py file \n
Go to your gmail account and create an App Password if you have Two Factor Authentication (Which you should by the way). \n
Create a new file called creds.py into the same directory as cowin-tracker.py script and add two variables in it :\n
emails = 'yourEmailHere'\n
pws = 'theGoogleGeneratedPasswordHere'\n
Tip: Use the code that has been commented out in the script if you do not know what your state_id is \n
> Replace the state_id parameter value in the Parameters Dictionary to change the script to run for your particular state.\n

