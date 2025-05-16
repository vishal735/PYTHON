# Write a Python program to merge two lists into one dictionary using a loop.
dict={}
keys=[1,2,3]
value=["a","b","c"]
le=len(keys)

for i in range(le):
  dict[keys[i]]=value[i]
print(dict)