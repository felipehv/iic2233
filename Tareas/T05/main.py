from PyQt4 import QtGui, uic, QtCore, QtCore
import threading
from classes import *
import os
# Cargamos la interfaz creada en QtDesigner
ui = uic.loadUiType("ui.ui")

class Game(ui[0], ui[1]):
    def __init__(self,app):
        super().__init__()
        self.app = app
        self.setupUi(self) 
        self.botonComenzar.clicked.connect(self.comenzar)
        self.grid.setSpacing(0)
        #self._create_thread()
        self.mouseEvent = QtGui.QMouseEvent()

        self.player = Player(0,0,self)

    def comenzar(self):
        sender = self.sender()
        pos = self.mouseEvent.x()
        sender.setText('Hola')
        sender.resize(sender.sizeHint())

    def actualizar_barra(self,mensaje):
        self.statusBar().showMessage('Cambié el Status')

    def agregar_player(self, filename, x, y, theta=0):
        path = os.path.join(os.path.dirname(__file__), "sprites", filename)
        pixmap = QtGui.QPixmap(path)
        label = self.grid.itemAtPosition(x, y).widget()
        pixmap = pixmap.scaled(self.img_size, QtCore.Qt.KeepAspectRatio)

        if theta != 0:
            pixmap = pixmap.transformed(QtGui.QTransform().rotate(theta))

        label.setPixmap(pixmap)
    """
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
    game = Game(app)
    game.agregar_imagen("ball.png",10,20)
    #game.tiempo_intervalo = 0
    game.show()
    app.exec_()