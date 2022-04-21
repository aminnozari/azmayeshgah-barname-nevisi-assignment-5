class time:
    def __init__(self,h=0,m=0,s=0,flag=0):
        self.h=h
        self.m=m
        self.s=s
        self.f=flag
        self.fix1()
        self.fix2()

    def show(self):
        print(self.h,":",self.m, ":",self.s)

    def sum(self,other):
        result=time()
        result.h=self.h+other.h
        result.m=self.m+other.m
        result.s=self.s+other.s
        result.fix1()
        return result
    
    def sub(self,other):
        result=time()
        result.h=self.h-other.h
        result.m=self.m-other.m
        result.s=self.s-other.s
        result.fix2()
        return result

    def fix1(self):
      if (self.f==0):  
        if self.s >=60:
            self.s -=60
            self.m +=1

        if self.m >=60:
            self.m -=60
            self.h+=1    

        

    def fix2(self):
      if (self.f==0):    
        if self.m < 0:
            self.m +=60
            self.h -=1

        if self.s <0:
            self.s +=60
            self.m -=1

    def convert_tosec(self):
        
        print("converted to seconds: ",self.h*3600+self.m*60+self.s,"s")


    def convert_totime(self):
        
        result=time()
        self.h=int(self.s/3600)
        self.m=int((self.s-(self.h*3600))/60)
        self.s=(x-(self.h*3600+self.m*60))
        result.h=self.h
        result.m=self.m
        result.s=self.s
        return result






              
while(True):    
    print("choose from menu:")
    print("1->sum ")
    print("2->sub")
    print("3->convert time to second")
    print("4->convert second to time")
    print("5-exit")
    n=int(input())

    if n==1:
        print("first time...")
        hour=int(input("hour: "))
        minute=int(input("minute:"))
        second=int(input("second:"))
        t1= time(hour,minute,second,0)
        print("second time...")
        hour2=int(input("hour: "))
        minute2=int(input("minute:"))
        second2=int(input("second:"))
        t2= time(hour2,minute2,second2,0)
        a=t1.sum(t2)
        a.show()
    if n==2:
        print("first time...")
        hour=int(input("hour: "))
        minute=int(input("minute:"))
        second=int(input("second:"))
        t1= time(hour,minute,second,0)
        print("second time...")
        hour2=int(input("hour: "))
        minute2=int(input("minute:"))
        second2=int(input("second:"))
        t2= time(hour2,minute2,second2,0)
        b=t1.sub(t2)
        b.show()

    if n==3:
       
        x=input("enter time in this format-> hour:minute:second :") 
        text=x.split(':')
        h=int(text[0])
        m=int(text[1])
        s=int(text[2])
        t4=time(h,m,s,flag=1)
        t4.convert_tosec()
        
       

    if n==4:
       
        x=int(input("enter the seconds: "))
        t3=time(s=x,flag=1)
        b=t3.convert_totime()
        b.show()

    if n==5:
        print("goodbye")
        exit()       