import os
import sqlite3
from tkinter import *
from PIL import ImageTk,Image
from excel_read import get_class_list, get_fileLocation
from exam_hall import get_exam_halls

from write_students import saveat1
from write_classes import finish

def allotement_fun(root):

    subframe1= LabelFrame(root,text='Selected class file ',padx=150)
    subframe1.pack(side=LEFT)
    subframe1.config(bg="white")

    
    subframe2= LabelFrame(root,text='Selected exam halls ', padx=150)
    subframe2.pack(side = RIGHT)
    subframe2.config(bg="white")
    
    # ok_button=Button(subframe1,text="Home1").pack(side=BOTTOM)
    print("allotement page")
    # class_file= get_fileLocation()
    global classes_list
    classes_list=0
    while classes_list == 0:
        subframe1.forget()
        subframe1.pack(side=LEFT)
        subframe1.config(bg="red")
        classes_list=get_class_list(subframe1)
        print('here',classes_list)
    halls_list=0
    subframe1.config(bg="green")
    while halls_list == 0:
        subframe2.forget()
        subframe2.pack(side = RIGHT)
        subframe2.config(bg="red")
        halls_list=get_exam_halls(subframe2)
        print("there", halls_list)
    subframe2.config(bg="green")
    finish(halls_list)
    saveat1(classes_list)
    

# allotement_fun()