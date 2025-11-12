from products import Product
from store import Store

def pause():
    """Wait for Enter so output is readable."""
    input("Please choose a number:\n")

def print_menu():
    print("""
1. List products
2. Total quantity
3. Make order
4. Exit
""")

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
    """Handle user order input and call store.order."""
    active_products = store.get_all_products()
    if not active_products:
        print("No products available right now.")
        return

    print("Available products:")
    for i, product in enumerate(active_products, start=1):
        print(f"{i}. {product.name} - €{product.price} ({product.quantity} in stock)")
    print()

    choice = input("Choose a product number (or 0 to cancel): ").strip()
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

    qty_input = input(f"How many '{selected_product.name}' would you like to buy? (0 to cancel): ").strip()
    if qty_input == "0":
        print("Order cancelled.")
        return

    try:
        quantity = int(qty_input)
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    shopping_list = [(selected_product, quantity)]

    try:
        total_price = store.order(shopping_list)
        print(f"Order successful! Total cost: €{total_price}\n")
    except Exception as e:
        print(f"Error while processing order: {e}")

def exit_program():
    print("Goodbye!")
    raise SystemExit

def run_menu(store):
    actions = {
        "1": lambda: list_all_products(store),
        "2": lambda: total_amount(store),
        "3": lambda: make_order(store),
        "4": exit_program,
    }

    while True:
        print_menu()
        choice = input("Please choose a number: ").strip()
        action = actions.get(choice)

        if action:
            try:
                action()
            except SystemExit:
                break
            except Exception as e:
                print("Error:", e)
                pause()
        else:
            print("Invalid choice, please enter 1-4.\n")
            pause()

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    product_list = [bose, mac, pixel]
    best_buy = Store(product_list)

    run_menu(best_buy)

if __name__ == "__main__":
    main()
