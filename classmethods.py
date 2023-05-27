class freelancer:
    company= "Boat"
    salary= "250"
    @classmethod
    def changesalary(cls,new):
        cls.salary=new
    #Alternative
    #def salarychange(self):
     #   self.__class__.salary=sal

mukul=freelancer()
mukul.changesalary(544)
print(mukul.salary)

# getter and setter method examples
class employee:
    company="Indian Oil"
    salary=5000
    salarybonus=600
    @property
    def totalsalary(self):
        return self.salary +self.salarybonus

    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus= val- self.salary
    
e=employee()
print(e.totalsalary)
e.totalsalary=7000
print(e.salary)
print(e.salarybonus)

# OPERATORS OVERLOADING
class numbers:

    def  __init__(self,num):
        self.num=num
    def __add__(self, num2):
        print("Lets Add")
        return self.num +num2.num
    
    def __mul__(self,num2):
        print("Lets Multiply")
        return self.num * num2.num

n1= numbers(35)
n2= numbers(10)
sum= n1+n2
print(sum)
mul= n1*n2
print(n1*n2)

#PRACTICE SET
class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
    
v2d = C2dVec(1, 3)
v3d = C3dVec(1, 9, 7)
print(v2d)
print(v3d)


#q2
class animals:
    animaltype= "mammmal"
class pets:
    colour= "white"
class dogs:
    @staticmethod
    def bark():
        print("bow bow!!")
d= dogs()
d.bark()

#Q3
class Vector:
    def __init__(self, vec):
       self.vec = vec
    
    def __str__(self):
        str1 = "" 
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1+v2)
print(v1*v2)  

# Number Guess Game
import random
randno= random.randint(1,100)
print(randno)
userguess=None
guess=0
while(userguess!= randno):
    userguess= int(input("Enter your guessed number!"))
    if (userguess==randno):
      print("You Guessed Right Number")
    else:
        if (userguess>randno):
          print("you guessed wrong! Your number is larger")
        else:
          print("you guessed wrong! Your number is smaller")
    guess += 1
print(f"You guessed the number in {guess} guesses ")
     