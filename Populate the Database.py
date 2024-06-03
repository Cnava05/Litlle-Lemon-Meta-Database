import pandas as pd

# Load the Excel file
file_path = 'path_to_your_file/LittleLemon_data.xlsx'
orders_df = pd.read_excel(file_path, sheet_name='Orders')

# Function to generate SQL insert statements
def generate_sql_inserts(df):
    customer_inserts = []
    order_inserts = []
    product_inserts = []
    cuisine_inserts = []
    menu_items_inserts = []
    
    for _, row in df.iterrows():
        # Customer insert
        customer_insert = f"INSERT INTO Customer (CustomerID, CustomerName, City, Country, PostalCode, CountryCode) VALUES ('{row['Customer ID']}', '{row['Customer Name']}', '{row['City']}', '{row['Country']}', '{row['Postal Code']}', '{row['Country Code']}');"
        customer_inserts.append(customer_insert)
        
        # Order insert
        order_insert = f"INSERT INTO `Order` (OrderID, OrderDate, DeliveryDate, CustomerID, Sales, Quantity, Discount, DeliveryCost) VALUES ('{row['Order ID']}', '{row['Order Date']}', '{row['Delivery Date']}', '{row['Customer ID']}', {row['Sales']}, {row['Quantity']}, {row['Discount']}, {row['Delivery Cost']});"
        order_inserts.append(order_insert)
        
        # Product insert
        product_insert = f"INSERT INTO Product (ProductCode, ProductName, SKU, Price) VALUES ('{row['Product Code']}', '{row['Product Name']}', '{row['SKU']}', {row['Price']});"
        product_inserts.append(product_insert)
        
        # Cuisine insert
        cuisine_insert = f"INSERT INTO Cuisine (CuisineName) VALUES ('{row['Cuisine Name']}');"
        cuisine_inserts.append(cuisine_insert)
        
        # Menu items insert
        menu_items_insert = f"INSERT INTO MenuItems (OrderID, CourseName, CuisineName, StarterName, DessertName, Drink, Sides) VALUES ('{row['Order ID']}', '{row['Course Name']}', '{row['Cuisine Name']}', '{row['Starter Name']}', '{row['Desert Name']}', '{row['Drink']}', '{row['Sides']}');"
        menu_items_inserts.append(menu_items_insert)
    
    return customer_inserts, order_inserts, product_inserts, cuisine_inserts, menu_items_inserts

# Generate the SQL insert statements
customer_inserts, order_inserts, product_inserts, cuisine_inserts, menu_items_inserts = generate_sql_inserts(orders_df)

# Save the SQL insert statements to a file
with open('LittleLemon_inserts.sql', 'w') as f:
    for insert in customer_inserts:
        f.write(insert + '\n')
    for insert in order_inserts:
        f.write(insert + '\n')
    for insert in product_inserts:
        f.write(insert + '\n')
    for insert in cuisine_inserts:
        f.write(insert + '\n')
    for insert in menu_items_inserts:
        f.write(insert + '\n')

print("SQL insert statements have been generated and saved to LittleLemon_inserts.sql")
