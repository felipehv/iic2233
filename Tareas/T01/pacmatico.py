import lib
import main
from main import dicc_personas, maxima
from cursos import dicc_cursos
from banner import login, buscacursos
"""
PACMATICO: Se definen las funciones de banner de nuev porque usan parte
de los modulos y asi no llamamos a banner. 
"""


def buscacursos():
    kw = input(
        'Ingrese palabra clave (Sigla o nombre de curso): ').strip().lower()
    cursosxmostrar = []
    for key in dicc_cursos:
        if kw in dicc_cursos[key].sigla.lower() or kw in dicc_cursos[key].nombre.lower():
            cursosxmostrar.append(dicc_cursos[key])
    if cursosxmostrar == []:
        print('No encontrado')
        return
    for curso in cursosxmostrar:
        print('Nombre: {}, Sigla: {}-{}, NRC: {} Cupos disponibles/totales: {}/{}'.format(
            curso.nombre, curso.sigla, curso.seccion, curso.nrc, curso.disp, curso.ofrecidos))


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


class Pacmatico:

    def __init__(self):
        self.opciones = {
            "1": login,
            "2": buscacursos,
        }

    def calcularpuntos(self):
        for key in dicc_personas:
            if not dicc_personas[key].isProfessor:
                alumno = dicc_personas[key]
                alumno.puntos_pacmatico = (
                    (1 + alumno.bacanosidad / 4 / maxima + alumno.creditos_aprobados / 4000) * 800)

    def displayMenu(self):
        print("""
            PACMATICO UC: El unico reemplazo que es mejor que lo que reemplaza.
                        ¿Que desea hacer?
                        1: Iniciar Sesion
                        2: Buscar cursos
                        0: Salir
            """)


if __name__ == '__main__':
    pacmatico = Pacmatico()
    pacmatico.calcularpuntos()
    while True:
        hora = input('¿Que hora es? (formato= HH:MM): ').strip()
        lib.verificar_hora(hora)
        pacmatico.displayMenu()
        opcion = input().strip()
        if opcion in pacmatico.opciones and pacmatico.opciones[opcion] == login:
            nombre = login()
            if nombre:
                persona = dicc_personas[nombre]
                while True:
                    if not persona.isProfessor:
                        print(
                            'Bienvenido {} // Puntos totales: {}'.format(nombre, persona.puntos_pacmatico))
                    else:
                        print('Bienvenido Profesor {}'.format(nombre))
                    persona.displayMenuP()
                    opcion = input('Ingrese opcion: ')
                    if opcion.isdigit() and opcion in persona.opcionesp:
                        persona.opcionesp[opcion]()
                    elif opcion.isdigit() and int(opcion) == 0:
                        break

        elif opcion in pacmatico.opciones:
            pacmatico.opciones[opcion]()
        else:
            break
