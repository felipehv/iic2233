import socket
import threading
import sys
from pickle import dumps, loads, dump, load
import os

"""
Formato de enviar y recibir

*Recibir*
Chatlogs: ("chatlog",,)
Download: ("down",(name,route),dump)
Upload: ("up",name,dump)
Conexion

"""
class Archivo():

    def __init__(self,nombre,ext=None):
        self.nombre = nombre
        self.ext = ext
        self.editable = True

class Carpeta(Archivo):
    
    def __init__(self,owner):
        self.nombre = nombre
        self.archivos = []
        self.owner = owner
        self.shared = [] #Strings de usuarios compartidos

    def compartir(user):
        self.shared.append(user.usuario)

class Cliente:

    def __init__(self,interface):
        self.interface = interface
        self.host = '127.0.0.1'
        self.port = 2230
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Un cliente se puede conectar solo a un servidor.
            self.socket.connect((self.host, self.port)) # El cliente revisa que el servidor esté disponible
            # Una vez que se establece la conexión, se pueden recibir mensajes

        except socket.error:
            print("No fue posible realizar la conexión")
            sys.exit()


    def start(self):
        recibidor = threading.Thread(target=self.recibir, args=())
        recibidor.daemon = True
        recibidor.start()

    def recibir(self):
        archivo = b""
        while True:
            try:
                data = self.socket.recv(2048)
                if data.endswith("ENDOFTHEFILE"):
                    self.crear_archivo(archivo[0:-12])
                else:
                    try:
                        data = loads(data)
                        func = self.funciones[data[0]] #Se asegura desde el cliente que data[0] es el codigo
                        func(data[1],data[2])
                    except:
                        archivo += data
            except:
                break

    def crear_archivo(self,fil): #Se recibe en el servidor para almacenar
        with open("./".format(user.route,fil[1]),"wb") as writer:
            dump(fil[2],writer)

    def cerrar(self):
        self.socket.close()
        exit()

    def enviar(self,tupla):
        tupla2 = dumps(tupla)
        if tupla[0] == "upload":
            tupla2 += b"ENDOFTHEFILE"
        elif tupla[0] == "chat":
            tupla2 += b"MSG"
        self.socket.send(tupla2)
        tupla = loads(tupla2)
        print("Enviado {}".format(tupla2))

    def desconectar(self):
        self.connection = False
        self.socket.close()