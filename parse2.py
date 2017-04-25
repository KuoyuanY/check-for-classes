from twilio.rest import Client
import urllib2
import re
import time

Account_SID = ""
Auth_TOKEN = ""
myTwilioNumber = ""
myNumber = ""
initialTime = round(time.clock())
keepRunning = True

print("started running")
def notify(message): #texts me with message
    client = Client(Account_SID, Auth_TOKEN)
    client.messages.create(
        to= myNumber,
        from_ = myTwilioNumber,
        body=message
    )

url = "https://ntst.umd.edu/soc/search?courseId=HIST289y&sectionId=&termId=201708&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"
sections = {'0': '0'} #dictionary of sections

response = urllib2.urlopen(url)
html = response.read()
html = html.decode("utf8")

#regex to find all sections
while keepRunning:
    currentTime = round(time.clock())
    counter = 1

    for m in re.finditer('<span class="open-seats-count">', html): #finds all occurrences
        sections[counter] = html[m.end()] #put in dictionary
        counter+=1

    for k, v in sections.items():
        if not v == '0':
            notify("a seated opened up!")
            keepRunning = False #stops the bot from running

    print("after a minute, ")
    time.sleep(60)#checks for open seats every 30 seconds
    if currentTime-initialTime > 14400: #messages the user that bot is still running after every 6 hours
        initialTime = round(time.clock())
        notify("It's been 4 hours, bot is still checking for seats")
notify("If you didn't get a message saying a seat opened up, the bot quit unexpectedly, contact Kuoyuan")
