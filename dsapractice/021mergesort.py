def mergearr(l,r):
  result=[]
  i,j=0,0
  n=len(l)
  m=len(r)
  while i < n and j < m :
    if l[i] <= r[j]:
      result.append(l[i])
      i+=1
    else:
      result.append(r[j])
      j+=1
  if i < n:
    while i < n:
      result.append(l[i])
      i+=1
  if j < m :
    while j < m:
      result.append(r[j])
      j+=1
  return result

def mergesort(arr):
  if len(arr) <= 1 :
    return arr
  mid = len(arr)//2
  left_arr=arr[mid:]
  Right_arr=arr[:mid]
  left=mergesort(left_arr)
  right=mergesort(Right_arr)
  return mergearr(left,right)

l=[5,4,6,3,2,1,4,775,6,5,3]
o=mergesort(l)
print(o)
