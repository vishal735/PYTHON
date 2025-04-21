number=int(input("enter a number to convert decimal to octalL:"))
octal=0
mul=1
while number!=0:
  rem=number%8
  octal=octal+(rem*mul)
  number//=8
  mul=mul*10
print(octal)