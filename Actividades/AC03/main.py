# coding=utf-8

# Defina la clase 'Rational' en este espacio
def mayor(x,y):
    if abs(x)>abs(y):
        return abs(x)
    else:
        return abs(y)
def simplificar(a,b):
    for i in range(2,mayor(a,b)+1):
        while i <= abs(a) and i <= abs(b):
            if a%i == 0 and b%i == 0:
                a = a//i
                b = b//i
            else:
                break
    if a>0 and a/b < 0 or (a<0 and b<0):
        return -a,-b
    return a,b

class Rational:
    def __init__(self,a,b):
        self.numeros = simplificar(a,b)
        self.a = self.numeros[0]
        self.b = self.numeros[1]
    def __str__(self):
        if self.b == 1:
            return '{}'.format(self.a)
        return '{}/{}'.format(self.a,self.b)

    def __repr__(self):
        return 'Rational({})'.format(self.__str__())

    #Suma
    def __add__(self,racional):
        h = self.a*racional.b + racional.a*self.b
        k = self.b*racional.b
        return Rational(h,k)

    #Resta
    def __sub__(self, racional):
        h = self.a*abs(racional.b) - racional.a*abs(self.b)
        k = self.b*racional.b
        return Rational(h,k)

    def __mul__(self,racional):
        h = self.a*racional.a
        k = self.b*racional.b
        return Rational(h,k)

    def __div__(self,racional):
        h = self.a*racional.b
        k = self.b*racional.a
        return Rational(h,k)

    #Igual
    def __eq__(self, racional):
        return abs(self.a) == abs(racional.a) and abs(self.b) == abs(racional.b)

    #Menor que
    def __lt__(self, racional):
        return self.a*abs(racional.b)<abs(self.b)*racional.a

    #Mayor que
    def __gt__(self,racional):
        return self.a*abs(racional.b)>abs(self.b)*racional.a

    #Menor o igual
    def __le__(self,racional):
        return self.a*abs(racional.b)<=abs(self.b)*racional.a

    #Mayor o igual
    def __ge__(self,racional):
        return self.a*abs(racional.b)>=abs(self.b)*racional.a

    #Division
    def __truediv__(self,racional):
        h = self.a*racional.b
        k = self.b*racional.a
        return Rational(h,k)

if __name__ == "__main__":
    r1 = Rational(26, 4)
    r2 = Rational(-2, 6)
    r3 = Rational(34, 7)

    # 13/2 -1/3 34/7
    print(r1, r2, r3, sep=", ")

    # [Rational(1), Rational(-11/2)]
    print([Rational(1, 1), Rational(22, -4)])

    # 41/6
    print(r1 - r2)

    # 221/7
    print(r1 * r3)

    # 7/15
    print(r2 / Rational(5, -7))

    # True
    print(Rational(-4, 6) < Rational(1, -7))

    # True
    print(Rational(12, 8) == Rational(-24, -16))
