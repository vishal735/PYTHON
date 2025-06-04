l=[9,7,6,8,4,3,5,2,1]

for i in range(len(l)-1,-1,-1):
  for j in range(0,i):
    if l[i] < l[j]:
      l[i],l[j]=l[j],l[i]
  print(l)