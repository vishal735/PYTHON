n=int(input())
l=[]
for i in range(n):
  name=input()
  marks=float(input())
  l.append([name,marks])
  
l.sort()
print(l[1])


  