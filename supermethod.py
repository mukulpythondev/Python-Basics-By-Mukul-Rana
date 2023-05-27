#super method ko hm kisi or class ke function ko apni class m call karne ke liye likhte h 
class papa:
    def papa_method(self):
        print("This is class of papa")

class beta(papa):
    def papa_method(self):
        print("Harry ")
    def beta_method(self):
        print("This is class of beta")
        super().papa_method()
child=beta()
child.beta_method()
child.papa_method()