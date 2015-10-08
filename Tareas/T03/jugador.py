def sumaV(x, y):
    return x[0] + y[0], x[1] + y[1]
direcciones = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Jugador():

    def __init__(self, n):
        self.n = int(n)
        self.nombre = input('Ingrese su nombre: ').strip()
        self.agua = [[["   "] for i in range(self.n)] for j in range(self.n)]
        self.aire = [[["   "] for i in range(self.n)] for j in range(self.n)]
        self.opciones = {1: None, 2: self.mover}
        self.vehiculos = []

        self.vehiculos_disponibles = []

        # Estadisticas
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
                            self.aire[i][j][0] = "   "
                        if self.agua[i][j] == v.key:
                            self.agua[i][j][0] = "   "

    def imprimir_tablero(self):
        print("aire")
        for i in range(self.n):
            print(i, end="")
            print(self.aire[i])
        print("agua")
        for i in range(self.n):
            print(i, end="")
            print(self.agua[i])

    def showMenu(self, otro):
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
            temp_list = [
                v for v in self.vehiculos if v.__class__.__name__ != "Puerto" and v.isAlive and v.mover]
            while True:
                print("""
                    Seleccione un vehiculo de los
                    disponibles para mover
                    """)
                v = input(' : ')
                try:
                    v = int(v)
                    vehiculo = self.vehiculos[v]
                except IndexError as err:
                    print("Seleccione un numero valido: {}".format(err))
                except ValueError as err:
                    print("Ingrese un numero entero: {}")
                else:
                    print("""
                        Elija una direccion
                        """)
                    direccion = input(
                        "1:abajo, 2:derecha, 3: arriba, 4:izquierda : ")
                    if direccion not in ["1", "2", "3", "4"]:
                        print("Intentalo de nuevo")
                        continue
                    else:
                        if vehiculo.tipo == "aire":
                            self.mover(vehiculo, direccion, vehiculo.aire)
                        else:
                            self.mover(vehiculo, direccion, vehiculo.agua)
                        self.imprimir_tablero()
                        break
        else:
            temp_list = [
                v for v in self.vehiculos if v.can_attack and v.isAlive]
            for i in range(len(temp_list)):
                print(i, temp_list[i].__class__.__name__)
            v = input("Seleccione vehiculo para atacar (1,2,..,n) ")
            vehiculo = temp_list[v]
            vehiculo.showAtaques()
            atk = input('Seleccione ataque: ')
            vehiculo.ataque[atk].atacar(self, otro)

    def rellenar_tablero(self):
        while self.vehiculos_disponibles != []:
            self.imprimir_tablero()
            vehiculo = self.vehiculos_disponibles.pop()
            print("Vehiculo {}".format(vehiculo.__class__.__name__))
            while True:
                pos = input("""Eija una posicion separada por coma: x,y
                            La cual sera la esquina superior 
                            izquierda del vehiculo\n""")

                if self.verificar_posicion(pos) and self.verificar_cupo(vehiculo, pos):
                    self.colocar_en_tablero(vehiculo, pos)
                    break

    def colocar_en_tablero(self, vehiculo, pos):
        pos = pos.split(',')
        x = int(pos[0])
        y = int(pos[1])
        if vehiculo.tipo == "agua":
            for i in range(x, x+vehiculo.dimension[0]):
                for j in range(y, y+vehiculo.dimension[1]):
                    self.agua[i][j][0] = vehiculo.key
        else:
            for i in range(x, x+vehiculo.dimension[0]):
                for j in range(y, y+vehiculo.dimension[1]):
                    self.aire[i][j][0] = vehiculo.key
        self.vehiculos.append(vehiculo)

    def verificar_posicion(self, pos):
        try:
            pos = pos.split(',')
            x = int(pos[0])
            y = int(pos[1])
        except ValueError:
            print("Ingrese una posicion valida: {}".format(err))
            return False
        else:
            return True

    def verificar_cupo(self, vehiculo, pos):
        pos = pos.split(',')
        x = int(pos[0])
        y = int(pos[1])
        if vehiculo.tipo == "agua":
            for i in range(x, x+vehiculo.dimension[0]):
                for j in range(y, y+vehiculo.dimension[1]):
                    try:
                        if self.agua[i][j][0] != "   ":
                            return False
                    except:
                        return False
        else:
            for i in range(x, x+vehiculo.dimension[0]):
                for j in range(y, y+vehiculo.dimension[1]):
                    try:
                        if self.aire[i][j][0] != "   ":
                            return False
                    except:
                        return False
        return True

    def mover(self, vehiculo, dir):
        if vehiculo.tipo == 'agua':
            for coord in self.vehiculo.lista_posiciones:
                nuevapos = sumaV(coord, direccion)
                self.tablero.agua[nuevapos[0]][nuevapos[1]] == vehiculo.key
                self.tablero.agua[coord[0]][coord[1]] = '   '
        else:
            for coord in self.vehiculo.lista_posiciones:
                nuevapos = sumaV(coord, direccion)
                self.tablero.aire[nuevapos[0]][nuevapos[1]] == vehiculo.key
                self.tablero.aire[coord[0]][coord[1]] = '   '

    def verificar_movimiento(self, vehiculo, direccion):
        if vehiculo.tipo == 'agua':
            for coord in self.vehiculo.lista_posiciones:
                nuevapos = sumaV(coord, direccion)
                if nuevapos[0] >= self.n or nuevapos[1] >= self.n or self.tablero.agua[nuevapos[0]][nuevapos[1]] != '   ':
                    return False
        else:
            for coord in self.vehiculo.lista_posiciones:
                nuevapos = sumaV(coord, direccion)
                if nuevapos[0] >= self.n or nuevapos[1] >= self.n or self.tablero.aire[nuevapos[0]][nuevapos[1]] != '   ':
                    return False
        return True


class Robot(Jugador):

    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    a = Jugador(5)
    a.imprimir_tablero()
