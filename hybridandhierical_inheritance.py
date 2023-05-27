#Hybrid Inheritance example
class baseclass:
    pass
class derived1class(baseclass):
    pass
class derived2class(baseclass):
    pass
class derived3class(derived1class, derived2class):
    pass
