import smtplib
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.base import MIMEBase
from os.path import basename
from random import randint

def sendmail(destination="",subject="A SUBJECT",html="The email content",files=["paths","to","files","to","include"]):
	import smtplib
	import os
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	smtp = smtplib.SMTP('smtp.gmail.com:587')
	smtp.set_debuglevel(False)
	smtp.ehlo()
	smtp.starttls()

	sender = "YOUR_EMAIL@gmail.com"
	smtp.login(sender, "YOUR_PASSWORD")


	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = sender
	msg['Cci'] = ", ".join(destination)

	# Create the body of the message (a plain-text and an HTML version).
	text = "" # I don't know what this might be for (???)

	for f in files :
		part = MIMEBase('application', 'octet-stream')
		part.set_payload(open(f, 'rb').read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition','attachment; filename="%s"' % basename(f))
		msg.attach(part)


	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)

	smtp.sendmail(sender, destination, msg.as_string())

if __name__ == "__main__":
	# sendmail()
	pass
