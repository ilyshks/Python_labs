import socket
import time
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPRecipientsRefused
from threading import Thread
from uuid import uuid4

from environs import Env

from collector import collect_mail


def is_valid_email(email):
    if email.count(' ') == 0 and email.count('@') == 1 and email.split('.')[-1] in ('com', 'ru', 'org', 'net'):
        return True
    return False

# EMAIL_LOGIN=ilyagorunov.04@gmail.com
# EMAIL_PASSWORD=ardx yqpf yeio gjiw
# IMAP_HOST= imap.gmail.com
# IMAP_PORT=993
# SMTP_HOST= smtp.gmail.com
# SMTP_PORT=587
# PERIOD_CHECK=10

env = Env()
env.read_env()
username = env("EMAIL_LOGIN")
password = env("EMAIL_PASSWORD")
PERIOD_CHECK = int(env("PERIOD_CHECK"))
HOST = '127.0.0.1'
PORT = 50007
data = ''
flag = True
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    collector_thread = Thread(target=collect_mail, daemon=True)
    collector_thread.start()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        while flag:
            while True:
                data = conn.recv(4096).decode('utf-8')
                if data:
                    break
            if len(data.split("\n")) == 2:
                email, msg = data.split("\n")
                if is_valid_email(email):
                    ID = uuid4()
                    with SMTP(f"{env('SMTP_HOST')}:{env('SMTP_PORT')}") as smtp:
                        msg = MIMEText(msg)
                        msg['Subject'] = f'[Ticket #{ID}] Mailer'
                        smtp.starttls()
                        smtp.login(username, password)
                        try:
                            smtp.sendmail(username, email, msg.as_string())
                            smtp.sendmail(username, username, msg.as_string())
                            conn.sendall(b'OK')
                            flag = False
                            time.sleep(PERIOD_CHECK*2+5)
                        except SMTPRecipientsRefused:
                            conn.sendall(b'The email has not been sent!')
                else:
                    ID = uuid4()
                    with SMTP(f"{env('SMTP_HOST')}:{env('SMTP_PORT')}") as smtp:
                        msg = MIMEText(msg)
                        msg['Subject'] = f'[Ticket #{ID}] Error'
                        smtp.starttls()
                        smtp.login(username, password)
                        smtp.sendmail(username, username, msg.as_string())

                    conn.sendall(b'Invalid input data format!')
            else:
                conn.sendall(b'Invalid input data format!')
            data = ''


