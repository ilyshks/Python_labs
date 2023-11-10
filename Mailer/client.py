import socket


HOST = '127.0.0.1'
PORT = 50007
data = ''
while True:
    email = input('Введите email:', )
    msg = input('Введите сообщение:', )
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall([email, msg])
        data = s.recv(1024)
    if data == 'OK':
        print('Успешно!')

