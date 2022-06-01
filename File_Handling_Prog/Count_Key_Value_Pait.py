from collections import Counter
from collections import defaultdict
d={}

new=defaultdict(list)
with open('Count.txt','r') as fin:
    for line in fin:
        key=line.split(':')[0]
        value=line.split(':')[1]
        new[key].append(value)
print(new)
for key,value in new.items():
    v=new.values()
    for each in v:
        print(len(each),key)