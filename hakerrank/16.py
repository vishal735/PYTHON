x=int(input())

x1=list(map(int,input().split()))
arr1=set(x1)
arr2=sorted(arr1)
print(arr2[-2])