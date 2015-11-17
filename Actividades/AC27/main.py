# coding=utf-8
# Probado en Windows
import requests,getpass
from requests.auth import HTTPBasicAuth


# Debe tener los atributos:
# * _id (string)
# * name (string)
# * votes (diccionario string: int)
class Table:
    def __init__(self, _id, name, votes):
        self._id = _id
        self.name = name
        self.votes = votes

mesas = []
if __name__ == '__main__':
    movimientos = dict()
    user = getpass.getpass(prompt='Ingrese el usuario: ', stream=None)
    password = getpass.getpass(prompt='Ingrese la contrasena: ', stream=None)
    movs = requests.get('http://votaciometro.cloudapp.net/api/v1/lists', auth=HTTPBasicAuth(user, password))
    if movs.status_code == 200:
        movs = movs.json()
        for mov in movs:
            movimientos[mov] = 0

    tables = requests.get('http://votaciometro.cloudapp.net/api/v1/tables', auth=HTTPBasicAuth(user, password))
    if tables.status_code == 200:
        tables = tables.json()
        for tabla in tables:
            _id = tabla["_id"]
            tables2 = requests.get('http://votaciometro.cloudapp.net/api/v1/tables/{}'.format(_id),
            auth=HTTPBasicAuth(user, password))
            if tables2.status_code == 200:
                j = tables2.json()
                mesa = Table(**j)
                for mov in mesa.votes:
                    movimientos[mov] += mesa.votes[mov]

    print(movimientos)
