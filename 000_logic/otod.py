n=input("enter a octal number TO CONVERT DECIMAL:")
lofn=len(n)
hexa=0
for i in n:
  a=int(i)
  hexa=hexa+(a*(8**(lofn-1)))
  lofn=lofn-1
 
print(hexa) 
