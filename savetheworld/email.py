import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import ssl


def send(from_email, to_email, message, password, server="smtp.gmail.com", port=465):
	"""
	Send an email
	Use from_email and password to log in to server on specified port
	(defaults are set to gmail server)
	Then send an email to to_email with message
	First line of message must start with Subject:
	"""
	with smtplib.SMTP_SSL(server, port, context = ssl.create_default_context()) as connection:
		connection.login(from_email, password)
		connection.sendmail(from_email, to_email, message)

def sendImage(from_email, to_email, message, subject, password, attachment, server="smtp.gmail.com", port=465):
    """
    Send an image by email
	Use from_email and password to log in to server on specified port
	(defaults are set to gmail server)
	Then send an email to to_email with specified subject and message,
	including attachment (which is the filename of an image)
    """
	#setup the email
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = from_email
	msg['To'] = to_email
	text = MIMEText(message)	
	msg.attach(text)
	
  #attach an image
	img_data = open(attachment, 'rb').read()
	image = MIMEImage(img_data, name=os.path.basename(attachment))
	msg.attach(image)		
	
	#send over ssl
	with smtplib.SMTP_SSL(server, port, context = ssl.create_default_context()) as connection:
		connection.login(from_email, password)
		connection.sendmail(from_email, to_email, msg.as_string())
