from twilio.rest import Client
import urllib.request
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
sections = {'0': '2'} #dictionary of sections


print("started running")

#regex to find all sections
while keepRunning:
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode("utf8")

    counter = 1

    for m in re.finditer('<span class="total-seats-count">', html): #finds all occurrences
        sections[counter] = html[m.end()+1] #put in dictionary
        counter+=1

    for k, v in sections.items():
        print time.asctime(time.localtime(time.time())) #prints current time
        print("section " + str(k) + ": " + str(v)) #prints each section
        if not v == '2':
            notify("a seated opened up in section " + str(k))
            keepRunning = False #stops the bot from running


    time.sleep(60)#checks for open seats every 30 seconds
    print("It's been a minute")
    currentTime = round(time.clock())
    if currentTime-initialTime >= 14400: #messages the user that bot is still running after every 4 hours
        initialTime = round(time.clock())
        notify("It's been 4 hours, bot is still checking for seats")
notify("The script ended")
