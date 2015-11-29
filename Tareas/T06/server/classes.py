import hashlib
import os 

class User:

	def __init__(self,user,pw):
		self.user = user
		self.password = pw
		self.amigos = [] #Strings users
		self.archivos = []

	def agregar_amigo(self,user):
		selg.amigos.append

	def mostrar_amigos(self):
		pass

	def __str__(self):
		return self.user


class Nodo:

	def __init__(self,parent,name,root):
		self.root = root
		self.name = name
		self.parent = parent
		self.files = []
		self.sons = []
		for d in os.listdir(root):
			if "." in d:
				self.files.append(d)
			else:
				self.sons.append(Nodo(self,d,root+"/"+d))

	def __repr__2(self):
		tupla = (self.name,[],[])
		for f in self.files:
			tupla[1].append(f)
		for s in self.sons:
			tupla[2].append(s.__repr__2())
		return tupla

	def __repr__(self):
		return str(self.__repr__2())
