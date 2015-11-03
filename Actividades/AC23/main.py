#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from pickle import loads, dumps, load, dump
from datetime import datetime


class Persona:
    
    def __init__(self,ide,nombre):
        self.id = ide
        self.nombre = nombre
        self.amigos = []
        self.favorito = ''
        self.ultima_fecha = None
        self.veces_guardado = 0

    def agregar_amigo(self,amigo):
        self.amigos.append(amigo)

    def __getstate__(self):
        diccionario = self.__dict__.copy()
        diccionario.update({"ultima_fecha": datetime.now(), "veces_guardado": self.veces_guardado + 1})
        diccionario.update()
        return diccionario

    def __str__(self):
        return self.id + " " + self.nombre

    def __repr__(self):
        return self.__str__()

def existe_persona(_id):
    lista = os.listdir("./db")
    for name in lista:
        if _id == name.replace(".iic2233","") and ".iic2233" in name:
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
        persona1 = get_persona(id_1)
        persona2 = get_persona(id_2)
        persona1.agregar_amigo(id_2)
        persona2.agregar_amigo(id_1)
        write_persona(persona1)
        write_persona(persona2)


def set_persona_favorita(_id, id_favorito):
    if existe_persona(_id) and existe_persona(id_favorito):
        persona = get_persona(_id)
        persona.favorito = id_favorito
        write_persona(persona)

def get_persona_mas_favorita():
    dict_personas = {}
    lista = os.listdir("./db")
    for archivo in lista:
        with open("./db/{}".format(archivo),"rb") as reader:
            persona = load(reader)
            print(persona,persona.favorito)
            if persona.favorito not in dict_personas:
                dict_personas[persona.favorito] = 1
            else:
                dict_personas[persona.favorito] += 1
    mas_favorito = '',0
    for key in dict_personas:
        if dict_personas[key] > mas_favorito[1]:
            mas_favorito = key,dict_personas[key]

    return get_persona(mas_favorito[0])

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

    print_data(jecastro1)
    print_data(bcsaldias)
    print_data(kpb)

    print(get_persona_mas_favorita())
