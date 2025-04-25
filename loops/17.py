for i in range(1,11):
  if(i%2==0):
    print(f'{i}'*i)
  else:
    print(f'{chr(64+i)}'*i)