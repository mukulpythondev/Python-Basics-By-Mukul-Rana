import time

def whileloop():
    i=0
    while i<5000:
        i=i+1
        print(i)
def forloop():
    for i in range(5000):
        i=i+1
        print(i)
init=time.time()# ye time h second m 1970 se ab tk ka 
whileloop()
t=time.time()- init
forloop()
print(t)
print(time.time()- init)
print(50)
time.sleep(4)
print("This text is print after 4 seconds")

