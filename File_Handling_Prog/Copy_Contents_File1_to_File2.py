import os
with open("File1.txt",mode='r') as file1:
     with open("File2.txt",mode='w') as file2:
          f=file1.read()
          file2.write(f)

'''
new_file = open("copy.txt", "w")
with open("hello.txt", "r") as f:
    new_file.write(f.read())

new_file.close()
'''
