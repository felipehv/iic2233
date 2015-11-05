import socket
import threading
from gato import Gato, sys


class Service:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 10001

    def escuchar(self):
        while True:
            data = self.socket.recv(1024)
            data = data.decode('ascii')
            print("El otro jugador puso su ficha en {}".format(data))

    def enviar(self, mensaje):
        if not self.turno:
            print('Presiona <enter> para actualizar y ver si es tu turno')
            return
        mensaje = mensaje.strip()
        if self.turno == self.gato.turno and 0 <= int(mensaje[0]) < 3 and 0 <= int(mensaje[2]) < 3:
            if self.gato.estado[int(mensaje[0])][int(mensaje[2])] == ' ':
                self.gato.editar_posicion(mensaje.split(','))
                s_otro, addr = self.socket.accept()
                s_otro.send(mensaje.encode('ascii'))
            else:
                print("Posicion ocupada")

        else:
            print("Espera tu turno, tu eres {}".format(self.turno))

class Cliente(Service):
    def __init__(self, gato):
        super().__init__()
        self.gato = gato
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.turno = "O"
        self.socket.connect((self.host,self.port))

    def enviar(self, mensaje):
        print(self.gato)
        if not self.turno:
            print('Presiona <enter> para actualizar y ver si es tu turno')
            return
        mensaje = mensaje.strip()
        if self.turno == self.gato.turno and 0 <= int(mensaje[0]) < 3 and 0 <= int(mensaje[2]) < 3:
            if self.gato.estado[int(mensaje[0])][int(mensaje[2])] == ' ':
                self.gato.editar_posicion(mensaje.split(','))
                self.socket.send(mensaje.encode('ascii'))
            else:
                print("Posicion ocupada")

        else:
            print("Espera tu turno, tu eres {}".format(self.turno))


class Servidor(Service):
    def __init__(self, gato):
        super().__init__()
        self.turno = "X"
        self.gato = gato
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host,self.port))
        self.socket.listen(10)

    def aceptar(self):
        cont = 0
        client, address = self.socket.accept()      
        print("Obtuvimos una conexión desde %s" % str(address))
        for i in range(10):
            data = client.recv(1024)
            data = data.decode('ascii')
            print("El jugador O jugo su ficha en {}".format(data))

        client.close()



if __name__ == "__main__":
    gato = Gato()
    pick = input("Ingrese X si quiere ser servidor o O si desea ser cliente: ")
    if pick == "X":
        server = Servidor(gato)
        #server.aceptar()
        escuchador = threading.Thread(target=server.aceptar)
        escuchador.daemon = True
        escuchador.start()
        while True:
            mensaje = input("Jugador {0} debe ingresar la posicion en que desea jugar".format(server.gato.turno))
            server.enviar(mensaje)

    elif pick == "O":
        client = Cliente(gato)
        escuchador = threading.Thread(target=client.escuchar)
        escuchador.daemon = True
        escuchador.start()
        while True:
            mensajes = input("Jugador {0} debe ingresar la posicion en que desea jugar".format(client.gato.turno))
            client.enviar(mensajes)
