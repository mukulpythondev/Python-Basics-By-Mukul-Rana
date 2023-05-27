from symtable import SymbolTableFactory


class employers:
    company="techverse"

    def __init__(self, name, pay , sector):
        self.name= name
        self.pay= pay 
        self.sector= sector
        print("Employee is entered!!!!")
    def getinfo(self) :
        print(f"The name of employee {self.name}")
        print(f"The salary of {self.name} {self.pay}")
        print(f"The sector of {self.name} {self.sector}")

adarsh= employers("Adarsh",100, "Back End")
adarsh.getinfo()

# PRACTICE SET
#Q1
class programmer:
    company= "Microsoft"
    def __init__(self, name , salary):
        self.name= name
        self.salary= salary
    def employedetail(self):
        print(f"The name of employe {self.name} ")
        print(f"The name of salary {self.salary} ")
vaibhav= programmer("vaibhav",10000)
vaibhav.employedetail()
#Q2
class Maths:     
    def __init__(self, num ) :
        self.num=num
    def square(self):
        print(f"The value of {self.num} square is {self.num**2}")
    def cube(self):
        print(f"The value of {self.num} cube is {self.num**3}")
    def square_root(self):
        print(f"The value of {self.num} square root is {self.num**0.5}")
    
    @staticmethod
    def greet():
        print("The most easy to use calculator")


a = Maths(3)
a.greet()
a.square()
a.cube()
a.square_root()        

# q3
class sample:
    a ="karan"
obj=sample()
obj.a= "harry"
print(sample.a)
print(obj.a)

#Q5
class train:
    def __init__(self, name, fare , seats ) :
        self.name= name
        self.fare= fare
        self.seats= seats
    def gettraininfo(self):
        print(f"The name of train is {self.name} ")
        print(f"The seats available in   train is {self.seats} ")
    
    def trainfare(self):
        print(f"The fare  of train is {self.fare} ")
    
    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked with seat no {self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry this train all seats are full")

intercity= train("Doronto Express 3432",500, 53)
intercity.gettraininfo()
intercity.bookticket()

#inheritance
class Human:
    company="spidernet"
    def workingmember(self):
        print(f"I am the working member of the {self.company}")

class Male(Human):
    
    def daywork(self):
        print(f"We are day workers of {self.company}")


h=Human()
h.workingmember()
mt=Male()
mt.daywork()


#There are three types of INHERITANCE
#SINGLE = WHEN one parent and single child

# MULTIPLE= WHEN two parents quality in single child

# MULTILEVEL = WHEN Grandfather+Father(child of !st class)+son(child of 2nd class )


    