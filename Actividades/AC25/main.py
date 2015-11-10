# coding=utf-8
import socket
import os
import threading
import time

class Juego:

    def __init__(self):
        self.palabras = []

    def agregar_palabras(self, mensaje):
        mensaje = mensaje.strip().split(" ")[-3:]
        for p in mensaje:
            self.palabras.append(p)

    def comprobar(self, string):
        if len(self.palabras) == 0 and len(string.split(' ')) != 3:
            return False
        return string.strip().split(' ')[0:-3] == self.palabras\
         and len(string.strip().split(' ')) - 3 == len(self.palabras)


class Cliente:

    def __init__(self, usuario):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s_cliente.connect((self.host, self.port))
        except socket.error:
            print("No fue posible realizar la conexión")
            sys.exit()

    def recibir_mensajes(self):
        while True:
            data = self.s_cliente.recv(1024)
            data = data.decode('utf-8')
            if data == "lose":
                print("Has ganado")
                break
            elif data == "win":
                print("Has perdido")
                break
            print(data)
            time.sleep(3)
            os.system("clear")
            mensaje = input(
                "Ingrese toda la historia (respetando mayusculas y minusculas)\n")
            self.enviar(mensaje)
            os.system("clear")

    def enviar(self, mensaje):
        self.s_cliente.send(mensaje.encode('utf-8'))


class Servidor:

    def __init__(self, usuario, juego):
        self.juego = juego
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_servidor.bind((self.host, self.port))
        self.s_servidor.listen(1)
        self.cliente = None
        self.aceptar()

    def recibir_mensajes(self):
        while True:
            os.system("clear")
            mensaje = input(
                "Ingrese toda la historia (respetando mayusculas y minusculas)\n")
            if not self.juego.comprobar(mensaje):
                self.enviar("lose")
                print("Has perdido")
                break
            self.juego.agregar_palabras(mensaje)
            self.enviar(mensaje)
            os.system("clear")
            data = self.cliente.recv(1024)
            data = data.decode('utf-8')
            if not self.juego.comprobar(data):
                self.enviar("win")
                print("Has ganado!")
                break
            self.juego.agregar_palabras(data)
            print(data)
            time.sleep(3)

    def aceptar(self):
        cliente_nuevo, address = self.s_servidor.accept()
        self.cliente = cliente_nuevo

    def enviar(self, mensaje):
        self.cliente.send(mensaje.encode('utf-8'))


if __name__ == "__main__":
    juego = Juego()
    pick = input("Ingrese S si quiere ser servidor o C si desea ser cliente: ")
    if pick == "S":
        nombre = input("Ingrese el nombre del usuario: ")
        server = Servidor(nombre, juego)
        server.recibir_mensajes()

    elif pick == "C":
        nombre = input("Ingrese el nombre del usuario: ")
        client = Cliente(nombre)
        client.recibir_mensajes()


if __name__ == '__main__':
    pass
