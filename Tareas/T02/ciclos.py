from estructuras import *
def cicloDoble(listain,listaout):
    for port in listain:
        for _port in port.salidas:
            if port in _port.salidas:
                tuplista = myList()
                tuplista.append(port.ide)
                tuplista.append(_port.ide)
                if ciclounico(tuplista,listaout):
                    listaout.append(tuplista)
    return listaout

def cicloTriangular(listain,listaout):
    for port in listain:
        for _port in port.salidas:
            for __port in _port.salidas:
                if port in __port.salidas:
                    tuplista = myList()
                    tuplista.append(port.ide)
                    tuplista.append(_port.ide)
                    tuplista.append(__port.ide)
                    if ciclounico(tuplista,listaout):
                        listaout.append(tuplista)
    return listaout

def cicloCuadrado(listain,listaout):
    for port in listain:
        for _port in port.salidas:
            for __port in _port.salidas:
                for ___port in __port.salidas:
                    if port in ___port.salidas:
                        tuplista = myList()
                        tuplista.append(port.ide)
                        tuplista.append(_port.ide)
                        tuplista.append(__port.ide)
                        tuplista.append(___port.ide)
                        if ciclounico(tuplista,listaout):
                            listaout.append(tuplista)
    return listaout

def ciclounico(ciclo,listaout):
    for ciclo_en_lista in listaout:
        contador = 0
        for ide in ciclo:
            if ide in ciclo_en_lista:
                contador += 1
        if contador == len(ciclo):
            return False
    return True