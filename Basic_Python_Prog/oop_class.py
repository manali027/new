class Employee:
    def __init__(self,fname,lname,sal):
        self.fname=fname
        self.lname=lname
        self.sal=sal


obj1=Employee('manali','singh','200')
obj2=Employee('raj','verma',400)

print(f"Object 1 is {obj1.fname}{obj1.lname},{obj1.sal}",end="")
print(f"Object 2 is {obj2.fname}{obj2.lname}{obj2.sal}")




