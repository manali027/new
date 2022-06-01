
import random
def cowsandbulls():
    words=["rate","fail","cake","sore","tear","calm","rich","time","face","swan"]
    rand=random.randrange(0,10)#to select random index
    word=words[rand]
    cnt=0
    while(cnt<=15):
        s=input("enter string")
        if s=="-1":
            print("Thank you")
            return
        cows=0
        bulls=0
        #seal calm
        chars=0
        for c in s:
            if c in word:
                chars+=1 #chars will be 2 becoz a and l are in calm
        for i in range(0,4):
            if(s[i]==word[i]):
                bulls+=1


        cows=chars-bulls
        print("cows: " ,cows,"\tBulls: " ,bulls)
        if bulls==4:
            print("You win")

    cnt+=1
    print("OOPS maximum guess limit reached")


cowsandbulls()