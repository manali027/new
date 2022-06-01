with open('File1.txt','r') as fin:
    for line in fin:
        for each_char in line:
            print(each_char)

'''with open('File1.txt','r') as fin:
    lst=fin.readlines()
    for l in lst:
        for  i in l:
          print(i)

with open('File1.txt','r') as fin:
    while True:
       c=fin.read(1)
       if not c:
          break

       print(c)'''