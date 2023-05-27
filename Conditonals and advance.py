# lets Start learning conditonals
a = 45
if(a>4):
    print("The value of a is greater than 4")
elif(a>10):
    print("The value of a is greater than 10")
else:
    print("The value of a is less than 4 or 10")

# Write a code print yes if age is equal or greater than 18
a = int(input("Enter Your Age to Check you are eligible or not " ))
if(a>18):
    print("Yes you are eligible")
elif(a==18):
    print("Yes you are eligible")
else:
    print("You are not eligible")

# program of using AND OR
ag = int(input("Enter your Age :"))
if(a>34 and a<60):
    print("u can work with us")
else:
    print("sorry u can't work with us ")
# Example of OR
# ag = int(input("Enter your Age :"))
# if(a>34 or a<60):
#     print("u can work with us")
# else:
#     print("sorry u can't work with us ")


# USE OF IS OR IN
g = None
if (g is None):
    print("yes")
else:
    print("NO")

# Spam filter code
text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")

# write a program to check length of user name
name=input("Enter your name\n")
le=len(name)
if le<=10:
    print("Your name is less than ten letter")
elif le>10:
    print("Your name is larger than ten letter")

#LOOPS
#while
n=0
while n<10:
    print("Yes" + str(n))
    n=n+1
print("Done")

#for
for i in range(1,9):
    print(i)
    if i==5:
        break
#Practice set
lst=["Mukul","Harshit","Manish"]
for name in lst:
    if name.startswith("M"):
        print("Hello" +name)
#program to get a factorial
fact=int(input("Enter the Number :"))
factorial=1
for i in range(1,fact+1):
    factorial=factorial+1
print(f"the factorial of {fact} is {factorial}")
# print a * pattern
n=3
for i in range(3):
    print(" " * (n-i-1), end=" ")
    print("*"*(2*1+1), end=" ")
    print(" " * (n-i-1),)

# Now learn Functions
def greet(name):
    print("Good day"+name)
greet("Mukul")
#Recursive functin
def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(0)
print(f)
#practice set
#code to convert celsius into faherneit
def far(cel):
    return (cel*(9/5) +32)
c =int(input("enter the temperature to be converted:"))
f=far(c) 
print("Faherneit temperature is :"+str(f))
#find the sum of n natural number
def recursive_sum(n):
    if n<=1:
        return n
    else :
        return n+recursive_sum(n-1)
hk=recursive_sum(4)
print(hk)


