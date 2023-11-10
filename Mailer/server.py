import socket
from smtplib import SMTP
from environs import Env


env = Env()
env.read_env()
username = env("EMAIL_LOGIN")
password = env("EMAIL_PASSWORD")
HOST = '127.0.0.1'
PORT = 50007
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen(1)
#     conn, addr = s.accept()
#     with conn:
#         while True:
#             data = conn.recv(1024)
#             if data:
#                 break

with SMTP(f"{env('SMTP_HOST')}:{env('SMTP_PORT')}") as smtp:
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(username, username, 'AAAAAAAAA')
    # try:
    #     smtp.sendmail(username, username, 'AAAAAAAAA')
    #     conn.sendall(b'OK')
    # except SMTPRecipientsRefused:
    #     conn.sendall(data)