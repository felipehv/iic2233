from PyQt4 import QtGui, uic, QtCore
import random
import threading
from math import atan2, degrees, pi
import os
class Player(QtGui.QLabel):

    def __init__(self,game):
        super().__init__(game)
        self.health = 1000
        self.ammo = 20
        self.game = game
        self.vector = 0,0

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
        else:
            xx,yy = self.vectorOrtogonal()
        x = self.x()
        y = self.y()
        self.move(x+xx*6,y+yy*6)

    def calcular_vector(self,m_x,m_y):
        x = self.x()
        y = self.y()
        x,y = m_x - x, m_y - y
        n = (x**2 + y**2)**0.5
        if n == 0:
            return 0,0
        self.persona.vector = x/n , y/n

    def vectorOrtogonal(self):
        vector = -self.vector[1],self.vector[0]
        return vector

    def rotate(self):
        theta = degrees(atan2(self.vector[1],self.vector[0]) + pi/2)
        self.pixmap = QtGui.QPixmap(os.getcwd() + "/sprites/player.png")
        self.pixmap = self.pixmap.transformed(QtGui.QTransform().rotate(theta))
        self.setPixmap(self.pixmap)

    def calcular_vector(self,m_x,m_y):
        x = self.x()
        y = self.y()
        x,y = m_x - x, m_y - y
        n = (x**2 + y**2)**0.5
        self.vector = x/n , y/n

    def caminar(self):
        pass

class Zombie(QtGui.QLabel):
    def __init__(self,game):
        super().__init__(game)
        self.health = 1000
        self.game = game
        self.vector = 0,0
        #self.setGeometry(10, 10, 50, 50)
        #self.setScaledContents(True)
        #use full ABSOLUTE path to the image, not relative
        self.pixmap = QtGui.QPixmap(os.getcwd() + "/sprites/player.png")
        self.setPixmap(self.pixmap)

    def mover(self):
        self.vector()
        xx,yy = self.vector
        x = self.x()
        y = self.y()
        self.move(x+xx*2,y+yy*2)

    def attack(self,player):
        player.health -= random.randint()

    def calcular_vector(self,m_x,m_y):
        x = self.game.persona.x()
        y = self.game.persona.y()
        x,y = m_x - x, m_y - y
        n = (x**2 + y**2)**0.5
        self.persona.vector = x/n , y/n

    def mover():
        self.move(self.x*6,self.y*6)
