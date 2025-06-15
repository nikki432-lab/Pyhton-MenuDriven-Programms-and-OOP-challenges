import uuid

TAX_RATE = 0.18
SHIPPING_FLAT_RATE = 50

class Product:
    def __init__(self, name, price, discount = 0):
        self.name = name 
        self.price = price
        self.discount = discount

    def get_final_price(self):
        return self.price * (1- self.discount / 100)
    
class inventory:
    def __init__(self):
        self.products= []
    
    def add_product(self, product):
        self.products.append(product)
    
    def display_products(self):
        for idx, p in enumerate(self.products):
            print(f"{idx + 1}.{p.name}= ${p.price:.2f} ({p.discount}%off)")

    def get_product(self, index):
        if 0 <= index < len(self.products):
            return self.products[index]
        return None
    
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def view_cart(self):
        if not self.items:
            print("Cart is empty..")
            return
        for idx, item in enumerate(self.items, 1):
            print(f"{idx}.{item.name} - ${item.get_final_price():.2f}")

    def calculate_total(self):
        subtotal = sum(item.get_final_price() for item in self.items)
        tax = subtotal + TAX_RATE
        total = subtotal + tax + SHIPPING_FLAT_RATE
        return subtotal, tax, SHIPPING_FLAT_RATE, total
    
    def checkout(self):
        subtotal, tax, shipping, total = self.calculate_total()
        order_id = str(uuid.uuid4())[:8]
        print(f"\n Order ID : {order_id}")
        print(f"subtotal: ${subtotal:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Shipping: ${shipping:.2f}")
        print(f"Total: ${total:.2f}")
        print("Order Placed Successfully: \n")
        self.items = []

class shipping:
    def __init__(self, address):
        self.address = address
    
    def calculate_shipping(self):
        return SHIPPING_FLAT_RATE
    
class order:
    def __init__(self, cart, customer_name, address):
        self.order_id = str(uuid.uuid4())[:8]
        self.items = cart.items[:]
        self.customer_name = customer_name
        self.address = address
        self.shipping = shipping(address).calculate_shipping()
        self.subtotal, self.tax, _ ,_ = cart.calculate_total()
        self.total = self.subtotal + self.tax + self.shipping

    def display_order_summary(self):
        print(f"\n order summary (order ID: {self.order_id})")
        print(f" customer: {self.customer_name}")
        print(f"shipping address: {self.address}\nItems: ")
        for item in self.items:
            print(f" - {item.name}: ${item.get_final_price():.2f}")
        print(f"subtotal: ${self.subtotal:.2f}")
        print(f"tax(18%): {self.subtotal:.2f}")
        print(f"Shipping: ${self.shipping:.2f}")
        print(f"total: ${self.total:.2f}")
        print("Order placed Successfully!")

def main():
    inv = inventory()
    cart = Cart()

    inv.add_product(Product("wireless Mouse", 799, 10))
    inv.add_product(Product("Keyboard", 1200, 5))
    inv.add_product(Product("Smart Watch", 2999, 5))

    while True:
        print("\n---E-Commerce Platform---")
        print("1.Browse Products.\n2. Add to cart.\n3. View cart.\n4. Checkout.\n5. Exit.")

        choice = input("Select an option: ")

        if choice == '1':
            inv.display_products()

        elif choice == '2':
            inv.display_products()
            try:
                selection = int(input("Enter product number to add to cart: ")) - 1
                product = inv.get_product(selection)
                if product:
                    cart.add_item(product)
                    print(f"{product.name} added to cart.")
                else:
                    print("Invalid option.")
            except ValueError:
                print("please enter a valid number.")

        elif choice == '3':
            cart.view_cart()

        elif choice == '4':
            cart.view_cart()
            if cart.items:
                confirm = input("Proceed to Checkout? (yes/no): ").lower()
                if confirm == 'yes':
                    name = input("Enter your name: ")
                    address = input("Enter your address: ")
                    Order = order(cart, name, address)
                    Order.display_order_summary()
                    cart.items.clear()

        elif choice == '5':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()




