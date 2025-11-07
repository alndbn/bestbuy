from products import Product
from store import Store


def print_menu():
    """prints the UI menu"""
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def pause():
    """Wait for Enter so output is readable."""
    input("Please choose a number:\n")


def list_all_products(store):
    """list all active products in store"""
    active_products = store.get_all_products()
    for product in active_products:
        print(f"Available products: {product.name}, Price: €{product.price}, Quantity: {product.quantity}\n")


def total_amount(store):
    """show total quantity in store"""
    amount_in_total = store.get_total_quantity()
    print(f"Total amount in store: {amount_in_total}\n")


def make_order(store):
    """handle order input and call store.order"""
    list_all_products(store)
    active_products = store.get_all_products()

    #choose product
    choice = input("Choose a product (enter number, or 0 to cancel): ").strip()
    if choice == "0":
        print("Order cancelled.")
        return

    try:
        chosen_index = int(choice) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if chosen_index < 0 or chosen_index >= len(active_products):
        print("Invalid product number.")
        return

    selected_product = active_products[chosen_index]

    #choose quantity
    qty_input = input(f"How many '{selected_product.name}' do you want to buy? (0 to cancel): ").strip()
    if qty_input == "0":
        print("Order cancelled.")
        return

    try:
        quantity = int(qty_input)
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return

    #generate shopping list
    shopping_list = [(selected_product, quantity)]

    #order complete
    try:
        total_price = store.order(shopping_list)
        print(f"Order successful! Total cost: {total_price} €")
    except Exception as e:
        print(f"Error while processing order: {e}")



def start(store):
    "route menu choices to actions"
    while True:
        print_menu()
        choice = input("Please choose a number: ").strip()
        print()

        if choice == "1":
            list_all_products(store)
        elif choice == "2":
            total_amount(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1-4.\n")
            pause()


def main():
    #create product objects
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    #list for the store
    product_list = [bose, mac, pixel]
    #Store
    best_buy = Store(product_list)
    #start UI
    start(best_buy)


if __name__ == "__main__":
    main()
