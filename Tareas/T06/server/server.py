import socket
import threading
import sys
from pickle import load, dump, loads, dumps
import hashlib
from datetime import datetime
from classes import *
"""
Formato de recepcion
Seran todos en formato de tupla

Mensajes: ("msg",None,Contenido) -> Tiene que existir chat
Archivos a subir: ("upload",(name,route),dump)
Inicio sesion: ("login",user,pass) -> 3 intentos
Logout: ("logout",None,None)
Iniciar chat: ("chat", otro_user, otro_user)
Solicitud de archivos directorio: ("dir",route,None)
Crear usuario: ("signin",user,pass)

Suponiendo que todos los archivos subidos tienen extension valida
*** Hecho en Windows, no se asegura funcionamiento en Linux ***
"""


class Server:

    def __init__(self, num_clients=10):
        self.host = '127.0.0.1'
        self.port = 2230
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s_servidor.bind((self.host, self.port))

        self.s_servidor.listen(num_clients)
        thread_aceptar = threading.Thread(target=self.aceptar, args=())
        #thread_aceptar.setDaemon(True)
        thread_aceptar.start()

        self.clientes = dict()
        self.chats = []  # Diccionarios
        self.nicknames = []
        self.funciones = {"msg": self.send_msg, "upload": self.upload, "login": self.login,
        "chat": self.create_chat, "signin": self.create_user,"dir": self.tree}


    """
    Funciones de procesamiento en el servidor
    """
    def upload(self,fil): #Se recibe en el servidor para almacenar
        fil = loads(fil)
        print(fil)
        with open("./users/{}".format(fil[1]),"wb") as writer:
            dump(loads(fil[2]),writer)

    def tree(self,ruta,b):
        nodo = Nodo(None,"./users/{}".format(user.user),".")

    def create_chat(self, user, otro_user): 
        """
        user: type User
        otro_user: type String
        """
        try:
            otro_user = self.clientes[otro_user]
        except:
            user.socket.send(dumps(("error",None,None)))
            return False
        for chat in self.chats:
            if user in chat and otro_user in chat:
                return False
        for chat in self.chats:
            if user in chat:
                self.chats.remove(chat)
                break
        logs = os.listdir("./chatlogs")
        for log in logs:
            if user in log:
                chatlog = open("./chatlogs/{}.chatlog","w".format(log))
                chats.append({user: self.clientes[otro_user.user], otro_user: user, "log": chatlog})
                return
        chatlog = open("./chatlogs/{}{}.chatlog".format(),"w")
        #chat.append({user: self.clientes[otro_user.user], otro_user: user, "log": chatlog}) #fix it

    def create_user(self,user,pw,sock):
        usernames = os.listdir("./users")
        if user not in usernames:
            usname = user
            user = User(user,pw)
            with open("./users/{}.dbuser".format(usname),"wb") as writer:
                dump(user,writer)
                self.clientes[usname] = user,sock
                return user

    def send_msg(self, user, mensaje, otro_usuario):
        mensaje = "{0} {1} {2}".format(datetime.datetime.now(),user,mensaje)
        c = self.clientes[otro_usuario]
        c.socket.send(msj_final.encode('utf-8'))

    def mostrar_archivos(self, ruta, username):
        nodo = Nodo("./maindir")
        return nodo.__repr__2()

    def login(self, socket):
        while True:
            data = socket.recv(1024)
            data = loads(data)
            print(data)
            user,pw = data[1:]
            if data[0] == "login":
                try:
                    with open("./users/{}.dbuser".format(user),"rb") as user_data:
                        user_data = load(user_data)
                        if user_data.password == pw:
                            self.clientes[user] = user_data,socket
                            return user_data
                        else:
                            socket.send(dumps(False))
                except Exception as ha:
                    print("No se pudo iniciar sesion", ha)
                    socket.send(dumps(False))
                    continue
            elif data[0] == "signin":
                return self.create_user(user,pw,socket)
        return False

    """
    Fin funciones de procesamiento
    """ 

    def recibir(self, user):
        socket = self.clientes[user][1]
        archivo = b""
        while True:
            try:
                data = socket.recv(2048)
                print(data)
                if data.endswith(b"ENDOFTHEFILE"):
                    archivo += data[0:-12]
                    print("Termino")
                    self.upload(archivo)
                else:
                    try:
                        data = loads(data)
                        func = self.funciones[data[0]] #Se asegura desde el cliente que data[0] es el codigo
                        func(data[1],data[2])
                    except:
                        archivo += data
            except Exception as ex:
                print(ex)
                del self.clientes[user]
                break


    def aceptar(self):
        while True:
            s_cliente, address = self.s_servidor.accept()
            cliente = self.login(s_cliente)
            if not cliente:
                msg = dumps(("login",True,None))
                s_cliente.send(msg)
                continue
            msg = dumps(True)
            s_cliente.send(msg)
            thread_mensajes = threading.Thread(
                target=self.recibir, args=(cliente.user,))
            thread_mensajes.daemon = True
            thread_mensajes.start()


if __name__ == "__main__":
    server = Server()