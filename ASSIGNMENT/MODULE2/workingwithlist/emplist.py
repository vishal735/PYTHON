# 6) Write a Python program to insert elements into an empty list using a for loop and append().

l=[]

while True:
  inp =input("enter a element to append list (or press e for exit):")
  l.append(inp)
  if inp == 'e':
    break
print(l)