n=int(input("enter a year"))

if(n%4==0 or n%100!=0) or (n%400==0):
  print("this year is leap year")
else:
  print("this year is not leap year")