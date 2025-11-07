from products import Product
from store import Store


def main():
    #create product objects
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    #list for the store
    product_list = [bose, mac, pixel]

    #Store
    best_buy = Store(product_list)

    #Testcode
    products = best_buy.get_all_products()
    print("Total items:", best_buy.get_total_quantity())
    print("Order cost:", best_buy.order([(products[0], 1), (products[1], 2)]))

    #Edge-Case-Test
    print("\n--- Edge cases test ---")
    try:
        best_buy.order([(bose, 0)])
    except Exception as e:
        print("Zero quantity:", e)


if __name__ == "__main__":
    main()
