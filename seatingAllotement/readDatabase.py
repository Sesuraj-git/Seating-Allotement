import sqlite3

def read_halls():
    halls = []
    file = open('halls.txt', 'r')
    lines = file.readlines()
    for line in lines:
        cls = line.split('\t', )
        try:
            cls[-1], a = cls[-1].split('\n')
            halls.append(cls)
        except ValueError:
            halls.append(cls)
    return halls


def read_classes():
    file = open('classes.txt', 'r')
    lines = file.readlines()
    classes = []
    for line in lines:
        cls = line.split('\n')
        classes.append(cls[0])
    return classes


def fetch_rollnos(classes):
    conn = sqlite3.connect('students.db')
    stu = conn.cursor()
    rollnos = []
    for cls in classes:
        get = ("SELECT rollno FROM student WHERE class=? ORDER BY rollno ASC ")
        stu.execute(get, [cls])
        temp = stu.fetchall()
        for t in temp:
            rollnos.append(t[0])
    return rollnos


def devide_rollnos(rollnos, sizes):
    
    class_limit = 172
    class_limit = sizes[0]
    r1, r2, r3, r4, r5, r6 = [], [], [], [], [], []

    start = 0
    end = start + class_limit
    # for1
    for i in range(start, end):
        r1.append(rollnos[i])
        start += 1
    
    class_limit = sizes[1]
    end = start + class_limit

    # for2
    for i in range(start, end):
        r2.append(rollnos[i])
        start += 1
    
    class_limit = sizes[2]
    end = start + class_limit

    # for3
    for i in range(start, end):
        r3.append(rollnos[i])
        start += 1
    
    class_limit = sizes[3]
    end = start + class_limit

    # for4
    for i in range(start, end):
        r4.append(rollnos[i])
        start += 1
    
    class_limit = sizes[4]
    end = start + class_limit

    # for5
    for i in range(start, end):
        r5.append(rollnos[i])
        start += 1
    
    class_limit = sizes[5]
    end = start + class_limit

    # for6
    r6=[]
    
    for i in range(start, end):
        try:
            r6.append(rollnos[i])
            start += 1
        except:
            pass
    

    i = 0
    out_nos = [r1, r2, r3, r4, r5, r6]

    file = open('test.txt', 'w')
    wr = str(r1), '\n', str(r2), '\n', str(r3), '\n', str(r4), '\n', str(r5), '\n', str(r6)
    file.writelines(wr)
    return out_nos
