class ranker:
    def __init__(self, name , salary):
        self.name= name 
        self.salary=salary
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0],string.split("-")[1])


s=ranker("Mukul", 15200)
print(s.name)
print(s.salary)
st="Harry-12000"
b=ranker.fromStr(st)
print(b.name)
print(b.salary)
