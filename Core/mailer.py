import os
import sys
from Core.helper.color import green, white, blue, start, alert, numbering
from Core.Mailer.gmail import Gmail
from Core.Mailer.yahoo import YahooEmail
from Core.Mailer.live import LiveEmail

def NormalEmail():
	os.system("clear")
	print(green)
	print("""
 __^__                                                        __^__
( ___ )------------------------------------------------------( ___ )
 | / |                                                        | \ |
 | / |+------------)PhishMailer BaitMailer V1.5(-------------+| \ |
 |___|                                                        |___|
(_____)------------------------------------------------------(_____) """)
	print("")
	print(numbering(1) + white + " @Gmail")
	print(numbering(2) + white + " @Yahoo")
	print(numbering(3) + white + " @Hotmail")
	print(numbering(4) + white + " @Outlook")
	print(numbering(5) + white + " @Live")
	print(alert + " There Might Be Some Bugs, Please Open An Issue On Github If Found! " + alert)
	
	Smtp_pick = int(input("\nroot@phishmailer/Mailer/:~ "))
	
	if Smtp_pick == 1:
		Gmail()
		
	elif Smtp_pick == 2:
		YahooEmail()
	
	elif Smtp_pick == 3:
		LiveEmail()
		
	elif Smtp_pick == 4:
		LiveEmail()
		
	elif Smtp_pick == 5:
		LiveEmail()
		
	else:
		print(alert + " Invalid Option " + alert) 
	
