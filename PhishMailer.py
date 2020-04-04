import time
import os
import sys 
#emails:
from Core.eletter import Instagram
from Core.eletter import facebook
from Core.eletter import Gmail
from Core.eletter import Twitter
from Core.eletter import Paypal1

#EmailSender:
from Core.mailer import NormalEmail

red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")

os.system("clear")
print(green + """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~
 PhishMailer Version 1.0     .                     .              |
 BiZken                      .                     .              |
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
print(green + "[" + white + "1" + green + "]" + white + " Instagram")
print(green + "[" + white + "2" + green + "]" + white + " Gmail")
print(green + "[" + white + "3" + green + "]" + white + " facebook")
print(green + "[" + white + "4" + green + "]" + white + " Twitter")
print(green + "[" + white + "5" + green + "]" + white + " Paypal")
print(green + "[" + white + "6" + green + "]" + white + " Send Phishing Email")
print(green + "[" + white + "99" + green + "]" + red + " EXIT")
print(green + "[" + white + "1337" + green + "]" + white + " Info\n")

print(green)
mailPick = int(input("root@phishmailer:~ " + white))

if mailPick == 1:
	Instagram()

elif mailPick == 2:
	Gmail()
	
elif mailPick == 3:
	facebook()

elif mailPick == 4:
	Twitter()

elif mailPick == 5:
	Paypal1()

elif mailPick == 6:
	NormalEmail()
	
elif mailPick == 99:
	os.system("clear")
	print("Hope I See You Soon")
	print("Happy Phishing")
	sys.exit()

elif mailPick == 1337:
	print("\n" + green + "[" + white + "+" + green + "]" + white + "This Tool Was Created So People Would Have It Easier To Launch Phishing Attacks")
	print("\n" + green + "[" + white + "+" + green + "]" + white + "I Do Not Take Any Responsibility For Your Actions")
	print("\n" + green + "[" + white + "+" + green + "]" + white + "But I Don't Give A F*ck About What You Do")
	print("\n" + green + "[" + white + "+" + green + "]" + white + "More Emails Will Come Soon!")
	print("\n" + green + "[" + white + "+" + green + "]" + white + "Contact:")
	print(green + "[" + white + "+" + green + "]" + white + "Wickr: BiZken")
	print(green + "[" + white + "+" + green + "]" + white + "Email: bizken@protonmail.com")
	print(green + "[" + white + "+" + green + "]" + white + "Github: BiZken [https://github.com/BiZken]")
	
else:
	print("\nSomething Went Wrong There Partner")
	print("Are You Ok? Did You Fell Out The Boat And Started Drowning?")
	sys.exit()
