# coding=utf-8

class Nodo:   
    def __init__(self, valor = "Nodo", padre = None):
        self.valor = valor
        self.padre = padre
        self.hijos = []

    def subnodo(self,valor):
        #valor corresponde al valor del nodo buscado
        try:
            if valor == self.valor:
                return self
            for N in self.hijos:
                A = N.subnodo(valor)
                if A:
                    return A
            return None

        except:
            print("Error")

    def add_hijos(self,lista):
        #lista es una lista de nodos o
        #lista tambien puede poseer valores y estos serán transformados en nodos
        try:
            for hijo in lista:
                if str(type(hijo))[17:-2] == "Nodo":
                    self.hijos.append(hijo)
                else:
                    self.hijos.append(Nodo(hijo,self.valor))
        except:
            print("Error")

    def add_subhijos(self,lista,valor): #agregar hijos a algun descendiente de este nodo
        #valor corresponde al valor del nodo al que se desean agregar hijos
        try:
            N = self.subnodo(valor)
            if N:
                N.add_hijos(lista)
        except:
            print("Error")

    @property
    def descendencia(self): #devuelve un setcon los valores del nodo y su descendencia
        try:
            A = set(); A.add(self.valor); R = A
            if self.hijos:
                for hijo in self.hijos:
                    R = R.union(hijo.descendencia)
            return R
        except:
            print("Error")

    def __repr__(self):
        return str(self.valor)

    

    def parentesco(self):
        #imprime en consola la información del nodo y su descendencia
        S = "'" + str(self)
        if self.padre:
            S += "', hijo de '" + str(self.padre)
        if self.hijos:
            S += "', es padre de:\n"
            for hijo in self.hijos:
                S += str(hijo) + " "
            print(S + "\n")
        else:
            S += "', es un leaf node"
            print(S + "\n")
        for hijo in self.hijos:
            hijo.parentesco()
    
  
A = Nodo("padre")
A.add_hijos(['hijo1','hijo2','hijo3'])
A.hijos[0].add_hijos(['nieto2','nieto3'])
A.add_subhijos(["nieto1"],"hijo2")

