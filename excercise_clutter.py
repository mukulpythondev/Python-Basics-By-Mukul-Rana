#use function that take input file type and rename 
import os 
f=os.listdir("tables")
i=0 
#for i in range(0,8):
 #   os.rename(f"sample{i+1}.txt", f"{i+1}.txt")
for file in f:
    if file.endswith("txt"):
        print(file)
        os.rename(f"tables/{i+1}.txt", f"tables/mukul{i+1}.txt")
        i=i+1
    