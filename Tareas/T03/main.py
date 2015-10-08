# Tarea 3
from jugador import *
from classes import *


def ganador(p1, p2):
    vp1 = [v for v in p1.vehiculos if v.isAlive and v.tipo != "aire"]
    vp2 = [v for v in p2.vehiculos if v.isAlive and v.tipo != "aire"]
    if len(vp1) == 0:
        return "Jugador 2"
    elif len(vp2) == 0:
        return "Jugador 1"
    else:
        print(len(vp1), len(vp2))
        return False


class Juego():

    def __init__(self):
        self.jugador1 = None
        self.jugador2 = None

        self.opciones_inicio = {1: self.jugar, 2: self.jugarvsPC}

    def menu(self):
        print('\tBienvenido a BattleSheep by Bummer\t')
        print("""
            Seleccione una opcion:
            1 : 1 vs 1
            2 : 1 vs PC\n
            """)
        opcion = self.verificar_opcion(input('Opcion: ').strip())
        try:
            opcion = int(opcion)
            self.opciones_inicio[opcion]()
        except Exception as ex:
            print('Error {}'.format(ex))

    def jugar(self):
        n = input("Ingrese el tamanio del tablero: ").strip()
        self.jugador1 = Jugador(n)
        self.jugador2 = Jugador(n)
        # Cargar vehiculos para jugar en los jugadores
        self.jugador1.vehiculos_disponibles = [v() for v in vehiculos]
        self.jugador2.vehiculos_disponibles = [v() for v in vehiculos]
        self.jugador1.rellenar_tablero()
        self.jugador2.rellenar_tablero()
        if randint(1, 2) == 1:
            while not ganador(self.jugador1, self.jugador2):
                self.turno(self.jugador1, self.jugador2)
        else:
            while not ganador(self.jugador1, self.jugador2):
                self.turno(self.jugador2, self.jugador1)
        print("Ha ganado {}".format(ganador(self.jugador1,self.jugador2)))
        informe(self.jugador1)
        informe(self.jugador2)
        print('Fin del juego')

    def jugarvsPC(self):
        """
        Gracias a proba no pude hacer esta parte =(
        """
        pass

    def turno(self, p1, p2):
        p1.showMenu(p2)
        p2.showMenu(p1)

    def verificar_opcion(self, n):
        try:
            n = int(n)
        except ValueError as err:
            print("Intentalo de nuevo")
            return False
        return True

    def informe(self, j): #j representa un jugador
        print(j.nombre)
        atk_total = 0
        dano_total_causado = 0
        atk_mas_efi = (None, 0)
        for vehiculo in j.vehiculos:
            vehiculo_exitosos = 0
            vehiculo_n_ataques = 0
            for atk in vehiculo.ataque:
                dano_total_causado += ataque.dano_realizado
                atk_total += ataque.canditad_ataques
                if ataque.exito / ataque.dano_realizado > atk_mas_efi[1]:
                    atk_mas_efi = (ataque.__class__.__name__,
                                   ataque.exito / ataque.dano_realizado)
        print("ataque total: {}".format(atk_total))
        print("dano total: {}".format(dano_total_causado))
        print("Ataque mas eficiente: {}".format(atk_mas_efi))


if __name__ == "__main__":
    juego = Juego()
    juego.menu()
