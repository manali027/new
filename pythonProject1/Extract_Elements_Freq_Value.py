ls_input=[4,3,2,2,3,4,1,3,2,4,4]
ls_ouput=[]
length=len(ls_input)
print(length)
count=1

for i in range(length):
  temp=ls_input[i]
  for j in range(i+1,length):
      if(ls_input[j]==temp):
          count+=1
  ls_ouput.append(temp)

print(ls_ouput)