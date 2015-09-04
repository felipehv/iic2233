import lib
"""
Clases Curso y Evaluacion.
Las instancias de Curso se guardan en un diccionario con el key NRC de cada curso
En el caso de las evaluaciones se guardan con key = Sigla del curso + '-' + seccion
"""


class Evaluacion:

    def __init__(self, sigla, tipo, sec, fecha):
        self.sigla = sigla
        self.tipo = tipo
        self.sec = sec
        self.fechastr = fecha  # Es la fecha que se pondra en el archivo
        self.fecha = fecha.split(' - ')
        self.fecha[0] = self.fecha[0].split('/')
        self.dia = int(self.fecha[0][0])
        self.mes = int(self.fecha[0][1])
        self.diames = (self.dia, self.mes)
        self.hora = self.fecha[1]


class Curso:

    requisitos = lib.parse('txt/requisitos.txt')
    req_dic = dict()
    for req in requisitos:
        req_dic[req['sigla']] = (req['equiv'], req['prerreq'])

    def __init__(self, sigla, curso, retiro, cred, sec, ofr, campus,
                 NRC, apr, profesor, hora_cat='', sala_cat='', hora_lab='',
                 sala_lab='', hora_ayud='', sala_ayud='', **kwargs):
        self.sigla = sigla
        self.nombre = curso
        self.apr = apr
        self.retiro = retiro
        self.creditos = cred
        self.seccion = sec
        self.campus = campus
        self.nrc = NRC
        self.ofrecidos = ofr
        self.disp = ofr
        self.equivalencia = Curso.req_dic[self.sigla][0]

        self.profesor = profesor

        ################ HORARIOS #####################
        self.horacat = hora_cat
        self.salacat = sala_cat

        self.horalab = hora_lab
        self.salalab = sala_lab

        self.horaayud = hora_ayud
        self.salaayud = sala_ayud
        ###############################################

        ########## PARA COMPROBAR REQUISITOS ##########
        self.requisitos = Curso.req_dic[self.sigla][1]
        self.fechaspruebas = []
        ##############################################

        ########### PACMATICO STUFFS #################
        self.lista_alumnos = []
        self.lista_sinreqs = []
        ##############################################

# Instanciando evaluaciones
lista_evaluaciones = lib.parse('txt/evaluaciones.txt')
dicc_evaluaciones = dict()
for i in range(len(lista_evaluaciones)):
    sec = lista_evaluaciones[i]['sec']
    dicc_evaluaciones[lista_evaluaciones[i][
        'sigla'] + '-' + str(sec) + lista_evaluaciones[i]['tipo']] = Evaluacion(**lista_evaluaciones[i])
print('Instancia de evaluaciones completa')
lista_evaluaciones = None


lista_cursos = lib.parse('txt/cursos.txt')
# Instanciando cursos
contador = 0
dicc_cursos = dict()
for i in range(len(lista_cursos)):
    dicc_cursos[lista_cursos[i]['NRC']] = Curso(**lista_cursos[i])
    ramo = dicc_cursos[lista_cursos[i]['NRC']]
    for key in dicc_evaluaciones:
        if dicc_evaluaciones[key].sigla == ramo.sigla and dicc_evaluaciones[key].sec == ramo.seccion:
            contador += 1
            ramo.fechaspruebas.append(dicc_evaluaciones[key])
print('Instancia de cursos completa', contador)
lista_cursos = None
