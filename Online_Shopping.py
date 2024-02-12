class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.name} - ${self.price} - Quantity: {self.stock_quantity}"

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product, quantity):
        if product in self.items:
            self.items[product] -= quantity
            if self.items[product] <= 0:
                del self.items[product]

    def get_total_price(self):
        total_price = 0
        for product, quantity in self.items.items():
            total_price += product.price * quantity
        return total_price

    def __str__(self):
        output = "Shopping Cart:\n"
        for product, quantity in self.items.items():
            output += f"{product} - Quantity: {quantity}\n"
        output += f"Total Price: ${self.get_total_price()}"
        return output

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.order_history = []

    def add_to_order_history(self, order):
        self.order_history.append(order)

    def __str__(self):
        return f"Username: {self.username}, Order History: {self.order_history}"

# Example usage:
if __name__ == "__main__":
    # Create some products
    product1 = Product("Laptop", 999, 10)
    product2 = Product("Phone", 699, 20)

    # Create a shopping cart
    cart = ShoppingCart()
    cart.add_item(product1, 2)
    cart.add_item(product2, 1)

    # Create a user
    user = User("user1", "password")

    # Add cart to user's order history
    user.add_to_order_history(cart)

    # Print user's order history
    print(user)
