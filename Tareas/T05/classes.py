from PyQt4 import QtGui, uic, QtCore
import random
import threading
class Player:

	def __init__(self,x,y,game):
		self.health = 1000
		self.ammo = 20
		self.pos = (x,y)
		self.game = game

	def move(self,x,y):
		self.label1.move(x,y)

	def attack(self):
		pass

class Zombie():
	def __init__(self,x,y):
		pass

	def attack(self,player):
		player.health -= random.randint()

	def recta(self,player):
		player_pos = player.pos()
"""
class Worker(QtCore.QThread):

    def __init__(self, queue, interval):
        super().__init__()
        self.queue = queue
        self.interval = interval

    def __del__(self):
        self.exiting = True
        self.wait()

    def run(self):
        while True:
            if len(self.queue) > 0:
                to_do = self.queue.popleft()
                self.emit(QtCore.SIGNAL("do"), to_do)
                time.sleep(self.interval)
            else:
                time.sleep(0.01)
"""