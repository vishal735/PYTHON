l=[5,4,6,3,2,1,7,8,5,6,3,2,4]
large=l[0]
secondlarge=l[0]

for i in l:
  if i > large:
    large=i
for i in l:
  if i < large and i > secondlarge:
    secondlarge=i
print(secondlarge)