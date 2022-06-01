with open('File1.txt','r') as fin:
    for each_line in fin:
        for each_word in each_line.split(' '):
            print(each_word)

