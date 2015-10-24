#!/usr/local/bin python3
# -*- encoding: utf-8 -*-
from PyQt4 import QtGui
from gui.gui import GrillaSimulacion
import random as rnd
import simpy

# EJEMPLO COMENTADO DE INTERFAZ GRÁFICA


def main():
    # Aquí se inicializa el sistema de ventanas de PyQt4. Es importante
    # tener claro que aquí aún NO se muestra la ventana de la simulación.
    app = QtGui.QApplication([])

    # Inicializamos la ventana propiamente tal, aún sin mostrarla. Le pasamos
    # una referencia al objeto instanciado más arriba para poder actualizar
    # la interfaz en cada cambio realizado.
    grilla_simulacion = GrillaSimulacion(app, 30)

    # Mostramos la ventana.
    grilla_simulacion.show()

    # Como la simulación es por eventos discretos (muy rápida), es
    # recomendable esperar algún intervalo de tiempo entre actualizaciones
    # de la interfaz. Es importante detallar en el README.md si se decide

    # Además existe el parámetro `tiempo_intervalo` de `GrillaSimulacion` que
    # controla el intervalo de tiempo entre actualizaciones. Por defecto parte
    # con un valor igual a 0, para inicializar la iterfaz rápido, pero luego
    # deben modificarlo para que la simulación muestre los cambios a una
    # velocidad más amigable.
    grilla_simulacion.tiempo_intervalo = 0.5

    for x in range(1, 21):
        for y in range(1, 31):
            grilla_simulacion.quitar_imagen(x, y)

    # Bloqueamos el thread principal para que la ventana permanezca abierta.
    # Cuando se cierra la ventana, el thread principal se libera y se termina
    # la ejecución del programa.
    app.exec_()

#Primera Parte
class Simulacion:

    def __init__(self,grilla,archivo):
        casas = []
        with open("mapa fix.txt","r") as reader:
            first = reader.readline().strip().split('x')
            height = int(first[0])
            width = int(first[1])
            self.matriz = [ ['x' for i in range(width) ] for j in range(height)]
            for linea in reader:
                linea = linea.split(' ')
                if linea[1] == "casa":
                    pass

        self.grilla = grilla
        self.grilla2 = [[] for i in range(1)]


    def pasar_segundo(self):
        pass

if __name__ == "__main__":
    sim = Simulacion(1,"map fix.txt")
    print(len(sim.matriz))