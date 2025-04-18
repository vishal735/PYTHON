number=int(input("enter a number"))

fact=1
# for i in range(number,0,-1):
#   fact=fact*i
# print(fact)

while number!=0:
  fact=fact*number
  number=number-1
  
print(fact)
