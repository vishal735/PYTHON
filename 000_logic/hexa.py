n=int(input("enter a number:"))
extra=''
while n!=0:
  rem=n%16
  if rem > 9:
    print(chr(55+rem))
    extra=chr(55+rem)+extra
  else:
    print(rem)
    extra=str(rem)+extra
  n=n//16
print(extra)