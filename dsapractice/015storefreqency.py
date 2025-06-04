l=[5,4,7,8,5,3,2,1,4,5,6,3,2,1]
d={}
for i in l:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
print(d)