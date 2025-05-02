from math import *
def countDigits(num):
  return int(log10(num)+1)

num=int(input("enter a number:"))
cnt=countDigits(num)
print(cnt)