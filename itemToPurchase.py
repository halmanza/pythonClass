class ItemToPurchase:
  item_name= str()
  item_price= float()
  item_quantity = int()

  def __init__(self,item_name="none",item_price= 0,item_quantity= 0):
    self.item_name= item_name
    self.item_price= item_price
    self.item_quantity=item_quantity
    return

  def print_item_cost(self):
     x= self.item_quantity * self.item_price
     print('{} {} @ ${:.0f} = ${:.0f}'.format(self.item_name,int(self.item_quantity),int(self.item_price), x))   
    
    
    

def process():
    item1=ItemToPurchase()
    item2=ItemToPurchase()
    
    """ Hi professor,
     I was curious if there's a more
    elegant solution to implement the same function without using two for loops?
    I was initally thinking a dictionary would make this simpler, but then realized I could create different
    class instances to act as key-value pairs. I'd appreciate any suggestions, Thank you! """

    for r in range(0,1):
      print('Item {}'.format(r + 1))
      user_entry= input('Enter the item name: \n')
      print()
      item1.item_name = user_entry
      price_input=input('Enter the item price: \n')
      item1.item_price= float(price_input)
      quantitiy_input=input('Enter the item quantity: \n')
      item1.item_quantity= int(quantitiy_input)
      print()

      for s in range(0,1):
        print('Item {}'.format(r + 2))
        user_entry= input('Enter the item name: \n')
        print()
        item2.item_name = user_entry
        price_input=input('Enter the item price: \n')
        item2.item_price= float(price_input)
        quantitiy_input=input('Enter the item quantity: \n')
        item2.item_quantity= float(quantitiy_input)
        print()
        
    print('TOTAL COST \n')    
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    total_price= (item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price)
    print('Total: ${:.0f}'.format(total_price))


      
      
process()

    
     