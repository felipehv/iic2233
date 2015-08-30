import lib
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