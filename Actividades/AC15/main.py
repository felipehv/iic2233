import threading

names = ['mean', 'var']


class Worker(threading.Thread):
    mean_data = dict()      # para guardar los promedios
    # Sientete libre para usar otras
    # variables estaticas aqui si quieres

    # programa el __init__
    # recuerda imprimir cual es el comando
    # para el cual se creo el worker
    def __init__(self, star_name, function_name):
        super().__init__()
        self.star_name = star_name
        self.func_name = function_name


    @staticmethod
    def functions(func_name):
        """
        Este metodo recibe el nombre de una funcion
        y retorna una funcion que calcula promedio
        o varianza segun el argumento.
        Se necesita haber calculado promedio
        para poder calcular varianza
        """

        def mean(star_name):
            with open("{}.txt".format(star_name), 'r') as file:
                lines = file.readlines()
                ans = sum(map(lambda l: float(l), lines)) / len(lines)
                Worker.mean_data[star_name] = ans
                return ans

        def var(star_name):
            prom = Worker.mean_data[star_name]
            with open("{}.txt".format(star_name), 'r') as file:
                lines = file.readlines()
                n = len(lines)
                suma = sum(map(lambda l: (float(l) - prom)**2, lines))
                return suma / (n - 1)

        return locals()[func_name]

    # escriba el metodo run
    def run(self):
        print("Creando worker para calcular {} {}".format(self.func_name,self.star_name))
        func = self.functions(self.func_name)
        if func.__name__ == "mean":
            media = func(self.star_name)
            Worker.mean_data[self.star_name] = media
            print("La media de {} es: {}".format(self.star_name, media))
        else:
            print("La varianza de {} es: {}".format(
                self.star_name, func(self.star_name)))
        print("Worker de {} calculando {} ha finalizado".format(
            self.star_name, self.func_name))


if __name__ == "__main__":
    #w = Worker("ejemplo", "var")
    # w.start()
    command = input("Ingrese siguiente comando:\n").strip()

    while command != "exit":
        workers_list = []
        # Complete el main:
        #   - Que no se caiga el programa al ingresar inputs invalidos
        #   - Revisar que no haya un worker ejecutando el comando
        #   - Revisar que solo se puede calcular var estrella
        #           si ya se calculo mean estrella
        #   - Si corresponde: crear worker, echarlo a correr
        if command not in names:
            print("Error, el comando no existe")
            command = input("Ingrese siguiente comando:\n").strip()
            continue

        estrella = input("Ingrese una estrella: ").strip()

        for worker in workers_list:
            if worker.func_name == command and worker.star_name == estrella and worker.isAlive():
                print("[DENIED] Ya hay un worker en esto, por favor paciencia -.-' ")
            command = input("Ingrese siguiente comando:\n").strip()
            continue

        if command == "var" and estrella not in Worker.mean_data:
            print("[DENIED] Primero debes calcular la media para esto.")
            command = input("Ingrese siguiente comando:\n").strip()
            continue

        try:
            w = Worker(estrella, command)
            w.setDaemon(True)
            workers_list.append(w)

        except Exception as err:
            print("Error: {}".format(err))

        else:
            workers_list[-1].start()

        command = input("Ingrese siguiente comando:\n").strip()

    # imprimir cuales comandos
    # alcanzaron a terminar, y cuales no
    print("Comandos ingresados por el usuario: ")
    for worker in workers_list:
        if worker.isAlive():
            #worker.stop()
            print("No alcanzo a terminar: {} {}, impaciente".format(
                worker.func_name, worker.star_name))
        else:
            print("Alcanzo a terminar: {} {}, muy bien".format(
                worker.func_name, worker.star_name))
