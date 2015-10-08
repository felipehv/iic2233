from random import randint
from ataques import *

class Vehiculo:

    def __init__(self):
        self.cantidad_movimientos = 0
        self.danio_realizado = 0
        self.n_ataques = 0
        self.ataques_exitosos = 0
        self.lista_posiciones = []
        self.tipo = "agua"
        self.mover = True

        self.isAlive = True

        self.dano_recibido = 0

    def actualizar(self):
        for ataque in self.ataques:
            if not ataque.can_attack:
                ataque.turnos_restantes -= 1
                if ataque.turnos_restantes == 0:
                    ataque.can_attack = True

    def showAtaque(self):
        for i in range((self.ataque)):
            print(i,self.ataque.__name__)
        atk = input("seleccione ataque: ")
        return self.ataque[atk]


class BarcoPequeno(Vehiculo):

    def __init__(self):
        super().__init__()
        self.resistencia = 30
        self.ataque = MBIMIII()
        self.dimension = (3, 1)
        self.key = "BCP"


class BuqueDeGuerra(Vehiculo):

    def __init__(self):
        super().__init__()
        self.resistencia = 60
        self.ataque = MBIMIII()
        self.dimension = (2, 3)
        self.key = "BDG"


class Lancha(Vehiculo):

    def __init__(self):
        super().__init__()
        self.resistencia = 1
        self.ataque = None
        self.dimension = (2, 1)
        self.key = "LAN"


class Puerto(Vehiculo):

    def __init__(self):
        self.resistencia = 80
        self.ataque = MBIMIII(),KitIngeniero()
        self.dimension = (4, 2)
        self.key = "PTO"
        self.tipo = "agua"
        self.mover = False
        self.isAlive = True

    def atacar(self):
        print("""
            Seleccione barco a reparar.
            """)

    def reparar(self, barco):
        pass


class AvionExplorador(Vehiculo):

    def __init__(self):
        super().__init__()
        self.key = "AVE"
        self.ataque = Paralizador(),Explorar()
        self.paralized = 0
        self.tipo = "aire"
        self.dimension = (3,3)

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
        super().__init__()
        self.key = "AVK"
        self.ataque = MBIMIII(),Kamikaze()
        self.tipo = "aire"
        self.dimension = (1,1)

    def actualizar(self):
        if self.ataque[1].can_attack == False:
            self.isAlive = False
        for ataque in self.ataques:
            if not ataque.can_attack:
                ataque.turnos_restantes -= 1
                if ataque.turnos_restantes == 0:
                    ataque.can_attack = True


class AvionCaza(Vehiculo):

    def __init__(self):
        super().__init__()
        self.key = "AVC"
        self.ataque = MBIMIII(),Napalm()
        self.tipo = "aire"
        self.dimension = (1,1)

vehiculos = [BarcoPequeno, Lancha, BuqueDeGuerra, Puerto,
             AvionCaza, AvionExplorador, AvionKamikazeIXXI]
