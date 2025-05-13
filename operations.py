# Import necessary modules and functions
from datetime import datetime
from write import write_customer_bill, write_supplier_invoice, write_inventory

# Function to display all available products in a formatted table
def view_products_with_price(product):
    # Use of Doc String
    """
    Summary:
    Displays the list of available products in a formatted table with pricing information.

    This function prints a decorative header followed by a tabular view of each product's
    ID, name, brand, retail price (calculated as double the base price), quantity in stock, 
    and country of origin. It is intended to help users quickly browse the current inventory 
    along with marked-up selling prices.

    Parameters: product(list)

    Returns: Displays Table of products
    """
    print("=" * 125)
    print("                                               |Welcome to WeCare Product|")
    print("=" * 125)
    print("                                            |Products Available in the Store|")
    print("\n")
    print("-" * 125)
    print("Product ID\t    Name\t\t  Brand\t\t\tPrice\t\t      Quantity\t\t       Country")
    print("-" * 125)
    for inventory in product:
        # Display each product with double price 
        print(str(inventory['id']) + "\t\t" + inventory['name'] + "\t\t" + inventory['brand'] + "\t\t" +
              str(inventory['price']*2) + "\t\t\t" + str(inventory['quantity']) + "\t\t     " + inventory['country'])
    print("=" * 125)
    print("-" * 125)

def view_products_with_price_restock(product):
    """
    Summary:
    Displays the list of products with original prices for supplier restocking.

    This function is similar to `view_products_with_price`, but it shows the base price 
    instead of the marked-up price. It is used internally when suppliers are restocking 
    inventory.

    Parameters: product (List) 
                        
    Returns: Displays Product Detail Table
    """
    print("=" * 125)
    print("                                               |Welcome to WeCare Product|")
    print("=" * 125)
    print("                                            |Products Available in the Store|")
    print("\n")
    print("-" * 125)
    print("Product ID\t    Name\t\t  Brand\t\t\tPrice\t\t      Quantity\t\t       Country")
    print("-" * 125)
    for inventory in product:
        # Display each product with double price 
        print(str(inventory['id']) + "\t\t" + inventory['name'] + "\t\t" + inventory['brand'] + "\t\t" +
              str(inventory['price']) + "\t\t\t" + str(inventory['quantity']) + "\t\t     " + inventory['country'])
    print("=" * 125)
    print("-" * 125)

def view_products_without_price(product):
    """
    Summary:
    Displays available products in a formatted table without showing their prices.

    This version is useful for views where pricing is not relevant, such as general 
    stock checks or customer inquiries. It includes ID, name, brand, quantity, and 
    country only.

    Parameters: product (list)
        
    Returns: Displays Product Detail Table
    """
    print("=" * 103)
    print("                                         |Welcome to WeCare Product|")
    print("=" * 103)
    print("")
    print("                                             |Products Available|")
    print("")
    print("-" * 103)
    print("Product ID\t    Name\t\t  Brand\t\t      Quantity\t\t       Country")
    print("-" * 103)
    for inventory in product:
        print(str(inventory['id']) + "\t\t" + inventory['name'] + "\t\t" + inventory['brand'] + "\t\t" + str(inventory['quantity']) + "\t\t     " + inventory['country'])
    print("=" * 103)
    print("-" * 103)

# Function to handle the buying process for customers
def buy_products(product):
    """
    Summary:
    Handles the customer purchasing workflow.

    Allows customers to select products by ID, specify quantities, and applies a free item 
    offer (1 free for every 3 bought). Updates inventory accordingly, calculates total cost 
    (using retail price), prints a detailed bill, and writes the transaction to a file.

    Parameters: product (list)
        
    Returns: Displays customer's bill and buying of product is done
    """
    view_products_with_price(product)
    total = 0  # Total cost of products purchased
    total_free = 0  # Total number of free products given
    invoice = []  # List to hold invoice details

    while True:
        productId = input("Enter the Id of the product or type 'exit': ")
        if productId.lower() == 'exit':
            if len(invoice) == 0:
                print("No items purchased. Exiting purchase process.")
                return
            else:
                break
        valid = False  # Flag to check if valid product id is entered
        for i in range(len(product)):
            if productId == str(product[i]['id']):
                quantity = int(input("Enter the quantity you desire: "))
                free = quantity // 3  # For every 3 products, 1 is free
                total_units = quantity + free

                if total_units <= product[i]['quantity']:
                    # Update stock after purchase
                    product[i]['quantity'] = product[i]['quantity'] - total_units
                    cost = quantity * product[i]['price'] * 2  # Selling at double the price
                    total = total + cost
                    total_free = total_free + free
                    # Add item to invoice
                    invoice.append({
                        'name': product[i]['name'],
                        'brand': product[i]['brand'],
                        'quantity': quantity,
                        'free': free,
                        'price': product[i]['price']
                    })
                    print(str(quantity) + " units of " + product[i]['name'] + " added with " + str(free) + " free items.")
                else:
                    print("Not enough stock left. Only " + str(product[i]['quantity']) + " available including free items.")
                valid = True
                break
        if valid == False:
            print("Invalid id")
            continue
            
        question = input("Do you want to buy more? (y/n)")
        if question.lower() == 'n' or question.lower() == 'no':
            break    

    name = input("Enter customer's name: ")
    now = datetime.now()  # Get current date and time

    # Print the customer bill
    print("\n")
    print("====================================|Customer bill|==================================\n")
    print("Customer:", name)
    print("Date:", now)
    print("\nItems Purchased: ")
    for item in invoice:
        print("Name: ", item['name'], "\tBrand: ", item['brand'], "\tQuantity: ", item['quantity'], "\tFree Items: ", item['free'], "\tPrice: ", item['price'])
    print("You have got ", total_free, " free products!!\n")
    print("======================================================================================\n")
    print("Total: Rs" + str(total))
    print("======================================================================================\n")
    print("\n")

    # Write the bill to a file and update inventory
    write_customer_bill(name, invoice, total, total_free, now)
    write_inventory(product)

# Function to handle restocking of products by suppliers
def restock_products(product):
    """
    Summary:
    Handles the restocking workflow for suppliers.

    Allows suppliers to restock products by entering product ID and quantity (up to a max limit). 
    Updates inventory, calculates the cost with VAT (13%), and prints a restocking invoice. 
    Also writes the transaction and updated inventory to files.

    Parameters: product (list)

    Returns: Display's Supplier's invoice and restocking of product is done

    Exceptions:
    ValueError: Raised when the user inputs a non-integer value for quantity
    """
    view_products_with_price_restock(product)
    supplier_name = input("Enter the name of the supplier: ")
    total_cost = 0  # Total cost of restocked items
    invoice = []  # List to store restock invoice
    date = datetime.now()
    max = 5000  # Maximum allowed restock quantity per product

    while True:
        productId = input("Enter the product id that needs to be restocked or type 'exit': ")
        if productId.lower() == 'exit':
            # Exit immediately if no product has been added yet
            if len(invoice) == 0:
                print("No products were restocked. Exiting restock process.")
                return
            else:
                break
            
        valid_sup = False  # Flag to check valid product id
        
        # Search for product with matching ID
        for i in range(len(product)):
            if productId == str(product[i]['id']):
                # Validate quantity input
                while True:
                    quantity_input = input("Enter the quantity of products that need to be restocked: ")
                    try:
                        quantity = int(quantity_input)
                        if quantity <= 0:
                            print("Quantity must be positive!")
                            continue
                        if quantity > max:
                            print("Cannot restock more than ",max," units at once!")
                            continue
                        break  # Valid quantity entered
                    except ValueError:
                        print("Invalid input! Please enter a numeric value.")
                        continue
                
                # Update product quantity and calculate cost
                product[i]['quantity'] += quantity
                cost = quantity * product[i]['price']
                total_cost += cost
                
                # Add to supplier invoice
                invoice.append({
                    'product_type': product[i]['name'],
                    'brand': product[i]['brand'],
                    'quantity': quantity,
                    'unit_price': product[i]['price'],
                    'supplier': supplier_name,
                    'date': date,
                    'total_price': cost
                })

                print(quantity," units were restocked.")
                valid_sup = True
                break
                
        if not valid_sup:
            print("Invalid Id!!")
            continue
            
        # Ask if user wants to add more products
        question = input("Do you want to add more?(y/n) ")
        if question.lower() == 'n' or question.lower() == 'no':
            break

    # Calculate total with VAT (13%)
    vat = total_cost * 0.13
    grand_total = total_cost + vat

    # Print the supplier invoice
    print("\n")
    print("====================================|Restock Invoice|==================================\n")
    print("Supplier:", supplier_name)
    print("Date:", date)
    print("\nItems Purchased: ")
    for item in invoice:
        print("Product: ", item['product_type'], "\tBrand: ", item['brand'],"\tQuantity: ", item['quantity'], "\tPrice: ", item['unit_price'])
    print("======================================================================================\n")
    print("Total: Rs" + str(grand_total))
    print("======================================================================================\n")
    print("\n")

    # Write the invoice to a file and update inventory
    write_supplier_invoice(supplier_name, invoice, grand_total, date)
    write_inventory(product)
