import os
import sys
from .color import green, white, blue, start, alert, numbering

def TODO():
	print(start + " ToDo List " + start)
	print(alert + " This List Will Be Updated" + alert)
	print("")
	print(numbering(1) + white + " Add More Email Template (will always update)" + numbering(1))
	print(numbering(2) + white + " Create Better Interface (might take a while) " + numbering(2))
	print(numbering(3) + white + " Add Mass Email Sender " + numbering(3))
	print(numbering(4) + white + " Add Emails With Different Languages " + numbering(4))
	print(numbering(5) + white + " Add More Target Specified Emails " + numbering(5))
	print(numbering(7) + white + " Add More Bypass Methods " + numbering(6))
	

