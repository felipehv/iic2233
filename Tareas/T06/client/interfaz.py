
from PyQt4 import QtGui, QtCore, uic
from cliente import *
class DrobPox(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()
        self.login = Login(self)
        self.chat = Chat(self)
        self.setGeometry(50,50,800,600)
        self.setCentralWidget(self.login)

        self.cliente = Cliente(self)

formulario = uic.loadUiType("chat.ui")
class Chat(formulario[0], formulario[1]):
    def __init__(self,main):
        super().__init__()
        self.setupUi(self)
        self.main = main

        self.chooseButton.clicked.connect(self.selectFile)
        self.uploadButton.clicked.connect(self.uploadFile)
        self.chatButton.clicked.connect(self.startChat)


    def startChat(self, button):
        otro_user = self.userchat.text()
        tupla = dumps(("chat", otro_user, otro_user))
        self.main.cliente.enviar(tupla)

    def uploadFile(self, button):
        ruta = self.fileroot.text()
        nombre = ruta.split("/")[-1]
        print(nombre)
        with open(ruta,"rb") as reader:
            archivo = reader.read()
        self.main.cliente.enviar(("upload",nombre,archivo))

    def selectFile(self):
        self.fileroot.setText(QtGui.QFileDialog.getOpenFileName())



formulario = uic.loadUiType("log.ui")
class Login(formulario[0], formulario[1]):
    def __init__(self,main):
        super().__init__()
        #self.initGUI()
        self.main = main
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.login)


    def login(self,button):
        print(button.text())
        if button.text() == "Cancel":
            exit()
        elif button.text() == "OK" and self.checkBox.isChecked():
            user,pw = self.user.text(),self.passw.text()
            self.main.cliente.enviar(("signin",user,pw))

        else:
            user,pw = self.user.text(),self.passw.text()
            self.main.cliente.enviar(("login",user,pw))

        resp = loads(self.main.cliente.socket.recv(1024))
        if resp:
            print("hola")
            self.main.setCentralWidget(self.main.chat)
            self.main.cliente.start()
        else:
            button.setText("Intenta de nuevo")




if __name__ == '__main__':
    # Inicializamos la aplicación de la misma forma que 
    # cuando la creamos manualmente
    app = QtGui.QApplication([])
    form = DrobPox()
    form.show()
    app.exec_()