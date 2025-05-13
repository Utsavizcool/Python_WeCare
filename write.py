# Function to write the current product inventory to a file
def write_inventory(product):
    """
    Summary:
    Writes the current inventory data to a file named 'inventory.txt'.

    Each product is written as a comma-separated line containing its ID, name, brand, price, quantity, and country.
    The file is overwritten with each call to ensure it reflects the latest stock levels.

    Parameters: product(list)

    Returns: writes and changes the details in inventory.txt
    """    
    file = open("inventory.txt", "w")  # Open the inventory file in write mode
    for p in product:
        # Convert product details into a comma-separated string
        line = str(p['id']) + "," + p['name'] + "," + p['brand'] + "," + str(p['price']) + "," + str(p['quantity']) + "," + p['country']
        file.write(line + "\n")  # Write each product as a new line
    file.close()  # Close the file after writing

# Function to write a customer bill to a uniquely named text file
def write_customer_bill(name, invoice, total, total_free, datetime):
    """
    Summary:
    Writes a detailed customer bill to a uniquely named text file.

    The filename is generated using the customer's name and the current date.
    The bill includes customer details, itemized purchases, quantities, free items, 
    total cost, and is saved in a structured format.

    Parameters:
    -----------
    name (str)
        Name of the customer.
    invoice (list)
        List of purchased items with keys: 'name', 'brand', 'quantity', 'free', and 'price'.
    total (float)
        Total amount charged to the customer.
    total_free (int)
        Total number of free items given.
    datetime (datetime)
        Timestamp of the purchase.

    Returns: Writes the customer's bill
    """
    # Create a filename based on customer name and current date
    f = "Customer_Bill " + name.replace(" ", "_") + "_" + str(datetime.year) + "_" + str(datetime.month) + "_" + str(datetime.day) + ".txt"
    file = open(f, "w")  # Open the customer bill file in write mode
    # Write bill header
    file.write("====================================|Customer bill|==================================\n")
    file.write("Customer Name: " + name + "\n")
    file.write("Date: " + str(datetime) + "\n\n")
    # Write each item in the invoice
    for item in invoice:
        file.write("Name: " + item['name'] + "\tBrand: " + item['brand'] + "\tQuantity: " + str(item['quantity']) + "\tFree Items: " +
                   str(item['free']) + "\tPrice: " + str(item['price']) + "\n")
    # Write bill footer with totals
    file.write("======================================================================================\n")
    file.write("\nTotal: Rs" + str(total) + "\n")
    file.write("Total Free items: " + str(total_free))
    file.write("\n======================================================================================\n")
    file.close()  # Close the file after writing

# Function to write a supplier invoice to a uniquely named text file
def write_supplier_invoice(supplier_name, invoice, grand_total, datetime):
    """
    Summary:
    Writes a detailed supplier invoice to a uniquely named text file.

    The filename is created using the supplier's name and the current date.
    The invoice includes supplier info, itemized restocked products, quantities, unit prices,
    and the grand total including VAT.

    Parameters:
    supplier_name (str)
        Name of the supplier.
    invoice (list)
        List of restocked items with keys: 'product_type', 'brand', 'quantity', 'unit_price'.
    grand_total (float)
        Total cost including VAT.
    datetime (datetime)
        Timestamp of the restock.

    Returns: Writes supplier's invoice
    """
    # Create a filename based on supplier name and current date
    f = "Supplier_Invoice " + supplier_name.replace(" ", "_") + "_" + str(datetime.year) + "_" + str(datetime.month) + "_" + str(datetime.day) + ".txt"
    file = open(f, "w")  # Open the supplier invoice file in write mode
    # Write invoice header
    file.write("====================================|Restock Invoice|==================================\n")
    file.write("Supplier: " + supplier_name + "\n")
    file.write("Date: " + str(datetime) + "\n\n")
    # Write each item in the supplier invoice
    for item in invoice:
        file.write("Product: " + item['product_type'] + "\tBrand: " + item['brand'] + "\tQuantity: " + str(item['quantity']) + "\tPrice: " + str(item['unit_price']) + "\n")
    # Write invoice footer with grand total
    file.write("======================================================================================\n")
    file.write("\nTotal: Rs" + str(grand_total) + "\n")
    file.write("======================================================================================\n")
    file.close()  # Close the file after writing
