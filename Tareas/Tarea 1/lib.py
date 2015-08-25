dateToCoord = {'L': 0, 'M': 1, 'W': 2, 'J': 3, 'V': 4, 'S': 5}


def verificar_tope(matriz, dias, mods):
    for dia in dias:
        for mod in mods:
            # Posicion equivalente en la matriz para un dia
            p_dia = dateToCoord[dia]
            if matriz[int(mod) - 1][p_dia] == [] or matriz[int(mod) - 1][p_dia] != dias:
                continue
            else:
                return False


def agregar_horario(matriz, ramo):
    if ramo.horacat:
        dias, mods = ramo.horacat.split(':')
        dias = dias.split('-')
        mods = mods.split(',')

    if ramo.horalab:
        dias, mods = ramo.horalab.split(':')
        dias = dias.split('-')
        mods = mods.split(',')
    if ramo.horaayud:
        dias, mods = ramo.horaayud.split(':')
        dias = dias.split('-')
        mods = mods.split(',')


def isList(string):
    return string[0] == '[' and string[len(string) - 1] == ']'


def SepararEnObjetos(texto, lista):
    i = 0
    intentos = 0
    while texto != ']':
        if texto[i] == '{':
            for j in range(i, len(texto)):
                if texto[j] == '}':
                    lista.append(text2dict(texto[i:j + 1]))
                    texto = texto[j + 1:]
                    i = 0
                    break
        else:
            i += 1


def text2dict(texto):
    diccionario = dict()
    text = texto[1:]
    valuesList = []
    k = 0
    while text != '':
        if text[k] == '}':
            valuesList.append(text[0:k])
            text = text[k + 1:]
            k = 0
            break
        elif text[k] == ',' and ('[' not in text[0:k] or ('[' in text[0:k] and ']' in text[0:k])):
            if text[k + 1] == '"':
                valuesList.append(text[0:k])
                text = text[k + 1:]
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
            lista1 = tupla[1][1:-1].split(',')
            for i in range(len(lista1)):
                lista1[i] = lista1[i][1:-1]
                if lista1 == ['']:
                    lista1 = []
            diccionario[tupla[0][1:-1]] = lista1
        else:
            diccionario[tupla[0][1:-1]] = tupla[1][1:-1]
    return diccionario


def parse(archivo):
    with open(archivo, 'r', encoding="utf8") as reader:
        texto_plano = ''
        for linea in reader:
            texto_plano += linea.strip()

        objetos = []
        SepararEnObjetos(texto_plano, objetos)

    return objetos


if __name__ == '__main__':
    pass
