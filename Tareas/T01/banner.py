import lib
import main
from main import dicc_personas, dicc_cursos

def login():
    usuario = input('Ingrese usuario: ').strip()
    for key in dicc_personas:
        if dicc_personas[key].user == usuario:
            contrasena = input('Ingrese contrasena: ')
            if dicc_personas[key].password == contrasena:
                return key
            else:
                print('Contrasena incorrecta try again')
                return False
    
    print('Usuario no encontrado')
    return False


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
        sigla = input('Ingrese sigla del curso')
        cursosxmostrar = []
        for key in dicc_cursos:
            if sigla in key:
                cursosxmostrar.append(dicc_cursos[key])
        if cursosxmostrar == []:
            print('No encontrado')
            return
        for curso in cursosxmostrar:
            print('Nombre: {}, Sigla: {}, Cupos disponibles/totales: {}/{}'.format(curso.nombre,curso.sigla,curso.disp,curso.ofrecidos))


    def exit(self):
        pass

if __name__ == '__main__':
    banner = Banner()
    while True:
        hora = input('¿Que hora es? (formato: HHMM): ').strip()
        banner.displayMenu()
        opcion = input().strip()
        if banner.opciones[opcion] == login:
            nombre = login()
            if nombre:
                persona = dicc_personas[nombre]
                while True:
                    print('Bienvenido {}'.format(nombre))
                    a = input()
                    break



        elif banner.opciones[opcion]:
            banner.opciones[opcion]()
        else:
            break

    print('Gracias por entrar a Bummer, adios.')
