from socket import *  # подключение модуля для работы с сокетами

clients_address = []  # массив для хранения подключенных клиентов
create_server = ('192.168.1.107', 15000)
tcp_sock = socket(AF_INET, SOCK_DGRAM)  # создание сокета
tcp_sock.bind(create_server)  # привязка сокета к определенному ip-адресу и порту
print('~~~ Server Start ~~~')
while True:
    message, address = tcp_sock.recvfrom(2048)  # получение данных от клиента(сообщение и адрес)
    if address not in clients_address:  # если адресса клиента нет в массиве, то добавляем его
        clients_address.append(address)  # добавление клиента в массив клиентов
    if message.decode('utf8') == "Exit":    # если получено сообщение 'Exit'
        tcp_sock.sendto('Bye =)'.encode('utf-8'), address)  # отправляет 'Bye =)' отключившемуся клиенту
        for i in range(len(clients_address)):  # цикл, который удаляет данного клиента из массива клиентов
            if clients_address[i] == address:
                clients_address.pop(i)
                break
        if not clients_address:  # если клиентов не осталось - выход из сервера
            break
        else:  # если остались, то ожидание следующих сообщений
            continue
    for client in clients_address:  # отправка сообщения всем клиентам
        tcp_sock.sendto(message, client)
print('~~~ Server Stop ~~~')
tcp_sock.close()  # закрытие сервера
