n=int(input("enter a numbe to check prime or not"))

flag=True

if n==0 or n==1 :
  print("number is not prime")
else:
  for i in range(2,n):
    if n%i==0:
      flag=False
      
if flag:
  print("prime number")
else:
  print("not prime")