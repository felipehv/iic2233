import lib
import main
from main import dicc_personas
from cursos import dicc_cursos
horario = ('08:30','11:30')
def buscacursos():
        kw = input('Ingrese palabra clave (Sigla o nombre de curso): ').strip().lower()
        cursosxmostrar = []
        for key in dicc_cursos:
            if kw in dicc_cursos[key].sigla.lower() or kw in dicc_cursos[key].nombre.lower():
                cursosxmostrar.append(dicc_cursos[key])
        if cursosxmostrar == []:
            print('No encontrado')
            return
        for curso in cursosxmostrar:
            print('Nombre: {}, Sigla: {}-{}, NRC: {} Cupos disponibles/totales: {}/{}'.format(curso.nombre
                ,curso.sigla,curso.seccion,curso.nrc,curso.disp,curso.ofrecidos))

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
            "2": buscacursos,
            "3": self.exit
        }

    def crearGrupos(self):
        with open('listabacanes.txt','r') as reader:
            for i in range(10):
                for j in range(435):
                    nombre = reader.readline().split('\t')[0]
                    if nombre == '':
                        break
                    dicc_personas[nombre].grupo = i + 1
                    dicc_personas[nombre].hora_de_banner = lib.horarioX(i,horario)
                    dicc_personas[nombre].creditosmax = 55 + (6 - i + 1) * 2
                    dicc_personas[nombre].creditosdisp = dicc_personas[nombre].creditosmax

    def displayMenu(self):
        print("""
            Bienvenido al sistema de toma de ramos Bummer
                        ¿Que desea hacer?
                        1: Iniciar Sesion
                        2: Buscar cursos
                        3: Salir
            """)

    def exit(self):
        pass

if __name__ == '__main__':
    banner = Banner()
    banner.crearGrupos()
    while True:
        hora = input('¿Que hora es? (formato: HHMM): ').strip()
        banner.displayMenu()
        opcion = input().strip()
        if banner.opciones[opcion] == login:
            nombre = login()
            if nombre:
                persona = dicc_personas[nombre]
                while True:
                    print('Bienvenido {}, Grupo {}'.format(nombre,persona.grupo))
                    persona.displayMenu()
                    opcion = input('Ingrese opcion: ')
                    if opcion.isdigit() and 0 < int(opcion) < 6:
                        persona.opciones[opcion]()

        elif banner.opciones[opcion]:
            banner.opciones[opcion]()
        else:
            break

    print('Gracias por entrar a Bummer, adios.')
