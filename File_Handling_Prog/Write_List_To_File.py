list_fruits=["Orange","apple","banana"]
with open("try.txt",mode='w') as file:
    for l in list_fruits:
        file.write(l + " ")