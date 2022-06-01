len_list=[]
with open("tech.txt",mode='r') as f:
      word=f.read().split()

l=len(max(word,key=len))
print(l)
for w in word:
    if(len(w)==l):
        print(w)

