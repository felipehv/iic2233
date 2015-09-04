import lib
from cursos import dicc_cursos
"""
Clases Persona, Alumno, Profesor.
"""


class Persona:

    def __init__(self, nombre, clave, usuario, idolos, **kwargs):
        self.nombre = nombre
        self.user = usuario
        self.password = clave
        self.isProfessor = False
        self.idolos = list(idolos)


class Alumno(Persona):

    def __init__(self, ramos_pre, **kwargs):
        super().__init__(**kwargs)
        self.cursosxtomar = []
        self.aprobados = ramos_pre
        self.seguidores = []
        self.cantidad_seguidores = 0
        self.puntosextra = 0
        self.bacanosidad = 0
        self.creditos_aprobados = 0

        self.puntosrecibidos = 0

        # Sumo los creditos de lo ramos a los cretidos aprobados
        for ramo in self.aprobados:
            for key in dicc_cursos:
                if dicc_cursos[key].sigla == ramo:
                    self.creditos_aprobados += dicc_cursos[key].creditos

        ####### Cosas Banner #######
        self.grupo = 0
        self.hora_de_banner = ('0', '0')
        self.maxcreditos = 0
        self.creditosdisp = 0
        ############################
        # 0  1  2  3  4  5
        self.horario = [[[], [], [], [], [], []],
                        [[], [], [], [], [], []],
                        [[], [], [], [], [], []],
                        [[], [], [], [], [], []],
                        [[], [], [], [], [], []],
                        [[], [], [], [], [], []]]

        ####### Cosas PUCMATICO ######
        self.cursospacmatico = []
        self.redistribucion = 0
        self.puntos_pacmatico = 0
        self.creditos_redistribucion = 0
        ##############################

        self.opciones = {'1': self.tomar_ramo, '2': self.botar_ramo, '3': self.imprimir_horario,
                         '4': self.imprimir_calendario}

        self.opcionesp = {'1': self.tomarenPucmatico,
                          '2': self.repartirpuntos, '3': self.mostrar_cursos}

    def tomar_ramo(self):
        print('Creditos disponibles: {}'.format(self.creditosdisp))
        nrc = input('Ingrese NRC: ').strip()
        for key in dicc_cursos:
            if dicc_cursos[key].nrc == int(nrc):
                ramo = dicc_cursos[key]
                if self.verificar_tope(ramo) and self.cumple_requisitos(ramo) and \
                        self.creditosdisp >= ramo.creditos and self.topa_prueba(ramo):
                    self.cursosxtomar.append(ramo)
                    self.horario = lib.agregar_horario(self.horario, ramo)
                    self.creditosdisp -= dicc_cursos[key].creditos
                    ramo.lista_alumnos.append(self)
                    print(
                        'Curso {} tomado.'.format(ramo.sigla + '-' + str(ramo.seccion)))
                    return
                else:
                    print(
                        'No puedes tomar el curso, veamos que dice el profe...')
                    ramo.lista_sinreqs.append(self)
                    return
        print('No se ha encontrado el NRC')

    def botar_ramo(self, nrc=None):
        if not ramo:
            nrc = int(input('Ingrese nrc del ramo: '))
        else:
            nrc = nrc
        if nrc in dicc_cursos and dicc_cursos[nrc] in self.cursosxtomar:
            for i in range(len(self.horario)):
                for j in range(len(self.horario)):
                    if dicc_cursos[nrc].nombre + '-' + str(dicc_cursos[nrc].seccion) in self.horario[i][j] or \
                            dicc_cursos[nrc].nombre + '-' + str(dicc_cursos[nrc].seccion) + 'a' in self.horario[i][j] or \
                            dicc_cursos[nrc].nombre + '-' + str(dicc_cursos[nrc].seccion) + 'L' in self.horario[i][j]:
                        try:
                            self.horario[i][j].pop(self.horario[i][j].index(
                                dicc_cursos[nrc].nombre + '-' + str(dicc_cursos[nrc].seccion)))
                        except:
                            try:
                                self.horario[i][j].pop(self.horario[i][j].index(
                                    dicc_cursos[nrc].nombre + '-' + str(dicc_cursos[nrc].seccion) + 'a'))
                            except:
                                self.horario[i][j].pop(self.horario[i][j].index(
                                    dicc_cursos[nrc].nombre + '-' + str(dicc_cursos[nrc].seccion) + 'L'))
            dicc_cursos[nrc].disp += 1
            self.creditosdisp += dicc_cursos[nrc].creditos
            dicc_cursos[nrc].lista_alumnos.pop(
                dicc_cursos[nrc].lista_alumnos.index(self))
        else:
            print('Curso no tomado o nrc no encontrado')

    ############ PACMATICO STUFFS###############
    def tomarenPucmatico(self):
        print('Creditos disponibles: {}'.format(self.creditosdisp))
        nrc = input('Ingrese NRC: ').strip()
        for key in dicc_cursos:
            if dicc_cursos[key].nrc == int(nrc) and dicc_cursos[key] not in self.cursospacmatico:
                ramo = dicc_cursos[key]
                self.cursospacmatico.append([ramo, self.puntos_pacmatico])
                self.creditosdisp -= dicc_cursos[key].creditos

    def repartirpuntos(self):
        if self.creditos_redistribucion < 45:
            print('Elija un curso por nrc')
            for curso in self.cursospacmatico:
                print(curso[0].nombre, curso[0].nrc, curso[1])
            nrc = input('Ingrese NRC: ').strip()
            ramo = None
            for i in range(len(self.cursospacmatico)):
                if self.cursospacmatico[i][0].nrc == int(nrc):
                    ramo = i
            puntos = int(input('¿Cuantos puntos desea sumar?: '))
            if ramo or ramo == 0:
                if puntos + self.redistribucion <= 1000 and puntos > 0 and len(self.cursospacmatico) > 1:
                    print('sfbsdfj')
                    self.cursospacmatico[ramo][1] += puntos
                    self.redistribucion += puntos
                    for i in range(len(self.cursospacmatico)):
                        if i != ramo:
                            self.cursospacmatico[i][
                                1] -= puntos / (len(self.cursospacmatico) - 1)
                else:
                    print('No puede sumar puntos en este momento')
            else:
                print('NRC invalido')

    def mostrar_cursos(self):
        for curso in self.cursospacmatico:
            print('Nombre: {}, Seccion: {}, Puntaje: {}'.format(
                curso[0].nombre, curso[0].seccion, curso[1]))
    #############################################

    def imprimir_horario(self):
        print('   L   M   W   J   V   S ')
        for i in range(len(self.horario)):
            print('Modulo {} {}'.format(i + 1, self.horario[i]))

    def imprimir_calendario(self):
        pruebas = []
        with open('calendario.txt', 'w') as writer:
            for curso in self.cursosxtomar:
                for evaluacion in curso.fechaspruebas:
                    pruebas.append(evaluacion)
            print(pruebas)
            pruebasordenadas = []
            while pruebas != []:
                # last es la ultima prueba que se ha encontrado menor
                last = pruebas[0]
                for i in range(len(pruebas)):
                    if pruebas[i].mes <= last.mes:
                        if pruebas[i].dia < last.dia:
                            last = pruebas[i]
                pruebasordenadas.append(pruebas.pop(pruebas.index(last)))
            for prueba in pruebasordenadas:
                writer.write(
                    '{} : {} {}-{}\n'.format(prueba.fechastr, prueba.tipo, prueba.sigla, prueba.sec))
        print('Calendario exportado a "calendario.txt"')

    def verificar_tope(self, ramo):
        return lib.verificar_tope(self.horario, ramo)

    def cumple_requisitos(self, ramo):
        if ramo.disp > 0:
            return True
        return False

    def topa_prueba(self, ramo):
        for evaluacion in ramo.fechaspruebas:
            for curso in self.cursosxtomar:
                for prueba in curso.fechaspruebas:
                    if evaluacion.fecha == prueba.fecha:
                        print('Tope de pruebas')
                        return False
        return True

    def displayMenu(self):
        print("""
            BUMMER UC: Mas rapido, mas eficiente, de nivel mundial.
                        ¿Que desea hacer?
                        1: Tomar ramos
                        2: Botar ramos
                        3: Imprimir horario
                        4: Imprimir Calendario
                        5: Salir
            """)

    def displayMenuP(self):
        print("""
            PACMATICO UC: El unico reemplazo que es mejor que lo que reemplaza.
                        ¿Que desea hacer?
                        1: Tomar ramos
                        2: Redistribuir puntaje
                        3: Mostrar ramos
            """)


class Profesor(Persona):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.isProfessor = True
        self.opciones = {'1': self.botar_ramo}
        self.opcionesp = {}
        self.nombreinvertido = self.nombre.split(' ')
        self.nombreinvertido = self.nombreinvertido[
            1] + ' ' + self.nombreinvertido[0]

    def displayMenu(self):
        print("""
            Bienvenido al sistema de toma de ramos Bummer
                        ¿Que desea hacer?
                        0: Salir
            """)

    def botar_ramo(self):
        cursosdelprofe = dict()
        for key in dicc_cursos:
            if self.nombreinvertido in dicc_cursos[key].profesor:
                cursosdelprofe[key] = dicc_cursos[key]
        print('Sus cursos (nombre y nrc)')
        for key in cursosdelprofe:
            print(cursosdelprofe[key].nombre, cursosdelprofe[key].nrc)
        nrc = int(input('Indique el nrc del curso').strip())
        alumnos_del_curso = dict()
        if nrc in cursosdelprofe:
            print('Lista de alumnos (nombre)')
            for alumno in cursosdelprofe[nrc].lista_alumnos:
                print(alumno.nombre)
                alumnos_del_curso[alumno.nombre] = alumno
        else:
            return
        nombre = input(
            'Escriba el nombre de quien quiera dar botar el ramo').strip()
        if nombre in alumnos_del_curso:
            alumnos_del_curso[alumno].botar_ramo(nrc=nrc)

    def aceptar_sinreqs(self):
        cursosdelprofe = dict()
        for key in dicc_cursos:
            if self.nombreinvertido in dicc_cursos[key].profesor:
                cursosdelprofe[key] = dicc_cursos[key]
        print('Sus cursos (nombre y nrc')
        for key in cursosdelprofe:
            print(cursosdelprofe[key].nombre, cursosdelprofe[key].nrc)
        nrc = int(input('Indique el nrc del curso').strip())
        alumnos_del_curso = dict()
        if nrc in cursosdelprofe:
            print('Lista de alumnos (nombre)')
            for alumno in cursosdelprofe[nrc].lista_sinreqs:
                print(alumno.nombre)
                alumnos_del_curso[alumno.nombre] = alumno
        else:
            return
        nombre = input(
            'Escriba el nombre de quien quiera dar botar el ramo').strip()
        if nombre in alumnos_del_curso:
            alumnos_del_curso[nombre].cursosxtomar.append(cursosdelprofe[nrc])
            alumnos_del_curso[nombre].horario = lib.agregar_horario(
                alumnos_del_curso[nombre].horario, cursosdelprofe[nrc])
            alumnos_del_curso[nombre].creditosdisp -= dicc_cursos[key].creditos
            cursosdelprofe[nrc].lista_alumnos.append(alumnos_del_curso[nombre])
