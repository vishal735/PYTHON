n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

print('\n1.addition\n2.subtraction\n3.multiplication\n4.division')
print('select your choice:')
choice=input("Enter your choice 1 to 4:")
if choice=='1':
  print(f'addition of {n1}+{n2}={n1+n2}')
elif choice=='2':
  print(f'subtraction of {n1}-{n2}={n1-n2}')
elif choice=='3':
  print(f'multiplication of {n1}*{n2}={n1*n2}')
elif choice=='4':
  print(f'division of {n1}/{n2}={n1/n2}')
else:
  print("wrong choice please enter 1 to 4")