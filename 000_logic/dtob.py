number=int(input("enter a number to convert decimal to binary:"))
binary=0
multiplyer=1
while number !=0:
  rem=number%2
  binary=binary+(rem*multiplyer)
  number//=2
  multiplyer*=10
  
print(binary)