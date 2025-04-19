n=int(input("enter a number:"))
st=''
while n!=0:
  rem=n%8
  print(rem)
  st=str(rem)+st
  
  n=n//8
print(st)
  