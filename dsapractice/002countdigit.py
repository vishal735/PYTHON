n=int(input("enter a number to find count of digit:"))
org = n
total=0
while org !=0:
  total=total+1
  org//=10
print(total)