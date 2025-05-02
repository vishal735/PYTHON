# Write a Python program to check if a number is prime using if_else.
number=int(input("enter a number:"))
for i in range(2,number):
  if number%i!=0:
    print("number is prime")
    break
  else:
    print("number is not prime")
    break