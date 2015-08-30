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
dicc_alumnos = dict()
dicc_profesores = dict()
for i in range(len(lista_personas)):
    if lista_personas[i]['alumno'] == 'SI':
        dicc_alumnos[lista_personas[i]['nombre']] = Alumno(**lista_personas[i])
    else:
        dicc_profesores[lista_personas[i]['nombre']] = Profesor(**lista_personas[i])
lista_personas = []
print('Instancia de personas completa')

#Instanciando cursos
dicc_cursos = dict()
for i in range(len(lista_cursos)):
    dicc_cursos[lista_cursos[i]['sigla']] = Curso(**lista_cursos[i])
print('Instancia de cursos completa')


#Numero de seguidores
for alumno in dicc_alumnos:
    for idolo in dicc_alumnos[alumno].idolos:
        dicc_alumnos[idolo].seguidores.append(idolo)
        dicc_alumnos[idolo].cantidad_seguidores += 1

#Sumando bacanosodad de los demas.
for key in dicc_alumnos:
    for seguidor in dicc_alumnos[key].seguidores:
        dicc_alumnos[key].puntosextra += dicc_alumnos[seguidor].cantidad_seguidores // len(dicc_alumnos[seguidor].idolos)
    dicc_alumnos[key].bacanosidad = dicc_alumnos[key].cantidad_seguidores + dicc_alumnos[key].puntosextra

print('Bacanosidad completa')

masbacan = [None,0]
menosbacan = [None,100000000]
for key in dicc_alumnos:
    if dicc_alumnos[key].bacanosidad > masbacan[1]:
        masbacan[0],masbacan[1] = key,dicc_alumnos[key].bacanosidad
    elif dicc_alumnos[key].bacanosidad < menosbacan[1]:
        menosbacan[0],menosbacan[1] = key,dicc_alumnos[key].bacanosidad
print(dicc_alumnos['Mateo Pizarro'].bacanosidad)
print(masbacan,menosbacan)



if __name__ == '__main__':
    pass
