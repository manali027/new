content_array=[]
with open("tech.txt",mode='r') as f:
    for line in f:
        content_array.append(line)
    print(content_array[1])