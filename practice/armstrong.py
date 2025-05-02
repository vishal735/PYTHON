n=int(input())
org=n
sum=0

while org!=0:
  rem= org%10
  sum=sum+rem**len(str(n))
  org=org//10
print(sum)

if n==sum:
  print('palindrome')
else:
  print("not a palindrome")