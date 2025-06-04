def fibo(n):
  if n==0:
    return n
  return fibo(n)+fibo(n-1)

print(fibo(5))