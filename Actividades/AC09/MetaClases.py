import random as ran


class MetaRobot(type):

    def check_creator(self):
        if self.creador in self.creadores:
            print('El creador se encuentra en la lista de programadores.')
        else:
            print('El creador no se encuentra en la lista de programadores')

    def cortar_conexion(self):
        if self.actual.hacker:
            self.actual.hacker = 0
            print(
                'Se ha detectado un hacker... que ya ha sido desconectado, ja!')

    def cambiar_nodo(self, hacker):
        print('Usuario en puerto {}'.format(hacker.ide))
        hacker.ide = ran.randint(0, 9)
        print('Cambiado a puerto {}'.format(hacker.ide))

    def __new__(meta, nombre, base_clases, diccionario):
        # Atributos
        diccionario['creador'] = 'felipehv'
        diccionario['ip_inicio'] = "190.102.62.283"
        # Funciones
        diccionario['check_creator'] = MetaRobot.check_creator
        diccionario['cortar_conexion'] = MetaRobot.cortar_conexion
        diccionario['cambiar_nodo'] = MetaRobot.cambiar_nodo
        return super().__new__(meta, nombre, base_clases, diccionario)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)
