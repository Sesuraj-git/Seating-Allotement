import sqlite3
from tkinter import *

from tkinter import messagebox  

"""root=Tk()
root.title('Seating in python')
root.iconbitmap('DBC.ico')
root.config(bg="gray17")
root.geometry("800x400")
"""
# frame=LabelFrame(root,text='Select classes ...',padx=300,pady=100)
# frame.place(x=100,y=50)

global stu
global Frame
global examers_classes
examers_classes=[]
conn =sqlite3.connect('students.db')
stu=conn.cursor()

def check_existing(value ):
    global stu

    global ttl1
    sr=value.upper()

    try:
        get=("SELECT * FROM student_classes WHERE class=?" )
        stu.execute(get,[sr])
        temp=stu.fetchall()
        rasp=temp[0][0]

    except:
        mssg=value + ' is miss-spelled \n concider replacing'
        messagebox.showinfo("information",mssg)  
        mylabel=Label(frame,text='miss-spelled class')
        mylabel.pack()
        return 0
        
    if sr in examers_classes:
        
        mssg=value + ' is duplicated  \n concider removing'
        messagebox.showinfo("information",mssg) 
        mylabel=Label(frame,text='there\'s a duplicate entry',fg='red')
        mylabel.pack()
        return 0
    else:
        insert_classtest = """INSERT INTO classtest(class_id, class) 
            SELECT class_id, class FROM student_classes WHERE class=?;"""
        
        stu.execute(insert_classtest, [sr])
        examers_classes.append(sr)
        
        mylabel=Label(frame,text=sr)
        mylabel.pack()
        # print(examers_classes)
        return 1
    
    

def get_classes(classes,frame1):

    global frame
    frame=frame1
	
    for cls1 in classes :
        truth= check_existing(cls1)

        if truth==0:
            return 0
    
    sorted_classtest = """select class from classtest order by class_id;"""
    stu.execute(sorted_classtest)
    fetched =stu.fetchall()
    final_return =[]
    for i in fetched:
        final_return.append(i[0])
    
    return final_return



# root.mainloop()