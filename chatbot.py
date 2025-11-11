from choice_func import return_item
from choice_func import exchange_item
from choice_func import display_inventory

print("Welcome to the Elite 101 Chatbot Retail Store!")
name = input("Please enter your name: ")
#age = input("Hello "+name+", how old are you? ")
print("Welcome "+name+"! What can I do for you? ")
print("")

talk_to_chatbot = True

while talk_to_chatbot:
    print("-------------------------------")
    print("Please Choose From the Following Options:")
    print("1. Return an Item")
    print("2. Exchange an Item")
    print("3. Exit")
    print("-------------------------------")
    print()

    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        returning_item = True
        while returning_item:
            id_num = int(input("Type the ID of the product you wish to return: "))
            refund = return_item(id_num)
            print("Your product has been returned! Your $"+str(refund)+" has been refunded!")
            print()
            second_choice = input("Would you like to return anything else(yes or no)?: ")
            if second_choice.lower() == "no":
                returning_item = False
            elif second_choice.lower() == "yes":
                returning_item = True
    elif user_choice == 2:
        id_num = int(input("Type the ID of the product you wish to exchange: "))
        display_inventory()
        new_product = int(input("What product would you like exchange for(input the ID)?: "))
        exchange_done = exchange_item(id_num, new_product)
        if exchange_done > 0:
            print("Product exchange made! We have refunded you the extra remaining $"+str(exchange_done))
        elif exchange_done <= 0:
            dummy_var = -1
            money_owe = exchange_done * dummy_var
            print("Product exchange made! You owe $"+str(money_owe))
    elif user_choice == 3:
        talk_to_chatbot = False
    print()

print("Goodbye "+name+"! Hope To See You Soon!")

# From Stack Overflow https://stackoverflow.com/questions/1077347/hello-world-in-python/1124893
