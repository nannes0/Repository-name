"""
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 400)

book1.show_info()
print()

book2.show_info()
"""

"""
class TemperatureSensor:
    def __init__(self, location, temperature):
        self.location = location
        self.temperature = temperature

    def increase_temperature(self):
        self.temperature += 1

    def decrease_temperature(self):
        self.temperature -= 1

    def show_temperature(self):
        print(self.location + ":", self.temperature, "degrees")


sensor1 = TemperatureSensor("Kitchen", 20)
sensor2 = TemperatureSensor("Bedroom", 22)

sensor1.increase_temperature()
sensor1.increase_temperature()

sensor2.decrease_temperature()

sensor1.show_temperature()
sensor2.show_temperature()
"""

"""
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self):
        if self.stock > 0:
            self.stock -= 1
        else:
            print("Product is out of stock!")

    def show_info(self):
        print("Product:", self.name)
        print("Price:", self.price, "kr")
        print("Stock:", self.stock)

    def restock(self, amount):
        self.stock += amount


product1 = Product("Keyboard", 399, 10)

product1.sell()
product1.sell()

product1.restock(5)

product1.show_info()
"""