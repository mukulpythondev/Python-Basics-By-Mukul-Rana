# CREATE THE SNAKE WATER GUN GAME
import random

def gamewin(comp,you):
    if comp==you:
        return None
    # now check all possibilty if comp choose "S"
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    # now check all possibilty if comp choose "w"
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    # now check all possibilty if comp choose "g"
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False
print("Comp turn: Snake(s) Water(w) Gun(g) ?\n")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you=input("Your turn Snake(s) Water(w) Gun(g)?\n")
a =gamewin(comp, you)

print(f"Computer Choose{comp}\n")
print(f"you choose {you}\n")
if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")

# File rename and open
f=open('python by mukul rana\sample.txt', 'r')
data= f.read(3)# only read 3 character of given text file and give output
print(data)
f.close()
# Read line function give line by line output
# Now let see how to write the file
f=open('python by mukul rana\sample.txt','w')
f.write("hi Mukul this text add by write function" )
f.close()

# with function Use
with open('python by mukul rana\sample.txt','r') as f :
    a=f.read()
# Bro lets create table from 2-20
for i in range(2,21):
    with open(f"python by mukul rana\sample{i}.txt", 'w') as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}\n")

#OOPS code example
#railway form
class Railwayform:
    formtype="Railwayform"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.Train}")
mukulapplication=Railwayform()
mukulapplication.name="Mukul"
mukulapplication.Train="Rajdhani Express"
mukulapplication.printdata()

class employee:
    company = "MINTERS"
    def getsalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary} ")
    # static methods
    @staticmethod 
    def greet():
        print("Good Morning ")

mukul = employee()
mukul.salary=100000
mukul.getsalary()
mukul.greet()


class freelance:
    company= "deverse"
    salary=100
adarsh=freelance()
rishabh=freelance()
adarsh.salary=101
rishabh.salary=99
print(adarsh.salary)
print(rishabh.salary)

