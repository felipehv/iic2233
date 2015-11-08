from PyQt4 import QtGui, uic, QtCore
import time
import random

class ZombieWorker(QtCore.QThread):
    trigger = QtCore.pyqtSignal()
    
    def __init__(self, parent):
        """
        Un Character es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.trigger.connect(parent.mover)
        self.parent = parent

    def __del__(self):
        self.exiting = True
        self.wait()
        
    def run(self):
        time.sleep(1)
        print("Me comienzo a mover")
        while self.parent.isAlive:
            self.trigger.emit()
            time.sleep(0.01)
        self.exiting = True
        self.parent.hide()
        self.parent.game.zombies.remove(self.parent)

class BalaWorker(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)
    
    def __init__(self, parent):
        super().__init__()
        self.trigger.connect(parent.mover)
        self.parent = parent

    def run(self):
        time.sleep(0.01)
        print("Pium")
        while self.parent.isAlive:
             self.trigger.emit("")
             time.sleep(0.01)
        self.parent.hide()
        self.trigger.emit("die")
        self.exiting = True

class GameWorker(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)
    
    def __init__(self, parent):
        super().__init__()
        self.trigger.connect(parent.accion)
        self.parent = parent

    def funcion(self,t):
        lamda = round(random.expovariate(1/10) + 0.5)
        lamda = lamda * t
        return lamda

    class event:
        def __init__(self,hola):
            self.a = hola
        
    def run(self):
        self.parent.t = 0
        prox_zombie = self.funcion(self.parent.t)
        while self.parent.isAlive:
            if self.parent.t >= prox_zombie:
                self.trigger.emit("zom")
                prox_zombie = self.funcion(self.parent.t)
            self.trigger.emit("sup")
            time.sleep(1)
            self.parent.t += 1
        self.exiting = True

class SupplyWorker(QtCore.QThread):
    trigger = QtCore.pyqtSignal()
    
    def __init__(self, parent):
        super().__init__()
        self.trigger.connect(parent.verificar)
        self.parent = parent
        
    def run(self):
        while self.parent.isAlive:
            self.trigger.emit()
            time.sleep(0.1)
        self.exiting = True

class LoadingWorker(QtCore.QThread):
    trigger = QtCore.pyqtSignal()
    
    def __init__(self, parent):
        super().__init__()
        self.trigger.connect(parent.cargar)
        self.parent = parent
        
    def run(self):
        while self.parent.isAlive:
            self.trigger.emit()
            time.sleep(1)
        self.exiting = True