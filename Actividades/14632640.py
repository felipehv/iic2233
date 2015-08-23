#Actividad 1 IIC2233
import random,datetime
tipos = [('RRLyrae',3),('Eclipsing Binaries',4),('Mira',6),('Cepheids',7)]

def promedio(elementos):
	suma = 0
	for i in elementos:
		suma += i
	return suma / len(elementos)

def varianza(elementos):
	x = promedio(elementos)
	suma = 0
	for i in elementos:
		suma += (i - x)**2
	return suma / len(elementos)



class Estrella:
	def __init__(self,brillo,tipo,coordenadaRA,coordenadaDEC):
		self.brillo = brillo
		self.tipo = tipo
		self.RA = coordenadaRA
		self.DEC = coordenadaDEC
		self.id = id(self)		#Uso el id que da por defecto python.
		self.historia_brillos = [brillo]
		self.observaciones = []

	def variar_brillo(self,variacion):
		self.brillo += variacion

	def ObtenerPromedio(self):
		return promedio(self.historia_brillos)

	def ObtenerVarianza(self):
		return varianza(self.historia_brillos)

	def agregarObservacion(self,instante,brillo):
		self.observaciones.append(Observacion(instante,brillo))

class Observacion:
	def __init__(self,instante,magnitud_brillo):
		self.instante = instante
		self.magnitud_brillo = magnitud_brillo

class Field:
	def __init__(self):
		self.estrellas = []

	def agregarEstrella(self,brillo,tipo,coordenadaRA,coordenadaDEC):
		self.estrellas.append(Estrella(brillo,tipo,coordenadaRA,coordenadaDEC))

class Cielo:
	def __init__(self):
		self.fields = []

	def agregarField(self):
		self.fields.append(Field())

def poblar():
	cielo = Cielo()
	cielo.agregarField()
	cielo.agregarField()
	for field in cielo.fields:
		for i in range(3):
			brillo = random.choice(tipos)[1]
			tipo = random.choice(tipos)[0]
			coordenadaRA = random.randint(-1000,1000)
			coordenadaDEC = random.randint(-1000,1000)
			field.agregarEstrella(brillo,tipo,coordenadaRA,coordenadaDEC)
		for estrella in field.estrellas:
			for i in range(4):
				brillo = estrella.brillo
				instante = datetime.datetime.now()
				estrella.agregarObservacion(instante,brillo)
poblar()