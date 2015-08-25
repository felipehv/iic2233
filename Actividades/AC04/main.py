# coding=utf-8

from collections import deque
# Completen los métodos
# Les estamos dando un empujoncito con la lectura del input
# Al usar la clausula: "with open('sonda.txt', 'r') as f", el archivo se cierra automáticamente al salir de la función.


def sonda():
    consultas = int(input('Numero de consultas'))
    a = dict()
    with open('data/sonda.txt', 'r') as f:
        for line in f:
            b = (line.strip().split(','))
            c = ','.join(b[0:4])
            a[c] = b[4]
    for i in range(consultas):
        coord = input().strip()
        if coord in a:
            print(a[coord])
        else:
            print('No hay nada')


def traidores():
    bufalos = set()
    with open('data/bufalos.txt', 'r') as f:
        for line in f:
            bufalos.add(line.strip())

    rivales = set()
    with open('data/rivales.txt', 'r') as f:
        for line in f:
            rivales.add(line.strip())
    traidores = rivales.intersection(bufalos)
    print('Lista de traidores: ')
    for traidor in traidores:
        print(traidor)


def pizzas():
    apiladas = []
    encoladas = deque()
    pizzas = 0
    with open('data/pizzas.txt', 'r') as f:
        for line in f.read().splitlines():
            if line.strip() == 'APILAR':
                pizzas += 1
                apiladas.append('Pizza {}'.format(pizzas))
                string = '{} apilada'.format(apiladas[len(apiladas)-1])
            elif line.strip() == 'ENCOLAR':
                encolar = apiladas.pop()
                encoladas.appendleft(encolar)
                string = '{} encolada'.format(encolar)
            elif line.strip() == 'SACAR':
                sacar = encoladas.popleft()
                string = '{} sacada'.format(sacar)
            print('{}, {} pizza apilada - {} pizzas en cola'.format(string,len(apiladas),len(encoladas)))

if __name__ == '__main__':
    exit_loop = False

    functions = {"1": sonda, "2": traidores, "3": pizzas}

    while not exit_loop:
        print(""" Elegir problema:
            1. Sonda
            2. Traidores
            3. Pizzas
            Cualquier otra cosa para salir
            Respuesta: """)

        user_entry = input()

        if user_entry in functions:
            functions[user_entry]()
        else:
            exit_loop = True
