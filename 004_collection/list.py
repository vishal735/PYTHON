# a=[10,20,30,40,50]
# print(a)
# print(len(a))
# print(type(a))

# thelist=list((10,20,30,40,50))
# print(thelist)

# accsess specifier
# l=[10,20,30,40,50]
# print(l)
# print(l[0])
# print(l[-1])
# print(l[:3])
# print(l[-4])
# print(l[1:3])
# print(10 in l)

#change list item
# l[1]='vishal'
# l[1:3]=['vishal','sagar','ankit']
# l.insert(1,'A')
# print(l)


#add list item
# l.append("visal")
# print(l)

#extend list
# ex=['vishal','sagar','ankit']
# l.extend(ex)
# l.extend('hello') #h e l l o iterate
# print(l)

#remove item in list
# l.remove(10)
# l.pop(3)
# l.clear()
# del l
# print(l)


#list with for loop
# for i in l:
#   print(i)

# for i in range(len(l)):
#   print(l[i])
  
# sort list
a=[1,5,3,4,8,3]
# a.sort()
# a.reverse()
# b=list(a)
b=a.copy()
b=a
print(b)
print(a)