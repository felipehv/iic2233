import lib
import main
from main import lista_personas

def login(usuario,contrasena):
	for i in range(len(lista_personas)):
		if lista_personas[i].user == usuario:
			if lista_personas[i].password == contrasena:
				return True,i
			else:
				print('Contrasena incorrecta try again')
				return False,''
		else:
			print('Usuario no encontrado')
			return False,''
			
class Banner:
    def __init__(self):
        self.opciones = {
                        "1": login,
                        "2": self.buscacursos,
                        "3": self.exit
                        }

    def displayMenu(self):
        print("""
        	Bienvenido al sistema de toma de ramos Bummer
        				¿Que desea hacer?
                		1: Iniciar Sesion
                		2: Buscar cursos
                		3: Salir
            """)

    def buscacursos(self):
    	pass

    def exit():
    	pass

if __name__ == '__main__':
	banner = Banner()
	while True:
		banner.displayMenu()
		opcion = input()


	print('Gracias por entrar a banner, adios.')
