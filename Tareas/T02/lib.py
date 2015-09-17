def portType(lista):
	value1 = lista[0].value
	value2 = None
	
	for i in range(len(lista)):
		if lista[i].value != value1:
			value2 = lista[i].value
		elif lista[i].value != value1 and lista[i].value != value2:
			return 'RAND'
	if 
