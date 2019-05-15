import smtplib
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

