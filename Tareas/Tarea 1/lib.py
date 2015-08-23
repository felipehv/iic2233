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


if __name__ == '__main__':
	pass

