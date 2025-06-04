n=int(input("enter a number to check armstrong or not:"))
org=n
total=0
while org != 0:
  rem = org % 10
  total=total+(rem**len(str(n)))
  org//=10
if n==total:
  print("number is armstrong")
else:
  print("number is not amrstrong")