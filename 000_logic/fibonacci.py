number=int(input("enter a number to print fib serires:"))
n1=0
n2=1
nextterm=n1+n2
print("fibonacci series 0 1 ",end="")
for i in range(number):
  print(nextterm,end=" ")
  n1=n2
  n2=nextterm
  nextterm=n1+n2