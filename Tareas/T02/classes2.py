from estructuras import *
import random
class Puerto:
	completes = 0
	def __init__(self,ide):
		self.ide = ide
		self.cantidad_conexiones = 0
		self.conexion_actual = 0
		self.n = 0
		self.salidas = []
		self.entradas = []
		self.complete = False
		self.lastconnection = 0

		"""
		Conexiones por puerto para ver si son random o no.
		"""
		self.salidas2 = []

	def __repr__(self):
		return str(self.ide)	

	def actualizarLista(self):
		for i in range(self.cantidad_conexiones):
			self.salidas2.append([])

	def connect(self,func):
		if self.conexion_actual >= self.cantidad_conexiones and not self.complete:
			self.conexion_actual -= self.cantidad_conexiones
			self.complete = True
			Puerto.completes += 1
			if Puerto.completes % 50 == 0:
				print(Puerto.completes)
				#a = input()
			self.lastconnection = self.conexion_actual
			func(self.conexion_actual)
		elif self.n >= 4 and not self.complete:
			self.n = 0
			self.lastconnection = self.conexion_actual
			func(self.conexion_actual)
			self.conexion_actual += 1
		elif self.n < 4 and not self.complete:
			self.n += 1
			self.lastconnection = self.conexion_actual
			func(self.conexion_actual)
		elif self.conexion_actual >= self.cantidad_conexiones:
			self.conexion_actual -= self.cantidad_conexiones
			self.lastconnection = self.conexion_actual
			func(self.conexion_actual)
		else:
			self.conexion_actual += 1
			self.lastconnection = self.conexion_actual
			func(self.conexion_actual)
