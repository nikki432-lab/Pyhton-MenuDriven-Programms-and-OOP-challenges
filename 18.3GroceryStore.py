class Grocerystore:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price):
        if item in self.cart:
            self.cart[item]['quantity'] += 1

        else:
            self.cart[item] = {'price': price, 'quantity': 1}
            print(f"{item} added to cart.")

    def remove_item(self, item):
            if item in self.cart:
                if self.cart[item]['quantity'] > 1:
                    self.cart[item]['quantity'] -= 1
                else:
                    del self.cart[item]
                    print(f"{item} removed from cart.")
            else:
                print("Item not found in cart.")
        
    def view_total(self):
        total = sum(details['price'] * details['quantity'] for details in self.cart.values())
        print(f"Total price ; {total:.2f}")

    def display_cart(self):
        if not self.cart:
            print("your cart is empty.")
        else:
            print("\nItems in your cart.")
            for item, details in self.cart.items():
                print(f"{item}: {details['price']} x {details['quantity']}")

def main():
    store = Grocerystore()

    while True:
        print("\nGrocery Store Menu")
        print("1. Add item")
        print("2. Remove item")
        print("3. View Total Price")
        print("4. Display cart")
        print("5. Exit")

        choice = input("Enter your choice(1-5): ")

        if choice == '1':
            item = input("Enter item name: ")
            price = float(input("Enter item price: "))
            store.add_item(item, price)
        
        elif choice == '2':
            item = input("Enter item name to remove: ")
            store.remove_item(item)
        
        elif choice == '3':
            store.view_total()

        elif choice == '4':
            store.display_cart()
        
        elif choice == '5':
            print("Thank You for shopping with us. Goodbye!")
            break
        else:
            print("Invalid choice please select a valid option.")

if __name__ == "__main__":
    main()

