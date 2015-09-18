from sistema import *
import random as rd
#from estructuras import *
from classes2 import *
from ciclos2 import *
from datetime import datetime
global banner

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

"""
Ruta a Bummer
"""
print(datetime.now())
def ruta(puerto,ultima_ruta=None,visitados=[]):
	print(puerto.ide,banner,puerto.ide in visitados,len(visitados))
	visitados.append(puerto.ide)
	retorno = []
	retorno.append(puerto.ide)
	if puerto.ide == banner:
		print('holi')
		return retorno
	for port in puerto.salidas:
		if port.ide not in visitados:
			route = ruta(port,visitados=visitados)
			retorno = retorno + route
			if puerto.ide == 0:
				if ultima_ruta == None or (len(retorno) < len(ultima_ruta) and retorno[len(retorno)-1] == banner):
					ultima_ruta = retorno
				retorno = []
				retorno.append(puerto.ide)
				visitados = []
				visitados.append(puerto.ide)
			else:
				return retorno
	if puerto.ide == 0:
		return ultima_ruta
	else:
		return retorno

ruta = ruta(lista_de_puertos[0])
print('ruta: ',ruta)
print(datetime.now())

"""
Rutas doble, triangulares y cuadradas
"""
rutas_doble_sentido = []
ciclos_triangulares = []
ciclos_cuadrados = []

rutas_doble_sentido = cicloDoble(lista_de_puertos,rutas_doble_sentido)
ciclos_triangulares = cicloTriangular(lista_de_puertos,ciclos_triangulares)
ciclos_cuadrados = cicloCuadrado(lista_de_puertos,ciclos_cuadrados)

"""
Maxima capacidad
"""
def maxCap(lista_de_puertos):
	pass
