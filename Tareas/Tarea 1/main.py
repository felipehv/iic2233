import lib
import datetime

alumnos = []
class Persona:
	def __init__(self,nombre,clave,usuario,**kwargs):
		self.nombre = nombre
		self.user = usuario
		self.password = clave
		self.isProfessor = False

class Alumno(Persona):
	def __init__(self,ramos_pre,idolos,**kwargs):
		super().__init__(**kwargs)
		self.cursosxtomar = []
		self.aprobados = ramos_pre
		self.idolos = list(idolos)
		self.seguidores = []
		self.cantidadIdolos = 0
					    #0  1  2  3  4  5
		self.horario =[[[],[],[],[],[],[]],
					   [[],[],[],[],[],[]],
					   [[],[],[],[],[],[]],
					   [[],[],[],[],[],[]],
					   [[],[],[],[],[],[]],
					   [[],[],[],[],[],[]]]

	def tomar_ramo(self,ramo):
		self.cursosxtomar.append(ramo)
		lib.agregar_horario(self.horario,ramo)

	def botar_ramo(self,ramo):
		for i in range(len(self.horario)):
			for j in range(len(self.horario)):
				if ramo.nombre in self.horario[i][j]:
					self.horario[i][j].pop(self.horario[i][j].index(ramo.nombre))
					

	def imprimir_horario(self):
		for i in range(len(self.horario)):
			print('Modulo {} {}'.format(i,self.horario[i]))

	def displayMenu(self):
		pass

class Profesor(Persona):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.isProfessor = True


class Curso:
	requisitos = lib.parser('requisitos.txt')
	def __init__(self,sigla,curso,retiro,cred,sec,ofr,campus,
		NRC,apr,eng,hora_cat='',sala_cat='',hora_lab='',
		sala_lab='',hora_ayud='',sala_ayud='',**kwargs):
		self.sigla = sigla
		self.nombre = curso
		self.eng = eng
		self.apr = apr
		self.retiro = retiro
		self.creditos = cred
		self.seccion = sec
		self.campus = campus
		self.nrc = NRC

		self.horacat = hora_cat
		self.salacat = sala_cat

		self.horalab = hora_lab
		self.salalab = sala_lab

	
		self.horaayud = hora_ayud
		self.salaayud = sala_ayud
"""
#Hago el parse a partir de los txt
lista_personas = lib.parser('personas.txt')
lista_cursos = lib.parser('cursos.txt')

#Instanciando personas
for i in range(len(lista_personas)):
	if lista_personas[i]['alumno'] == 'SI':
		lista_personas[i] = Alumno(**lista_personas[i])
	else:
		lista_personas[i] = Profesor(**lista_personas[i])

#Instanciando cursos
for i in range(len(lista_cursos)):
	lista_cursos[i] = Curso(**lista_cursos[i])

#Numero de seguidores
#print(datetime.datetime.now())
#for alumno in lista_personas:
#	if not alumno.isProfessor:
#		for idolo in alumno.idolos:
#			for i in range(len(lista_personas)):
#				if idolo == lista_personas[i].nombre and not lista_personas[i].isProfessor:
#					lista_personas[i].seguidores.append(alumno)
#					lista_personas[i].cantidadIdolos += 1
#					break

#Ordenando por bacanosidad
#sorted(ut, key=lambda x: x.cantidadIdolos, reverse=True)

#print(datetime.datetime.now())

if __name__ == '__main__':
	pass
"""