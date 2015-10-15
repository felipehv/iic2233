import random
import simpy

SIM_TIME = 500
INTERVAL = 10
TABLES = 3
NAME = "Cliente {0}"


def paciencia(cliente):
    return 2 * cliente.priority + 7


class Cliente():

    def __init__(self, *args, **kwargs):
        self.priority = kwargs['priority']
        self.name = kwargs['name']
        self.arrive = kwargs['arrive']
        self.number = kwargs['arrival_number']
        self.exit = None


class Restaurante():

    def __init__(self, env, capacity):
        self.env = env
        self.mesas = simpy.PriorityResource(env, capacity=capacity)
        self.__clientes = []
        self.n_atendidos = 1

    def espera(self, cliente):
        """
        ToDo
        """
        with self.mesas.request(priority=cliente.priority) as req:
            print('Cliente {} Esperando mesa en ={}. Prioridad={}.'.
                  format(cliente.name, self.env.now, paciencia(cliente)))
            result = yield req | self.env.timeout(paciencia(cliente))
            if req in result:
                print('cliente {} obtiene su mesa en tiempo={}'.format(
                    cliente.name, self.env.now))
                self.n_atendidos += 1
                # Recibe llamada?
                if random.randint(1, 10) == 1:
                    tiempo = round(random.uniform(7, 12))
                    yield self.env.timeout(tiempo)
                    print("El cliente {} recibio una llamada en tiempo= {}".format(cliente.name, self.env.now))
                else:
                    tiempo = round(random.uniform(30, 40))
                    yield self.env.timeout(tiempo)
                    print("El cliente {} se ha ido en tiempo = {}".format(cliente.name,self.env.now))
            else:
                print("El cliente {} se aburrio de esperar en tiempo = {}".format(
                    cliente.name, self.env.now))


def generador_clientes(env, lambdat, res):
    count = 0
    while True:
        yield env.timeout(random.expovariate(1 / lambdat))
        priority = random.randint(0, 25)
        cliente = Cliente(name=NAME.format(
            count), priority=priority, arrive=int(env.now), arrival_number=count)
        print("{0} ha arrivado al restaurant al instante {1} y \
                es el cliente numero {2}  del dia".format
              (
                  cliente.name,
                  env.now,
                  count
              ))
        count += 1
        env.process(res.espera(cliente))


if __name__ == '__main__':
    env = simpy.Environment()     # creamos un ambiente para simular
    res = Restaurante(env, TABLES)  # agregamos al ambiente un proceso
    env.process(generador_clientes(env, INTERVAL, res))
    env.run(until=SIM_TIME)  # ejecutamos la
