from PyQt4 import QtGui, uic, QtCore, QtCore
import threading
from classes import *
import os
from math import atan2, degrees

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()
        self.game_widget = GameWidget(self)
        self.menu_widget = MenuWidget(self)
        self.pause_widget = PauseWidget(self)
        self.setCentralWidget(self.menu_widget)

        self.setGeometry(50,50,800,600)

    def actualizar_barra(self,mensaje):
        self.statusBar().showMessage(mensaje)

    def juego(self):
        self.game_widget.juego()

    def keyPressEvent(self,event):
        #sender = self.sender()
        print(event)
        if event.text() == "w":
            self.game_widget.persona.mover()
        elif event.text() == "d":
            self.game_widget.persona.mover(True)
        elif event.text() == "p":
            self.setCentralWidget(self.mainwindow.pause_widget)
    """
    def keyPressEvent(self,event):
        #sender = self.sender()
        print(event.text())
        if event.text() == "w":
            self.game_widget.persona.mover()
    """
class MenuWidget(QtGui.QWidget):

    def __init__(self,main):
        super().__init__()
        self.init_GUI()
        self.MainWindow = main

    def init_GUI(self):
        self.start_button = QtGui.QPushButton('Comenzar el juego', self)
        self.start_button.resize(self.start_button.sizeHint())
        self.start_button.move(400,400)
        self.start_button.clicked.connect(self.empezar)

    def empezar(self):
        sender = self.sender()
        self.MainWindow.setCentralWidget(self.MainWindow.game_widget)

class PauseWidget(QtGui.QWidget):
    def __init__(self,main):
        super().__init__()
        self.init_GUI()
        self.MainWindow = main

    def init_GUI(self):
        self.pause_button = QtGui.QLabel(self)
        self.pause_button.setText("Juego en pausa <enter> para continuar.")
        self.pause_button.resize(self.pause_button.sizeHint())
        self.pause_button.move(400,400)

class GameWidget(QtGui.QWidget):
    def __init__(self,main):
        super().__init__()
        self.init_GUI() 
        self.setMouseTracking(True)
        self.mainwindow = main
        self.zombies = []

    def init_GUI(self):
        self.persona = Player(self)
        self.persona.move(50,50)

    def keyPressEvent(self,event):
        #sender = self.sender()
        print(event)
        if event.text() == "p":
            self.mainwindow.setCentralWidget(self.mainwindow.pause_widget)

        #self.persona = QtGui.QLabel(self)
        #self.persona.setGeometry(10, 10, 50, 50)
        #self.persona.setScaledContents(True)
        #use full ABSOLUTE path to the image, not relative
        #self.persona.setPixmap(QtGui.QPixmap(os.getcwd() + "/sprites/player.png"))

    def mover(self,ortogonal = False):
        if not ortogonal:
            xx,yy = self.vector
        else:
            xx,yy = self.vectorOrtogonal()
        #sender = self.sender()
        x = self.persona.x()
        y = self.persona.y()
        self.persona.move(x+xx*2,y+yy*2)

    def vectorOrtogonal(self):
        vector = self.vector[1],self.vector[0]
        return vector

    def keyPressEvent(self,event):
        sender = self.sender()
        print(event)
        if event.text() == "w":
            self.persona.mover()
        elif event.text() == "p":
            self.mainwindow.setCentralWidget(self.mainwindow.pause_widget)

    def mousePressEvent(self,event):
        pass
        #print('hola')

    def mouseMoveEvent(self,event):
        self.mx = event.x()
        self.my = event.y()
        self.persona.calcular_vector(event.x(),event.y())
        self.persona.rotate()

if __name__ == '__main__':
    # Inicializamos la aplicación de la misma forma que 
    # cuando la creamos manualmente
    app = QtGui.QApplication([])
    game = MainWindow()
    #game.tiempo_intervalo = 0
    game.show()
    app.exec_()