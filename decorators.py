#decorator mtlb jo weelcome ya gesture de

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this functions")
    return mfx()
@greet
def hello():
    print("Namaste Deshwasiyo")
import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b
#Getters 
class myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"Value is {self._value}")
    @property
    def ten_value(self):
        return 10 * self._value
    @ten_value.setter#is method se hmne variable ki value change karke uspe funtion run kiya 
    def ten_value(self, new):
        self._value=new/10

obj=myclass(10)
obj.ten_value=60

print(obj.ten_value)
obj.show()
