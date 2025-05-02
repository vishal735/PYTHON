n=int(input("enter a number:")) #547
org=n
rev=0

while org>0:
  rem=org%10 #547%10 = 7
  rev=rev*10+rem #0+70+7
  org=org//10

if n==rev:
  print("palindrome")
else:
  print("not a palindrome")