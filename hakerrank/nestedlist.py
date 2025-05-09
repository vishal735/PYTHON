n=int(input())
l=[]
for i in range(n):
  name=input()
  marks=float(input())
  l.append([name,marks])
second_highest=sorted(set([marks for name,marks in l]))[1]
print('\n'.join(sorted([name for name, marks in l if marks == second_highest])))