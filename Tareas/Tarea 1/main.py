import lib


alumnos = []
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

    def botar_ramo(self,ramo):
        for i in range(len(self.horario)):
            for j in range(len(self.horario)):
                if ramo.nombre in self.horario[i][j] or ramo.nombre + 'a' in self.horario[i][j]:
                    try:
                        self.horario[i][j].pop(self.horario[i][j].index(ramo.nombre))
                    except:
                        self.horario[i][j].pop(self.horario[i][j].index(ramo.nombre+'a'))


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


class Curso:
    
    requisitos = lib.parse('txt/requisitos.txt')
    req_dic = dict()
    for req in requisitos:
        req_dic[req['sigla']] = (req['equiv'],req['prerreq'])

    def __init__(self,sigla,curso,retiro,cred,sec,ofr,campus,
        NRC,apr,eng,hora_cat='',sala_cat='',hora_lab='',
        sala_lab='',hora_ayud='',sala_ayud='',**kwargs):
        self.sigla = sigla
        self.nombre = curso
        self.eng = eng #Requisito ingles
        self.apr = apr
        self.retiro = retiro
        self.creditos = cred
        self.seccion = sec
        self.campus = campus
        self.nrc = NRC
        self.ofrecidos = ofr
        self.disp = ofr
        self.equivalencia = Curso.req_dic[self.sigla][0]

        self.horacat = hora_cat
        self.salacat = sala_cat

        self.horalab = hora_lab
        self.salalab = sala_lab

        self.horaayud = hora_ayud
        self.salaayud = sala_ayud

        self.requisitos = Curso.req_dic[self.sigla][1]


#Hago el parse a partir de los txt
lista_personas = lib.parse('txt/personas.txt')
lista_cursos = lib.parse('txt/cursos.txt')
print('Parse completado')

#Instanciando personas
dicc_personas = dict()
for i in range(len(lista_personas)):
    if lista_personas[i]['alumno'] == 'SI':
        dicc_personas[lista_personas[i]['nombre']] = Alumno(**lista_personas[i])
    else:
        dicc_personas[lista_personas[i]['nombre']] = Profesor(**lista_personas[i])
lista_personas = []
print('Instancia de personas completa')

#Instanciando cursos
dicc_cursos = dict()
for i in range(len(lista_cursos)):
    dicc_cursos[lista_cursos[i]['sigla']] = Curso(**lista_cursos[i])
print('Instancia de cursos completa')


#Numero de seguidores
for alumno in dicc_personas:
    if not dicc_personas[alumno].isProfessor:
        for idolo in dicc_personas[alumno].idolos:
            dicc_personas[idolo].seguidores.append(idolo)
            dicc_personas[idolo].cantidad_seguidores += 1

print('Seguidores completa')

#Ordenando por bacanosidad
#sorted(ut, key=lambda x: x.cantidadIdolos, reverse=True)

if __name__ == '__main__':
    pass
