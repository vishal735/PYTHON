n1=int(input("enter a first number:"))
n2=int(input("enter a second number:"))
n3=int(input("enter a third number:"))

if n1 >n2 and n1 >n3:
  print(f"{n1} is gretest number")
elif n2 >n1 and n2 >n3:
  print(f'{n2} is gretest number')
else:
  print(f'{n3} is gretest number')