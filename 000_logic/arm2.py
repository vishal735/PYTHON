number=int(input("enter a number to check its armstrong or not:")) #153
temp=number
sum=0
while number != 0:
  rem=number%10  #3
  count=rem * rem * rem
  sum=sum+count
  number=number//10
  
if(temp==sum):
  print("number is armstrong")
else:
  print("number is not armstrong")