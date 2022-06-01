'''from Calc_Module1 import *


a=5
b=5
c=add(a,b)
print(c)'''

#print(__name__)

def abc():
    print("in Demo_Module")

def main():
    abc()

if(__name__=="__main__"):# this means that this file will run only while running this module standalone
    main()
