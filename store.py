from products import Product

class Store:
    def __init__(self, products):        #initializatio
    #instance variable - parameter
        self.products = products #self.products -> data type lst[]

    def add_product(self, product):
        """adds a new product to the list"""
        self.products.append(product)

    def remove_product(self, product):
        """removes a product from the list"""
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
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


