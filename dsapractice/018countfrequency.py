arr=[3, 3, 3, 3]
extra=[0]*len(arr)
for i in arr:
  extra[i-1]+=1
print(extra)