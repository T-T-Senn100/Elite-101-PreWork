print("Welcome to the Elite 101 Chatbot!")
name = input("Please enter your name: ")
age = input("Hello "+name+", how old are you? ")
print("Welcome "+name+". We're both "+age+"! What can I do for you? ")
print("")

talk_to_chatbot = True

while talk_to_chatbot:
    print("-------------------------------")
    print("Please Choose From the Following Options:")
    print("1. Placeholder Option 1")
    print("2. Placeholder Option 2")
    print("3. Placeholder Option 3")
    print("4. Exit")
    print("-------------------------------")
    print()

    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        print("Placholder 1")
    elif user_choice == 2:
        print("Placholder 2")
    elif user_choice == 3:
        print("Placholder 3")
    elif user_choice == 4:
        talk_to_chatbot = False

print("Goodbye "+name+"! Cya Soon!")

# From Stack Overflow https://stackoverflow.com/questions/1077347/hello-world-in-python/1124893
