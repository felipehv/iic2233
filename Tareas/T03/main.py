# Tarea 3
from jugador import *
from classes import *

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
            2 : 1 vs PC\n
            """)
        opcion = input('Opcion: ').strip()
        try:
            int(opcion)
            self.opciones_inicio[opcion]()
        except Exception as ex:
            print('Error {}'.format(ex))

    def jugar(self):
        n = input("Ingrese el tamanio del tablero: ").strip()
        self.jugador1 = Jugador(n)
        self.jugador2 = Jugador(n)
        #Cargar vehiculos para jugar en los jugadores
        self.jugador1.rellenar_tablero()
        self.jugador2.rellenar_tablero()
        if randint(1,2) == 1:
            while nadie_ha_perdido(p1,p2):
                    turno(p1,p2)
        else:
            while nadie_ha_perdido(p1,p2):
                turno(p2,p1)
        print('Fin del juego')


    def jugarvsPC(self):
        pass

    def turno(self,p1,p2):
        p1.showMenu()
        p2.showMenu()

if __name__ == "__main__2":
    juego = Juego()
    juego.menu()