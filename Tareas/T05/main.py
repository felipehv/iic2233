from PyQt4 import QtGui, uic, QtCore, QtCore, QLabel
import threading
from classes import *
import os
from math import atan
# Cargamos la interfaz creada en QtDesigner
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
        self.player = Player(0,0,self)
        self.mainwindow = main

    def init_GUI(self):
        self.persona = QtGui.QPushButton("Jugador",self)
        self.persona.clicked.connect(self.mover)

    def mover(self):
        x = self.persona.x
        sender = self.sender()
        sender.move(20,20)
        self.mainwindow.actualizar_barra(MouseCoordinates())

    def vector(self):
        pass

    def vectorOrtogonal(self):
        vector = self.vector()


    class MouseCoordinates(QLabel):
     
        def __init__(self, parent=None):
            super(MouseCoordinates, self).__init__(parent)
     
            self.update()
     
        def update(self):
     
            currentPos = QCursor.pos()
     
            x = currentPos.x()
            y = currentPos.y()
     
            self.setText(" Mouse: %d / %d " % (x, y))
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


    @property
    def tiempo_intervalo(self):
        return self.thread.interval

    @tiempo_intervalo.setter
    def tiempo_intervalo(self, value):
        self.thread.interval = value

    def _create_thread(self):
        self.thread = Worker(self.__act_queue, 0)
        self.connect(self.thread, QtCore.SIGNAL("do"), self.__do)
        self.thread.start()
    """

if __name__ == '__main__':
    # Inicializamos la aplicación de la misma forma que 
    # cuando la creamos manualmente
    app = QtGui.QApplication([])
    game = MainWindow()
    #game.tiempo_intervalo = 0
    game.show()
    app.exec_()