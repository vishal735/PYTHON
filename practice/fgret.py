n1=int(input("enter a first number:"))
n2=int(input("enter a second number:"))
n3=int(input("enter a third number:"))
n4=int(input("enter a fourth number:"))
if n1 >n2 and n1 >n3 and n1>n4:
  print(f"{n1} is gretest number")
elif n2 >n1 and n2 >n3 and n2>n4:
  print(f'{n2} is gretest number')
elif n3 >n1 and n3 >n2 and n3>n4:
  print(f'{n3} is gretest number')
else:
  print(f'{n4} is gretest number')