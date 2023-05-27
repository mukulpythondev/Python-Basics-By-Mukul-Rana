class Maths:
    def  __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num=self.num+n
    @staticmethod#isko lagane se ye universal bn gya or isko self ki jarurat nhi h 
    def add(a,b):
        return a+b

m=Maths(100)
print(m.num)
m.addtonum(50)
print(m.num)