from sistema import *
from estructuras import *
from classes import *
from ciclos import *
import datetime
from ruta import ruta

lista_de_puertos = myList()
lista_de_puertos.append(None)

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

while Puerto.completes < maximus:
	a = len(lista_de_puertos)
	if a > ultimolen:
		print(a,maximus)
		ultimolen = a

	count = 0
	puertoanterior.connect(hacer_conexion)

	conexiones = posibles_conexiones()

	puertoactual,boolean = preguntar_puerto_actual()

	if puertoactual > maximus:
		maximus = puertoactual

	while len(lista_de_puertos) <= maximus:
		lista_de_puertos.append(None)

	if lista_de_puertos[puertoactual] == None:
		i = puertoactual
		puertoactual = Puerto(puertoactual)
		lista_de_puertos[i] = puertoactual
		puertoactual.cantidad_conexiones = conexiones
		puertoactual.actualizarLista()
		puertoactual.capacidad = get_capacidad()
		puertosencontrados += 1
		print(puertosencontrados)
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
with open('red.txt','w') as writer:
	for port in lista_de_puertos:
		writer.write("PUERTO {}\n".format(port.ide))
	for port in lista_de_puertos:
		for salida in port.salidas:
			writer.write("CONEXION {} {}\n".format(port.ide,salida.ide))

"""
Ruta a bummer
"""
ruta = ruta(lista_de_puertos[0],banner)

with open("rutaABummer.txt","w") as writer:
	for i in range(len(ruta)-1):
		writer.write('CONEXION {} {}\n'.format(ruta[i],ruta[i+1]))


"""
Parte II 
"""
rutas_doble_sentido = myList()
ciclos_triangulares = myList()
ciclos_cuadrados = myList()

cicloDoble(lista_de_puertos,rutas_doble_sentido)
cicloTriangular(lista_de_puertos,ciclos_triangulares)
cicloCuadrado(lista_de_puertos,ciclos_cuadrados)

with open('rutasDobleSentido.txt','w'):
	for i in range(len(rutas_doble_sentido)-1):
		writer.write('{} <-> {}')

with open('ciclos.txt','w') as writer:
	for ciclo in ciclos_triangulares:
		writer.write('{} {} {}\n'.format(ciclo[0],ciclo[1],ciclo[2]))
	for ciclo in ciclos_cuadrados:
		writer.write('{} {} {} {}\n'.format(ciclo[0],ciclo[1],ciclo[2],ciclo[3]))

"""
MaxCapacidad
"""

def maxCap(puerto,cap,max_cap=0,visitados=myList(),retorno=myList(),ultima_ruta=None):
	visitados.append(puerto.ide)
	retorno.append(puerto.ide)

	if puerto.ide == banner:
		if ultima_ruta == None or cap > max_cap:
			ultima_ruta = retorno
			max_cap = cap
		return ultima_ruta
	if puerto.capacidad < cap:
		cap = puerto.capacidad
	for port in puerto.salidas:
		if port.ide not in visitados:
			visitados_copia = myList()
			retorno_copia = myList()
			for element in visitados:
				visitados_copia.append(element)
			for element in retorno:
				retorno_copia.append(element)

			ultima_ruta = ruta(port,banner,visitados=visitados_copia,ultima_ruta=ultima_ruta,retorno=retorno_copia)

	return ultima_ruta,max_cap

ruta_max_cap = maxCap(lista_de_puertos[0],lista_de_puertos[0].capacidad)

with open('rutaMaxima.txt','w') as writer:
	writer.write('CAP {}'.format(ruta_max_cap[1]))
	for i in range(len(ruta_max_cap)-1)[0]:
		writer.write('{} {}'.format(ruta_max_cap[0][i],ruta_max_cap[0][i+1])

