n=int(input("enter number to check palindrome or not:"))
rev=0
org=n
while org != 0:
  rem=org%10
  rev=rev*10+rem
  org//=10
if n==rev:
  print("number is palindrome")
else:
  print("number is not palindrome")