email=input("enter your email L") 
extra=0
if len(email)>=6:
  if '@' in email and email.count('@')==1:
    if email[0].isalpha():
      if (email[-4]=='.') ^ (email[-3]=='.'):
        for i in email:
          if i==' ':
            extra=extra+1
          
        if extra ==0:
          print("right email")
        else:
          print("wrong email 5")
      else:
        print("wrong email 4")
    else:
      print("wrong email 3")
  else:
    print("wrong email 2 ")
else:
  print("wrong email 1")