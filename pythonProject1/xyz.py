import random
import math,sys



def cowsandbulls():
    #n = 43365644
    #b=([(n // (10 ** i)) % 10 for i in range(math.ceil(math.log(n, 10)) - 1, -1, -1)])
    #for i in range(0,4):
    #    print(b[i])

    count_bulls = 0
    count_cows = 0
    user_number=int(input('enter a  number'))
    u_n= ([(user_number // (10 ** i)) % 10 for i in range(math.ceil(math.log(user_number, 10)) - 1, -1, -1)])

    n=7
    while(n<=7):
        #1223print('Chance'+ n)
        comp_number=random.randint(1000,9999)
        print(comp_number)
        c_n=([(comp_number // (10 ** i)) % 10 for i in range(math.ceil(math.log(comp_number, 10)) - 1, -1, -1)])

        for i in range(0,4):
            temp=u_n[i]

            for j in range(0,4):
                if temp==c_n[j]:
                    if i==j:

                        count_bulls+=1


                    count_cows+=1
    n-=1


    print(count_cows)
    print(count_bulls)









cowsandbulls()
