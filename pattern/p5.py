extra=1
for i in range(1,6):
  for j in range(1,i+1):
    print(chr(64+extra),end="")
    extra=extra+1
  print()