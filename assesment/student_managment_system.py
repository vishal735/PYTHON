student={}
again=None
choice=int(input("enter a role ID:"))
print('press 1 for Counsellor')
print('press 2 for Facultiy')
print('press 3 for Student')

if choice==1:
  while again != 'n':
    print('1.Add Student')
    print('2.Remove Student')
    print('3.view All Student')
    print('4.View Specific Student')
    choice_councellor=int(input("Enter Choice by counsellor"))
    if choice_councellor==1:
        student_id=int(input("Enter a Serial Number:"))
        first_name=input("Enter a first name:")
        last_name=input("Enter a last name:")
        contact_no=int(input("Enter a contact number:"))
        subject={}
        student.update({student_id:{'fname':first_name,'lname':last_name,'contact':contact_no,'subject':subject}})
        total_sub=int(input("enter total subject:"))
        for i in range(1,total_sub+1):
          sub=input("Enter a Subject:")
          marks=int(input("Enter a Marks:"))
          fees=int(input("Enter a Fees:"))
          subject.update({sub:{'marks':marks,'fees':fees}})
    elif choice_councellor==2:
      student_id=int(input("Enter a Serial Number:"))
      student.pop(student_id)
    elif choice_councellor==3:
      for i in student.items():
        print(i)
    elif choice_councellor==4:
          student_id=int(input("Enter a Serial Number:"))
          if student_id in student.keys():
            print(student[student_id])
          else:
            print("this student id is not valid")
    else:
      print("please choose 1 to 4")
    again=input("do yo want to perform more operations?(y/n):")
elif choice==2:
  print('1.add marks to student')
  print('2.view all student')
  choice_faculty=int(input("enter a choice by faculty:"))
  if choice_faculty==1:
    student_id=int(input("enter a student id to update marks:"))
    
  elif choice_faculty==2:
    student_id=int(input("Enter a Serial Number:"))
    if student_id in student.keys():
      print(student[student_id])
    else:
      print("this student id is not valid")
  else:
    print("invalid choice")
print(student)