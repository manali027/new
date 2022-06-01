import random
from idlelib import mainmenu


def welcome():

  for i in range(0,5):
    print("*\t",end="") #end means print wont transfer to next line automatically,instead * gets printed on same line
    #end suppreses the new line character
print()

print("*\t",end="")
for i in range(0,3):
    print("\t",end="")
print("*")


print("*\t",end="")
for i in range(0,3):
    print("\t",end="")
print("*")


print("*\t",end="")
for i in range(0,1):
    print("\t",end="")
print("welcome",end=" ")
for i in range(0,1):
    print("\t",end="")
print("*")


print("*\t",end="")
for i in range(0,3):
    print("\t",end="")
print("*")


print("*\t",end="")
for i in range(0,3):
    print("\t",end="")
print("*")

input("Press any key to start:")






def mainmenu():
    print("1.Rock,Paper,Scissor\n2.Cows and Bulls\n3.Exit")
    ch=int(input("enter your choice:"))
    if ch==1:
       rockpaperscissorsmenu()
    elif ch==2:
       cowsandbullsmenu()
    elif ch==3:
        exit()
    else:
        print("entered wrong option,kindly enter again")
        mainmenu()



def rockpaperscissorsmenu():
    ch=int(input("1.Play\n2.Show Rules\n3.Return to main menu"))
    if ch==1:
        rockpaperscissors()
    elif ch==2:
        rockpaperscissorsrules()
    elif ch==3:
        mainmenu()
    else:

        print("entered wrong option,kindly enter again")
        rockpaperscissorsmenu()



def cowsandbullsmenu():
    ch=int(input("1.Play\n2.Show Rules\n3.Return to main menu"))
    if ch==1:
        cowsandbulls()
    elif ch==2:
        cowsandbullsrules()
    elif ch==3:
        mainmenu()
    else:

        print("entered wrong option,kindly enter again")
        cowsandbullsmenu()




def rockpaperscissors():
    print("wwlcome to Rock paper scissor")
    print("you will be computing against computer.The player that scores 5 poimts first will be winner")
    print("if your choice is rock,enter 0")
    print("if your choice is paper,enter 1")
    print("if your choice is scissor,enter 2")
    print("if you wish to exit,enter -1")
    user=0
    comp=0
    cnt=0 #used for setting a maxmum limit of entering same values by user and comp/to prevent infinte loop

    chc=['Rock','Paper','Scissors'] #creating a list her

    while(user<5 and comp<5 and cnt<25):
        cnt=cnt+1
        u_ch=int(input("enter your choice"))

        if u_ch == -1:
            print("thank you for palying")
            break    #break or return statement

        c_ch=random.choice([0,1,2])
        if u_ch==0 and c_ch==1 : #rock /paper
            comp=comp+1
        elif u_ch==0 and c_ch==2 : #rock/scissor
            user=user+1
        elif u_ch==1 and c_ch==0: #paper/rock
            user=user+1
        elif u_ch==1 and c_ch==2: #paper/scissor
            comp+=1
        elif u_ch==2 and c_ch==0: #scissor/rock
            comp+=1
        elif u_ch==2 and c_ch==1: #scissor/paper
            user+=1
        print("You:" , chc[u_ch])
        print("Computer:", chc[c_ch])
        print("your score:",user,"\t Computer's score :",comp)

    if user>comp :
       print("Congrats ,You win")
    elif comp>user :
       print("Sorry you lost")
    else:
      print("match draw")
    mainmenu()


welcome()
print("\n"*100)#repliction operator * is used to see as a new page
mainmenu()




def cowsandbulls():
    user_number=int(input("enter the number"))
    user_cows,user_bulls=0
    comp_cows,comp_bulls=0
    n=7
    while(n<=7):
        {
            user_num



            n--
        }














