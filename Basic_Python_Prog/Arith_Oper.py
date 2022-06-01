def add(a,b):
    return (a+b)

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

a=int(input("enter values of a "))
b=int(input("enter values of b "))
sum=add(a,b)
print(f"sum is : {sum}")
subt=sub(a,b)
print(f"subtraction of two are: {subt}")
division=div(a,b)
print(f"division of two are: {division}")
multiply=mult(a,b)
print(f"multiplication of two are: {multiply}")