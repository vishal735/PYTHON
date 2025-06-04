l=[1,1,1,2,2,2,3,5,5,7,8,8,9,9]
d={}
for i in l:
  if i not in d:
    d[i]=0

j=0
for k in d:
  l[j]=k
  j+=1
print(l)
print(j)