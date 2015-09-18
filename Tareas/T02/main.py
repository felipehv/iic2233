from sistema import *
import random as rd
from estructuras import *
from classes import *
from ciclos import *

import datetime

tiempoinicial = datetime.datetime.now()
def not_complete(lista):
	for element in lista:
		if not element.value.complete:
			return True
	return False

lista_de_puertos = myList()
lista_de_puertos.append(None)
#listaids = myList()

inicio = puerto_inicio()
banner = puerto_final()

puertoanterior,boolean = preguntar_puerto_actual() 
i = puertoanterior
puertoanterior = Puerto(puertoanterior)
lista_de_puertos[i] = puertoanterior
puertoanterior.cantidad_conexiones = posibles_conexiones()
puertoanterior.actualizarLista()

maximus = 3
maxlen = 0
ultimolen = 0
puertosencontrados = 1
#for i in range(10):
while not_complete(lista_de_puertos):
	a = len(lista_de_puertos)
	if a > ultimolen:
		print(a,maximus)
		ultimolen = a

	count = 0
	puertoanterior.connect(hacer_conexion)

	conexiones = posibles_conexiones()

	puertoactual,boolean = preguntar_puerto_actual()
	#print(str(len(lista_de_puertos)),maximus,puertoactual)

	if puertoactual > maximus:
		maximus = puertoactual

	while len(lista_de_puertos) <= maximus:
		lista_de_puertos.append(None)

	if lista_de_puertos[puertoactual].value == None:
		i = puertoactual
		puertoactual = Puerto(puertoactual)
		lista_de_puertos[i] = puertoactual
		puertoactual.cantidad_conexiones = conexiones
		puertoactual.actualizarLista()
		puertoactual.capacidad = get_capacidad()
		puertosencontrados += 1
		print(puertosencontrados)
	else:
		puertoactual = lista_de_puertos[puertoactual].value

	if not boolean:
		#Puerto actual no en salidas de puerto anterior
	
		if puertoactual not in puertoanterior.salidas:
			puertoanterior.salidas.append(puertoactual)

		lc = puertoanterior.lastconnection
		puertoanterior.salidas2[lc].value.append(puertoactual)

		#Puerto anterior no en entradas de puerto actual
		if puertoanterior not in puertoactual.entradas:
			puertoactual.entradas.append(puertoanterior)

	puertoanterior = puertoactual

with open('red.txt','w') as writer:
	for port in lista_de_puertos:
		port = port.value
		writer.write("PUERTO {}\n".format(puerto.ide))
	for port in lista_de_puertos:
		port = port.value
		for salida in salidas:
			writer.write("CONEXION {} {}".format(puerto.ide,salida.ide))

"""
Ruta a bummer
"""

def ruta(puerto,ultima_ruta=None):
	retorno = myList()
	retono.append(puerto.ide)
	if puerto.ide == banner:
		return retorno
	for port in puerto.salida:
		port = port.value
		retorno = retorno + ruta(port)
		if puerto.ide == 0:
			if ultima_ruta == None or len(retorno) < ultima_ruta:
				ultima_ruta = retorno
			retorno = myList()
			retorno.append(puerto.ide)
		else:
			return retorno
	if port.ide == 0:
		return ultima_ruta

ruta = ruta(lista_de_puertos[0])

with open("rutaABummer.txt","w") as writer:
	pass

print(tiempoinicial,datetime.datetime.now())

"""
Parte II 
"""
rutas_doble_sentido = myList()
ciclos_triangulares = myList()
ciclos_cuadrados = myList()

cicloDoble(lista_de_puertos,rutas_doble_sentido)
cicloTriangular(lista_de_puertos,ciclos_triangulares)
cicloCuadrado(lista_de_puertos,ciclos_cuadrados)
print(len(rutas_doble_sentido))
print(len(ciclos_triangulares))
print(len(ciclos_cuadrados))

"""
with open('ciclos.txt','w') as writer:
	writer.write('Rutas Doble Sentido\n')
	for elemento in rutas_doble_sentido:
		writer.write(elemento.value+'\n')
	writer.write('')
"""