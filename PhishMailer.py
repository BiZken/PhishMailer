#!/usr/bin/env python3
#Created By BiZken

#Normal Import
import time
import os
import sys 

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
from Core.eletter import RiotGames
from Core.eletter import Steam
from Core.eletter import Gamehag
from Core.eletter import GmailActivity
from Core.eletter import SnapchatSimple
from Core.devicemenu import Linkedin
from Core.devicemenu import Dropbox
from Core.ipmenu import Discord
from Core.ipmenu import Paypal1
from Core.ipmenu import Snapchat

#EmailSender:
from Core.mailer import NormalEmail

red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")

os.system("clear")
print(green + """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~
 PhishMailer Version 1.2     .                     .              |
 Coded By BiZken             .                     .              |
 bizken@protonmail.com       .   /                  .  ___        |
          .                   . /--\ /                /   \       |
          .                    <o)  =<               /     \      J
          .                     \__/ \              (__O_O__)
 |  |    .                       \                    |||||
  \/        Y           )                             |||||
  |  /!-!\  |          (                           \_///| \\__/
   \|     |/            )                           _// |  \_
    _\___/_            (   (                         / /
   / /   \ \            )   )
^^^^^^^^^^^^^^^^\      (   (
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\                /^^
                                                   ^^^^^^^^^^^^^^^^ """)

time.sleep(0.5)
print(green + "[" + red + "!" + green + "]" + white + "More Versions Will Come Soon Stay Updated, Follow My Github\n")
print(white + "options:")
print(green + "[" + white + "1" + green + "]" + white + " Instagram" + green + "			[" + white + "11" + green + "]" + white + " Paypal")
print(green + "[" + white + "2" + green + "]" + white + " Facebook" + green + "			[" + white + "12" + green + "]" + white + " Discord")
print(green + "[" + white + "3" + green + "]" + white + " Gmail" + green + "			[" + white + "13" + green + "]" + white + " Spotify")
print(green + "[" + white + "4" + green + "]" + white + " Gmail (simple)" + green + "		[" + white + "14" + green + "]" + white + " Blockchain")
print(green + "[" + white + "5" + green + "]" + white + " Twitter" + green + "			[" + white + "15" + green + "]" + white + " RiotGames")
print(green + "[" + white + "6" + green + "]" + white + " Snapchat" + green + "			[" + white + "16" + green + "]" + white + " Rockstar")
print(green + "[" + white + "7" + green + "]" + white + " Snapchat (simple)" + green + "		[" + white + "17" + green + "]" + white + " AskFM")
print(green + "[" + white + "8" + green + "]" + white + " Steam" + green + "			[" + white + "18" + green + "]" + white + " 000Webhost")
print(green + "[" + white + "9" + green + "]" + white + " Dropbox" + green + "			[" + white + "19" + green + "]" + white + " Dreamteam")
print(green + "[" + white + "10" + green + "]" + white + " Linkedin" + green + "			[" + white + "20" + green + "]" + white + " Gamehag")
print(green + "-----------------------------------------------------------------------")
print(green + "[" + white + "30" + green + "]" + white + " Send Phishing Email")
print(green + "[" + white + "99" + green + "]" + red + " EXIT")
print(green + "[" + white + "1337" + green + "]" + white + " Info\n")

print(green)
mailPick = int(input("root@phishmailer:~ " + white))

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
	Paypal1()
	
elif mailPick == 12:
	Discord()
	
elif mailPick == 13:
	Spotify()
	
elif mailPick == 14:
	Blockchain()
	
elif mailPick == 15:
	RiotGames()
	
elif mailPick == 16:
	Rockstar()
	
elif mailPick == 17:
	AskFM()

elif mailPick == 18:
	Webhost000()

elif mailPick == 19:
	Dreamteam()
	
elif mailPick == 20:
	Gamehag()

elif mailPick == 30:
	NormalEmail()

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
	print(green + "[" + white + "+" + green + "]" + white + " Wickr: BiZken")
	print(green + "[" + white + "+" + green + "]" + white + " Email: bizken@protonmail.com")
	print(green + "[" + white + "+" + green + "]" + white + " Github: BiZken [https://github.com/BiZken]")
	
else:
	print("\nSomething Went Wrong There Partner")
	print("Are You Ok? Did You Fell Out The Boat And Started Drowning?")
	sys.exit()
