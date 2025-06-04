
items={}
total=0
while True:
  item=input("enter item name and press (q) for exit:")
  if item=='q':
    break
  else:
    price=int(input("enter item price:"))
    items.update({item:price})
    total=total+price
 
print("-------your bill--------")   
print('item \t price')
for i in items.keys():
  print(f'{i}  {items[i]}')
print("------------------------")
print(f'your total bill : {total}')