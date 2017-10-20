# snapcam
Python script for automatic detecting a failed logon (Event ID 4625) and then take a photo from webcam and send it by email.

Use the XML to add an scheduled task in Windows, which will launch the snapcam.py (renemae to .pyw!).
Snapcam.py will take a photo through the webcam of your laptop and send it through email to the designated email address.

Steps to setup:

- edit snapcam.py to your likings for email configurtation
- rename to .pyw to execute hidden
- import a scheduled task via the XML file
- adjust scheduled task to you're likings

Test by locking (Win+L) and enter a wrong password for your account. 
- on screen you should receive a message
- and en email with a photo should be received

Unfortunately sometimes the event also arises at undesignated times and you'll still get the email and the on screen message. 

Always investigate!
