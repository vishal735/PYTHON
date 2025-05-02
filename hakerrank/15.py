n=int(input())
m=int(input())
hlf=m//2
for i in range(1,n+1):
  for j in range(1,m+1):
    if j==hlf:
      print("|",end="")
    
    else:
      print("-",end="")
  print()