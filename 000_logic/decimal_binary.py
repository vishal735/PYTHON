#38
#38/2
n=int(input("enter a decimal number to convert binary format:")) #38
ans=''
while n!=2:
  if(n%2==0): #38/2
    ans=ans+'0'
    n=n//2
  elif(n%2==1):
    ans=ans+'1'
    n=n//2
print(ans)