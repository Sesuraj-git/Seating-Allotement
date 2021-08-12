import sqlite3
from tkinter import *

root=Tk()
root.title('Seating in python')
root.iconbitmap('DBC.ico')
root.config(bg="gray17")
root.geometry("800x400")

frame=LabelFrame(root,text='Select classes ...',padx=300,pady=100)
frame.place(x=100,y=50)


global Frame
global exam_halls
exam_halls=[]
conn =sqlite3.connect('classes.db')
clsses=conn.cursor()

def check_existing(value ):
    global clsses
    
    sr=value.upper()

    # try:
    get=("SELECT class, rows, colls FROM exam_halls WHERE class=?" )
    clsses.execute(get,[sr])
    temp=clsses.fetchall()
    rasp=temp
    print(rasp)

    """except:
        mylabel=Label(frame,text='miss-spelled class')
        mylabel.pack()
        return 2"""
        
    if sr in exam_halls:
        mylabel=Label(frame,text='there\'s a duplicate entry',fg='red')
        mylabel.pack()
        return 3
    else:
        insert_classtest = """INSERT INTO exam_halls_test(class, rows, colls) 
            SELECT class, rows, colls FROM exam_halls WHERE class=?;"""
        
        clsses.execute(insert_classtest, [sr])
        exam_halls.append(sr)
        
        mylabel=Label(frame,text=sr)
        mylabel.pack()
        # print(exam_halls)
        return 1
    
    

def get_halls(classes):    
	
    for cls1 in classes :
        truth= check_existing(cls1)

        if truth==1:
            pass
        elif truth==2:
            return 2
        elif truth==3:
            return 3
    
    sorted_classtest = """select class from exam_halls_test ;"""
    clsses.execute(sorted_classtest)
    fetched =clsses.fetchall()
    final_return =[]
    for i in fetched:
        final_return.append(i[0])
    
    return final_return

get_halls(["1caa", "2caa"])


root.mainloop()