from pickle import dumps, loads
a = dumps("hola mundo")
b = loads(a[0:10])
