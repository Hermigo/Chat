import socket


def Main():
	host = '127.0.0.1'
	port = 6666
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))

	print (s.recv(1024).decode())

	message = input('Introduce tu nombre: ')
	s.send(message.encode('ascii'))
	print (s.recv(1024).decode())

	while True:
		message = input("Ingrese el mensaje a mandar poniendo el usuario al que se le enviara un'>'y el mensaje:\n")
		s.send(message.encode('ascii'))
		data = s.recv(1024)
		print('Received from the server :',str(data.decode('ascii')))

		ans = input('\nQuieres mandar otro mensaje? (y/n) :')
		if ans == 'y':			
			continue
		else:
			break
	s.close()


if __name__ == '__main__':
	Main()
n
