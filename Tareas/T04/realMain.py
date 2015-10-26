#!/usr/local/bin python3
# -*- encoding: utf-8 -*-
from PyQt4 import QtGui
from gui.gui import GrillaSimulacion
import random as rnd
import simpy
from classes import *
import random as rd

# EJEMPLO COMENTADO DE INTERFAZ GRÁFICA


def main():
    # Aquí se inicializa el sistema de ventanas de PyQt4. Es importante
    # tener claro que aquí aún NO se muestra la ventana de la simulación.
    app = QtGui.QApplication([])

    # Inicializamos la ventana propiamente tal, aún sin mostrarla. Le pasamos
    # una referencia al objeto instanciado más arriba para poder actualizar
    # la interfaz en cada cambio realizado.
    grilla = GrillaSimulacion(app, 30)

    # Mostramos la ventana.
    grilla.show()

    # Como la simulación es por eventos discretos (muy rápida), es
    # recomendable esperar algún intervalo de tiempo entre actualizaciones
    # de la interfaz. Es importante detallar en el README.md si se decide

    # Además existe el parámetro `tiempo_intervalo` de `GrillaSimulacion` que
    # controla el intervalo de tiempo entre actualizaciones. Por defecto parte
    # con un valor igual a 0, para inicializar la iterfaz rápido, pero luego
    # deben modificarlo para que la simulación muestre los cambios a una
    # velocidad más amigable.
    grilla.tiempo_intervalo = 0.5

    for x in range(1, 21):
        for y in range(1, 31):
            grilla.quitar_imagen(x, y)

    # Bloqueamos el thread principal para que la ventana permanezca abierta.
    # Cuando se cierra la ventana, el thread principal se libera y se termina
    # la ejecución del programa.
    app.exec_()

#Primera Parte
class Simulacion:

    def __init__(self):
        #Variables estadisticas
        self.cantidad_autos = 0
        self.tiempo_incendios = []
        self.ladron_escapa = 0
        self.ladron_capturado = 0

        with open("mapa fix.txt","r") as reader:
            first = reader.readline().strip().split('x')
            height = int(first[0])
            width = int(first[1])
            self.app = QtGui.QApplication([])
            self.grilla = GrillaSimulacion(self.app, height, width)
            self.grilla.tiempo_intervalo = 0.1
            self.matriz = [ [ [] for i in range(width) ] for j in range(height)]
            for linea in reader:
                linea = linea.split(' ')
                pos = linea[0].strip().split(',')
                pos_x = int(pos[0])
                pos_y = int(pos[1])
                if linea[1] == "casa":
                    print(pos)
                    self.grilla.agregar_casa(pos_x,pos_y)
                    #self.matriz[pos_x][pos_y] = Casa(1,1)
                    self.grilla.actualizar()
                elif linea[1] == "calle":
                    self.grilla.agregar_calle(pos_x,pos_y)
                    #self.matriz[pos_x][pos_y].append(Calle(False,linea[2].strip()))
                    #self.grilla.actualizar()
                elif linea[1] == "vacio":
                    #.grilla.actualizar()
                    pass
        self.matriz = [[] for i in range(1)]
        self.grilla.show()
        self.app.exec_()


    def pasar_segundo(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                self.matriz.simular()

    def generar_incendio(self):
        lista_casas = []
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                pass

    def simular(self):
        with open("informe.txt") as writer:
            t = 0
            prox_incendio = rd.expovariate(1/10)
            prox_robo = 0
            prox_enfermo = 0
            while t < 


    def escribir_informe(self):
        pass


if __name__ == "__main__":
    sim = Simulacion()
    print(len(sim.matriz))