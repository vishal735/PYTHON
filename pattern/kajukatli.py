#   *
#  * *
# * * *
#  * *
#   * 
a=int(input("enter row:"))
row=a//2
for i in range(row,0,-1):
  # print(i)
  print(" "*i ," *"*((row+1)-i))
for j in range(1,row):
  print(" "*(j+1)," *"*(row-j))

 
