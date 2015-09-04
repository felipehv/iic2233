import lib
from personas import Persona, Profesor, Alumno

"""
En este main se realizan los parse de los archivos con los datos de cursos,
personas, etc. y las instancias de las mismas, ademas del calculo de la 
bacanosidad.

"""

# Hago el parse a partir de los txt
lista_personas = lib.parse('txt/personas.txt')
print('Parse completado')

# Instanciando personas
dicc_personas = dict()
for i in range(len(lista_personas)):
    if lista_personas[i]['alumno'] == 'SI':
        dicc_personas[lista_personas[i]['nombre']] = Alumno(
            **lista_personas[i])
    else:
        dicc_personas[lista_personas[i]['nombre']] = Profesor(
            **lista_personas[i])
lista_personas = []
print('Instancia de personas completa')


# Numero de seguidores
for alumno in dicc_personas:
    if not dicc_personas[alumno].isProfessor:
        for idolo in dicc_personas[alumno].idolos:
            dicc_personas[idolo].seguidores.append(alumno)
            dicc_personas[idolo].cantidad_seguidores += 1 / \
                len(dicc_personas[alumno].idolos)

# Sumando bacanosodad de los demas.


for key in dicc_personas:
    if not dicc_personas[key].isProfessor:
        for seguidor in dicc_personas[key].seguidores:
            dicc_personas[key].puntosextra += dicc_personas[
                seguidor].cantidad_seguidores / len(dicc_personas[seguidor].idolos)
        dicc_personas[key].bacanosidad = dicc_personas[
            key].puntosextra  # dicc_personas[key].puntosextra
        dicc_personas[key].puntosextra
print('Bacanosidad completa')

for i in range(4):  # Para hacer el calculo mas exacto
    for alumno in dicc_personas:
        if not dicc_personas[alumno].isProfessor:
            for idolo in dicc_personas[alumno].idolos:
                dicc_personas[
                    idolo].puntosrecibidos += dicc_personas[alumno].bacanosidad / len(dicc_personas[alumno].idolos)

    for alumno in dicc_personas:
        if not dicc_personas[alumno].isProfessor:
            dicc_personas[alumno].bacanosidad = dicc_personas[
                alumno].puntosrecibidos
            dicc_personas[alumno].puntosrecibidos = 0

# Escribiendo en txt el orden de los alumnos.
lista_alumnos = [dicc_personas[key]
                 for key in dicc_personas if not dicc_personas[key].isProfessor]
lista_alumnos.sort(key=lambda x: x.bacanosidad, reverse=True)

with open('listabacanes.txt', 'w') as writer:
    for linea in lista_alumnos:
        writer.write(
            linea.nombre + '\t' + str(linea.bacanosidad / lista_alumnos[0].bacanosidad) + "\n")
maxima = lista_alumnos[0].bacanosidad


##########################################################################
# Funcion para comprobar bacanosidad
"""for alumno in dicc_personas:
    if not dicc_personas[alumno].isProfessor:
        for idolo in dicc_personas[alumno].idolos:
            dicc_personas[idolo].puntosrecibidos += dicc_personas[alumno].bacanosidad / len(dicc_personas[alumno].idolos)


print('Bacanosidad2 completa')

#Escribiendo en txt el orden de los alumnos.
lista_alumnos = [dicc_personas[key] for key in dicc_personas if not dicc_personas[key].isProfessor]
lista_alumnos.sort(key=lambda x: x.puntosrecibidos, reverse=True)

with open('listabacanes2.txt','w') as writer:
    for linea in lista_alumnos:
        writer.write(linea.nombre + '\t' + str(linea.puntosrecibidos) + "\n")
"""

if __name__ == '__main__':
    pass
