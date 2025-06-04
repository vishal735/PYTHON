l=[5,6,7,6,8,9]

def checksort(l):
  for i in range(0,len(l)-1):
    if l[i] > l[i+1]:
      return False
  return True
print(checksort(l))