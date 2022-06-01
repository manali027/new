def read(n):
    with open("tech.txt") as myfile:
        firstNlines = myfile.readlines()[0:5] #slicing the list returned
        print(firstNlines)




n=int(input("enter the number of lines to be read"))
read(n)