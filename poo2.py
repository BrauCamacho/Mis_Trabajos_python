#sobrecarga de operadores
import random
class Fraccion: 
    def __init__(self, num =0, den =0):
        self.num = num
        self.den = den
    def __add__(self, other):
        if isinstance(other, Fraccion):
            num = self.num* other.den + other.num* self.den
            den = self.den  * other.den
            return Fraccion(num, den)
        elif isinstance(other, int):
            num = self.num + other * self.den
            den = self.den
            return Fraccion(num, den)
    def __radd__(self, other):
        if isinstance(other, Fraccion):
            num = self.num* other.den + other.num* self.den
            den = self.den  * other.den
            return Fraccion(num, den)
        elif isinstance(other, int):
            num = self.num + other * self.den
            den = self.den
            return Fraccion(num, den)
    def __lt__(self, other):
        return (self.num /self.den)< (other.num / other.den)
    def __str__(self):
        return f'{self.num}/{self.den}'
if __name__=="__main__":
    lista = []
    for i in range(5):
        lista.append(Fraccion(random.randint(1,10),random.randint(1,10)))
    for i in sorted(lista):
        print(i)
    fr1 = Fraccion(2,1)
    fr2 = Fraccion(2,1)
    fr3 = fr1+fr2
    print(fr3)
    fr1 = Fraccion(2,1)
    fr3 = fr1+5
    print(fr3)
    fr1 = Fraccion(2,1)
    fr3 = 5+fr1
    print(fr3)