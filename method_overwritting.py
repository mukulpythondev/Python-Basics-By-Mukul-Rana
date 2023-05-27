class  shape:
    def __init__(self, x,y):
        self.x=x
        self.y=y 
    def area(self):
        return self.x * self.y
re=shape(3,6)
print(re.area())
class circle(shape):
    def __init__(self, radius):
        self.radius=radius
        super().__init__(radius, radius)
    def area(self):
        return 3.14* super().area()

        #return 3.14*self.radius*self.radius
    
cr=circle(39)
print(cr.area())
