import lib
from cursos import dicc_cursos
"""
Clases Persona, Alumno, Profesor.
"""
class Persona:
    def __init__(self,nombre,clave,usuario,idolos,**kwargs):
        self.nombre = nombre
        self.user = usuario
        self.password = clave
        self.isProfessor = False
        self.idolos = list(idolos)

class Alumno(Persona):
    def __init__(self,ramos_pre,**kwargs):
        super().__init__(**kwargs)
        self.cursosxtomar = []
        self.aprobados = ramos_pre
        self.seguidores = []
        self.cantidad_seguidores = 0
        self.puntosextra = 0
        self.bacanosidad = 0

        ####### Cosas Banner #######
        self.grupo = 0
        self.hora_de_banner = ('0','0')
        self.maxcreditos = 0
        self.creditosdisp = 0
        ############################
                        #0  1  2  3  4  5
        self.horario =[[[],[],[],[],[],[]],
                       [[],[],[],[],[],[]],
                       [[],[],[],[],[],[]],
                       [[],[],[],[],[],[]],
                       [[],[],[],[],[],[]],
                       [[],[],[],[],[],[]]]

        self.ramosPacmatico = []

        self.opciones = {'1': self.tomar_ramo, '2': self.botar_ramo, '3': self.imprimir_horario,
                        '4': False, '5': False}

    def tomar_ramo(self):
        print('Creditos disponibles: {}'.format(self.creditosdisp))
        nrc = input('Ingrese NRC: ').strip()
        for key in dicc_cursos:
            if dicc_cursos[key].nrc == int(nrc):
                ramo = dicc_cursos[key]
                if self.verificar_tope(ramo) and self.cumple_requisitos(ramo) and self.creditosdisp >= ramo.creditos:
                    self.cursosxtomar.append(ramo)
                    self.horario = lib.agregar_horario(self.horario,ramo)
                    self.creditosdisp -= dicc_cursos[key].creditos
                    print('Curso {} tomado.'.format(ramo.sigla+'-'+str(ramo.seccion)))
                    return
                else:
                    print('No puedes tomar el curso')
                    return
        print('No se ha encontrado el NRC')

    def botar_ramo(self):
        nrc = int(input('Ingrese nrc del ramo: '))
        if nrc in dicc_cursos and dicc_cursos[nrc] in self.cursosxtomar:
            for i in range(len(self.horario)):
                for j in range(len(self.horario)):
                    if dicc_cursos[nrc].nombre + '-' + str(dicc_cursos[nrc].seccion) in self.horario[i][j] or \
                    dicc_cursos[nrc].nombre + '-' + str(dicc_cursos[nrc].seccion) + 'a' in self.horario[i][j] or \
                    dicc_cursos[nrc].nombre + '-' + str(dicc_cursos[nrc].seccion) + 'L' in self.horario[i][j]:
                        try:
                            self.horario[i][j].pop(self.horario[i][j].index(dicc_cursos[nrc].nombre+'-'+str(dicc_cursos[nrc].seccion)))
                        except:
                            try:
                                self.horario[i][j].pop(self.horario[i][j].index(dicc_cursos[nrc].nombre+'-'+str(dicc_cursos[nrc].seccion)+'a'))
                            except:
                                self.horario[i][j].pop(self.horario[i][j].index(dicc_cursos[nrc].nombre+'-'+str(dicc_cursos[nrc].seccion)+'L'))
            dicc_cursos[nrc].disp += 1
            self.creditosdisp += dicc_cursos[nrc].creditos
        else:
            print('Curso no tomado o nrc no encontrado')


    def imprimir_horario(self):
        print('   L   M   W   J   V   S ')
        for i in range(len(self.horario)):
            print('Modulo {} {}'.format(i+1,self.horario[i]))

    def verificar_tope(self,ramo):
        return lib.verificar_tope(self.horario,ramo)

    def cumple_requisitos(self,ramo):
        if ramo.disp > 0:
            return True
        return False

    def displayMenu(self):
        print("""
            BUMMER UC: Mas rapido, mas eficiente, de nivel mundial.
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

    def displayMenu(self):
        print("""
            Bienvenido al sistema de toma de ramos Bummer
                        ¿Que desea hacer?
                        1: Botar ramos ( a algun alumno :( )
                        2: Buscar cursos
                        3: Salir
            """)