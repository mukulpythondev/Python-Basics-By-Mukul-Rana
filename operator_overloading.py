class vector:
    def __init__(self, i , j , k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    def __add__(self, m):
        return vector(self.i+m.i,self.j+m.j, +self.k+m.k)
        

v1=vector(3,5,3)
print(v1)
v2=vector(6, 4, 7)
print(v2)
print(v1+v2)