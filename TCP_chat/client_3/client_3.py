from socket import *
import threading
import time


def read_sok():  # функция, которая будет получать сообщения от сервера
    while True:
        data = tcp_socket.recv(2048)
        print(data.decode('utf-8'))
        if data.decode('utf8') == 'Bye =)':
            break
    return


server = '192.168.1.107', 15000  # данные сервера
nick = input('Enter your nickname:')  # ввод псевдонима
tcp_socket = socket(AF_INET, SOCK_DGRAM)  # создание сокета
tcp_socket.bind(('', 0))
tcp_socket.sendto((nick + ' Connect to server').encode('utf-8'), server)  # уведомление сервера о подключении
potok = threading.Thread(target=read_sok)  # создание потока, для функции према сообщений сервера
potok.start()  # старт потока
while True:
    message = input('Enter your message or Exit:')  # ввод сообщения
    if message == 'Exit':  # Если получено сообщение 'Exit' - то происходит выход из чата
        tcp_socket.sendto((nick + ' disconnect to server').encode('utf-8'), server)  # отправка сообщения на сервер
        tcp_socket.sendto(message.encode('utf-8'), server)  # отправка сообщения 'Exit'
        time.sleep(1.0)  # пауза на 1 секунду
        break
    tcp_socket.sendto(('[' + nick + ']' + message).encode('utf-8'), server)  # отправка сообщения на сервер
    time.sleep(1.0)  # пауза на 1 секунду
tcp_socket.close()  # закрытие соединения
