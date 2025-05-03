#student system

def add_student():
  student_id=int(input('enter a serial number:'))
  fname=input('enter first name:')
  lname=input('enter last name:')
  contact=int(input('enter a contact number:'))
  student.update({student_id:{'fname':fname,'lname':lname,'contact':contact,'subject':subject}})
  total_sub=int(input("enter a total subject:"))
  for i in range(1,total_sub+1):
    sub=input('enter a subject name:')
    marks=0
    fees=int(input('enter a fees:'))
    subject.update({sub:{'marks':marks,'fees':fees}})  
    
def remove_student():
  student_id=int(input("Enter a Serial Number:"))
  student.pop(student_id)

def view_all_student():
  for i in student.items():
    print(i)
    
def view_specific_student():
  student_id=int(input("Enter a Serial Number:"))
  if student_id in student.keys():
    print(student[student_id])
  else:
    print("this student id is not valid")
    
def counsellor():
  print('1.Add Student')
  print('2.Remove Student')
  print('3.view All Student')
  print('4.View Specific Student')
  choice_councellor=int(input("Enter Choice by counsellor"))
  if choice_councellor==1:
    add_student()
  elif choice_councellor==2:
    remove_student()
  elif choice_councellor==3:
    view_all_student()
  elif choice_councellor==4:
    view_specific_student()
  else:
    print('wrong choice')
    
def faculty():
  print('1.add marks to student')
  print('2.view all student')
  choice_faculty=int(input("enter a choice by faculty:"))
  if choice_faculty==1:
    student_id=int(input('enter student id :'))
    sub_marks=input('enter subject to add marks:')
    marks=int(input(f"enter a {sub_marks} marks "))
    if sub_marks in subject:
      subject[sub_marks]=marks
    else:
      print('this subject not availabe in this student')
  elif choice_faculty==2:
    view_all_student()
    
def student():
  pass


student={}
subject={}
again=None
while again != 'n':
  print('press 1 for Counsellor')
  print('press 2 for Facultiy')
  print('press 3 for Student')
  choice=int(input("enter a role ID:"))
  if choice==1:
    repeat=None
    while repeat != 'n':
      counsellor()
      repeat=input("counsellor want to perform more operations?(y/n):")
  elif choice==2:
    repeat=None
    while repeat != 'n':
      faculty()
      repeat=input("faculty want to perform more operations?(y/n):")
  elif choice==3:
    repeat=None
    while repeat != 'n':
      student()
      repeat=input("student want to perform more operations?(y/n):")
  else:
    print('wrong choice please select 1 to 3')
  again=input("press (y) for repeat or (n) for exit.(y/n):")