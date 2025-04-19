#38
#38/2
n=int(input("enter a decimal number to convert binary format:")) #38
ans=''
while n!=0:
  if(n%2==0): #453/2
    ans='0'+ans
    print(n)
    n=n//2
  else:
    ans='1'+ans
    print(n)
    n=n//2
print(ans)