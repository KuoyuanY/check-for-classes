# check-for-classes
Script that checks if a class opens up on Testudo.umd.edu. <br />
When a seat is open, script will text phone

### Description
This script works for Testudo.umd.edu only.
The file parse2.py is for python 2 <br />
The file parse.py is for python 3

### Set up 
Get a free twilio account at https://www.twilio.com/try-twilio<br />
Put your account sid, auth token, twilio number(given from creating your account), and the phone number to receive the message 
```Python
Account_SID = ""
Auth_TOKEN = ""
myTwilioNumber = ""
myNumber = ""
```
Replace url with the url of your desired class
```Python
url = "PUT YOUR URL IN HERE"
```
Before running, make sure to install twilio module
```
$ pip install twilio
```
Run the script now locally 
```
$ python parse2.py
```
Or if you have python 3
```
$ python3 parse.py
```
If you want to run it online, go to heroku or use Amazon Web Service EC2.
