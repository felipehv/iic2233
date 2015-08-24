dateToCoord = {'L':0, 'M':1, 'W': 2, 'J':3, 'V':4, 'S':5}
def text2dict(texto):
	objetos = []
	i = 0
	intentos = 0
	while texto != ']':
		if texto[i] == '{':
			for j in range(i,len(texto)):
				if texto[j] == '}':
					objetos.append(eval(texto[i:j+1]))
					texto = texto[j+1:]
					i = 0
					break
		else:
			i += 1
	return objetos


def parser(archivo):
	with open(archivo,'r',encoding="utf8") as reader:
		texto_plano = reader.readlines()
		lista = [p.strip() for p in texto_plano]
		texto_plano = None #Ahorro de memoria
		texto = ''.join(lista)

	return text2dict(texto)

def verificar_tope(matriz,dias,mods):
	for dia in dias:
		for mod in mods:
			p_dia=dateToCoord[dia]
			if matriz[int(mod)-1][p_dia] != [] or matriz[int(mod)-1][p_dia] != dias:
				pass

def agregar_horario(matriz,ramo):
	if ramo.horacat:
		dias,mods=ramo.horacat.split(':')
		dias = dias.split('-')
		mods = mods.split(',')

	if ramo.horalab:
		dias,mods=ramo.horalab.split(':')
		dias = dias.split('-')
		mods = mods.split(',')
	if ramo.horaayud:
		dias,mods=ramo.horaayud.split(':')
		dias = dias.split('-')
		mods = mods.split(',')

def isList(string):
	return string[0] == '[' and string[len(string)-1] == ']'

def SepararEnObjetos(texto):
	objetos = []
	i = 0
	intentos = 0
	while texto != ']':
		if texto[i] == '{':
			for j in range(i,len(texto)):
				if texto[j] == '}':
					objetos.append(texto[i:j+1])
					texto = texto[j+1:]
					i = 0
					break
		else:
			i += 1
	return objetos

def parser2(archivo):
	with open(archivo,'r',encoding="utf8") as reader:
		texto_plano = reader.readlines()

		texto_plano = [p.strip() for p in texto_plano]

		texto_plano = ''.join(texto_plano)

		objetos = SepararEnObjetos(texto_plano)

	for i in range(len(objetos)):
		diccionario = dict()
		text = objetos[i][1:]
		valuesList = []
		k = 0
		while text != '':
			if text[k] == '}':
				valuesList.append(text[0:k])
				text = text[i+k:]
				k = 0
				break
			elif text[k] == ',' and ('[' not in text[0:k] or ('[' in text[0:k] and ']' in text[0:k])):
				if text[k+1] == '"':
					valuesList.append(text[0:k])
					text = text[k+1:]
					k = 0
				else:
					k += 1
			else:
				k += 1
		for value in valuesList:
			tupla = value.split(': ')
			if tupla[1].isdigit():
				diccionario[tupla[0][1:-1]] = int(tupla[1])
			elif isList(tupla[1]):
				diccionario[tupla[0][1:-1]] = tupla[1][1:-1].split(',')
			else:
				diccionario[tupla[0][1:-1]] = tupla[1][1:-1]
		objetos[i] = diccionario
	return objetos





if __name__ == '__main__':
	pass

