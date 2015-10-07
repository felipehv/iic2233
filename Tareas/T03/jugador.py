def sumaV(x,y):
    return x[0] + y[0] , x[1] + y[1]
class Jugador():

    def __init__(self, n):
        self.n = n
        self.nombre = input('Ingrese su nombre: ').strip()
        self.agua = [[["   "] for i in range(n)] for j in range(n)]
        self.aire = [[["   "] for i in range(n)] for j in range(n)]
        self.opciones = {1: self.atacar, 2: self.mover}
        self.vehiculos = []

        self.vehiculos_disponibles = []

        #Estadisticas
        self.n_ataques = 0
        self.ataques_efectivos = 0
        self.daño_realizado = 0
        self.barcos_atacados = 0

    def terminar_turno(self):
        for v in self.vehiculos:
            if not v.isAlive:
                for i in range(self.n):
                    for j in range(self.n):
                        if self.aire[i][j] == v.key:
                            self.aire[i][j] = "   "
                        if self.agua[i][j] == v.key:
                            self.agua[i][j] = "   "


    def imprimir_tablero(self):
        print("aire")
        for i in range(self.n):
            print(i,end="")
            print(self.agua[i])
        print("agua")
        for i in range(self.n):
            print(i,end="")
            print(self.agua[i])


    def showMenu(self):
        while True:
            print("""
                Seleccione una opcion:
                1 - Atacar
                2 - Mover
                3 - Ver resumen de jugadas
                """)
            opcion = input('Opcion: ').strip()
            try:
                opcion = int(opcion)
                accion = self.opciones[opcion]
            except ValueError as err:
                print('Ingrese un numero valido: err')
            except KeyError as err:
                print('Ingrese un numero valido: err')
            else:
                break
        if accion == self.mover:
            temp_list = [v for v in self.vehiculos if v.__name__ != Puerto and v.isAlive]
            while True:
                print("""
                    Seleccione un vehiculo de los
                    disponibles para mover
                    """)
                for i in range(len(self.vehiculos)):
                    print(i, vehiculo.__name__)
                v = input('')
                try:
                    v = int(v)
                    vehiculo = self.vehiculos[v]
                except IndexError as err:
                    print("Seleccione un numero valido: {}".format(err))
                except ValueError as err:
                    print("Ingrese un numero entero: {}")
                else:
                    break
        else:
            temp_list = [
                v for v in self.vehiculos if v.can_attack and v.isAlive]


    def rellenar_tablero(self):
        while self.vehiculos_disponibles != []:
            vehiculo = self.vehiculos_disponibles.pop()
            while True:
                pos = input("""Eija una posicion separada por coma: x,y
                            La cual sera la esquina superior 
                            izquierda del vehiculo""")

                if verificar_posicion(pos) and verificar_cupo(pos):
                    colocar_en_tablero(vehiculo,pos)
                    break

    def colocar_en_tablero(self,vehiculo,pos,tab):
        pos = pos.split(',')
        x = int(pos[0])
        y = int(pos[1])
        if tab == "t"
        for i in range(x,vehiculo.dimension[0]):
            for j in range(y,vehiculo.dimension[1]):
                self.agua[i][j] = vehiculo.key
        else:
            for i in range(x,vehiculo.dimension[0]):
                for j in range(y,vehiculo.dimension[1]):
                self.aire[i][j] = vehiculo.key

    def verificar_posicion(self,pos,tab):
        try:
            pos = pos.split(',')
            x = int(pos[0])
            y = int(pos[1])
        except ValueError:
            print("Ingrese una posicion valida: {}".format(err))
            return False
        else:
            return True

    def verificar_cupo(self,vehiculo,pos):
        pos = pos.split(',')
        x = int(pos[0])
        y = int(pos[1])
        if tab == "t":
            for i in range(x,vehiculo.dimension[0]):
                for j in range(y,vehiculo.dimension[1]):
                    if self.agua[i][j] != "   ":
                        return False
        else:
            for i in range(x,vehiculo.dimension[0]):
                for j in range(y,vehiculo.dimension[1]):
                    if self.aire[i][j] != "   ":
                        return False 
        return True

    def mover(self,vehiculo,dir,tab):
        if tab == 't':
            for coord in self.vehiculo.lista_posiciones:
                nuevapos = sumaV(coord,direccion)
                self.tablero.tierra[nuevapos[0]][nuevapos[1]] == vehiculo.key
                self.tablero.tierra[coord[0]][coord[1]] = '   '
                

    def verificar_movimiento(self,vehiculo,direccion,tab):
        if tab == 't':
            for coord in self.vehiculo.lista_posiciones:
                nuevapos = sumaV(coord,direccion)
                if nuevapos[0]>=self.n or nuevapos[1]>=self.n or self.tablero.tierra[nuevapos[0]][nuevapos[1]] != '   ':
                    return False
        else:
            for coord in self.vehiculo.lista_posiciones:
                nuevapos = sumaV(coord,direccion)
                if nuevapos[0]>=self.n or nuevapos[1]>=self.n or self.tablero.tierra[nuevapos[0]][nuevapos[1]] != '   ':
                    return False
        return True






class Robot(Jugador):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    a = Jugador(5)
    a.imprimir_tablero()
