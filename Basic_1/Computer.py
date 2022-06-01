class Computer:

    def __init__(self,cpu,ram):#like a constructor,called when object is created
        #print("in init")
        self.cpu=cpu
        self.ram=ram

    def config(self):#self is the object that wwe are passing
        print(self.cpu,self.ram)

#a=5
com1=Computer("i5","6gb")#creating an object here

com2=Computer("r3","8gb")
#print(type(com1))
#Computer.config(com1)#calling config of object com1
#Computer.config(com2)

#method 2 to call method from object
#normally this is used
com1.config()
com2.config()

