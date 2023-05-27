class officer:
    company="MukulDev"
    def __init__(self, name):
        
        self.name=name
        self.increment=0.5#ye sab instance variable
    def show(self):
        print(f"the officer name is {self.name} and iraise amount in {self.company} is {self.increment}")

ab=officer("Mukul")

ab.increment=0.9
officer.show(ab)#another method for input users
yz=officer("Harry")
yz.company="Coders"#ye company change ho gyi h 
yz.show()

