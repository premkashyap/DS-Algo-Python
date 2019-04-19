import urllib.request 
from bs4 import BeautifulSoup
import smtplib
import time
import datetime

venue_code ='AMBH' #this can be found by inspecting the element data-id for the venue where you would like to watch
date = '20190426'
venue_name = 'amb-cinemas-gachibowli'
show_ids = ['ET00100559', 'ET00090482']
delay=300 #timegap in seconds between 2 script runs

TO = 'kashyap18.prem@gmail.com' #mail id for which you want to get alerted
# Please add your username and password here, and make sure you 
# toggle allow less secure apps to on 
# https://myaccount.google.com/lesssecureapps?pli=1 
GMAIL_USER = 'alerts.premkashyap@gmail.com'
GMAIL_PASS = 'Alerts.887'
SUBJECT = 'Tickets are now available, Book fast'
TEXT = 'The tickets are now available for the End Game show at the venue ' + venue_code

def send_email(username, password, subject, text, to):
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(username, password)
    header = 'To:' + to + '\n' + 'From: ' + username
    header = header + '\n' + 'Subject:' + subject + '\n'
    print(header)
    msg = header + '\n' + text + ' \n\n'
    smtpserver.sendmail(username, to, msg)
    smtpserver.close()

def is_show_available(venue_name, venue_code, date, show_id):
    req = urllib.request.Request(f"https://in.bookmyshow.com/buytickets/{venue_name}/cinema-hyd-{venue_code}-MT/{date}")
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page)
    return any(show_id in str(soup) for show_id in show_ids)

count = 0
while True:
    if is_show_available(venue_name, venue_code, date, show_ids):
        print("Available")
        if count < 10:
            send_email(GMAIL_USER, GMAIL_PASS, SUBJECT, TEXT, TO)
            count+=1
        else:
            exit(0)
    else :
        print(f"Not available yet")
    time.sleep(delay)
