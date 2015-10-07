def verificar_posicion(self,pos,tab):
        try:
            pos = pos.split(',')
            x = int(pos[0])
            y = int(pos[1])
        except ValueError:
            print("Ingrese una posicion valida: {}".format(err))
            return False
        else:
            if x < len(tab) and y < len(tab):
                return True
class Ataque:

    def __init__(self):
        self.area = (1, 1)
        self.cantidad_ataques = 0
        self.exito = 0
        self.dano_realizado = 0

    def atacar(self, p1, p2):
        pos = input('Elija una posicion')
        if verificar_posicion(pos,p2.agua):
            for i in range(self.area[0]):
                if self.area[1] == 'n':
                    for j in range(self.n):
                        if otro.tierra[pos[0] + i][j] != '   ':
                            key = otro.tierra[pos[0] + i][j]
                            for v in otro.vehiculos:
                                if key == v.nombre and v.isAlive:
                                    v.dano_recibido += self.damage
                                    self.dano_realizado += self.damage
                                    self.exito += 1
                                    if v.dano_recibido >= v.resistencia:
                                        v.isAlive = False
                                self.cantidad_ataques += 1
                else:
                    for j in range(self.area[1]):
                        if otro.tierra[pos[0] + i][pos[1] + j] != '   ':
                            key = otro.tierra[pos[0] + i][pos[1] + j]
                            for v in otro.vehiculos:
                                if key == v.nombre and v.isAlive:
                                    v.dano_recibido += self.damage
                                    self.dano_realizado += self.damage
                                    self.exito += 1
                                    if v.dano_recibido >= v.resistencia:
                                        v.isAlive = False
                                self.cantidad_ataques += 1


class MBIMIII(Ataque):

    def __init__(self):
        self.nombre = "Misil Balistico Intercontinental Minuteman III"
        self.damage = 15
        self.restriccion = 3
        self.can_attack = True
        self.turnos_restantes = 0
        super().__init__()


class UGM133(Ataque):

    def __init__(self):
        super().__init__()
        self.nombre = "Misil UGM-133 Trident II"
        self.damage = 5
        self.restriccion = 0
        self.can_attack = True
        self.turnos_restantes = 0
        self.area = (1, "n")


class BGM109(Ataque):

    def __init__(self):
        self.nombre = "Misil de crucero BGM-109 Tomahawk"
        self.damage = 0
        self.restriccion = 3
        self.can_attack = True
        self.turnos_restantes = 0
        super().__init__()


class GBU43(Ataque):

    def __init__(self):
        self.nombre = "GBU-43/B Massive Ordnance Air Blast Paralizer"
        self.damage = 0
        self.restriccion = 0
        self.can_attack = True
        self.turnos_restantes = 0
        super().__init__()

    def atacar(self,p1,p2):
        pos = input("Elija una posicion: x,y")
        if verificar_posicion(pos,p2.aire):
            pos = pos.split(',')
            if input("Horizontal? 1: True, Otra Cosa: False"):
                horiz = True
                if horiz:
                    for i in range(2):
                        if p2.aire[pos[0]+i][pos[1]] == "AVE":
                            p2.vehiculos[1].paralized = 5
                else:
                    for j in range(2):
                        if p2.aire[pos[0]][pos[1]+j] == "AVE":
                            p2.vehiculos[1].paralized = 5


class KitIngeniero(Ataque):

    def __init__(self):
        self.nombre = "Kit de Ingenieros"
        self.damage = 0
        self.restriccion = 2
        self.can_attack = True
        self.turnos_restantes = 0
        super().__init__()

    def atacar(self,p1,p2):
        while True:
            for i in range(len(p1.vehiculos)):
                print(i,p1.vehiculos[i].__name__)
            v = input("Seleccione el numero de vehiculo a reparar").strip()
            if v == '4' or not v.isdigit() or int(v) > 7:
                print("Intente de nuevo")
            else:
                p1.vehiculos[v].dano_recibido = 0
        self.can_attack = False
        self.turnos_restantes = self.restriccion


class Napalm(Ataque):

    def __init__(self):
        self.nombre = "Misil Balistico Intercontinental Minuteman III"
        self.damage = 0
        self.restriccion = 8
        self.can_attack = True
        self.turnos_restantes = 0
        super().__init__()


class Kamikaze(Ataque):

    def __init__(self):
        self.nombre = "Kamikaze"
        self.damage = 100000000000
        self.restriccion = 0
        self.can_attack = True
        self.turnos_restantes = 0
        super().__init__()
        

class Explorar(Ataque):

    def __init__(self):
        self.nombre = "Explorar"
        self.damage = 0
        self.restriccion = 2
        self.can_attack = True
        self.turnos_restantes = 0
        super().__init__()

ataques = {1: MBIMIII(), 2: UGM133(), 3: BGM109(), 4: GBU43(),
           5: KitIngeniero(), 6: Napalm(), 7: Kamikaze(), 8: Explorar()}
