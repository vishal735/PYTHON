n=input("enter a binary number:")
lOfn=len(n)
decimal=0
for i in n:
  a=int(i)
  decimal=decimal+(a*(2**(lOfn-1)))
  lOfn=lOfn-1
  
print(decimal)  