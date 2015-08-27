import lib
import main
from main import dicc_personas, dicc_cursos

def login(usuario, contrasena):
    for key in dicc_pesrsonas:
        if lista_personas[i].user == usuario:
            if lista_personas[i].password == contrasena:
                return True, i
            else:
                print('Contrasena incorrecta try again')
                return False, ''
        else:
            print('Usuario no encontrado')
            return False, ''


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
        try:
            for key in dicc_cursos:
                if sigla in key:
                    cursosxmostrar.append(dicc_cursos[key])
            for curso in cursosxmostrar:
                print('Nombre: {}, Sigla: {}, Cupos disponibles/totales: {}/{}'.format(curso.nombre,curso.sigla,curso.disp))
        except:
            print('Curso no encontrado')

    def exit():
        break

if __name__ == '__main__':
    banner = Banner()
    while True:
        hora = input('¿Que hora es? (HHMM)').strip()
        banner.displayMenu()
        opcion = input().strip()
        if self.opciones[opcion]:
            self.opciones[opcion]()
        else:
            break

    print('Gracias por entrar a banner, adios.')
