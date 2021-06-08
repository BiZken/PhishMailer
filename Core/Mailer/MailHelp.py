import os
import sys
import time
red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")
start = (green + "[" + white + "+" + green + "]" + white)
alert = (green + "[" + red + "!" + green + "]" + white)

def AskPerm():
	print(alert + "I'm Trying To See How Many Emails That Gets Sent With PhishMailer")
	print(alert + "Is It Okay For You That PhishMailer Sends Me An Email Saying That An Email Has Been Sent?")
	print(alert + "You Will Not Be Asked This Again!")
	print(alert + 'And No Info Will Be Sent About You Just "Email Sent with PhishMailer"')
	print(alert + "Y or N")
	Ask = input(green + "root@phishmailer/Mailer/Permission:~ " + white)
	
	if Ask == "Y" or Ask == "yes":
		Permission = open("Permission.txt", "w+")
		Permission.write("Yes")
		Permission.close()
		os.system("clear")
	
	elif Ask == "N" or Ask == "no":
		NoPerm = open("Permission.txt", "w+")
		NoPerm.write("No")
		NoPerm.close()
		os.system("clear")
		
	else:
		while True:
			os.system("clear")
			print("")
			print(alert + "Something Went Wrong, Try Again...")
			AskPerm()

def CheckPerm():
	PermCheck = open("Permission.txt", "r")
	Check = PermCheck.read()
	PermCheck.close()
	if "Yes" in Check:
		os.system("clear")
	elif "No" in Check:
		os.system("clear")
	else:
		AskPerm()
