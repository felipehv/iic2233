import lib
import main
from main import lista_personas,lista_cursos

def SignIn(usuario,contrasena):
	for i in range(len(lista_personas)):
		if lista_personas[i].user == user:
			if lista_personas[i].contrasena == contrasena:
				return True,i
			else:
				return False,'Contrasena incorrecta'
		else:
			return False,'Usuario no existe'
			
class Banner:
    def __init__(self):
        self.opciones = {
                        "1": print('Bien'),
                        "2": print('Bien'),
                        "3": print('Bien'),
                        "4": print('Bien'),
                        "5": print('Bien')
                        }

    def display_menu_alumno(self):
        print("""
            Menu:
                1: Buscar cursos
                2: Tomar curso
                3: Eliminar curso
                4: Modificar Post-It existente
                5: Salir
            """)

    def buscar_ramos(self):
    	pass




if __name__ == '__main__':
	banner = Banner()
	while True:
		print('Bienvenido al sistema banner')
		usuario = input('Ingrese su usuario, exit para salir')
		if usuario == 'exit':
			break
		contrasena = input('Ingrese contrasena')
		if SignIn(usuario,contrasena)[0]:
			while True:
				user_id = SignIn(usuario,contrasena)[0]
				print('Bienvenido {}'.format(lista_personas[user_id]))
				banner.display_menu()



	print('Gracias por entrar a banner, adios.')
