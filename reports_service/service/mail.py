import os
import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from db import mailing_list_emails
from settings import EMAIL_HOST, EMAIL_PORT


def open_server():
    host = EMAIL_HOST
    port = EMAIL_PORT
    user = os.environ['EMAIL_USER']
    password = os.environ['EMAIL_PASSWORD']

    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(user, password)
    return server


def attach_files_to_msg(attachments_paths: str, mail_msg: MIMEMultipart):
    for path in attachments_paths:
        attachment_filename = path.split('/')[-1]
        attachment_file = open(path, 'rb')
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(attachment_file.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f"attachment; filename={attachment_filename}")
        attachment_file.close()
        mail_msg.attach(attachment)


def send_report(attachments_paths: tuple, report: str):
    server = open_server()

    body = "<p>Please, find attached.</p>"
    mail_msg = MIMEMultipart()
    mail_msg['From'] = os.environ['EMAIL_USER']
    mail_msg['To'] = mailing_list_emails()
    mail_msg['Subject'] = f"Reports Automation Framework - {report}"
    mail_msg.attach(MIMEText(body, 'html'))

    attach_files_to_msg(attachments_paths, mail_msg)

    server.sendmail(mail_msg['From'], mail_msg['To'], mail_msg.as_string())
    server.quit()