def oneton(n):
  if n==1:
    print(n)
    return 
  oneton(n-1)
  print(n)

oneton(5)