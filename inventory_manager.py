class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} - {self.quantity} units - ${self.price:.2f} each"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = product

    def inventory_value(self):
        return sum(p.total_value() for p in self.products.values())

    def show_inventory(self):
        for p in self.products.values():
            print(p)

if __name__ == "__main__":
    inv = Inventory()
    inv.add_product(Product("Laptop", 1000, 3))
    inv.add_product(Product("Mouse", 50, 10))
    inv.show_inventory()
    print("Total Value:", inv.inventory_value())
