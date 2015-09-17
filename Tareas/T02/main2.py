from sistema import *
import random as rd
#from estructuras import *
from classes2 import *
from ciclos2 import *
from datetime import datetime


def not_complete(lista):
	for element in lista:
		if not lista[element].complete:
			return True
	return False

lista_de_puertos = dict()

inicio = puerto_inicio()
banner = puerto_final()

puertoanterior,boolean = preguntar_puerto_actual() 

ide = puertoanterior

puertoanterior = Puerto(puertoanterior)
lista_de_puertos[ide] = puertoanterior
conexiones = posibles_conexiones() 
puertoanterior.cantidad_conexiones = conexiones
puertoanterior.actualizarLista()


maximus = 3
maxlen = 0
ultimolen = 0
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

	if puertoactual not in lista_de_puertos:
		ide = puertoactual
		puertoactual = Puerto(puertoactual)
		lista_de_puertos[ide] = puertoactual
		puertoactual.cantidad_conexiones = conexiones
		puertoactual.actualizarLista()

	else:
		puertoactual = lista_de_puertos[puertoactual]

	if not boolean and not puertoanterior.complete:
		#Puerto actual no en salidas de puerto anterior

		if puertoactual not in puertoanterior.salidas:
			puertoanterior.salidas.append(puertoactual)

		lc = puertoanterior.lastconnection
		puertoanterior.salidas2[lc].append(puertoactual)
		#Puerto anterior no en entradas de puerto actual
		if puertoanterior not in puertoactual.entradas:
			puertoactual.entradas.append(puertoanterior)

	puertoanterior = puertoactual
print('holi')
with open('output.txt','w') as writer:
	for key in lista_de_puertos:
		port = lista_de_puertos[key]
		writer.write(str(port.ide) +'\n')
		writer.write('Entradas: ')
		writer.write(str(port.entradas) + '\n')
		writer.write('Salidas: ')
		writer.write(str(port.salidas2) + '\n')
print(datetime.now())
rutas_doble_sentido = []
ciclos_triangulares = []
ciclos_cuadrados = []

cicloDoble(lista_de_puertos,rutas_doble_sentido)
cicloTriangular(lista_de_puertos,ciclos_triangulares)
cicloCuadrado(lista_de_puertos,ciclos_cuadrados)
print(len(rutas_doble_sentido))
print(len(ciclos_triangulares))
print(len(ciclos_cuadrados))

print(datetime.now())