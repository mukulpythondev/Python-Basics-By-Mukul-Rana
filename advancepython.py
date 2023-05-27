while(True):
    print("press q to quit program")
    a= input("Enter a Number :")
    if a == 'q':
        break
    try:
        print("Trying....")
        a= int(a)
        if a>6:
            print(f"{a} is greater than 6 :")
    except  Exception as e :
            print(f" Your input resulted a error :{e}")

print("Thanks for playing game!")

# handeling different type of errors and exceptions
try :
    a= int(input("Enter you number: "))
    c= 1/a
    print(c)
except ValueError as e :
    print("Please enter only integer ")
    print(e)
except ZeroDivisionError as  e :
    print("Do not divide by zero ")
    print(e)

print("Thanks for using code ")

# Raising Errors 
def increment(num):
    try:
        return int(num)+1
    except :
        raise ValueError( "Please enter only integer !")
a= increment(5)
print(a)

# else and try 
try :
    m = int(input("Enter the number to be multiplied : "))
    x= m*5
    
except Exception as e :
    print(" enter the integer only ")
    print(e)
else : # this run if our try code run 
    print(f" Your input is calculated {x}")

# try and finally 
try:
    z= int(input("Enter your number :"))
    v= 1/z
except Exception as e :
    print(e)
    exit()
finally : # this print in all case if try run or except run 
    print("We have done!!!1")

# global variable example 
a= 43
def func1():
    global a 
    print(f" The value of first statement 1 , {a}")
    a= 7 # local variable
    print(f" The value of first statement 2 , {a}", )
func1()
print(f" The value of first statement 3 {a}"  )
