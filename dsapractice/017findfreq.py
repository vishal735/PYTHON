l=[11,2,5,4,3,22,6,2,1,2,5]

a=int(input("enter a number"))
d={}
for i in l:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
print(f'frequency of {a} is {d[a]}')