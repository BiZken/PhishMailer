import smtplib
import os
import getpass
import sys
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email import encoders  
from email.mime.text import MIMEText

red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")

start = (green + "[" + white + "+" + green + "]" + white)
alert = (green + "[" + red + "!" + green + "]" + white)

def NormalEmail():
	os.system("clear")
	print(green)
	print("""
 __^__                                                        __^__
( ___ )------------------------------------------------------( ___ )
 | / |                                                        | \ |
 | / |+-------------)PhishMailer BaitMailer V1(--------------+| \ |
 |___|                                                        |___|
(_____)------------------------------------------------------(_____) """)

	print(alert + "It Mitht Take A Few Minutes Until The Target Gets The Email" + alert)
	print(alert + "You Need To Allow Less Secure Apps On You Gmail Account" + alert)
	
	print("")
	fromaddr = input(start + "Enter Your Email-Address: ")
	password = getpass.getpass(start + "Enter Your Password (will not be shown): ")
	toaddr = input(start + "Enter Email-Address To Send To: ")
	subject = input(start + "Enter Subject: ")
	pathfile = input(start + "Enter Path To Html File: ")

	html = open(pathfile)
	msg = MIMEText(html.read(), 'html')
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject

	debug = False
	if debug:
		print(msg.as_string())
	else:
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(fromaddr, password)
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		print(alert + "Email Sent" + alert)




