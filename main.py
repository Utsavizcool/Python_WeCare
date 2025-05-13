# Import necessary functions from other modules
from read import read_inventory
from operations import view_products_with_price, view_products_without_price, buy_products, restock_products,view_products_with_price_restock

# Load product data from the inventory file
product = read_inventory()

# Main loop for the inventory management system menu
while True:
    print("\n------|WeCare Inventory Management System|------")6
    print(" ")
    print("Enter 1 to View Products")
    print("Enter 2 to Buy Products")
    print("Enter 3 to Restock Products")
    print("Enter 4 to Exit")
    choice = input("Enter your choice (1-4): ")

    # Handle user choice
    if choice == '1':
        view_products_without_price(product)  # View current inventory
    elif choice == '2':
        buy_products(product)  # Start buying process
    elif choice == '3':
        restock_products(product)  # Start restocking process
    elif choice == '4':
        print("Thank you for shopping with us....\nPlease visit us again <3")
        break  # Exit the program
    else:
        print("Your choice is invalid!!")  # Handle invalid input
