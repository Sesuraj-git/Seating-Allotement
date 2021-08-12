
import sqlite3
import os 
# check if file exists 

#     file=open("Rollnos.txt","w")
#     file.close()

conn =sqlite3.connect('students.db')
stu=conn.cursor()



class Divide_rolls():
	conn =sqlite3.connect('students.db')
	stu=conn.cursor()
	count=counti=countk=1
	num=flag=cnum=0
	i=0
	row1=row2=row3=row4=row5=row6=0
	seats=[]
	crows=[]
	seating=[]
	classes=[]
	row11=[]
	row12=[]
	row13=[]
	row14=[]
	row15=[]
	row16=[]

	def convertFile(self):
		i=0
		size1=100
		size2=100
		size3=100
		size4=100
		size5=100
		size6=100

		# sub_code1='1CAB'
		global set1
		# set1=['1CAA','1CAB']
		temp1=[]
		print('convertFile')
		for h in set1:
			temp=classwise(h)
			for j in temp:
				for k in j:
					temp1.append(k)
		one=open("forpy1.txt","w")
		pri=len(temp1)
		one.write(str(pri))
		one.close()
		sizearr={}
		# for
		print(os.listdir())
		os.startfile("forpy.exe")
		# import time 
		# time.sleep(5.0)
		is_open=False
		while(is_open!=True):
			try:
				print("file opened")
				one=open("forpy.txt","r")
				sizearr=one.readlines()
				print("reff\n\nreff ",one.readlines())
				print('sea',sizearr)
				# a=input()
				size1=int(sizearr[0])
				size2=int(sizearr[1])
				size3=int(sizearr[2])
				size4=int(sizearr[3])
				size5=int(sizearr[4])
				size6=int(sizearr[5])
				break
			except Exception as e:
				# print("noo")
				is_open=False
			
		
		flag=False
		while (i <len(temp1)) :
			# print(i)
			self.row14.append(temp1[i])
			if len(self.row14)==int(size4):
				i=i+1
				flag=True
				break				
			i=i+1
		print(i,'\t4\t',self.row14,len(temp1),'\n')
		#
		while (i <len(temp1)) :
			# print(i)
			self.row16.append(temp1[i])
			if len(self.row16)==int(size6):
				i=i+1
				flag=True
				break				
			i=i+1
		print(i,'\t6\t',self.row16,len(temp1),'\n')
		#
		while (i <len(temp1)) :
			# print(i)
			self.row12.append(temp1[i])
			if len(self.row12)==int(size2):
				i=i+1
				flag=True
				break				
			i=i+1
		print(i,'\t2\t',self.row12,len(temp1),'\n')
		#
		while (i <len(temp1)) :
			self.row11.append(temp1[i])
			if len(self.row11)==int(size1):
				i=i+1
				flag=True
				break		
			i=i+1
		print(i,'\t1\t',self.row11,len(temp1),'\n')
		
		while (i <len(temp1)) :
			# print(i)
			self.row13.append(temp1[i])
			if len(self.row13)==int(size3):
				i=i+1
				flag=True
				break				
			i=i+1
		print(i,'\t3\t',self.row13,len(temp1),'\n')
		#
		
		while (i <len(temp1)) :
			# print(i)
			self.row15.append(temp1[i])
			if len(self.row15)==int(size5):
				i=i+1
				flag=True
				break				
			i=i+1
		print(i,'\t5\t',self.row15,len(temp1),'\n')
		#
		
		
		# print(self.row12,'hi\n')
		print(i)
		file=open("Rollnos.txt","w")
		a1,a2,a3,a4,a5,a6=0,0,0,0,0,0
		i=0
		while a1==0 or a2==0 or a3==0 or a4==0 or a5==0 or a6==0 :	
			# for row in self.row11:
			if i<len(self.row11):
				file.write(self.row11[i])
				file.write('\t')
				# print('hihi')
			else:
				# print('hi')
				file.write('......\t')
				a1=1

			if i<len(self.row12):
				file.write(self.row12[i])
				file.write('\t')
			else:
				file.write('......\t')
				a2=1

			if i<len(self.row13):
				file.write(self.row13[i])
				file.write('\t')
			else:
				file.write('......\t')
				a3=1

			if i<len(self.row14):
				file.write(self.row14[i])
				file.write('\t')
			else:
				file.write('......\t')
				a4=1

			if i<len(self.row15):
				file.write(self.row15[i])
				file.write('\t')
			else:
				file.write('......\t')
				a5=1

			if i<len(self.row16):
				file.write(self.row16[i])
				file.write('\t')
			else:
				file.write('......\t')
				a6=1
			i=i+1
			file.write('\n')

		file.close()
	def get(self):
		# import seating as imp
		goo=[]
		
		goo.append(self.row11)
		goo.append(self.row12)
		goo.append(self.row13)
		goo.append(self.row14)
		goo.append(self.row15)
		goo.append(self.row15)
		goo.append(self.row16)
		print('\n\n\n\n\n\n\n\n',goo)
		# imp.invite(goo)
def classwise(sub_code):
	print("classwise")
	get=("SELECT rollno FROM student WHERE class=? ORDER BY rollno" )
	stu.execute(get,[(sub_code)])
	thislist=stu.fetchall()
	return thislist
	# mylist=change_to_list(year11)
def gatdata(sub_code):
	
	get=("SELECT rollno FROM student WHERE sub_code1=? or sub_code2=? or sub_code3=? or sub_code4=? or sub_code5=? or sub_code6=? ORDER BY rollno" )
	stu.execute(get,[(sub_code),(sub_code),(sub_code),(sub_code),(sub_code),(sub_code)])
	thislist=stu.fetchall()
	return thislist

def main(receive):
	# receive=['1CAA','1CAB','2CAA','2CAB','3CAA','3CAB']
	print('\n\n receive',receive,'\n\n')
	# user=input()
	global set1
	set1=receive
	seat=Divide_rolls()
	seat.convertFile()
	print("here")
	seat.get()
	os.startfile("seating.exe")
			# get=("SELECT rollno FROM student WHERE year=?" )
			# self.stu.execute(get,[(year)])
	conn.commit()
	conn.close()
