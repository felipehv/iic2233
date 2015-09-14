from sistema import *
import random as rd
from estructuras import *
from classes import *

def verificar_puerto(lista,puerto):
	if puerto in lista:
		return True

def not_complete(lista):
	for element in lista:
		if not element.value.complete:
			return True
	return False

lista_de_puertos = myList()
listaids = myList()

inicio = puerto_inicio()
banner = puerto_final()


puertoanterior,boolean = preguntar_puerto_actual() 
listaids.append(puertoanterior)
puertoanterior = Puerto(puertoanterior)
conexiones = posibles_conexiones() 

lista_de_puertos.append(puertoanterior)
puertoanterior.cantidad_conexiones = conexiones

maximus = 3
#for i in range(10):
while not_complete(lista_de_puertos):
	#print(contador)
	count = 0
	puertoanterior.connect(hacer_conexion)

	conexiones = posibles_conexiones()

	puertoactual,boolean = preguntar_puerto_actual()
	print(str(len(lista_de_puertos)),maximus)

	if puertoactual > maximus:
		maximus = puertoactual

	if puertoactual not in listaids:
		listaids.append(puertoactual)
		puertoactual = Puerto(puertoactual)
		lista_de_puertos.append(puertoactual)
		puertoactual.cantidad_conexiones = conexiones

	else:
		for puerto in lista_de_puertos:
			if puerto.value.ide == puertoactual:
				puertoactual = puerto.value

	if not boolean:
		#Puerto actual no en salidas de puerto anterior
		if puertoactual not in puertoanterior.salidas:
			puertoanterior.salidas.append(puertoactual)

		#Puerto anterior no en entradas de puerto actual
		if puertoanterior not in puertoactual.entradas:
			puertoactual.entradas.append(puertoanterior)

	puertoanterior = puertoactual

with open('output.txt','w') as writer:
	for port in lista_de_puertos:
		port = port.value
		writer.write(str(port.ide) +'\n')
		writer.write('Entradas: ')
		writer.write(str(port.entradas) + '\n')
		writer.write('Salidas: ')
		writer.write(str(port.salidas) + '\n')

