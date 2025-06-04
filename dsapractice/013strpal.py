def strpal(s):
  s1=''
  for i in s:
    s1=i+s1
  if s==s1:
    return True
  else:
    return False
  
print(strpal("vishal"))