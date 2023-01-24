import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'My email with attachment'
msg['From'] = 'youremail@example.com'
msg['To'] = 'receiver@example.com'

# Open the file in bynary
binary_file = open('file.txt', 'rb')
payload = MIMEBase('application', 'octate-stream', Name='file.txt')
payload.set_payload((binary_file).read())

# Encode the payload using Base64
encoders.encode_base64(payload)

# Add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename='file.txt')
msg.attach(payload)

# Send the email via our SMTP server.
s = smtplib.SMTP('smtp.example.com')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
