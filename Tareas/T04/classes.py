import random as rd
"""
Classes
"""
def isCalle(algo):
    return algo.__class__.__name__ == "Calle"

class Calle:
    direcciones = {"izquierda": (
        0, -1), "derecha": (0, 1), "arriba": (-1, 0), "abajo": (1, 0)}

    def __init__(self, sem, direccion):
        self.semaforo = sem
        self.direccion = Calle.direcciones[direccion]




class Vehiculo():
    
    def __init__(self, pos, sim):
        self.pos = pos
        self.sim = sim

    def avanzar(self):
        if self.sim[pos[0]][pos[1]]: ############3
            pass

    def calcular_camino(self):
        caminos = []

        def recur(camino, pos_actual, pos_final):
            if pos_actual == pos_final:
                caminos.append(camino)
            for x, y in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                nueva_pos = pos_actual[0] + x, pos_actual[1] + y
                if isCalle( self.mapa[nueva_pos[0]][nueva_pos[1]][0] ):
                    pass
                elif nueva_pos in camino:
                    return
            return caminos


class Taxi(Vehiculo):

    def __init__(self, *args):
        self.sim = sim
        self.proximo_pasajero = round(rd.expovariate(1/10) + 0.5)
        self.busy = False
        self.destino = None

    def avanzar(self):
        if self.proximo_pasajero == self.sim.t:
            self.busy = True
        if self.sim.matriz[0][0]:
            pass

    def recoger(self):
        self.tiempo_recoger = rd.randint()

    def dejar(self):
        pass

    @property
    def velocidad(self):
        return (rd.uniform(0.5,1))
    


class Ambulance(Vehiculo):

    def __init__(self, *args):
        self._velocidad = 0.5
        self.sirena = False
        super().__init__(**kwargs)

    @property
    def velocidad(self):
        if self.sirena:
            return 1
        return self._velocidad


class CarroBomba(Vehiculo):

    def __init__(self, **kwargs):
        self._velocidad = 0.5
        self.sirena = False
        super().__init__(**kwargs)

    @property
    def velocidad(self):
        if self.sirena:
            return 1
        return self._velocidad


class Casa:
    tiempo_apagado = {"madera": (30, 120), "ladrillo": (
        40, 100), "hormigon": (60, 80), "metal": (30, 40)}
    peso = "madera": 10, "ladrillo": 7 "hormigon": 4, "metal": 2}

    def __init__(self, material, posicion, simulacion, rango_robo):
        self.material = material
        self.busy = False
        self.sim = simulacion
        self.pos = posicion
        self.peso = Casa.peso[material]
        self.rango_robo = rango_robo

        self.robo = False
        self.incendio = False
        self.enfermo = False

        self.copsHere = False
        self.ffHere = False  # Firefighters
        self.ambulanceHere = False


    #Incendios#######################################################
    def incendiar(self):
        self.sim.tiempo_incendios.append(0)
        self.incendio = True
        self.ide_incendio = len(self.sim.tiempo_incendios) - 1
        self.busy = True
        self.sim.quitar_imagen(*self.pos)
        print("Se ha desatado un incendio en {}".format(self.pos))

    def comenzar_apagado(self):
        rango = Casa.tiempo_apagado[self.material]
        self.tiempo_apagado = self.sim.t + round(rd.uniform(*rango))*60
    ##################################################################

    #Robos############################################################
    def robar(self):
        self.robo = True
        self.busy = True
        self.tiempo_escape = self.sim.t + round(rd.uniform(2,10))

    def escape(self):
        self.sim.ladron_escapa += 1
        self.busy = False
        self.robo = False

    ##################################################################

    def pasar_segundo(self):
        if self.incendio and self.ffHere :
            

        elif self.robo and self.tiempo_escape == self.sim.t:
            self.escape()

class EstacionBomberos:

    def __init__(self,pos,sim):
        self.pos = pos
        self.sim = sim

    def crear_carro(self):
        for x,y in ((0, 1), (0, -1), (-1, 0), (1, 0)):
           pass 