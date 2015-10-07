# Tarea 3
from jugador import *


class Juego():

    def __init__(self):
        self.opciones = {"1": self.agregar_jugador}
        self.jugador1 = None
        self.jugador2 = None

        self.opciones_inicio = {1: self.jugar, 2: self.jugarvsPC}

    def menu(self):
        print('\tBienvenido a BattleSheep by Bummer\t')
        print("""
            Seleccione una opcion:
            1 : 1 vs 1
            2 : 1 vs PC:\n
            """)
        opcion = input('Opcion: ').strip()
        try:
            int(opcion)
            self.opciones_inicio[opcion]()
        except Exception as ex:
            print('Error {}'.format(ex))

    def jugar(self):
        n = input("Ingrese el tamanio del tablero: ").strip()
        P1 = Jugador(n)
        P2 = Jugador(n)
        while True:
            P1.im

    def jugarvsPC(self):
        pass


if __name__ == "__main__2":
    juego = Juego()
    juego.menu()