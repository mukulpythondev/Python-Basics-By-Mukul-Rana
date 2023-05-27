def my_generator():
    for i in range(5):
        yield i#buddy isne stop laga diya aab jab tu bolega toh start hogi 
gen=my_generator()
print(next(gen))#ye 0 dega
print(next(gen))#ye 1 dega
print(next(gen))#ye 2 dega
print(next(gen))#ye 3 dega
print(next(gen))#ye 4 dega


