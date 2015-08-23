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
		self.horario = []
		self.aprobados = ramos_pre
		self.idolos = list(idolos)
		self.seguidores = []
		self.cantidadIdolos = 0

	def tomar_ramo(self,ramo):
		self.horario.append = ramo

	def imprimir_horario(self):
		pass

	def displayMenu(self):
		pass

class Profesor(Persona):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.isProfessor = True


class Curso:
	def __init__(self,**kwargs):
		super().__init__(**kwargs)


#Hago el parse a partir de los txt
lista_personas = lib.parser('personas.txt')
#lista_cursos = lib.parser('cursos.txt')

#Instanciando personas
for i in range(len(lista_personas)):
	if lista_personas[i]['alumno'] == 'SI':
		lista_personas[i] = Alumno(**lista_personas[i])
	else:
		lista_personas[i] = Profesor(**lista_personas[i])

#Numero de seguidores
print(datetime.datetime.now())
for alumno in lista_personas:
	if not alumno.isProfessor:
		for idolo in alumno.idolos:
			for i in range(len(lista_personas)):
				if idolo == lista_personas[i].nombre and not lista_personas[i].isProfessor:
					lista_personas[i].seguidores.append(alumno)
					lista_personas[i].cantidadIdolos += 1
					break

#Ordenando por bacanosidad
sorted(ut, key=lambda x: x.cantidadIdolos, reverse=True)

print(datetime.datetime.now())
#Instanciando cursos
#for i in range(len(lista_cursos)):
#	lista_personas[i] = Curso(**lista_personas[i])

if __name__ == '__main__':
	pass
