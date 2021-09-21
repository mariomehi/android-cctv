import os
import smtplib
import time
import json
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def sendMail():
    
    html = """\
    <html>
        <head></head>
        <body>
            <p>guarda chi è: <br>
             <center><img src="body.jpg"  width="300" height="300"></center>
        </body>
    </html>
    """


    f  = open('data.json','r')
    data = json.load(f)
    recipient = str(data['email'])

    img_data = open('body.jpg', 'rb').read()

    content  = 'il sistema ha rilevato un ladro alle '
    
    t0 = str(time.asctime( time.localtime(time.time()) ))

    content = content + t0

    msg = MIMEMultipart()
    msg['Subject'] = 'rilevamento ladro'
    msg['From'] = 'ilsorvegliante27@gmail.com'
    msg['To'] = recipient

    
    part2 = MIMEText(html, 'html')
    text = MIMEText(content)

    msg.attach(text)
    msg.attach(part2)
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login('ilsorvegliante27@gmail.com', "Supermario.99")
    s.sendmail('ilsorveglinte27@gmail.com', recipient, msg.as_string())
    s.quit()


    
