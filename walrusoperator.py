#a=True
print(a:=False)#: ye use karne se print kar dega
number=[1,2,3,4,5]
while (n :=len(number))>0:
    print(number.pop())
print(number)
foods=list()
while (food:=input("What Food do you like ?"))!="quit":
    foods.append(food)
print(foods)