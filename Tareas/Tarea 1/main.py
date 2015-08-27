import lib
from personas import Persona, Profesor, Alumno
from cursos import Curso

"""
En este main se realizan los parse de los archivos con los datos de cursos,
personas, etc. y las instancias de las mismas, ademas del calculo de la 
bacanosidad.

"""

#Hago el parse a partir de los txt
lista_personas = lib.parse('txt/personas.txt')
lista_cursos = lib.parse('txt/cursos.txt')
print('Parse completado')

#Instanciando personas
dicc_personas = dict()
for i in range(len(lista_personas)):
    if lista_personas[i]['alumno'] == 'SI':
        dicc_personas[lista_personas[i]['nombre']] = Alumno(**lista_personas[i])
    else:
        dicc_personas[lista_personas[i]['nombre']] = Profesor(**lista_personas[i])
lista_personas = []
print('Instancia de personas completa')

#Instanciando cursos
dicc_cursos = dict()
for i in range(len(lista_cursos)):
    dicc_cursos[lista_cursos[i]['sigla']] = Curso(**lista_cursos[i])
print('Instancia de cursos completa')


#Numero de seguidores
for alumno in dicc_personas:
    if not dicc_personas[alumno].isProfessor:
        for idolo in dicc_personas[alumno].idolos:
            dicc_personas[idolo].seguidores.append(idolo)
            dicc_personas[idolo].cantidad_seguidores += 1

#Sumando bacanosodad de los demas.
for alumno in dicc_personas:
    for seguidor in alumno.
print('Seguidores completa')

#Ordenando por bacanosidad
#sorted(ut, key=lambda x: x.cantidadIdolos, reverse=True)

if __name__ == '__main__':
    pass
