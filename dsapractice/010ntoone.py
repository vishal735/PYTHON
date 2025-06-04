def ntoone(n):
  if n==1:
    print(n)
    return
  print(n)
  ntoone(n-1)
ntoone(5)