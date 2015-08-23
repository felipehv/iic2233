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


if __name__ == '__main__':
	string = '[{"hola":1,"chao":2}]'
	lista = eval(string)
	print(lista[0]['hola'])

