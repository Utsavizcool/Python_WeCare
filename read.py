# Define a function to read the inventory from a file
def read_inventory():
    """
    Summary:
    Reads inventory data from the 'inventory.txt' file and loads it into a list of dictionaries.

    Each line in the file is expected to be in the format:
    id,name,brand,price,quantity,country

    Returns:
    product(list):
        A list where each element is a dictionary representing a product with keys:
        'id' (int), 'name' (str), 'brand' (str), 'price' (float), 'quantity' (int), and 'country' (str).

    Exceptions:
    FileNotFoundError:
        If 'inventory.txt' does not exist, an error message is printed and an empty list is returned.
    """
    product = []  # Initialize an empty list to store product dictionaries
    try:
        # Try to open the inventory file in read mode
        file = open("inventory.txt", "r")
        lines = file.readlines()  # Read all lines from the file
        
        # Loop through each line in the file
        for line in lines:
            product_list = line.split(',')  # Remove comma by split 
            
            # Ensure the line contains at least 6 elements
            if len(product_list) >= 6:
                # Create a dictionary for the product with appropriate data types
                products = {
                    'id': int(product_list[0]),
                    'name': product_list[1],
                    'brand': product_list[2],
                    'price': float(product_list[3]),
                    'quantity': int(product_list[4]),
                    'country': product_list[5]
                }
                product.append(products)  # Add the product dictionary to the list
        file.close()  # Close the file after reading
    except FileNotFoundError:
        # Print an error message if the file is not found
        print("Error: The file was not found")
    
    return product  # Return the list of product dictionaries
