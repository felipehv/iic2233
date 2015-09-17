def cicloDoble(listain,listaout):
    for port in listain:
        port = listain[port]
        for _port in port.salidas:
            if port.ide in _port.salidas:
                listaout.append(port.ide,_port.ide)

def cicloTriangular(listain,listaout):
    for port in listain:
        port = listain[port]
        for _port in port.salidas:
            for __port in _port.salidas:
                if port.ide in __port.salidas:
                    listaout.append(port.ide,_port.ide,__port.ide)

def cicloCuadrado(listain,listaout):
    for port in listain:
        port = listain[port]
        for _port in port.salidas:
            for __port in _port.salidas:
                for ___port in __port.salidas:
                    if port.ide in ___port.saidas:
                        listaout.append(port.ide,_port.ide,__port.ide,___port.ide)