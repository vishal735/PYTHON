for i in range(1,6):
  for k in range(6-i):
    print(" ",end="")
  for j in range(2,i+1):
    print((i+2)-j,end="")
  for n in range(1,i+1):
    print(n,end="")
  print()