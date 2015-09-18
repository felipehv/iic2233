from estructuras import *
def ruta(puerto,banner,ultima_ruta=None,visitados=myList(), retorno = myList()):
	visitados.append(puerto.ide)
	retorno.append(puerto.ide)

	if puerto.ide == banner:
		if ultima_ruta == None or len(retorno) < len(ultima_ruta):
			ultima_ruta = retorno
			print(ultima_ruta)
		return ultima_ruta

	for port in puerto.salidas:
		if port.ide not in visitados:
			visitados_copia = myList()
			retorno_copia = myList()
			for element in visitados:
				visitados_copia.append(element)
			for element in retorno:
				retorno_copia.append(element)

			ultima_ruta = ruta(port,banner,visitados=visitados_copia,ultima_ruta=ultima_ruta,retorno=retorno_copia)

	return ultima_ruta

