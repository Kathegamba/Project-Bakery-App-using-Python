
class Bakery:

    # Initialize categories 

    def __init__ (self, name, price, category):
        self.category = category
        self.name = name
        self.price = price
    

class Order:

    # Initialize the order with an empty list of products

    def __init__(self):
        self.products = []

    # Add the products

    def addProduct(self, product):
        self.products.append(product)

        print (f"{product.name} has been added to your order." )

    # Calculate the total price 

    def total(self):
        return sum(product.price for product in self.products)
    
    # Summary order 

    def order(self):
        if not self.products:

            print ("There are no products in your order.")
        
            return
        
        print ("\nThis is your order: ")

        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product.name} - ${product.price}")
        
        print (f"Total Order: ${self.total()}\n")

    
    # Checkout process

    def checkout(self):
        if not self.products:
            print("Your cart is empty. Please add products to your order.")

            return 
        
        self.order()

        clientConfirmation = input("Ready to checkout? (Yes / No): ").strip().lower()

        if clientConfirmation == 'yes':
            print("Your order has been comfirmed. Thank you!")

            self.products.clear()

        else:
            print("Your order has been cancelled.")

# Menu 

def main():
    menu = [
        Bakery ("Roll", 5.0, "Bread"),
        Bakery ("French", 7.5, "Bread"),
        Bakery ("7 grains", 10.0, "Bread"),

        Bakery ("Cinnamon", 3.0, "Cookies"),
        Bakery ("Chocolate", 5.0, "Cookies"),
        Bakery ("Oats", 8.0, "Cookies"),

        Bakery ("Coffee", 5.25, "Drinks"),
        Bakery ("Chocolate", 6.0, "Drinks"),
        Bakery ("Tea", 4.5, "Drinks"),
    ]

    order = Order()

    while True:
        print("*** BAKERY MENU ***")

        for i, product in enumerate(menu, 1):
            print(f"{i}. {product.name} - ${product.price}")

        print("A. View Order")
        print("B. Go to checkout")
        print("C. Exit")

        
        choice = input("Choose an option: ")

        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            order.addProduct(menu[int(choice) - 1])

        elif choice == 'A':
            order.order()

        elif choice == 'B':
            order.checkout()
        
        elif choice == 'C':
            print("Thank you! Have a wonderful day!")

            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




