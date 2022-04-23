class complex :

    def __init__(self, real=None, image=None):
        self.x = real
        self.y = image
        #sorat o makhraj 

    def sub(self, second):
        result=complex()
        result.x= self.x - second.x
        result.y= self.y - second.y
        return result
    #tafrigh 2 kasr

    def sum(self, second):
        result=complex()
        result.x= self.x + second.x
        result.y= self.y + second.y
        return result
    #jam 2 kasr

    def multiple(self, second):
        result=complex()
        result.x= self.x * second.x - self.y * second.y
        result.y= self.x * second.y - self.y * second.x
        return result
    #zarb 2 kasr

    def show(self):
        return str(self.x) +'+('+str(self.y) +')i'
    #show kasr

while True:
    print('enter the complex number1 :')
    real1 = int(input('enter complex num1 --> real : '))
    image1 = int(input('enter complex num1 --> image  : '))
    n1 = complex(real1 ,image1)
    print('enter the complex number2 :')
    real2 = int(input('enter complex num2 --> real : '))
    image2 = int(input('enter complex num2 --> image  : '))
    n2 = complex(real2, image2)
    while True:
        print('\nmenu:\n1.add\n2.sub\n3.mul\n4.exit')
        c = int(input())
        if c==1:
            print(n1.sum(n2).show())
        if c==2:
            print(n1.sub(n2).show())
        if c==3:
            print(n1.multiple(n2).show())
        if c==4:
            break
    e = input('Do you want to continue ? (y/n)  ')
    if e == 'n':
        break