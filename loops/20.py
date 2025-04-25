
for i in range(0,6):
  for j in range(0,6):
    if i==j or i==6-1-j:
      print("*",end="")
    else:
      print(' ',end="")

  print()
  