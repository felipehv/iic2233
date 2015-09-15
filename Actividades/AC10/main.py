"""
Parte1
"""
class RestrictedAccess(type):
	def __new__(meta, nombre, base_clases, diccionario):

		def init(self,*args,diccionario = diccionario):
			for i in range(len(diccionario['attributes'])):
				setattr(self,'__{}'.format(diccionario['attributes'][i].strip()),args[i])
			diccionario.pop("attributes", None)

		diccionario['__init__'] = init

		return super().__new__(meta, nombre, base_clases, diccionario)

	def __call__(cls, *args, **kwargs):
	    return super().__call__(*args)

 
class Person ( metaclass = RestrictedAccess ):
	attributes = [ " name " , " lastname " , " alias " ]


a = Person('hola','chao','hola')
print(a.__name)





"""
Parte2
"""

class Singleton(type):
	classes = dict()
	def __new__(meta, nombre, base_clases, diccionario):
		return super().__new__(meta, nombre, base_clases, diccionario)

	def __call__(cls, *args, **kwargs):
		if not cls in Singleton.classes:
			Singleton.classes[cls] = super().__call__(*args, **kwargs)
		elif cls in Singleton.classes:
			return Singleton.classes[cls]
		return Singleton.classes[cls]

class Person(metaclass = Singleton):
	def __init__(self,nombre):
		self.nombre = nombre

a = Person('hola')
b = Person('chao')

print(a)
print(b)
"""


class Person ( metaclass = RestrictedAccess ):
attributes = [ " name " , " lastname " , " alias " ]
p = Person ( " Bruce " , " Wayne " , " Batman " )
print ( p . name , p . lastname , " es " , p . alias , " ! " ))
# # Bruce Wayne es Batman !
p . alias = " Robin "
# # AttributeError : cant set attribute

"""