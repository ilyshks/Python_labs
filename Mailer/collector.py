import datetime
import email
import re
from email.header import decode_header
from imaplib import IMAP4_SSL
from environs import Env
import time


def write_success(ID, msg):
    with open('success_request.log', mode='a+') as f:
        f.write(f'Successfully written at: {datetime.datetime.now()}\nID: {ID}\nMessage: {msg}')


def write_error(msg):
    with open('error_request.log', mode='a+') as f:
        f.write(f'Failed to be written at: {datetime.datetime.now()}\nMessage: {msg}')


def collect_mail():
    time.sleep(PERIOD_CHECK)

    with IMAP4_SSL(IMAP_HOST, IMAP_PORT) as gmail:
        gmail.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        while True:
            print("COLLECTING MAIL...")
            gmail.select('inbox')
            typ, data = gmail.search(None, 'ALL')
            letter_number = len(data[0].decode().split(' '))

            res, msg = gmail.fetch(str(letter_number), '(RFC822)')
            msg = email.message_from_bytes(msg[0][1])
            header = decode_header(msg["Subject"])[0][0]
            if msg in error_set or msg in success_set:
                continue
            # print(header)
            if re.fullmatch(r'^\[Ticket #.+] Mailer$', header):
                if header not in success_set:
                    start_indx = header.index('#') + 1
                    finish_indx = header.index(']')
                    write_success(header[start_indx:finish_indx], msg)
                    success_set.add(header)
                    print("MAILER COLLECTED", msg)
            elif re.fullmatch(r'^\[Ticket #.+] Error$', header):
                if header not in error_set:
                    write_error(msg)
                    error_set.add(header)
                    print("ERROR COLLECTED", msg)
            time.sleep(PERIOD_CHECK)


env = Env()
env.read_env()
EMAIL_LOGIN = env('EMAIL_LOGIN')
EMAIL_PASSWORD = env('EMAIL_PASSWORD')
IMAP_HOST = env('IMAP_HOST')
IMAP_PORT = int(env('IMAP_PORT'))
PERIOD_CHECK = int(env('PERIOD_CHECK'))

error_set = set()
success_set = set()

