n=int(input("enter a number to reverse :"))
rev=0
org=n
while org != 0:
  rem=org%10
  rev=rev*10+rem
  org//=10
print(rev)