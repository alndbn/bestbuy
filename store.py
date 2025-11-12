from products import Product

class Store:
    def __init__(self, products):        #initializatio
        if not isinstance(products, list)
            raise TypeError("Products must be a list")
        for p in products:
            if not isinstance(p, Product):
                raise TypeError("All elements in Product must be Product instance")
        if not products:
            raise ValueError("Products list cannot be empty.")

    #instance variable - parameter
        self.products = products #self.products -> data type lst[]

    def add_product(self, product):
        """adds a new product to the list"""
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of Product")
        self.products.append(product)

    def remove_product(self, product):
        """removes a product from the list"""
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance Product")
        if product not in self.products:
            raise ValueError("Product not found in store.")
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """returns how many articles available in store"""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> list:
        """returns active products in a list"""
        new_product_list = []
        for product in self.products:
            if product.is_active() == True:
                new_product_list.append(product)
        return new_product_list

    def order(self, shopping_list) -> float:
        """Takes a list(Product, quantity) and returns total price"""
        if not isinstance(shopping_list, list):
            raise TypeError("Shopping_list must be a list")
        total_price = 0
        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("Each item must be a (Product, quantity) tuple")
            product, quantity = item
            if not isinstance(product, Product):
                raise TypeError("First element must be a Product instance")
            if not isinstance(quantity, int):
                raise TypeError("Quantity must be int")
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
            total_price += product.buy(quantity)
        return total_price

