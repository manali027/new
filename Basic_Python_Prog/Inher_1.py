class Base1:
    def display(self):
        return "Hello i am base class"

class Sub(Base1):
    __h=5
    def display_new(self):
        return "Hello i am child class"
        #print(Sub.__h)

Sub_obj1=Sub()
s1=Sub_obj1.display_new()
s2=Sub_obj1.display()
print(s1)
print(s2)
