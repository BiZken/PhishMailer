#!/usr/bin/env python3
#Created By BiZken

#Normal Import
import time
import os
import sys
import json
import requests
from sys import version_info

if version_info<(3,0,0):
    print('[!] Please use Python 3. $ python3 PhishMailer.py')
    sys.exit()

#emails:
from Core.eletter import Instagram
from Core.eletter import Facebook
from Core.eletter import Gmail
from Core.eletter import Twitter
from Core.eletter import AskFM
from Core.eletter import Webhost000
from Core.eletter import Blockchain
from Core.eletter import Spotify
from Core.eletter import Rockstar
from Core.eletter import Dreamteam
from Core.eletter import Mega
from Core.eletter import RiotGames
from Core.eletter import Steam
from Core.eletter import Gamehag
from Core.eletter import GmailActivity
from Core.eletter import SnapchatSimple
from Core.eletter import Playstation
from Core.devicemenu import Linkedin
from Core.devicemenu import Dropbox
from Core.ipmenu import Discord
from Core.ipmenu import Paypal1
from Core.ipmenu import Snapchat
from Core.pre import *
from Core.helper.RedirectBypass import *
from Core.anotherLang import *
#EmailSender:
from Core.Mailer.MailerMain import *
from Core.helper.ToDo import TODO

red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")

os.system("clear")

def CurrentDir():
	path = os.getcwd()
	print(green + "[" + white + "+" + green + "]" + white + " Your Templates Will Be Saved Here " + path + '/"TemplateName.html"')


def mainMenu():
	menu()

	print(green)
	
	CurrentDir()
	
	mailPick = int(input(green + "root@phishmailer:~ " + white))

	try:

            if mailPick == 1:
                    Instagram()

            elif mailPick == 2:
                    Facebook()

            elif mailPick == 3:
                    Gmail()

            elif mailPick == 4:
                    GmailActivity()

            elif mailPick == 5:
                    Twitter()

            elif mailPick == 6:
                    Snapchat()

            elif mailPick == 7:
                    SnapchatSimple()

            elif mailPick == 8:
                    Steam()

            elif mailPick == 9:
                    Dropbox()

            elif mailPick == 10:
                    Linkedin()

            elif mailPick == 11:
                    Playstation()

            elif mailPick == 12:
                    Paypal1()

            elif mailPick == 13:
                    Discord()

            elif mailPick == 14:
                    Spotify()

            elif mailPick == 15:
                    Blockchain()

            elif mailPick == 16:
                    RiotGames()

            elif mailPick == 17:
                    Rockstar()

            elif mailPick == 18:
                    AskFM()

            elif mailPick == 19:
                    Webhost000()

            elif mailPick == 20:
                    Dreamteam()

            elif mailPick == 21:
                    print("Gamehag Coming Soon")

            elif mailPick == 22:
                    Mega()

            elif mailPick == 30:
                    MailerMenu()

            elif mailPick == 69:
                    RedirectionMain()

            elif mailPick == 80:
                    Languages()

            elif mailPick == 99:
                    os.system("clear")
                    print("Hope I See You Soon")
                    print("Happy Phishing")
                    sys.exit()

            elif mailPick == 1337:
                    print("\n" + green + "[" + white + "+" + green + "]" + white + " This Tool Was Created So People Would Have It Easier To Launch Phishing Attacks")
                    print("\n" + green + "[" + white + "+" + green + "]" + white + " I Do Not Take Any Responsibility For Your Actions")
                    print("\n" + green + "[" + white + "+" + green + "]" + white + " But I Don't Give A F*ck About What You Do")
                    print("\n" + green + "[" + white + "+" + green + "]" + white + " More Emails Will Come Soon!")
                    print("\n" + green + "[" + white + "+" + green + "]" + white + " Contact:")
                    print(green + "[" + white + "+" + green + "]" + white + " Instagram: BiZk3n (most Active)")
                    print(green + "[" + white + "+" + green + "]" + white + " Github: BiZken [https://github.com/BiZken]")
                    CurrentDir()
                    print(green + "[" + white + "+" + green + "]" + white + " Restart PhishMailer? Y/N")

                    ReRun = input("root@phishmailer:~ " + white)
                    if ReRun == "Y" or ReRun == "y":
                            os.system("clear")
                            mainMenu()
                    else:
                            os.system("clear")
                            print(alert + " shuting Down")

            elif mailPick == 4444:
                    TODO()
                    print(start + " Restart PhishMailer? Y/N")
                    restart = input("root@phishmailer:~ " + white)
                    if restart == "Y" or restart == "y":
                            os.system("clear")
                            mainMenu()
                    else:
                            print(alert + " shuting Down")
                            sys.exit()

            else:
                    print("\nSomething Went Wrong There Partner")
                    print("Are You Ok? Did You Fell Out The Boat And Started Drowning?")
                    sys.exit()
                    
	except ValueError:
		print("\nSomething Went Wrong There Partner")
		print("Are You Ok? Did You Fell Out The Boat And Started Drowning?")
		sys.exit()

mainMenu()
