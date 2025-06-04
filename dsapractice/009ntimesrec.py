def ntimes(s,n):
  if n==1:
    print(s)
    return
  print(s)
  ntimes(s,n-1)
  
ntimes("vishal",5)