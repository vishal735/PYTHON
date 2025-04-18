#cafe managment system

menu={
  'Pizza':150,
  'Burger':90,
  'Sandwich':50,
  'Cold-drink':20,
  'Tea':30,
  'Coffe':40
  }


orders=[]

def show_menu():  
 
  print('\t Menu')
  for item,price in menu.items():
    print(f'{item}: RS-{price}')

def take_order():
  #order for user
  order=input("\nEnter item to order (or type 'done' to finish): ")
  while order !="Done":
    if order in menu:
      qty=int(input(f"Enter quantity of {order}: "))
      orders.append((order,qty))
    else:
      print("item not in menu")
    order = input("\nEnter next item (or 'done' to finish): ")
    
def calculate_bill():
  #order summury
  total_order=0
  print('-----Order Summury-----')
  for item,qty in orders:
    price=menu[item]
    cost=price * qty
    total_order=total_order+cost
    print(f'{item} X {qty}=RS{cost}')
  print(f"Total Bill : RS{total_order}")
  
def main():
   print("------Welcome to Unique Cafe------")
   
   while True:
      print("\nOptions: [1] Show Menu  [2] Take Order  [3] Calculate Bill  [4] Exit")
      choice = input("Select an option: ")
      if choice == '1':
          show_menu()
      elif choice == '2':
          take_order()
      elif choice == '3':
          calculate_bill()
      elif choice == '4':
          print("Thank you! Visit again.")
          print(orders)  
          break
      else:
          print("Invalid choice.")
  
if __name__ == "__main__":
    main()