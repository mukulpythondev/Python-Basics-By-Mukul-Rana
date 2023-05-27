class Employee:
    def __init__(self,name ,id):
        self.name=name 
        self.id =id 
    def showdetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")
m= Employee("Mukul", 118853)
m.showdetails()
#kya hua hme pasand nhi aya nam class ka or code h bhot bada har jagha class ka nam nhi change karnege is class ko 
#new class m inherit karke new class m run karenge 
class programmer(Employee):
    def showlangurage(self):
        print("the default langurage is Python")

m2=programmer("Harry", 95343)
m2.showlangurage()
m2.showdetails()