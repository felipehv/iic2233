"""
#Segunda parte
class Simulacion:

    def __init__(self,env,grilla):
        app = QtGui.QApplication([])

        # Inicializamos la ventana propiamente tal, aún sin mostrarla. Le pasamos
        # una referencia al objeto instanciado más arriba para poder actualizar
        # la interfaz en cada cambio realizado.
        self.grilla_simulacion = GrillaSimulacion(app, 30)
        self.env = simpy.Environment() 
        self.grila = 
        self.masterGrid = [[ [] for i in range(20)] for i in range(20)]
"""