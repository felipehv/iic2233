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

movimientos = {"Solidaridad": 0 , "Nau!": 0, "1A":0, "Crecer": 0}
mesas = []
if __name__ == '__main__':
    user = getpass.getpass(prompt='Ingrese el usuario: ', stream=None)
    password = getpass.getpass(prompt='Ingrese la contrasena: ', stream=None)
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
