class Bummer:

    def __init__(self):
        self.alumnos = {"Vicente Besa": Alumno("vabesa", 12345),
                        "Juan Pablo Schele": Alumno("jpschele", 54321),
                        "Ariel Seisdedos": Alumno("robocop6", 123456789)}

        self.ramos = [Ramo("IIC2133", 10), Ramo("ING2030", 100),
                      Ramo("ICH1104", 100), Ramo("IIC2143", 30),
                      Ramo("IIC2413", 30)]

        self.conectado = False

    def ingresar(self, usuario, clave):
        if not self.conectado:
            try:
                if self.alumnos[usuario].clave == clave:
                    self.usuario_actual = self.alumnos[usuario]
                    self.conectado = True
                    print("se conecto {0}".format(self.usuario_actual.usuario))
            except (KeyError) as err:
                print(
                    'Error de tipo KeyError: El usuario {} no se encuentra en nuestra base de datos'.format(err))

    def inscribir_ramo(self, numero):
        if self.conectado:
            try:
                ramo_inscribir = self.ramos[numero]
                if ramo_inscribir.vacantes > 0:
                    self.usuario_actual.agregar_ramos(ramo_inscribir)
            except (IndexError):
                print('Error de tipo IndexError al tomar ramo: {}, no se ha encontrado el numero de ramo.'.format(
                    self.usuario_actual.usuario))
            except (TypeError):
                print('Error de tipo TypeError al tomar ramo: {}, ingreso un ({}) pero se esperaba un int'.format(
                    self.usuario_actual.usuario, type(numero).__name__))
            else:
                print("Se inscribio el curso de sigla {0} a {1}".format(ramo_inscribir.sigla,
                                                                        self.usuario_actual.usuario))

    def quitar_ramo(self, numero):
        if self.conectado:
            try:
                ramo_quitar = self.ramos[numero]
                self.usuario_actual.quitar_ramos(ramo_quitar.sigla)
            except (IndexError):
                print('{}: Error de tipo IndexError: el numero de ramo no existe'.format(
                    self.usuario_actual.usuario))
            except (KeyError) as err:
                print('{}: Error de tipo KeyError al quitar ramo: Usted no tiene inscrito el ramo {}.'.format(
                    self.usuario_actual.usuario, err))
            except (TypeError):
                print('{}: Error de tipo TypeError al quitar ramo: ingreso un dato ({}) y se esperaba un int'.format(
                    self.usuario_actual.usuario, type(numero).__name__))
            else:
                print("Se quito el curso de sigla {0} de la carga academica de {1}".format(ramo_quitar.sigla,
                                                                                           self.usuario_actual.usuario))

    def calificar(self, numero, nota):
        if self.conectado:
            try:
                ramo = self.ramos[numero]
                self.usuario_actual.calificar_curso(ramo.sigla, nota)
            except (KeyError) as err:
                print('Error de tipo KeyError al calificar, {} no tiene el ramo {} inscrito.'.format(
                    self.usuario_actual.usuario, err))
            except (ValueError) as err:
                print('Error de tipo ValueError al calificar al usuario {}, la nota ingresada no es float.'.format(
                    self.usuario_actual.usuario, err))
            except (IndexError):
                print('Error de tipo IndexError al calificar al usuario {}, el numero no se asocia a ningun ramo.'.format(
                    self.usuario_actual.usuario))

            else:
                print("Se califico a {} en el curso {} con la nota {}".format(self.usuario_actual.usuario, ramo.sigla,
                                                                              nota))

"""

No se puede modificar desde aquí

"""


class Ramo:

    def __init__(self, sigla, vacantes):
        self.sigla = sigla
        self.vacantes = vacantes
        self.alumnos = {}

    def inscrito(self, alumno):
        self.vacantes -= 1
        self.alumnos[alumno.usuario] = alumno


class Alumno:

    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave
        self.ramos = {}
        self.ramos_aprobados = {}

    def agregar_ramos(self, ramo):
        self.ramos[ramo.sigla] = ramo
        ramo.inscrito(self)

    def quitar_ramos(self, sigla):
        del self.ramos[sigla]

    def calificar_curso(self, sigla, nota):
        ramo = self.ramos[sigla]
        nota = float(nota)
        self.ramos_aprobados[sigla] = (ramo, nota)


if __name__ == '__main__':
    bummer = Bummer()
    bummer.ingresar("Marco Bucchi", 12345)
    bummer.ingresar("Juan Pablo Schele", 54321)
    bummer.inscribir_ramo(5)
    bummer.inscribir_ramo(0)
    bummer.inscribir_ramo("IIC2111")
    bummer.inscribir_ramo(2)
    bummer.quitar_ramo(0)
    bummer.quitar_ramo("Investigación")
    bummer.quitar_ramo(4)
    bummer.quitar_ramo(5)
    bummer.calificar(2, "siete")
    bummer.calificar(0, "7.0")
    bummer.calificar(2, "7.0")
    bummer.calificar(5, "1.0")
