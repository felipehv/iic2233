class Audifono:
	def __init__(self,frecMin,frecMax,impedancia,VolumenMax,**kwargs):
		print(frecMin)
		self.frecMin = frecMin
		self.frecMax = frecMax
		self.impedancia = impedancia
		self.VolumenMax = VolumenMax

	def escuchar(self,cancion):
		print(('La cancion {} esta siendo reproducida en este Audifono').format(cancion))

class OverEar(Audifono):
	def __init__(self,aislacion,**kwargs):
		super().__init__(**kwargs)
		self.aislacion = aislacion

	def escuchar(self,cancion):
		super().escuchar(cancion)

class Intraaurales(Audifono):
	def __init__(self,incomodidad,**kwargs):
		super().__init__(**kwargs)
		self.incomodidad = incomodidad

	def escuchar(self,cancion):
		super().escuchar(cancion)

class Inalambrico(Audifono):
	def __init__(self,rango,**kwargs):
		super().__init__(**kwargs)
		self.rango = rango
		self.conectado = False

	def escuchar(self,cancion):
		if self.conectado:
			print(('La cancion {} esta siendo reproducida en un audifono inalambrico.').format(cancion))
		else:
			print('Audifono desconectado')

	def conectar(self,rango):
		if rango <= self.rango:
			print('Conectado')
			self.conectado = True
		else:
			print('Error, el reproductor esta muy lejos.')

class Bluetooth(Inalambrico):
	def __init__(self,identificador,**kwargs):
		super().__init__(**kwargs)
		self.identificador = identificador

	def escuchar(self,cancion):
		if self.conectado:
			print(('La cancion {} esta siendo reproducida en un audifono Bluetooth').format(cancion))

if __name__ == '__main__':
	audifono = Audifono(frecMin=20,frecMax=18000,impedancia=15,VolumenMax=100)
	inalambrico = Inalambrico(rango=10,frecMin=18,frecMax=15000,
					impedancia=10,VolumenMax=60)
	bluetooth = Bluetooth(frecMin=18,frecMax=15000,\
					impedancia=10,VolumenMax=60,rango=10,identificador=2233)
	audifono.escuchar('Money')
	inalambrico.conectar(12)
	inalambrico.conectar(8)
	inalambrico.escuchar('Money')
	bluetooth.conectar(2)
	bluetooth.conectar(120)
	bluetooth.escuchar('Money')