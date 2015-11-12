import socket
import threading
import sys
import pickle
import os

class Cliente:

    def __init__(self, usuario):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3492    
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.por_enviar = {}
        try:
            # Un cliente se puede conectar solo a un servidor.
            self.s_cliente.connect((self.host, self.port)) # El cliente revisa que el servidor esté disponible
            # Una vez que se establece la conexión, se pueden recibir mensajes
            recibidor = threading.Thread(target=self.recibir_mensajes, args=())
            recibidor.daemon = True
            recibidor.start()
        except socket.error:
            print("No fue posible realizar la conexión")
            sys.exit()

    def recibir_mensajes(self):
        while True:
            data = self.s_cliente.recv(1024)
            data = bytearray(data)
            nombre_archivo = pickle.loads(data[-1])
            data = bytes(data[0:-1])
            with open("./Cliente_{}".format(nombre_archivo),"wb") as writer:
                writer.write(data[0:-1])
            
    def menu(self):
        while True:
            print("""
                (1) Mostrar por enviar
                (2) Agregar Archivos
                (3) Quitar Archivos
                (4) Enviar Archivos
                (5) Terminar comunicacion
                """)
            opcion = input("Ingrese opcion: ")
            if opcion == "1":
                for key in self.por_enviar:
                    print(key)

            elif opcion == "2":
                lista = os.listdir("./Archivos")
                for i in range(len(lista)):
                    print(i,lista[i])
                opcion = input("Seleccione archivo para agregar: ")

                with open("./Archivos/{}".format(lista[int(opcion)]),"rb") as reader:
                    byte_array = reader.read()
                    byte_array = byte_array + pickle.dumps(lista[int(opcion)])
                    self.por_enviar[lista[int(opcion)]] = byte_array


            elif opcion == "3":
                for key in self.por_enviar:
                    print(key)
                archivo = input("Ingrese nombre de archivo: ")
                try:
                    del self.por_enviar[archivo]
                except:
                    print("Ups algo fallo")

            elif opcion == "4":
                for key in self.por_enviar:
                    mensaje = self.por_enviar[key]
                    self.enviar(mensaje)

            elif opcion == "5":
                print("Adios")
                self.s_cliente.close()
                break

    def enviar(self,mensaje):
        self.s_cliente.send(mensaje)


class Servidor:

    def __init__(self, usuario, num_clients=1):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3492    
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Debemos hacer el setup para poder escuchar a los clientes que se quieran conectar
        self.s_servidor.bind((self.host, self.port))
        # En este caso solo queremos escuchar un cliente
        self.s_servidor.listen(1)
        self.cliente = None
        self.por_enviar = {}

        
        # No hacemos self.aceptar()
        thread_aceptar = threading.Thread(target=self.aceptar, args=())
        thread_aceptar.daemon = True
        thread_aceptar.start()

    def recibir_mensajes(self):
        while True:
            data = self.cliente.recv(1024)
            data = bytearray(data)
            nombre_archivo = pickle.loads(data[-1])
            data = bytes(data[0:-1])
            with open("./Servidor_{}".format(nombre_archivo),"wb") as writer:
                writer.write(data[0:-1])

    def aceptar(self):
        while True:
            cliente_nuevo, address = self.s_servidor.accept()
            self.cliente = cliente_nuevo
            thread_mensajes = threading.Thread(target=self.recibir_mensajes, args=())
            thread_mensajes.daemon = True
            thread_mensajes.start()

    def menu(self):
        while True:
            print("""
                (1) Mostrar por enviar
                (2) Agregar Archivos
                (3) Quitar Archivos
                (4) Enviar Archivos
                (5) Terminar comunicacion
                """)
            opcion = input("Ingrese opcion: ")
            if opcion == "1":
                for key in self.por_enviar:
                    print(key)

            elif opcion == "2":
                lista = os.listdir("./Archivos")
                for i in range(len(lista)):
                    print(i,lista[i])
                opcion = input("Seleccione archivo para agregar: ")

                with open("./Archivos/{}".format(lista[int(opcion)]),"rb") as reader:
                    byte_array = reader.read()
                    byte_array = byte_array + pickle.dumps(lista[int(opcion)])
                    self.por_enviar[lista[int(opcion)]] = byte_array

            elif opcion == "3":
                for key in self.por_enviar:
                    print(key)
                archivo = input("Ingrese nombre de archivo: ")
                try:
                    del self.por_enviar[archivo]
                except:
                    print("Ups algo fallo")

            elif opcion == "4":
                for key in self.por_enviar:
                    mensaje = self.por_enviar[key]
                    self.enviar(mensaje)

            elif opcion == "5":
                print("Adios")
                self.cliente.close()
                break

    def enviar(self,mensaje):
        self.cliente.send(mensaje)

if __name__ == "__main__":

    pick = input("Ingrese S si quiere ser servidor o C si desea ser cliente: ")
    if pick == "S":
        nombre = input("Ingrese el nombre del usuario: ")
        server = Servidor(nombre, num_clients=2)
        server.menu()

    else:
        nombre = input("Ingrese el nombre del usuario: ")
        client = Cliente(nombre)
        client.menu()