"""
Classes
"""


class Esquina:

	def __init__(self):
		self.semaforo = True


class Vehiculo()

	def __init__(self, env, ciudad):
		self.env = env
		self.ciudad = ciudad


class Ambulance()

	def __init__(self, **kwargs):
		self._velocidad = 0.5
		self.sirena = False
		super().__init__(**kwargs)


	@property
	def velocidad(self):
		if self.sirena:
			return 1
	    return self._velocidad
	

class CarroBomba(Vehiculo):

	def __init__(self,**kwargs):
		self._velocidad = 0.5
		self.sirena = False
		super().__init__(**kwargs)

	@property
	def velocidad(self):
		if self.sirena:
			return 1
	    return self._velocidad


Madera: 40 a 60 minutos
Ladrillo: 50 a 80 minutos
Hormigon: 60 a 100 minutos
Metal: 60 a 200 minuto

class Casa:
	resistencias = {"madera":(40,60),"ladrillo":(50,80),"hormigon":(60,100),"metal":(60,200)}
	def __init__(self,material,posicion):
		self.material = material
		self._resistencia_material = 0

	@property
	def resistencia_material(self):
	    return self._resistencia_material
	


