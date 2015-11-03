#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from pickle import loads, dumps, load, dump


class Persona:
    
    def __init__(self,ide,nombre):
        self.id = ide
        self.nombre = nombre
        self.amigos = []
        self.seguidores = []
        self.idolos = []

    def agregar_amigo(self,amigo):
        self.amigos.append(amigo)

    def __str__(self):
        return self.id + " " + self.nombre

    def __repr__(self):
        return self.__str__(self)

def existe_persona(_id):
    lista = os.listdir("./db")
    for name in lista:
        if _id in name:
            return True
    return False

def get_persona(_id):
    if existe_persona(_id):
        with open("./db/{}.iic2233".format(_id),'rb') as archivo:
            return load(archivo)



def write_persona(persona):
    ide = persona.id
    with open('./db/{}.iic2233'.format(ide),'wb') as archivo:
        dump(persona,archivo)


def crear_persona(_id, nombre_completo):
    persona = Persona(_id,nombre_completo)
    write_persona(persona)


def agregar_amigo(id_1, id_2):
    if existe_persona(id_1) and existe_persona(id_2):
        with open("./db/{}.iic2233".format(id_1),"rb") as persona1:
            persona1 = load(persona1)
        with open("./db/{}.iic2233".format(id_2),"rb") as persona2:
            persona2 = load(persona2)
        persona1.agregar_amigo(persona2)
        persona2.agregar_amigo(persona1)
        with open("./db/{}.iic2233".format(id_1),"wb") as archivo1:
            dump(persona1,archivo1)
        with open("./db/{}.iic2233".format(id_2),"wb") as archivo2:
            dump(persona2,archivo2)


def set_persona_favorita(_id, id_favorito):
    if existe_persona(_id) and existe_persona(id_favorito):
        with open("./db/{}.iic2233".format(_id),"rb") as persona1:
            persona = load(persona1)
        with open("./db/{}.iic2233".format(id_favorito),"rb") as persona2:
            persona_favorita = load(persona2)

        if persona not in persona_favorita.seguidores:
            persona_favorita.seguidores.append(persona)

        with open("./db/{}.iic2233".format(_id),"wb") as archivo1:
            dump(persona,archivo1)
        with open("./db/{}.iic2233".format(id_favorito),"wb") as archivo2:
            dump(persona_favorita,archivo2)


def get_persona_mas_favorita():
    lista = os.listdir("./db")
    mas_favorito = None,0
    print(lista)
    for archivo in lista:
        with open("./db/{}".format(archivo),"rb") as reader:
            persona = load(reader)
            if len(persona.seguidores) > mas_favorito[1]:
                mas_favorito = persona,len(persona.seguidores)
    return mas_favorito[0]

# ----------------------------------------------------- #
# Codigo para probar su tarea - No necesitan entenderlo #


def print_data(persona):
    if persona is None:
        print("[AVISO]: get_persona no está implementado")
        return

    for key, val in persona.__dict__.items():
        print("{} : {}".format(key, val))
    print("-" * 80)


# Metodo que sirve para crear el directorio db si no existia #

def make_dir():
    if not os.path.exists("./db"):
        os.makedirs("./db")


if __name__ == '__main__':
    make_dir()
    crear_persona("jecastro1", "Jaime Castro")
    crear_persona("bcsaldias", "Belen Saldias")
    crear_persona("kpb", "Karim Pichara")
    set_persona_favorita("jecastro1", "bcsaldias")
    set_persona_favorita("bcsaldias", "kpb")
    set_persona_favorita("kpb", "kpb")
    agregar_amigo("kpb", "jecastro1")
    agregar_amigo("kpb", "bcsaldias")
    agregar_amigo("jecastro1", "bcsaldias")

    jecastro1 = get_persona("jecastro1")
    bcsaldias = get_persona("bcsaldias")
    kpb = get_persona("kpb")
    """
    print_data(jecastro1)
    print_data(bcsaldias)
    print_data(kpb)
    """
    print(existe_persona(""))
    print(get_persona_mas_favorita())
