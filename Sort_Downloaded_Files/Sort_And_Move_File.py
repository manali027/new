import os
import shutil
import time,datetime
from plyer import notification

input_location='C:/Users/lenovo/Downloads/File_Collection/'
images_output_location='E:/Down/Images_Check/'
docs_output_location='E:/Down/Docs_Check/'
pdf_document_location='E:/Down/Pdf_Check/'
current_time=time.time()


file_set=set()
def move_file(fin):

     file_type=fin.split('.')[1]

     if(file_type.lower() in ['jpg','jpeg','png']):
        file_mod_time = os.stat(input_location + fin)[8]
        output_file_path = images_output_location + fin
        input_file_path = input_location + fin
        if (current_time > file_mod_time) or (os.path.isdir(output_file_path) == 'False'):

          shutil.move(input_file_path,images_output_location)
          print(f"{input_file_path} moved successfully")

        else:
            print(input_file_path + " file has been already moved to ouput location")

     if(file_type.lower() in ['docx','doc','txt']):
        file_mod_time = os.stat(input_location + fin)[8]
        output_file_path = docs_output_location + fin
        input_file_path=input_location+fin
        if (current_time > file_mod_time) or (os.path.isfile(output_file_path) == 'False'):

          shutil.move(input_file_path,docs_output_location)
          print(f"{input_file_path} moved successfully")

        else:
            print(input_file_path + " file has been already moved to ouput location")

     if(file_type.lower() in ['pdf']):
        file_mod_time = os.stat(input_location + fin)[8]
        output_file_path = pdf_document_location+fin
        input_file_path = input_location+fin

        if (current_time > file_mod_time) or (os.path.isfile(output_file_path) == 'False'):

          shutil.move(input_file_path,pdf_document_location)
          print(f"{input_file_path} moved successfully")

        else:
            print(input_file_path + " file has been already moved to ouput location")

def check_new_file():
    for fin in os.listdir(input_location):
        if(input_location+fin) not in file_set:
            notification.notify(title="HEY!!NEW FILE",
                                message=f"New file {fin} is added in your data folder",
                                app_icon="C:\\Users\\lenovo\\Downloads\\picture.ico",
                                timeout=60)

            move_file(fin)

def create_file_set():

    for fin in os.listdir(input_location):
        file_set.add(input_location+fin)
        move_file(fin)

while(True):
    create_file_set()
    time.sleep(60)
    check_new_file()






