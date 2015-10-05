class Jugador():

    def __init__(self, n):
        self.n = n
        self.nombre = input('Ingrese su nombre: ').strip()
        self.tierra = [[[] for i in range(n)] for j in range(n)]
        self.aire = [[[] for i in range(n)] for j in range(n)]
        self.opciones = {1: self.atacar, 2: self.mover}
        self.vehiculos = []

    def showMenu(self):
        while True:
            print("""
                Seleccione una opcion:
                1 - Atacar
                2 - Mover
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
            temp_list = [v for v in self.vehiculos]
        else:
            temp_list = [
                v for v in self.vehiculos if self.vehiculos.can_attack]

        while True:
            print("""
                Seleccione un vehiculo de los
                disponibles para atacar
                """)
            for i in range(len(self.vehiculos)):
                print(i, vehiclo.__name__)
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

    def mover(self, vehiculo):
        pass

    def atacar(self, vehiculo):
        pass

if __name__ == "__main__":
    a = Jugador(5)
    print(a.tierra)
