from random import randint
from ataques import *

class Vehiculo:

    def __init__(self):
        self.cantidad_movimientos = 0
        self.danio_realizado = 0
        self.n_ataques = 0
        self.ataques_exitosos = 0
        self.lista_posiciones = []

        self.isAlive = True

        self.dano_recibido = 0

        #self.menu = {1: self.atacar, 2: self.mover}
    def actualizar(self):
        for ataque in self.ataques:
            if not ataque.can_attack:
                ataque.turnos_restantes -= 1
                if ataque.turnos_restantes == 0:
                    ataque.can_attack = True


class BarcoPequeno(Vehiculo):

    def __init__(self):
        self.resistencia = 30
        self.ataque = MBIMIII()
        self.dimension = (3, 1)
        self.key = BCP
        super().__init__(self)


class BuqueDeGuerra(Vehiculo):

    def __init__(self):
        self.resistencia = 60
        self.ataque = MBIMIII()
        self.dimension = (2, 3)
        self.key = BDG
        super().__init__(self)


class Lancha(Vehiculo):

    def __init__(self):
        self.resistencia = 1
        self.ataque = None
        self.dimension = (2, 1)
        self.key = LAN
        super().__init__(self)


class Puerto(Vehiculo):

    def __init__(self):
        self.resistencia = 80
        self.ataque = MBIMIII(),KitIngeniero()
        self.dimension = (4, 2)
        self.key = PTO

    def atacar(self):
        print("""
            Seleccione barco a reparar.
            """)

    def reparar(self, barco):
        pass


class AvionExplorador(Vehiculo):

    def __init__(self):
        super().__init__(self)
        self.key = AVE
        self.ataque = Paralizador(),Explorar()
        self.paralized = 0

    def paralizar(self):
        self.paralized = True
        self.turnos_restantes = 5

    def actualizar(self):
        for ataque in self.ataques:
            if not ataque.can_attack:
                ataque.turnos_restantes -= 1
                if ataque.turnos_restantes == 0:
                    ataque.can_attack = True
        if self.paralized:
            self.paralized -= 1


class AvionKamikazeIXXI(Vehiculo):

    def __init__(self):
        super().__init__(self)
        self.key = AVK
        self.ataque = MBIMIII(),Kamikaze()

    def actualizar(self):
        if self.ataque[1].can_attack = False:
            self.isAlive = False
        for ataque in self.ataques:
            if not ataque.can_attack:
                ataque.turnos_restantes -= 1
                if ataque.turnos_restantes == 0:
                    ataque.can_attack = True


class AvionCaza(Vehiculo):

    def __init__(self):
        super().__init__(self)
        self.key = AVC
        self.ataque = MBIMIII(),Napalm()

vehiculos = [BarcoPequeno, Lancha, BuqueDeGuerra, Puerto,
             AvionCaza, AvionCaza, AvionExplorador, AvionKamikazeIXXI]
