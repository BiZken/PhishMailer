import time 
import sys
import os

red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")
yellow = ("\033[1;33;40m")
start = (green + "[" + white + "+" + green + "]" + white)
alert = (green + "[" + red + "!" + green + "]" + white)
question = (green + "[" + yellow + "?" + green + "]" + white)


def AnimationMain():
	SeenCheck = open("Core/IntroSeen.txt", "r")
	Check = SeenCheck.read()
	SeenCheck.close()
	if "Yes" in Check:
		pass
	else:
		os.system("clear")
		IntroSeen = open("Core/IntroSeen.txt", "w+")
		IntroSeen.write("Yes")
		IntroSeen.close()

		print(blue + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + white + "|" + blue + "~~~")
		time.sleep(0.1)
		print(white + " PhishMailer Version 2.2     .                     .              |")
		time.sleep(0.1)
		print(" Instagram: bizk3n           .                     .              |")
		time.sleep(0.1)
		print(" bizken@protonmail.com        . " + green + " /                " + white + " .  " + blue + " ___ " + white + "       |")
		time.sleep(0.1)
		print(green + "                              . /--\ /     " + blue + "           /   \ " + white + "      |")
		time.sleep(0.1)
		print("           ." + green + "                   <o)  =< " + blue + "              /     \    " + red + "  J")
		time.sleep(0.1)
		print(white + "          .                     " + green + "\__/ \ " + blue + "             (__O_O__)")
		time.sleep(0.1)
		print(yellow + "  |  |" + white + "    ." + green + "                        \ " + blue + "                 |||||")
		time.sleep(0.1)
		print(yellow + "   \/        Y " + green + "         ) " + blue + "                            |||||")
		time.sleep(0.1)
		print(yellow + "   |  /!-!\  | " + green + "        ( " + blue + "                          \_///| \\__/")
		time.sleep(0.1)
		print(yellow + "    \|     |/  " + green + "         ) " + blue + "                          _// |  \_")
		time.sleep(0.1)
		print(yellow + "     _\___/_ " + green + "           (   ( " + blue + "                         / /")
		time.sleep(0.1)
		print(yellow + "    / /   \ \ " + green + "           )   ) ")
		time.sleep(0.1)
		print(white + "^^^^^^^^^^^^^^^^\ " + green + "      (   ( ")
		time.sleep(0.1)
		print(white + "                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\                /^^")
		time.sleep(0.1)
		print("                                                   ^^^^^^^^^^^^^^^^ ")


		lines = [green + " PhishMailer 2.2 New Major Update!",
				white + " For Those Who Are New To PhishMailer I Just Want To Say Welcome! \n", 
				alert + " Quick Info About The New Update:",
				start + " For Every New Update That Comes You Will See This Print Out With Info But You Will Only See It Ones",
				"    When You Run PhishMailer For The First Time \n",
				start + " Working On Video Tutorials On How To Use PhishMailer \n",
				start + " But The Wiki Is Up On Github \n",
				alert + " You Can Now Create Soem Emails With 3 New Languages \n",
				"    It Will Come Really Soon, I Just Need To Finish It First \n",
				question + " What's Coming In The Next Update? \n",
				start + " Right Now Im Working On SMTP So That The Phishing Attacks Looks More Legit, like spoofing",
				start + " Add More Templates (DM for Ideas And I Can See What I Can Do) \n",
				start + " Create Mass-Sender And Templates For That \n",
				alert + " More Will Come For Each Update! \n",
				start + " If You Have Any Questions I'm Most Active On Instagram: bizk3n, Send A Dm If You Want To Know Anything Or If You Have Any Ideas\n",
				start + " Happy Phishing -BiZken"]
				
		for line in lines:         
			for c in line:          
				print(c, end='')    
				sys.stdout.flush()  
				time.sleep(0.05)          
			print('') 





