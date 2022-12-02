import socket

from _thread import *
import threading

lista_usr = {} 

def threaded(c):
    while True:
        data = c.recv(1024).decode()
        nom,ms=data.split(">")
		
        if not data:
            print('Bye')
            break
        
        b=lista_usr[nom]	
        b.send(ms.encode())

    c.close()


def Main():
	host = ""
	port = 6666
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print("socket binded to port", port)
	s.listen(5)

	print("El servidor esta esperando")

	while True:
		c, addr = s.accept()

		c.send('Bienvenido al chat'.encode())
		data = c.recv(1024).decode()
		lista_usr[data]=c

		c.send('Lista de usuarios conectados'.encode())
		for usuario in lista_usr.keys():
			print (usuario)			
		print('Connected to :', addr[0], ':', addr[1])
		start_new_thread(threaded, (c,))
	s.close()


if __name__ == '__main__':
	Main()