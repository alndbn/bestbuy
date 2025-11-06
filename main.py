from products import Product
from store import Store


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    best_buy = Store([bose, mac, pixel])

    print("Total items:", best_buy.get_total_quantity())

    active_products = best_buy.get_all_products()
    for product in active_products:
        product.show()

    total = best_buy.order([(bose, 5), (mac, 3)])
    print("Order cost:", total)


    print("\n--- Edge cases test---")
    try:
        best_buy.order([(bose, 0)])
    except Exception as e:
        print("Zero quantity:", e)


if __name__ == "__main__":
    main()
