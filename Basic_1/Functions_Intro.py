# A simple Python function to check
# whether x is even or odd
'''def evenOdd(x):
    if (x % 2 == 0):
        print ("even")
    else:
        print ("odd")


# Driver code
evenOdd(2)
evenOdd(3)'''

#x=int(input("enter a  number"))

#def chc(x):
#    if (x%2==0):
#        print("even")

#    else:
#        print("odd")


#chc(x)

#passing values to a functions


def update(x):
    print(id(x))
    x=8
    print(id(x))
    print(x)

a=10
print(id(a))
update(a)#this is call by value
print(a)


#this is example of call by refernec becoz list is mutable(in python everthing is object as both li are pointing to same)
'''def update(li):
    li[0]=10
    print("in function")
    print(li)

li=[3,4,5]
print("befor passinf ")
print(li)
update(li)
print("after passinf ")
print(li)'''

#using keyword args to recive multiple arguments
'''def myFun(*args):
    for i in args:
        print(i)


myFun("Hello","Bye","SeeYou")'''

#local and global variables
'''a="manu"
def cha():
    a="manali"
    print(a)

print(a)
cha()'''

'''total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total;

# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total)'''


