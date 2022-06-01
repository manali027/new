def check(a,b):
    c=a+b
    d=a-b
    return c,d

a=int(input("enter values of a "))
b=int(input("enter values of  b"))

c,d=check(a,b)
print(c,end=" ")
print(d,end="")