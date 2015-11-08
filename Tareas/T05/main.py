from PyQt4 import QtGui, uic, QtCore, QtCore
import threading
from classes import *
import os
from math import atan2, degrees
import time
from collections import deque

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()
        self.game_widget = None
        self.menu_widget = MenuWidget(self)
        self.setCentralWidget(self.menu_widget)
        self.setStyleSheet("QMainWindow border-image: url({}/sprites/image.jpg);".format(os.getcwd()))
        self.setGeometry(50,50,800,600)
        self.pause = False

    def actualizar_barra(self,mensaje):
        self.statusBar().showMessage(mensaje)

    def keyPressEvent(self,event):
        if self.game_widget:
            if event.text() == "w" and not self.pause:
                self.game_widget.persona.mover()
            elif event.text() == "d" and not self.pause:
                self.game_widget.persona.mover("d")
            elif event.text() == "a" and not self.pause:
                self.game_widget.persona.mover("a")
            elif event.text() == "s" and not self.pause:
                self.game_widget.persona.mover("s")
            elif event.text() == "p" and not self.pause:
                self.pauseIt()
                self.pause = True
            elif event.text() == "e" and self.pause:
                self.unpauseIt()
                self.pause = False

    def start(self):
        self.game_widget = GameWidget(self)
        self.setCentralWidget(self.game_widget)

    def pauseIt(self):
        self.pause_button = QtGui.QLabel(self)
        self.pause_button.setText("Juego en pausa <enter> para continuar.")
        self.pause_button.resize(self.pause_button.sizeHint())
        self.pause_button.move(0,400)
        self.pause_button.show()
        #Pause
        self.game_widget.worker.pause()
        for zombie in self.game_widget.zombies:
            zombie.worker.pause()
        for bala in self.game_widget.persona.balas:
            bala.worker.pause()
        for supply in self.game_widget.supplies:
            supply.worker.pause()

    def unpauseIt(self):
        self.pause_button.hide()
        #Unpause
        self.game_widget.worker.unpause()
        for zombie in self.game_widget.zombies:
            zombie.worker.unpause()
        for bala in self.game_widget.persona.balas:
            bala.worker.unpause()
        for supply in self.game_widget.supplies:
            supply.worker.unpause()


class MenuWidget(QtGui.QWidget):

    def __init__(self,main):
        super().__init__()
        self.init_GUI()
        self.mainwindow = main

    def init_GUI(self):
        self.fondo = QtGui.QLabel(self)
        self.fondo.setPixmap
        pixmap = QtGui.QPixmap(os.getcwd() + "/sprites/fondo_menu.png")
        self.fondo.setPixmap(pixmap)

        self.start_button = QtGui.QPushButton('Comenzar el juego', self)
        self.start_button.resize(self.start_button.sizeHint())
        self.start_button.move(400,400)
        self.setGeometry(200,200,200,200)
        self.start_button.clicked.connect(self.empezar)

    def empezar(self):
        self.mainwindow.loading_widget = Loading(self.mainwindow)
        self.mainwindow.setCentralWidget(self.mainwindow.loading_widget)


class GameWidget(QtGui.QWidget):
    def __init__(self,main):
        super().__init__()
        self.zombies = []
        self.init_GUI() 
        self.setMouseTracking(True)
        self.mainwindow = main
        self.isAlive = True
        self.supplies = []

        #Thread
        self.worker = GameWorker(self)
        self.worker.start()

    def init_GUI(self):
        self.persona = Player(self)
        self.persona.move(50,50)

    def mousePressEvent(self,event):
        if not self.worker.paused:
            print(event.x(),event.y())
            self.persona.shoot()

    def mouseMoveEvent(self,event):
        if not self.worker.paused:
            self.mx = event.x()
            self.my = event.y()
            self.persona.calcular_vector(event.x(),event.y())   
            self.persona.rotate()

    def keyPressEvent(self,event):
        print(event)
        if event.text() == "w" :
            self.persona.mover()
        elif event.text() == "d":
            self.persona.mover("d")
        elif event.text() == "p":
            self.mainwindow.setCentralWidget(self.mainwindow.pause_widget)

    def accion(self,action):
        if action == "sup":
            self.supply()
        elif action == "zom":
            self.zombies.append(Zombie(self))

    def supply(self):
        self.supplies.append(Supply(self))

loading_ui = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "loading.ui")
)
class Loading(*loading_ui):

    def __init__(self,main):
        super().__init__()
        self.isAlive = True
        self.setupUi(self)
        #self.setStyleSheet("background-image: url({}/sprites/image.jpg);".format(os.getcwd()))
        self.mainwindow = main
        self.worker = LoadingWorker(self)
        self.worker.start()
        self.progressBar.show()

    def cargar(self):
        valor = self.progressBar.value()
        suma = random.randint(15,15)
        if valor + suma >= 100:
            self.progressBar.setValue(valor + suma)
            self.isAlive = False
            self.mainwindow.start()
            time.sleep(2)
        self.progressBar.setValue(valor + suma)

if __name__ == '__main__':
    app = QtGui.QApplication([])
    game = MainWindow()
    game.show()
    app.exec_()