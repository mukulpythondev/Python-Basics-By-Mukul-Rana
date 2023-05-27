class student:
    def __init__(self,name):
        self.name= name
    def __len__(self):
        #return len(self.name) alternative method
        i=0
        for c in self.name:
            i=i+1
        return i 
    def __str__(self):
        return f"The name of student is   {self.name}"
    
    def __repr__(self): # ye alternative h str ka agar str chalegi to nhi chalegi  
        return f"The name of student is   {self.name}"

