def cicloDoble(listain,listaout):
    for port in listain:
        port = port.value
        for i in port.salidas:
            _port = listain[i].value
            if port.ide in _port.salidas:
                listaout.append(port.ide,i)

def cicloTriangular(listain,listaout):
    for port in listain:
        port = port.value
        for i in port.salidas:
            _port = listain[i].value
            for j in _port.salidas:
                __port = listain[j].value
                if port.ide in __port.salidas:
                    listaout.append(port.ide,i,j)

def cicloCuadrado(listain,listaout):
    for port in listain:
        port = port.value
        for i in port.salidas:
            _port = listain[i].value
            for j in _port.salidas:
                __port = listain[j].value
                for k in __port.salidas:
                    ___port = listain[k].value
                    if port.ide in ___port.saidas:
                        listaout.append(port.ide,i,j,k)

    