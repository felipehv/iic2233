dateToCoord = {'L': 0, 'M': 1, 'W': 2, 'J': 3, 'V': 4, 'S': 5}


def verificar_tope(matriz, ramo):
    if ramo.horacat:
        dias, mods = ramo.horacat.split(':')
        dias = dias.split('-')
        mods = mods.split(',')
        for dia in dias:
            for mod in mods:
                # Posicion equivalente en la matriz para un dia
                p_dia = dateToCoord[dia]
                if matriz[int(mod) - 1][p_dia] == []:
                    continue
                else:
                    for elemento in matriz[int(mod) - 1][p_dia]:
                        if elemento[-1] == 'a':
                            continue
                        else:
                            return False
                if mod - 2 > 0:
                    for otroramo in matriz[mod - 1][p_dia]:
                        for key in dicc_cursos:
                            if dicc_cursos[key].sigla in otroramo and dicc_cursos[key].campus != ramo.campus:
                                return False
                if mod < 7:
                    for otroramo in matriz[mod][p_dia]:
                        for key in dicc_cursos:
                            if dicc_cursos[key].sigla in otroramo and dicc_cursos[key].campus != ramo.campus:
                                return False

    if ramo.horalab:
        dias, mods = ramo.horalab.split(':')
        dias = dias.split('-')
        mods = mods.split(',')
        for dia in dias:
            for mod in mods:
                # Posicion equivalente en la matriz para un dia
                p_dia = dateToCoord[dia]
                if matriz[int(mod) - 1][p_dia] == []:
                    continue
                else:
                    for elemento in matriz[int(mod) - 1][p_dia]:
                        if elemento[-1] == 'a':
                            continue
                        else:
                            return False
                if mod - 2 > 0:
                    for otroramo in matriz[mod - 1][p_dia]:
                        for key in dicc_cursos:
                            if dicc_cursos[key].sigla in otroramo and dicc_cursos[key].campus != ramo.campus:
                                return False
                if mod < 7:
                    for otroramo in matriz[mod][p_dia]:
                        for key in dicc_cursos:
                            if dicc_cursos[key].sigla in otroramo and dicc_cursos[key].campus != ramo.campus:
                                return False
    return True


def agregar_horario(matriz, ramo):
    if verificar_tope(matriz, ramo):
        if ramo.horacat:
            dias, mods = ramo.horacat.split(':')
            dias = dias.split('-')
            mods = mods.split(',')
            for dia in dias:
                for mod in mods:
                    p_dia = dateToCoord[dia]
                    matriz[
                        int(mod) - 1][p_dia].append(ramo.nombre + '-' + str(ramo.seccion))

        if ramo.horalab:
            dias, mods = ramo.horalab.split(':')
            dias = dias.split('-')
            mods = mods.split(',')
            for dia in dias:
                for mod in mods:
                    p_dia = dateToCoord[dia]
                    matriz[
                        int(mod) - 1][p_dia].append(ramo.nombre + '-' + str(ramo.seccion) + 'L')

        if ramo.horaayud:
            dias, mods = ramo.horaayud.split(':')
            dias = dias.split('-')
            mods = mods.split(',')
            for dia in dias:
                for mod in mods:
                    p_dia = dateToCoord[dia]
                    matriz[
                        int(mod) - 1][p_dia].append(ramo.nombre + '-' + str(ramo.seccion) + 'a')

    return matriz


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


def procesar_reqs():
    requisitos = []
    izq = 0
    text = text.replace(' o ', ' or ')
    text = text.replace(' y ', ' and ')
    return


def verificar_hora(hora):
    if len(hora) < 5:
        return False
    hora = hora.split(':')
    if hora[0].isdigit() <= 24 and hora[1].isdigit():
        return 0 < int(hora[0]) <= 24 and 0 < int(hora[1]) < 60


def horario_entre(actual, tupla):
    actual = actual.split(':')
    tupla = (tupla[0].split(':'), tupla[1].split(':'))
    # return tupla[0][0] <= actual[0] <= tupla[1][0] and (tupla[0][1] <=
    # actual[1] or actual[1] <= tupla[1][1])
    if tupla[0][0] == actual[0] and actual[1] >= tupla[0][1]:
        return True
    elif tupla[1][0] == actual[0] and actual[1] <= tupla[1][1]:
        return True
    elif tupla[0][0] <= actual[0] <= tupla[1][0]:
        return True
    return False


def horarioX(n, horario):
    hora1 = horario[0]
    hora2 = horario[1]
    hora1 = hora1[0] + str(int(hora1[1]) + n) + hora1[2:]
    hora2 = hora2[0] + str(int(hora2[1]) + n) + hora2[2:]
    if len(hora1) == 6:
        hora1 = hora1[1:]
    return (hora1, hora2)

if __name__ == '__main__':
    pass
