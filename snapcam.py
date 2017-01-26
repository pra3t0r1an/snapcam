'''
	This script will take snapshot with your webcam and send it to the specified email adres.

	The script is tested on Python 2.7....you'll need the pygame module. It worked with the 1.9.1 version
	get it here : http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi

	After that and put the python 2.7 in to your path you'll be able to schedule it on an failed logon event in Windows 10:

	Import from XML file or if you want to create manually:

	Event ID : 4625
	Source 	 : Microsoft-Windows-Security-Auditing
	Keywords : Audit Failure
	User account : SYSTEM
	Run wether user logged on or not.

	Change the needed email adres for sending and receiving and path in the xml when make use of import.
'''
import argparse
import os
import sys
import time
import subprocess
import csv
import smtplib
import datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import atexit
import pygame
import pygame.camera
from pygame.locals import *
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
pygame.camera.init()
cam = pygame.camera.Camera(0,(640,480),"RGB")
cam.start()
img = pygame.Surface((640,480))
cam.get_image(img)
pygame.image.save(img, "cam" + timestr + ".jpg")
cam.stop()

def sendMail(tekst, snapcamFile):
    '''
            sendMail sends the screenshots of results.csv domains
	    to your selected address using a given address.

            Specify your sending account username in mail_user.
            Specify your account password in mail_pwd.

            Configure for your mail server by modifying the
            mailServer = line.

            This assumes your mail server supports starttls.
            Future versions will allow you to specify whether
            or not to use starttls. To suppress starttls,
            remove the line mailServer.starttls().
    '''

    mail_user = "sendingaccount@gmail.com"
    mail_pwd = "some password"
    mail_recip = ["you own account@whatever.com"]

    def mail(to, subject, text, snapcamFile, numResults):
        msg = MIMEMultipart()

        msg['From'] = mail_user
        msg['To'] = ", ".join(to)
        msg['Subject'] = subject

        msg.attach(MIMEText(text))

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(snapcamFile, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
              'attachment; filename="%s"' % os.path.basename(screenshotFile))
        msg.attach(part)

        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(mail_user, mail_pwd)
        mailServer.sendmail(mail_user, to, msg.as_string())
        mailServer.close()
    
    mail(mail_recip,
         "NEW Laptop intruder alarm!", # subject line
         tekst ,
         snapcamFile, 1)


sendMail ('Look! we have an intruder', "cam" + timestr + ".jpg")