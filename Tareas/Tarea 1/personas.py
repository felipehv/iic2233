import lib
class Persona:
    def __init__(self,nombre,clave,usuario,**kwargs):
        self.nombre = nombre
        self.user = usuario
        self.password = clave
        self.isProfessor = False

class Alumno(Persona):
    def __init__(self,ramos_pre,idolos,**kwargs):
        super().__init__(**kwargs)
        self.cursosxtomar = []
        self.aprobados = ramos_pre
        self.idolos = list(idolos)
        self.seguidores = []
        self.cantidad_seguidores = 0
                        #0  1  2  3  4  5
        self.horario =[[[],[],[],[],[],[]],
                       [[],[],[],[],[],[]],
                       [[],[],[],[],[],[]],
                       [[],[],[],[],[],[]],
                       [[],[],[],[],[],[]],
                       [[],[],[],[],[],[]]]

        self.opciones =  0

    def tomar_ramo(self):
        ramo = input('Ingrese sigla: ').strip()
        if self.verificar_tope(ramo) and self.cumple_requisitos(ramo):
            self.cursosxtomar.append(ramo)
            self.horario = lib.agregar_horario(self.horario,ramo)

    def botar_ramo(self):
        sigla = input('Ingrese sigla del ramo: ')
        for i in range(len(self.horario)):
            for j in range(len(self.horario)):
                if dicc_cursos[sigla].nombre in self.horario[i][j] or dicc_cursos[sigla].nombre + 'a' in self.horario[i][j]:
                    try:
                        self.horario[i][j].pop(self.horario[i][j].index(ramo.nombre))
                    except:
                        self.horario[i][j].pop(self.horario[i][j].index(ramo.nombre+'a'))
        if sigla in dicc_cursos:
            dicc_cursos[sigla].disp += 1


    def imprimir_horario(self):
        print('   L  M  W  J  V  S ')
        for i in range(len(self.horario)):
            print('Modulo {} {}'.format(i+1,self.horario[i]))

    def verificar_tope(self,ramo):
        lib.verificar_tope(self.horario,ramo)
        return True #Para probar

    def displayMenu(self):
        print("""
            Bienvenido al sistema de toma de ramos Bummer
                        ¿Que desea hacer?
                        1: Tomar ramos
                        2: Botar ramos
                        3: Imprimir horario
                        4: Buscar cursos
                        5: Salir
            """)


class Profesor(Persona):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.isProfessor = True