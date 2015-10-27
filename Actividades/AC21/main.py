__author__ = 'ivania'

import json
from collections import defaultdict
start_hour = '23:30'


class Tweet():

    def __init__(self, nombre, fecha, mensaje):
        self.nombre = nombre
        fecha = fecha.strip().split(' ')[3]
        fecha = fecha.split(':')
        self.hour = fecha[0]
        self.min = fecha[1]
        self.hora = fecha[0], fecha[1]
        self.mensaje = mensaje

    @property
    def obtener_palabras(self):
        palabras = self.mensaje.strip('"').split(' ')
        return palabras

##########################################################################


def read_tweet(tweet, words_frequency, players_frequency, players_names):
    # Implementar
    words_frequency = dict()
    players_frequency = dict()
    for palabra in tweet.obtener_palabras:
        if palabra not in words_frequency:
            words_frequency[palabra] = 0
        else:
            words_frequency[palabra] += 1
        for player in player_names:
            if palabra in players[player]:
                if player not in players_frequency:
                    players_frequency[player] = 0
                else:
                    player_frequency[player] += 1
    # Buscar palabras frecuentes
    # Revisar si las palabras corresponden a un jugador
    return words_frequency, players_frequency


def read_tweets_window(start, end, tweets, players_names):
    # Implementar
    # Revisar las palabras para cada tweet si está en la ventana de tiempo
    words_frequency = {}
    players_frequency = {}
    for tweet in tweets:
        if is_in_time_window(tweet.hour, start, end):
            words_frequency, players_frequency = read_tweet(tweet, words_frequency, players_frequency, players_name)
    # Filtrar palabras infrecuentes
        #   
    return words_frequency, players_frequency


def is_in_time_window(hour, start, end):
    # Implementar
    if hour[0] == start[0] or hour[1] == start[1]:
        return hour[1] <= end[1] or hour[1] >= start[1]


def transform_event_time(minute):
    hour_s, min_s = start_hour.split(':')
    min_s = int(min_s)
    hour_s = int(hour_s)
    if min_s + minute > 59:
        if hour_s + (min_s + minute) / 60 > 23:
            hour_s = int((min_s + minute) / 60 - 1)
        min_s = (min_s + minute) % 60
    else:
        min_s += minute

    return hour_s, min_s


def frequent_words(tweets, events, players_words):
    event_statistics = {}

    for event in events:
        event_hour = transform_event_time(event[0])
        start = (event_hour[0], event_hour[1] - 3)
        end = (event_hour[0], event_hour[1] + 5)
        word_frequency, players_frequency = read_tweets_window(
            start, end, tweets, player_words)
        # Implementar
        # Obtener frecuencias de las palabras de la ventana del evento

        # Cada uno de estos archivos lo pueden utilizar en wordcloud
        with open('Evento{}.txt'.format(minute), 'w+') as file_words:
            for word, frequency in words_frequency.items():
                file_words.write('{}\t{}\n'.format(frequency, word))

    return event_statistics


def load_names_players(players):
    players_names = {}
    for player in players:
        if player['Nombre'] not in players_names:
            players_names[player['nombre']] = player[
                'Twitter'] + player['Apodos']
    # Implementar
    # Crear diccionario para guardar las palabras asociadas a cada uno de los
    # jugadores

    return players_names


if __name__ == "__main__":
    string_players = ''
    with open("players.json") as reader:
        for linea in reader:
            linea = linea.strip()
            string_players += linea
    players = json.loads(string_players)

    tweets = []
    with open("tweets.csv", encoding="utf-8") as reader:
        for linea in reader:
            if linea in ("", "\n"):
                continue
            linea = linea.strip().split(',')
            if len(linea) > 1:
                tweets.append(Tweet(linea[0],linea[1],linea[2]))

    events = []
    with open("events.csv", encoding="utf-8") as reader:
        for linea in reader:
            if linea in ("", "\n"):
                continue
            linea = linea.strip().split(',')
            events.append(linea)

    players_words = load_names_players(players)
    events_statistics = frequent_words(tweets, events, players_words)
