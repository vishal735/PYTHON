l=[]
counter={}
x=int(input("enter the number of shoes:"))
x2=input().split()
l.append(x2)
print(l)
n=int(input("number of customers:"))
for i in range(1,n+1):
  n2=input().split()
  counter.update({n2})
  