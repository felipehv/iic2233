from utils.parser import ApacheLogsParser
from functools import reduce
from utiltools import groupby

#Sin for, sum, len, while
class BigAnalizador:

    def __init__(self, logs):
        self.logs = logs
        print(len(self.logs))

    def bytes_transferidos(self):
        return reduce(lambda x,y : x + y , iter(map(lambda x: x.size, iter(self.logs))))   

    def errores_servidor(self):
        lista = list(filter(lambda x: x.status in [404,500,501], iter(self.logs)))
        lista = list(map(lambda x: 1,lista))
        return reduce(lambda x,y : x + y , iter(lista)) 
        #return reduce(max, map(lambda x : len(l.rstrip()), [line for line in open('logs_out.txt')]))

    def solicitudes_exitosas(self):
        lista = list(filter(lambda x: x.status in [200,302,304], iter(self.logs)))
        lista = list(map(lambda x: 1,lista))
        return reduce(lambda x,y : x + y , iter(lista))

    def url_mas_solicitada(self):
        diccionario = dict()
        lista = list(map(lambda x: x.request, iter(self.logs)))
        return 

if __name__ == '__main__':
    parser = ApacheLogsParser("./utils/nasa_logs_week.txt")
    logs = parser.get_apache_logs()
    biganalizador = BigAnalizador(logs)

    biganalizador.bytes_transferidos()
    biganalizador.errores_servidor()
    biganalizador.solicitudes_exitosas()
    biganalizador.url_mas_solicitada()