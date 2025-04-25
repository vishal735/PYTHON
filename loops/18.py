for i in range(1,11):
  for j in range(1,11):
    if (i==5 or j==5):
      print("* ",end="")
    else:
      print("  ",end="")
  print()