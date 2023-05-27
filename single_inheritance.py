class animal:
    def __init__(self, name , species):
        self.name= name 
        self.species=species
    def sound(self):
        print("The sound made by the Animal")
class cat(animal):
    def __init__(self, name , breed):
        animal.__init__(self, name, species='cat')
        self.breed=breed
    def sound(self):
        print("mewww")
a=animal("doneky", 'england')
a.sound()
c=cat("desi ", "england")
c.sound()

        