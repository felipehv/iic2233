from estructuras import *
import random
class Puerto:
	def __init__(self,ide):
		self.ide = ide
		self.cantidad_conexiones = 0
		self.conexion_actual = 0
		self.n = 0
		self.salidas = myList()
		self.entradas = myList()
		self.complete = False
		#self.conexiones_realizadas = myList()

	def __repr__(self):
		return str(self.ide)	

	def connect(self,func):
		if self.conexion_actual >= self.cantidad_conexiones:
			self.conexion_actual -= self.cantidad_conexiones
			self.complete = True
			func(self.conexion_actual)
		elif self.n > 4 and not self.complete:
			self.n = 0
			self.conexion_actual += 1
			func(self.conexion_actual)
		elif self.n <= 4 and not self.complete:
			self.n += 1
			func(self.conexion_actual)
		else:
			self.conexion_actual += 1
			func(self.conexion_actual)




