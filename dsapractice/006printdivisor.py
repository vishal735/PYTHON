import math
n=int(input("enter a number to print divisor"))
l=[]
for i in range(1,int(math.sqrt(n))+1):
  if n%i == 0:
    l.append(i)
    l.append(n//i)
print(l)