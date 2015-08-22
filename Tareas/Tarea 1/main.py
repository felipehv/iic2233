import lib
alumnos = []
class Persona:
	def __init__(self,nombre,clave,usuario,**kwargs):
		self.nombre = nombre
		self.user = usuario
		self.clave = clave

class Alumno(Persona):
	def __init__(self,ramos_pre,idolos,**kwargs):
		super().__init__(**kwargs)
		self.horario = []
		self.aprobados = ramos_pre
		self.idolos = idolos
		self.isProfessor = False

	def tomar_ramo(self,ramo):
		self.horario.append = ramo

	def imprimir_horario(self):
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
lista_cursos = lib.parser('cursos.txt')

#Instanciando personas
for i in range(len(lista_personas)):
	if lista_personas[i]['alumno'] == 'SI':
		lista_personas[i] = Alumno(**lista_personas[i])
	else:
		lista_personas[i] = Profesor(**lista_personas[i])

#Instanciando cursos
#for i in range(len(lista_cursos)):
#	lista_personas[i] = Curso(**lista_personas[i])

if __name__ == '__main__':
	pass
