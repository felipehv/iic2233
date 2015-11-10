from PyQt4 import QtGui, uic, QtCore
import time
import random

class ZombieWorker(QtCore.QThread):
    trigger = QtCore.pyqtSignal(bool)
    
    def __init__(self, parent):
        super().__init__()
        self.trigger.connect(parent.mover)
        self.parent = parent
        self.paused = False

    def __del__(self):
        self.exiting = True
        self.wait()

    def pause(self):
        self.paused = True
        print("Zombies pausados")
    def unpause(self):
        self.paused = False
        
    def run(self):
        time.sleep(1)
        print("Me comienzo a mover")
        while self.parent.isAlive:
            if not self.paused:
                self.trigger.emit(False)
            time.sleep(0.01)
        self.trigger.emit(True)
        time.sleep(1)
        self.exiting = True
        self.parent.hide()
        self.parent.game.zombies.remove(self.parent)

class BalaWorker(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)
    
    def __init__(self, parent):
        super().__init__()
        self.trigger.connect(parent.mover)
        self.parent = parent
        self.paused = False

    def pause(self):
        self.paused = True
        print("Balas Pausadas")
    def unpause(self):
        self.paused = False

    def run(self):
        time.sleep(0.01)
        print("Pium")
        while self.parent.isAlive:
            if not self.paused:
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
        self.paused = False

    def funcion(self,t):
        lamda = round(random.expovariate(1/10) + 0.5)
        #if t>0:
        #    lamda = lamda//t + t
        return t + lamda

    def pause(self):
        self.paused = True
        print("Juego pausado")
    def unpause(self):
        self.paused = False
        
    def run(self):
        self.parent.t = 0
        prox_zombie = self.funcion(self.parent.t)
        while self.parent.isAlive:
            if not self.paused:
                self.parent.t += 1
                if self.parent.t >= prox_zombie:
                    self.trigger.emit("zom")
                    prox_zombie = self.funcion(self.parent.t)
                if self.parent.t % 10 == 0:
                    self.trigger.emit("sup")
                self.trigger.emit("time")
            time.sleep(1)
        self.exiting = True

class SupplyWorker(QtCore.QThread):
    trigger = QtCore.pyqtSignal()
    
    def __init__(self, parent):
        super().__init__()
        self.trigger.connect(parent.verificar)
        self.parent = parent
        self.paused = False

    def pause(self):
        self.paused = True
        print("Supplies pausado")
    def unpause(self):
        self.paused = False
        
    def run(self):
        while self.parent.isAlive:
            if not self.paused:
                self.trigger.emit()
            time.sleep(0.1)
        self.parent.game.supplies.remove(self.parent)
        self.exiting = True

class LoadingWorker(QtCore.QThread):
    trigger = QtCore.pyqtSignal()
    
    def __init__(self, parent):
        super().__init__()
        self.trigger.connect(parent.cargar)
        self.parent = parent
        self.paused = False

    def pause(self):
        self.paused = True
    def unpause(self):
        self.paused = False
        
    def run(self):
        while self.parent.isAlive:
            if not self.paused:
                self.trigger.emit()
            time.sleep(1)
        self.exiting = True