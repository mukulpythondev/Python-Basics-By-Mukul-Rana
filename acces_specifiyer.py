class mukul:
    def __init__(self):
        self.name = "Harry" #ye public specifyer h hm isse access kar sakte 

a=mukul()
print(a.name)
class coder:
    def __init__(self):
        self.__name="Mukul" #ye private ka example h isse access nhi kar sakte h

b=coder()
#print(b.__name) ye error de rha h 
print(b._coder__name)# ye acces karne ka shi tarika h 

print(a.__dir__())#ye attribut or method show kar rha h

print(b.__dir__())