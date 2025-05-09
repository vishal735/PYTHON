questions=[]
  
  
# welcome()
def quiz_master():
  
  operation=None
  while operation !=4:
    print("SHAKE YOUR BRAIN AND ADD SOME CHALLENGING QUESTIONS..")
    print("\t\t MENU")
    print("\t press 1 for add question")
    print("\t press 2 for view question")
    print("\t press 3 for delete question")
    print("\t press 4 for exit")
    operation=int(input("which operations you want to perform:"))
    if operation ==1:
      question()
    elif operation==2:
      view_quesiton()
    elif operation==3:
      delete_question()
    elif operation==4:
      print("thank you for visit")
    else:
      print("wrong input")
    


def question():
  t=int(input("enter total question:"))
  for q in range(1,t+1):
    option=[]
    question=input('enter question:')
    total_op=int(input("enter a total option:"))
    for i in range(1,total_op+1):
      op=input(f'enter a option {i}:')
      option.append(op) 
    ans=input("enter answer")
    questions.append({'question':question,'option':option,'ans':ans})
   
def view_quesiton():
  for i in questions:
    print(f' question. {i['question']}')
    print(f'option :{i['option']}')  
    print(f'ans:{i['ans']}')
     
    
def delete_question():
  delete=int(input("enter delete question number:"))
  del questions[delete]
  
print('''\t WELCOME TO TOPS QUIZ GAMING CHALLENGE
        \n\t select your role:
        \n\t\t ->Quiz Master \t(press 1)
        \n\t\t ->Quiz Cracker \t(press 2)
        ''')
role=int(input("Enter Your Role:"))
if role ==1:
  quiz_master()
elif role ==2:
  pass
else:
  print("wrong input")
