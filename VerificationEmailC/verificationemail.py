import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Generator import Generator


class VerificationEmail:
	
	def __init__(self, From, Password, To):
	
		self.From = From
		self.Password = Password
		self.To = To
		
		code = Generator(False, True, True, False, False, 6).start()
		
		Subject = 'Verification Code'
		Message = f'Code: {code}'
		
		Msg = MIMEMultipart()
		Msg['From'] = From
		Msg['To'] = To
		Msg['Subject'] = Subject
		Msg.attach(MIMEText(Message))
		Msg = Msg.as_string()
		
		Server = smtplib.SMTP('smtp.gmail.com', 587)
		Server.starttls()
		Server.login(From, Password)
		Server.sendmail(From, To, Msg)
		Server.quit()
		
		check = input('Enter The Code: ')
		
		if check == code:
		
			print('\nDone the code is correct.')
			
		else:
		
			print('\nError, Please check again.')
