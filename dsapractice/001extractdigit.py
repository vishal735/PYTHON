n=int(input("enter a number to extract digit:"))
org=n
while org !=0:
  rem=org%10
  print(rem)
  org=org//10