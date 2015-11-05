from PyQt4 import QtGui, uic, QtCore, QtCore
import threading
from classes import *
import os
from math import atan2

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

class MenuWidget(QtGui.QWidget):

    def __init__(self,main):
        super().__init__()
        self.init_GUI()
        self.MainWindow = main

    def init_GUI(self):
        self.start_button = QtGui.QPushButton('Comenzar el juego', self)
        self.start_button.resize(self.start_button.sizeHint())
        self.start_button.move(5, 70)
        self.start_button.clicked.connect(self.empezar)

    def empezar(self):
        sender = self.sender()
        self.MainWindow.setCentralWidget(self.MainWindow.game_widget)

class PauseWidget(QtGui.QWidget):
    def __init__(self,main):
        pass

class GameWidget(QtGui.QWidget):
    def __init__(self,main):
        super().__init__()
        self.init_GUI() 
        self.setMouseTracking(True)
        self.mainwindow = main

    def init_GUI(self):
        self.persona = QtGui.QLabel(self)
        self.persona.setGeometry(10, 10, 50, 50)
        #use full ABSOLUTE path to the image, not relative
        self.persona.setPixmap(QtGui.QPixmap(os.getcwd() + "/sprites/ball.png"))

    def mover(self):
        xx,yy = self.vector
        #sender = self.sender()
        x = self.persona.x()
        y = self.persona.y()
        self.persona.move(x+xx*2,y+yy*2)

    def calcular_vector(self,m_x,m_y):
        x = self.persona.x()
        y = self.persona.y()
        x,y = m_x - x, m_y - y
        n = (x**2 + y**2)**0.5
        self.vector = x/n , y/n

    def vectorOrtogonal(self):
        vector = self.vector()

    def rotar(self):
        pass

    def mousePressEvent(self,event):
        print('hola')

    def keyPressEvent(self,event):
        sender = self.sender()
        print(event.text())
        if event.text() == "w":
            self.mover()
    def mouseMoveEvent(self,event):
        self.calcular_vector(event.x(),event.y())
        self.rotar()


class MouseCoordinates():
 
    def __init__(self, parent=None):     
        self.update()
 
    def update(self):
 
        currentPos = QCursor.pos()
 
        x = currentPos.x()
        y = currentPos.y()
        return x,y


    """
    def agregar_player(self, filename, x, y, theta=0):
        path = os.path.join(os.path.dirname(__file__), "sprites", filename)
        pixmap = QtGui.QPixmap(path)
        label = self.grid.grid_2.itemAtPosition(x, y).widget()
        pixmap = pixmap.scaled(self.img_size, QtCore.Qt.KeepAspectRatio)

        if theta != 0:
            pixmap = pixmap.transformed(QtGui.QTransform().rotate(theta))

        label.setPixmap(pixmap)

    def agregar_imagen(self,filename, x, y):
        path = os.path.join(os.path.dirname(__file__), "assets", filename)
        pixmap = QtGui.QPixmap(path)
        label = self.grid_2.itemAtPosition(x, y)
        pixmap = pixmap.scaled(self.img_size, QtCore.Qt.KeepAspectRatio)

        #if theta != 0:
        #    pixmap = pixmap.transformed(QtGui.QTransform().rotate(theta))
        #if reflection:
        #    pixmap = pixmap.transformed(QtGui.QTransform().scale(-1, 1))

        label.setPixmap(pixmap)
    """

if __name__ == '__main__':
    # Inicializamos la aplicación de la misma forma que 
    # cuando la creamos manualmente
    app = QtGui.QApplication([])
    game = MainWindow()
    #game.tiempo_intervalo = 0
    game.show()
    app.exec_()