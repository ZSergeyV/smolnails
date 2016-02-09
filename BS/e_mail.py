from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import smtplib
from BeautySpot import settings


def sendmail(to, subject, text, attach=[], mtype='html'):
    ok = True
    gmail_user = settings.EMAIL_HOST_USER
    gmail_pwd  = settings.EMAIL_HOST_PASSWORD

    msg = MIMEMultipart('alternative')

    msg['From']    = gmail_user
    msg['To']      = to
    msg['Cc']      = 'you@gmail.com'
    msg['Subject'] = subject

    msg.attach(MIMEText(text, mtype))

    for a in attach:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(a))
        msg.attach(part)

    try:
        mailServer = smtplib.SMTP('smtp-relay.gmail.com', port=587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, [to,msg['Cc']], msg.as_string())
        mailServer.close()
    except:
        ok = False
    return ok