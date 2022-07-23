import socket

# Определим констатны
BUFFER_SIZE = 1024
LISTEN_COUNT = 1
IP_SERVER = '192.168.1.148'
PORT_SERVER = 2222

# Создаем сервер и резервируем порт для него
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP_SERVER, PORT_SERVER))

command = ''
while command != 'exit':
	command = ''
	# Слушаем порт, для ожидания подключений
	print("Waiting connection...\n")
	server.listen(LISTEN_COUNT)

	# Если есть подключаемый пользователь, подключаем его
	client, adress = server.accept()
	print(f"[+] User connected from: {adress}\n")
	
	# Получим действующую директорию
	cwd = client.recv(BUFFER_SIZE).decode("utf-8")
	
	while command[:5] != 'dsnt' and command[:5] != 'exit':
		command = ''
		# Получим команду от сервера
		command = input(f"{cwd}>")
	
		# Отправим команду клиенту
		client.send(command.encode("utf-8"))
	

		if command[:3] == 'dir':
			strdir = client.recv(BUFFER_SIZE).decode("utf-8")
			strdir = strdir.replace(' ',', ')
			print(f"[{strdir}]\n")
		elif command[:3] == 'cd ':
			cwd = client.recv(BUFFER_SIZE).decode("utf-8")
		elif command[:5] == 'dsnt' or command[:5] == 'exit':
			print(f"[-] User disconnected from: {adress}\n")

# После того как пользователь получил ответ, отключаем его
server.close()
