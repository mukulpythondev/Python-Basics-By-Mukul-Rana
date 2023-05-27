# Author : Mukul (examplw of comments)
'''hi i am mukul programmer
and coder''' 
import os
print(os.listdir()) #show hua ki kon kon si file save h

# comment karne ka shortcut h ctrl+/
print("hello world")
print('''twinkle twinkle little star
how are wonder what you are ''')# multiple line print karne ke liye '''
a='''mukul
is 
good 
boy'''
b=34
c=4.59
# d="mukul is a good boy"
e=False
f=None
# printing the variable
print(a)
print(b)
print(c)
print(e)
print(f)
# printing the Datatype
print(type(a))
print(type(b))
#Arithmetic  Operators
a=4
b=3
print("The value of 4+3 is " , 4+3)
print("The value of 4-3 is " , 4-3)
print("The value of 4*3 is " , 4*3)
print("The value of 4/3 is " , 4/3)

# Assingnment operator
a =34
a +=2
print(a)
a -=5
print(a)
a *=3
print(a)
a /=3
print(a)

# Comparision Operators
# # b =(7>=7)
# b =(13>7)
# b =(25<10)
# b =(25<=10)
# b =(25==10)
# b =(50!=59)

# logical Operator
bool1 = True
bool2 = False

print("The value of Bool1 and Bool2 is" , (bool1 and bool2))
print("The value of Bool1 or Bool2 is", (bool1 or bool2)) 
print("The value of not Bool2 is",  (not bool2) )

# lets learn typecasting means change datatypes
n ="4005"
n = int(n)
print(n+6)

#lets learn about input 
a =input("Enter the number")
a =int(a) #convert a to intiger (if possible)
print(type(a))

# make code for calculating average
a = input("Enter the first number :")
b = input("Enter the Second number:")
a = int(a)
b = int(b)
Avg = (a+b)/2
print( "The average of a and b", Avg)

#code for square of any number
a =input("Enter the Number :")
a = int(a)
print("the square of a", a*a)

# Lets learn more about Strings
b = "Mukul's" # This double quote used when we use single quote
b = "Mukul's" # This single quote used when we use double quote
b = '''Muku'l"s'''  # This triple quote used when we want to use single and double quote
print(b)
 # Lets Learn about Slicing
# 1st we learn concatnating
# greeting = "Good Morining,"
# name = "Mukul Rana"
# c =( greeting + name)
# print(c)
name = "Mukul"
# print(name[0])
# name[3] = "d" ->> it does not support or work
#print(name[0:3])
#print(name[:3]) # ye iski tarah same h name[0:3])
# print(name[0:]) # ye iski tarah same h name[0:5])
# print(name[-1:-5])# ye iski tarah same h name[0:5])
d = name[1:4:2] # yha par character ek chod chod ke likhaga
print(d)
# Lets learn about Sting Functions
Aim = "best Developer and competion with himself not from age group"
# print(len(Aim))
# print(Aim.endswith ("group"))
# print(Aim.count ("o")) 
# print(Aim.capitalize ())  # isne hame string ke first letter ko capatalixe karke diya 
print(Aim.find("best")) #agar sting hoti h to uski value data varna nhi hoti to -1
print(Aim.replace("group","criteria"))
#lets learn escape sequece characters
topic = "hi i am Mukul rana.\n I \tam good web developer\\coder" # new line ke liye ham \n ye tag use karte h 
#yad rakhiyo isme matleab \n danda enter ke pass wala use kiya h or \t ham tab ke liye use karte h
print(topic)
#\n -new line
#\t -tab
#\'- ye hame text ko single quote m likh ke de dega
#\\ - back slash hi print kar dega
# name = input("Enter your name\n")
# print("Welcome and good morning", name)

# Ab ham sekhenge ki ek letter ko 10-30 logo ko kaisa ek sath bhej sakete h
letter = ''' Dear <Name>,
You are selected!
Date :<Date>
'''  
Name = input("Enter your name\n")
Date = input("Enter the Date\n")
letter =letter.replace("<Name>",Name)
letter =letter.replace("<Date>",Date)
print(letter)

#Lets learn about lists and tuples
List =[1,3,"Mukul",1.4]
# Print using print functtion
print(List)
# access using index number= List[o], list[1] etc
print(List[0])
# change the list element
List[0]=34
# list slicing
Friends = ["Mukul", "Harshit", "Vaibhav", "Aryan"]
print(Friends[0:4])
# list methods
L1= [3,6,2,1,0]
L1.sort() # bro yha par list ascending order m lag jayegi
L1.reverse() # ye reverse order m value dega
L1.append(5) # ise se ham list ke end m apne koi bhi text add kar sakete h
L1.insert(0,44) # yha par pehle no index hoga or dusra no vo h jo index no ki value of change kar dega
L1.pop(3)# jo no diya h us index no par element ko delete kar dega
L1.remove(6) #  bro remove 6 from the list 
print(L1)

# Lets learn about TUPLES
# creating a tuple using ()
T = (2,5,3,6,3,)
T1 = () # ye bas bracket print karega
T2 = (2,) # ek element m comma jarrori h !!!
# we can print the value of tuples
#print(T[9])
# we can not change or update the value of tuples!!!

# methods in tuple
#print(T.count(1)) # isme ye 1  count karega kitne bar aya h
#print(T.index(1)) # isme ye index par jo value hogi return  karega

# Creating a list of fruits that input by user
F1 = input("Enter The  Fruit Number 1: ")
F2 = input("Enter The  Fruit Number 2: ")
F3 = input("Enter The  Fruit Number 3: ")
F4 = input("Enter The  Fruit Number 4: ")
F5 = input("Enter The  Fruit Number 5: ")
F6 = input("Enter The  Fruit Number 6: ")
F7 = input("Enter The  Fruit Number 7: ")
Myfruitbasket = [F1,F2,F3 ,F4,F5,F6,F7]
print(Myfruitbasket)

# how to get sum of elements of list
l = [2,5,34,53]
#print(l[0]+l[3])
print(sum(l))


# Lets Learn About The Dictionaries in Python
mukuldict = {"Mukul" : "A Coder",
"Time" : "Precious",
"Marks" : [34,35],
"anotherdict" : {"Mukul" : "A Player"},
1 : 2
}
# print(mukuldict["Time"])
# how to change the values in dictionaries
mukuldict["Marks"] = [53,55]

# Methods the to print the dictionaries
print(mukuldict.keys()) # ye hamari dict ki sari keys ko print karega
print(mukuldict.values()) # ye hamari dic ki sari values ko print karega
print(mukuldict.items()) # ye hamari dic ki sari key and values ko print karega
updatedict = { "Harshit Shrivastav" : "Friend"
}

mukuldict.update(updatedict) # update the dictionary with new key value
print(mukuldict)

# SAME
print(mukuldict.get("Marks")) # ye hamari is key jo value hogi generate karega
print(mukuldict["Marks"])  # ye bhi same hi kam karega

# Difference between [ ] and .get Syntax
print(mukuldict.get("Harry")) # ye word hamari dict m nhi lekin ye none output dega
#print(mukuldict["Harry"])  # ye output m error ko generate karega

# Now lets LEARN SETS
Sets = {2,5,3,6,3}
print(Sets)

# Important
sample = {}
print(type(sample)) # ye dictionary Print Karega
 
# An empty SET can be printed by below Syntax
sample2 = set()
print(type(sample2))

# Adding values to Empty SET
sample2.add(4)
sample2.add(6)
sample2.add((3,5,7,9)) # here we add a tuple in the SET

# WE CANNOT ADD LIST AND DICTIONARY BECAUSE THEY ARE MUTUABLE BUT SET AND TUPLE ARE IMMUTABLE

print(len(sample2)) # Prints the length of the SET
# Removal of item in sets
print(sample2.remove(4))

# pop method 
print(sample2.pop()) # Ye method hame remove element karne ke bad value return kar dega 



















