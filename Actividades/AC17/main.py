import random
from collections import deque
nombres = ["juan","pedro","carlos","felipe","florencia","tamara","ignacio","gonzalo","claudia"]
apellidos = ["perez", "johnson","jackson","felipeson","carlson","peterson"]
class Mesa():

	def __init__(self):
		self.jugador1 = Jugador()
		self.jugador2 = Jugador()
		self.lista_espera = deque()
		self.lista_espera.appendleft(Jugador())
		self.tiempo_partido = round(random.uniform(4,6))
		self.tiempo_partido_actual = 0

		self.t = 0
		self.t_proximo_jugador = self.t + round(random.expovariate(1/15) + 0.5)

	def pasar_minuto(self):
		print("Minuto {} del almuerzo".format(self.t))
		print("Se estan enfrentando {} y {}".format(self.jugador1,self.jugador2))
		print("Estan esperando su turno: {}".format(self.lista_espera))

		if self.t == self.t_proximo_jugador:
			self.t_proximo_jugador = self.t + round(random.expovariate(1/15) + 0.5)
			nuevo_jugador = self.agregar_jugador()
			print("{} se ha unido a la fila.".format(nuevo_jugador))
		if self.tiempo_partido_actual == self.tiempo_partido:
			if not self.terminar_partido():
				return False
		else:
			self.tiempo_partido_actual += 1
		return True



	def terminar_partido(self):
		self.jugador1.partidos_jugados += 1
		self.jugador2.partidos_jugados += 1
		self.tiempo_partido_actual = 0
		self.tiempo_partido = round(random.uniform(4,6))
		ganador = self.elegir_ganador()
		print("Ha ganado {}".format(ganador))
		if len(self.lista_espera) == 0:
			print("No quedan mas jugadores en la fila =(")
			return False
		nuevo_jugador = self.lista_espera.pop()
		if ganador == self.jugador1:
			if not self.jugador2.retirarse():
				self.lista_espera.appendleft(self.jugador2)
			self.jugador2 = nuevo_jugador
		else:
			if not self.jugador1.retirarse():
				self.lista_espera.appendleft(self.jugador1)
			self.jugador1 = nuevo_jugador
		return True


	def elegir_ganador(self):
		#Sumamos las habilidades, para que la probabilidad de ganar
		#sea proporcional a su habilidad.
		prob_total = self.jugador1.habilidad + self.jugador2.habilidad
		if random.random() * prob_total < self.jugador1.habilidad:
			return self.jugador1
		else:
			return self.jugador2

	def agregar_jugador(self):
		nuevo_jugador = Jugador()
		self.lista_espera.appendleft(nuevo_jugador)
		return nuevo_jugador

	def run(self):
		while self.t < 70:
			if not self.pasar_minuto():
				break
			self.t += 1
		print("Ha terminado la simulacion, a clases !!!")
		

class Jugador:

	def __init__(self):
		self.nombre = random.choice(nombres) + " " + random.choice(apellidos)
		self.habilidad = random.uniform(1,10)
		self.partidos_jugados = 0

	def retirarse(self):
		return random.randint(0,10) < self.partidos_jugados

	def __repr__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

mesa = Mesa()
mesa.run()