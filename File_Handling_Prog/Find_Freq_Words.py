with open("tech.txt", mode='r') as file:
    word=file.read().split()
    print(word)
d=dict()  #creating an empty dictionary



for w in word:
    if w in d:
        d[w]=d[w]+1
    else:
        d[w]=1

for k in list(d.keys()):
    print(k, ":" ,d[k])
