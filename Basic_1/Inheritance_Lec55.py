class A:

    def __init__(self):
        print("in init A")
    def feature1(self):
        print("this is feature 1")

    def feature2(self):
        print("this is feature 2")

class B(A):#by writing () we mean B is child

    def __init__(self):
        super().__init__()#this is constructor overloading
        print("in init B")
    def feature3(self):
        print("this is feature 3")

    def feature4(self):
        print("this is feature 4")



'''a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature3()
b1.feature4()
b1.feature1()#from inheritance
b1.feature2()#from inheritance'''

b2=B()