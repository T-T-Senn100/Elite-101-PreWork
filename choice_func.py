inventory = [
  {'product_id': 1112, 'type': 'Shoes', 'price': 35.00},
  {'product_id': 1122, 'type': 'Shirt', 'price': 12.00},
  {'product_id': 1222, 'type': 'Pants', 'price': 12.00},
  {'product_id': 2222, 'type': 'Math Textbooks', 'price': 41.00},  
  {'product_id': 2223, 'type': 'Phone Charger', 'price': 8.00},
]

def return_item(num):
    length = len(str(num))
    if length >= 5 or length <= 3:
        return "**INVALID ID NUMBER**"
    else:
        for index, product in enumerate(inventory):
            if inventory[index]["product_id"] == num:
                return inventory[index]["price"]

def exchange_item(num, num2):
    new_product = 0
    length = len(str(num))
    length2 = len(str(num2))
    if length >= 5 or length <= 3 or length2 >= 5 or length2 <= 3:
        return "**INVALID ID NUMBER**"
    else:
        for index, product in enumerate(inventory):
            if inventory[index]["product_id"] == num2:
                new_product = inventory[index]["price"]
        for index, product in enumerate(inventory):
            if inventory[index]["product_id"] == num:
                exchanged_product = inventory[index]["price"]
                return exchanged_product - new_product
                    
def display_inventory():
    for product in inventory:
        print('---------------------')
        for key, value in product.items():
            print(f"{key}: {value}")