class Product: #Class definition
    def __init__(self, name, price, quantity): #initialization
        if  not isinstance(name, str) or not name:
            raise Exception("Name cannot be empty or has to be instance of string")
        if not isinstance(price, (int, float)) or price < 0:
            raise Exception("Price must be a positive number (int or float)")
        if not isinstance(quantity, int) or quantity < 0:
            raise Exception("Quantity must be a non-negative integer")
        #static and dynamic Instance variable and parameter:
        self.name = name
        self.price = price
        self.quantity = quantity  #self.quantity = Mac, quantity = 3(Anzahl)->Eigenschaft
        self.active = True


    def get_quantity(self) -> int:
        """returns the actual number of products in stock"""
        return self.quantity

    def set_quantity(self, quantity):
        """sets a new quantity, raise Exception if quantitie is negative, if quantity reaches 0, product becomes inactive"""
        if self.quantity < 0:
            raise Exception("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """returns a boolean True when product is active, otherwise False"""
        return self.active

    def activate(self):
        """activates the product -> sets active to True"""
        self.active = True

    def deactivate(self):
        """deactivates the product -> sets active to False"""
        self.active = False

    def show(self):
        """prints the product information for display"""
        print(f"Product: {self.name}, Price {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """raises an exception if the product is not active
        or if there is not enough stock available,
        calculates the total price and updates the stock,
        deactivates the product if the stock reaches zero,
        returns the total price"""
        if self.active == False:
            raise Exception("Product is not active")
        if self.quantity < quantity: #self.quantity = in Stock, quantity = purchase quantity
            raise Exception("Product is out of stock")
        if not isinstance(quantity, int):
            raise Exception("Quantity must be an integer")
        if quantity <= 0:
            raise Exception("Quantity must be positive")
        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price

