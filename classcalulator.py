class calculator():
    def __init__ (self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)
        print(self.a-self.b)
        print(self.a*self.b)
        print(self.a/self.b)


x=eval(input('enter a no  '))
y=eval(input('enter 2nd no  '))

c = calculator(x,y)


