import os
import datetime
from zipfile import ZipFile
def create():
    #os.chdir("C:/Users/lenovo/PycharmProjects/Basic_1/")
    #with ZipFile('C:/Users/lenovo/PycharmProjects/Basic_1/manali.zip','w') as zip:
                         #zip.write('C:/Users/lenovo/PycharmProjects/Basic_1/test.txt')
    #print(os.getcwd())

    #time1=os.stat('C:/Users/lenovo/PycharmProjects/Basic_1/test.txt').st_ctime
    #time1_f=time1/(3600*24)
    #print(time1_f)
    #a=datetime.datetime.today()
    #print(a)
    s=os.stat('C:/Users/lenovo/PycharmProjects/Basic_1/test.txt')[8]
    d=datetime.datetime.fromtimestamp(s)
    print(d)

create()