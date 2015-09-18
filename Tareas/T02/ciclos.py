def cicloDoble(listain,listaout):
    for port in listain:
        port = listain[port]
        for _port in port.salidas:
            if port in _port.salidas:
                if ciclounico((port.ide,_port.ide),listaout):
                    listaout.append((port.ide,_port.ide))
    return listaout

def cicloTriangular(listain,listaout):
    for port in listain:
        port = listain[port]
        for _port in port.salidas:
            for __port in _port.salidas:
                if port in __port.salidas:
                    if ciclounico((port.ide,_port.ide,__port.ide),listaout):
                        listaout.append((port.ide,_port.ide,__port.ide))
    return listaout

def cicloCuadrado(listain,listaout):
    for port in listain:
        port = listain[port]
        for _port in port.salidas:
            for __port in _port.salidas:
                for ___port in __port.salidas:
                    if port in ___port.salidas:
                        if ciclounico((port.ide,_port.ide,__port.ide,___port.ide),listaout):
                            listaout.append((port.ide,_port.ide,__port.ide,___port.ide))
    return listaout

def ciclounico(ciclo,listaout):
    for ciclo_en_lista in listaout:
        ciclo_en_lista = ciclo_en_lista.value
        contador = 0
        for ide in ciclo:
            if ide in ciclo_en_lista:
                contador += 1
        if contador == len(ciclo):
            return False
    return True