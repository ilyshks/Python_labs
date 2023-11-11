import socket


HOST = '127.0.0.1'
PORT = 50007
data = ''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        email = input('Введите email:', )
        msg = input('Введите сообщение:', )
        s.send(f'{email}\n{msg}'.encode('utf-8'))
        data = s.recv(4096).decode('utf-8')
        if data == 'OK':
            print('Успешно!')
            break
        else:
            print(data)