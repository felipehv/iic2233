import threading
import datetime


class Worker(threading.Thread):
    instances = list()
    mean_data = dict()

    def __init__(self, star_name, function_name):
        super().__init__()
        self.star_name = star_name
        self.function = Worker.functions(function_name)
        self.command = "{} {}".format(function_name, star_name)
        print("Creando Worker para: {}".format(self.command))
        self.setDaemon(True)
        Worker.instances.append(self)
        self.lock = threading.Lock()

    @staticmethod
    def functions(func_name):
        """
        Este metodo estatico recibe el nombre de una funcion
        y retorna una FUNCION. Esta recibira un string
        con el nombre de la estrella, ya sea para
            - Cargarla al diccionario loaded_stars (open)
            - Calcular promedio (mean)
            - Calcular varianza (var)
        """

        def open(star_name):
            if star_name not in loaded_stars:
                with __builtins__.open('{}.txt'.format(star_name), 'r') as reader:
                    lista = reader.readlines()
                return lista
            # completa aqui: debe leer el archivo
            # y cargarlo a un diccionario
            # TIP: desde el scope de esta funcion open,
            # puedes acceder al builtin "open" como
            # __builtins__.open

        def mean(star_name):
            # Modifica esto para que
            # no se abra el archivo nuevamente
            # sino que se trabaje con el diccionario
            # de estrellas ya cargadas
            lines = loaded_stars[star_name]
            ans = sum(map(lambda l: float(l), lines)) / len(lines)
            Worker.mean_data[star_name] = ans
            return ans

        def var(star_name):
            prom = Worker.mean_data[star_name]
            # modifica esto para que
            # no se abra el archivo nuevamente
            # sino que se trabaje con el diccionario
            # de estrellas ya cargadas
            lines = loaded_stars[star_name]
            n = len(lines)
            suma = sum(map(lambda l: (float(l) - prom)**2, lines))
            return suma / (n - 1)

        return locals()[func_name]

    def run(self):
        with self.lock:
            if self.function.__name__ == "open":
                loaded_stars[self.star_name] = self.function(self.star_name)
                output_list.append('Open de {} terminado'.format(self.star_name))
                return

            output = self.function(self.star_name)

            # Modifica aqui para que no se imprima
            # sino que se agregue la tupla a la lista de outputs
            output_list.append((self.getName(), self.command, "DONE", datetime.datetime.now()))


if __name__ == "__main__":
    output_list = list()    # variables agregadas
    loaded_stars = dict()   # para esta actividad
    command = input("Ingrese siguiente comando:\n")

    while command != "exit":
        # Preocupate del comando "status"
        if command == "status":
            print("Resultados: ")
            for s in output_list:
                print(s)
            command = input("Ingrese siguiente comando:\n")

        else:
            try:
                function, starname = command.split(" ")

                executed = False
                for w in Worker.instances:
                    if w.command == command and w.isAlive():
                        print("[DENIED] Ya hay un worker ejecutando el comando")
                        executed = True
                        break

                if not executed:
                    # preocupate de que solo se cree un worker
                    # si la estrella ya fue cargada
                    # al diccionario
                    if function == "var" and starname not in Worker.mean_data:
                        print("[DENIED] No se puede calcular varianza "
                              "sin haber calculado el promedio antes!")

                    elif starname in ["AlphaCentauri", "Arcturus",
                                      "Canopus", "Sirius", "Vega"]:
                        if function == "open" and starname not in loaded_stars:
                            Worker(starname, function).start()
                        elif function == "var" and starname in Worker.mean_data:
                            Worker(starname, function).start()
                        elif function == "mean" and starname in loaded_stars:
                            Worker(starname, function).start()

                    else:
                        print("[DENIED] Comando invalido\n\t"
                              "El nombre de la estrella no es correcto")

            except (ValueError, KeyError) as err:
                print("[DENIED] {}\n\tComando invalido".format(
                    type(err).__name__))

            command = input("Ingrese siguiente comando:\n")

    # Reemplazar esto por imprimir lista de outputs
    # y luego, imprimir los que aun no han terminado
    print("Lista de outputs: ")
    for s in output_list:
        print('***', s)
    print("No alcanzo a terminar:")
    for w in Worker.instances:
        if w.isAlive():
            print("{} / {}".format(w.getName(), w.command))
