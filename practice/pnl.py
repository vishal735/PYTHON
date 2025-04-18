cost=int(input("enter total cost of product:"))
sell=int(input("enter sell price:"))

if(cost > sell):
  print(f"total loss is {cost-sell}")
elif(sell > cost):
  print(f'total profit is {sell-cost}')
else:
  print("no profit no loss")
