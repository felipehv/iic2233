class Vehiculo:

    def __init__(self):
        self.cantidad_movimientos = 0
        self.danio_realizado = 0
        self.n_ataques = 0
        self.ataques_exitosos = 0
        self.lista_posiciones = []

        self.dano_recibido = 0

        self.menu = {1: self.atacar, 2: self.mover}

    def actualizar(self):
        pass

class BarcoPequeno(Vehiculo):

    def __init__(self):
        self.resistencia = 30
        self.ataque = Ataque('Misil Balistico Intercontinental Minuteman III')
        self.dimension = (3, 1)
        super().__init__(self)


class BuqueDeGuerra(Vehiculo):

    def __init__(self):
        self.resistencia = 60
        self.ataque = Ataque(None, None)
        self.dimension = (2, 3)
        super().__init__(self)


class Lancha(Vehiculo):

    def __init__(self):
        self.resistencia = 1
        self.ataque = None
        self.dimension = (2, 1)
        super().__init__(self)


class Puerto():

    def __init__(self):
        self.resistencia = 80
        self.ataque = None
        self.dimension = (4, 2)

    def showMenu(self):  # Pendiente
        print("""
            Seleccione barco a reparar.
            """)

    def reparar(self, barco):
        pass


class AvionExplorador(Vehiculo):

    def __init__(self):
        pass


class Ataque():

    def __init__(self, nombre, damage):
        self.nombre = nombre
        self.damage = damage
        self.restriccion = 0
        self.can_attack = True
        self.turnos_restantes = 0
