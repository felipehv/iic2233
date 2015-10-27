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

# Primera Parte


class Simulacion:
        nuevo_auto = [
                grilla_simulacion.agregar_convertible,
                grilla_simulacion.agregar_sedan,
                grilla_simulacion.agregar_pickup
            ]
    def __init__(self):
        # Variables estadisticas
        self.cantidad_autos = 0
        self.tiempo_incendios = []
        self.ladron_escapa = 0
        self.ladron_capturado = 0

        with open("mapa fix.txt","r") as reader:
            first = reader.readline().strip().split('x')
            height = int(first[0])
            width = int(first[1])
            self.app = QtGui.QApplication([])
            self.grilla = GrillaSimulacion(self.app, height+1, width+1)
            self.grilla.tiempo_intervalo = 0.01
            self.matriz = [ [ [] for i in range(width+1) ] for j in range(height+1)]
            print(self.matriz)
            for linea in reader:
                linea = linea.split(' ')
                pos = linea[0].strip().split(',')
                pos_x = int(pos[0])+1
                pos_y = int(pos[1])+1
                if linea[1] == "casa":
                    print(pos)
                    self.grilla.agregar_casa(pos_x,pos_y)
                    # self.matriz[pos_x][pos_y] = Casa(1,1)
                    self.grilla.actualizar()
                elif linea[1] == "calle":
                    self.grilla.agregar_calle(pos_x,pos_y)
                    # self.matriz[pos_x][pos_y].append(Calle(False,linea[2].strip()))
                    self.grilla.actualizar()
                elif linea[1] == "vacio":
                    self.grilla.actualizar()
                    pass
        self.matriz = [[] for i in range(1)]
        self.grilla.show()
        self.app.exec_()


    def generar_incendio(self):
        lista_casas = []
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[i][j][0].__class__.__name__ == "Casa":
                    lista_casas.append([self.matriz[i][j][0]])
        ultimo_rango
        peso_total = 0
        for i in range(len(lista_casas)):
            peso_total += lista_casas[i].peso
            lista_casas[i].peso


    def pasar_segundo(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                self.matriz.simular()

    def simular(self):
        with open("informe.txt") as writer:
            t = 0 #En segundos
            prox_incendio = rd.expovariate(1/10)*60*60
            prox_robo = t + rd.expovariate(1/4)*60*60
            prox_enfermo = t + rd.expovariate(1/2)*60*60
            while t < 50400:
                if prox_incendio == t:
                    self.generar_incendio()

    def escribir_informe(self):
        pass


if __name__ == "__main__":
    sim = Simulacion()
    print(len(sim.matriz))
