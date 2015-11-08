from PyQt4 import QtGui, uic, QtCore
import random
import threading
from math import atan2, degrees, pi
import os
import random
import time
from backend import *

class Player(QtGui.QLabel):

    def __init__(self,game):
        super().__init__(game)
        self.health = 100
        self.ammo = 50
        self.game = game
        self.vector = 0,0
        self.balas = []
        self.life_bar = QtGui.QProgressBar(self.game)
        self.life_bar.setValue(self.health)
        self.life_bar.setMaximum(100)
        self.ammo_counter = QtGui.QLCDNumber(self.game)
        self.ammo_counter.move(500,0)
        self.ammo_counter.display(self.ammo)
        self.ammo_counter.show()

        #self.setGeometry(40, 40, 50, 50)
        self.setScaledContents(True)
        #use full ABSOLUTE path to the image, not relative
        self.pixmap = QtGui.QPixmap(os.getcwd() + "/sprites/player.png")
        self.setPixmap(self.pixmap)

    def mover(self, ort = False):
        self.calcular_vector(self.game.mx,self.game.my)
        self.rotate()
        if not ort:
            xx,yy = self.vector
        elif ort == "d":
            xx,yy = self.vectorOrtogonal()
        elif ort == "a":
            xx,yy = self.vectorOrtogonal()
            xx = -xx
            yy = -yy
        elif ort == "s":
            xx,yy = self.vector
            xx,yy = -xx,-yy
        x = self.x()
        y = self.y()
        self.move(x+xx*5,y+yy*5)

    def vectorOrtogonal(self):
        vector = -self.vector[1],self.vector[0]
        return vector

    def rotate(self):
        del self.pixmap
        theta = degrees(atan2(self.vector[1],self.vector[0]) + pi/2)
        self.pixmap = QtGui.QPixmap(os.getcwd() + "/sprites/player.png")
        self.pixmap = self.pixmap.scaledToHeight(60, QtCore.Qt.SmoothTransformation)
        self.pixmap = self.pixmap.transformed(QtGui.QTransform().rotate(theta))
        self.setPixmap(self.pixmap)

    def calcular_vector(self,m_x,m_y):
        x = self.x()
        y = self.y()
        x,y = m_x - x, m_y - y
        n = (x**2 + y**2)**0.5
        if n == 0:
            self.vector = 0,0
            return
        self.vector = x/n, y/n


    def shoot(self):
        if self.ammo > 0:
            self.balas.append(Bala(self.game))
            self.ammo -= 1
            self.ammo_counter.display(self.ammo)

    def morir(self):
        self.isAlive = False
        self.game.isAlive = False
        menu = self.game.mainwindow.menu_widget()
        self.game.mainwindow.setCentralWidget()

class Zombie(QtGui.QLabel):
    def __init__(self,game):
        super().__init__(game)
        self.esperar = 0
        self.game = game
        self.vector = 0,0
        self.setScaledContents(True)
        #use full ABSOLUTE path to the image, not relative
        self.pixmap = QtGui.QPixmap(os.getcwd() + "/sprites/pacman.png")
        self.setPixmap(self.pixmap)
        pos = self.aparecer()
        print(pos)
        self.move(pos[0],pos[1])
        self.show()

        #Thread part
        self.isAlive = True
        self.worker = ZombieWorker(self)
        self.worker.start()

    def aparecer(self):
        if random.randint(1,2) == 1:
            return 0,random.randint(0,200)
        else:
            return random.randint(0,200),0

    def mover(self):
        if self.x() - 15 <= self.game.persona.x() <= self.x() + 15\
        and self.y() - 15 <= self.game.persona.y() <= self.y() + 15:
            self.attack()
        self.calcular_vector()
        xx,yy = self.vector
        x = self.x()
        y = self.y()
        self.move(x+xx*1.5,y+yy*1.5)
        self.rotate()

    def attack(self):
        if self.esperar > 0:
            self.esperar -= 1
            return
        self.game.persona.health -= 1
        if self.game.persona.health <= 0:
            self.game.persona.morir()
        life = self.game.persona.health
        self.game.persona.life_bar.setValue(life)
        self.esperar = 100
        print("ataque")

    def calcular_vector(self):
        m_x = self.game.persona.x()
        m_y = self.game.persona.y()
        x = self.x()
        y = self.y()
        x,y = m_x - x, m_y - y
        n = (x**2 + y**2)**0.5
        if n == 0:
            self.vector = 0,0
            return
        self.vector = x/n , y/n

    def rotate(self):
        theta = degrees(atan2(self.vector[1],self.vector[0]))
        self.pixmap = QtGui.QPixmap(os.getcwd() + "/sprites/pacman.png")
        self.pixmap = self.pixmap.transformed(QtGui.QTransform().rotate(theta))
        self.setPixmap(self.pixmap)

    def morir(self):
        self.isAlive = False

class Bala(QtGui.QLabel):

    def __init__(self,game):
        super().__init__(game)
        self.game = game
        self.isAlive = True
        self.inicial = self.game.persona.x(),self.game.persona.y()
        self.vector = self.calcular_vector()
        self.max_dist = 400
        self.setScaledContents(True)
        self.pixmap = QtGui.QPixmap(os.getcwd() + "/sprites/bala.png")
        self.setPixmap(self.pixmap)
        self.move(self.inicial[0],self.inicial[1])
        self.show()

        #Thread part
        self.worker = BalaWorker(self)
        self.worker.start()

    def mover(self,a):
        if a != '':
            self.game.persona.balas.remove(self)
            return
        diferencia = ((self.x()-self.inicial[0])**2 +
                     (self.y()-self.inicial[1])**2) ** 0.5
        if diferencia > self.max_dist:
            self.isAlive = False

            return
        self.verificar()
        xx = self.vector[0]
        yy = self.vector[1]
        self.move(self.x()+xx*4,self.y()+yy*4)

    def calcular_vector(self):
        m_x,m_y = self.game.mx, self.game.my
        x = self.game.persona.x()
        y = self.game.persona.y()
        x,y = m_x - x, m_y - y
        n = (x**2 + y**2)**0.5
        if n == 0:
            
            return 0,0
        print(x/n,y/n)
        return x/n , y/n

    def verificar(self):
        for zombie in self.game.zombies:
            if self.x() - 20 <= zombie.x() <= self.x() + 20\
            and self.y() - 20 <= zombie.y() <= self.y() + 20:
                zombie.morir()
                break

class Supply():
    types = ["ammo", "health"]
    def __init__(self,game):
        print("Supply here!")
        self.type = random.choice(types)
        self.supply = random.randint(10,40)
        self.game = game
        self.isAlive = True
        self.max_dist = 400
        self.setScaledContents(True)
        self.pixmap = QtGui.QPixmap(os.getcwd() + "/sprites/supply.png")
        self.setScaledContents(True)
        self.setGeometry(0,0,15,15)
        self.setPixmap(self.pixmap)
        self.move(self.inicial[0],self.inicial[1])
        self.show()

    def verificar(self):
        if self.x() - 15  <= self.game.persona.x() <= self.x() + 15\
        and self.y() - 15 <= self.game.persona.y() <= self.y() + 15:
            self.entregar()

    def entregar(self):
        if self.type == "ammo":
            self.game.persona.ammo += self.supply
        else:
            self.game.persona.health += self.supply
        self.hide()

class ListaZombies(list):
    def __init__(self):
        super().__init__()
        lock = threading.lock()
        pass