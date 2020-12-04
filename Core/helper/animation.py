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
		print(white + " PhishMailer Version 1.5     .                     .              |")
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


		lines = [green + " PhishMailer 1.5 New Update!",
				white + " For Those Who Are New To PhishMailer I Just Want To Say Welcome! \n", 
				alert + " Quick Info About The New Update:",
				start + " Added & Changed Some Thing In The Mailer Section \n",
				start + " For Every New Update That Comes You Will See This Print Out With Info But You Will Only See It Ones \n",
				"    When You Run PhishMailer For The First Time",
				start + " Added A Spam-Filter Bypass Method (read more under the redirection option in the main menu option 69)",
				start + " Changed The Code A Bit",
				start + " If You Read This That Means That I Have Not Published The Wiki Yet With The Tutorials On How To Use PhishMailer",
				"    It Will Come Really Soon, I Just Need To Finish It First",
				start + " If You Have Any Questions I'm Most Active On Instagram: bizk3n, Send A Dm If You Want To Know Anything Or If You Have Any Ideas",
				start + " Happy Phishing -BiZken"]
				
		for line in lines:         
			for c in line:          
				print(c, end='')    
				sys.stdout.flush()  
				time.sleep(0.07)          
			print('') 


