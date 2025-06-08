def menu():
    print("Welcome to the Menu-Driven Program!")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print("You selected Option 1.")
    elif choice == '2':
        print("You selected Option 2.")
    elif choice == '3':
        print("You selected Option 3.")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")