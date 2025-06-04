l=[5,4,8,6,3,25,41,23,5,4,2,3,65,1]

for i in range(0,len(l)-1):
  for j in range(i+1,len(l)):
    if l[i] > l[j]:
      l[i],l[j]=l[j],l[i]
print(l)