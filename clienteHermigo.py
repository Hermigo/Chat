import socket   
import threading

username = input("Introduce tu nombre de usuario: ")

host = '127.0.0.1'
port = 65433

user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user.connect((host, port))


def recib_mens():
    while True:
        try:
            mensaje = user.recv(1024).decode('utf-8')

            if mensaje == "username":
                user.send(username.encode("utf-8"))
            else:
                print(mensaje)#mensaje normal de otros usuarios
        except:
            print("Vaya ah ocurrido un error!")
            user.close
            break

def escrib_mens():#formato de mensajes a enviar 
    while True:
        mensaje = f"{username} Dice: {input('')}"
        user.send(mensaje.encode('utf-8'))

recib_hilo = threading.Thread(target=recib_mens)
recib_hilo.start()

escrib_hilo = threading.Thread(target=escrib_mens)
escrib_hilo.start()#inicia el hilo
