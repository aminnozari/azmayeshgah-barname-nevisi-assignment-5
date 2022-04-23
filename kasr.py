from math import gcd
def decore():
    print("\033[38;5;41m*****************")
class fraction:
    def __init__(self, n=0,d=None):
        self.n = n
        self.d=d
        self.reduceFraction()
    def show(self):
        if self.n==self.d:
            print("\033[38;5;211m",self.n)
        elif self.n==0:
            print('0')
        else:
            print("\033[38;5;211m",self.n,"/",self.d)
        
    def reduceFraction(self) :
        c = gcd(self.n,self.d);
        self.n = self.n // c;
        self.d= self.d // c;
    def Sum(self,other):
        numerator=self.n*other.d+self.d*other.n
        denominator=self.d*other.d
        result=fraction(numerator,denominator)
        return result
    def Sub(self,other):
        numerator=self.n*other.d-self.d*other.n
        denominator=self.d*other.d
        result=fraction(numerator,denominator)
        return result
    def Mult(self,other):
        numerator=self.n*other.n
        denominator=self.d*other.d
        result=fraction(numerator,denominator)
        return result
    def Div(self,other):
        numerator=self.n*other.d
        denominator=self.d*other.n
        result=fraction(numerator,denominator)
        return result

    
print('\033[38;5;225mwelcome !')
print('\033[38;5;225mwe need 4 ints for two fractions.')
print('\033[38;5;225mplease enter 4 num:')
n1=int(input())
d1=int(input())
while d1==0:
    print('\033[38;5;209wrong num, try again:')
    d1=int(input())
n2=int(input())
d2=int(input())
while d2==0:
    print('\033[38;5;209mwrong num, try again:')
    d2=int(input())
f1=fraction(n1,d1)
f2=fraction(n2,d2)
decore()
f3=f1.Sum(f2)
print('\033[38;5;111mSum:')
f3.show()
decore()
f3=f1.Sub(f2)
print('\033[38;5;111mSub:')
f3.show()
decore()
f3=f1.Mult(f2)
print('\033[38;5;111mMult:')
f3.show()
decore()
f3=f1.Div(f2)
print('\033[38;5;111mDiv:')
f3.show()