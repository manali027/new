with open("tech.txt") as myfile:
    firstNlines = myfile.readlines()[-3:]
    print(firstNlines)
