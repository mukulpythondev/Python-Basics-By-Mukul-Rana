#Introduction To Object Oreinted Program
class noob:
    name="Mukul"
    occ="Penetreat Tester"
    networt=1999999
    def info(self):#self ko hm object mante h jisme hmne class di h jaise a
        print(f'The {self.name} is a {self.occ} ')
a=noob()
a.name="Adarsh"
a.occ="Software Developer"
print(a.occ)
print(a.name)
a.info()
#Constructor use karke hm data ko input lekar ek class m dal denge 
class employee:
    def __init__(self,n,o):#ye class call karne par automatic run ho jyega
        self.name=n
        self.occupation=o
    def infi(self):
        print(f"{self.name} is a {self.occupation}")
mukul=employee('Mukul', 'Web developer')
mukul.infi()
        