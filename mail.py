import smtplib
from email.message import EmailMessage
import ssl
import requests
import socket
from time import sleep


sender_email = "raspberrypiallium@gmail.com"
receiver_email = "20bcs121@nith.ac.in"
password = "spptbmptonthxofw"

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

endpoint_url = f'http://{ip_address}/device/'
status=requests.get(endpoint_url).headers['status']

subject="Storage status is not good"
body=f"Storage status is very critical. The status code is {status}"

em=EmailMessage()
em['From']=sender_email
em['To']=receiver_email
em['Subject']=subject
em.set_content(body)

context = ssl.create_default_context()
print(f"status :{status}")
while True:
    if float(status) < 1:
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(sender_email,password=password)
            smtp.sendmail(sender_email,receiver_email,em.as_string())
        print("mail send")
        sleep(3600)
    sleep(10)


        








