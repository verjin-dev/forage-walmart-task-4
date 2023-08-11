import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('shipment_database.db')
cursor = conn.cursor()

# Read and insert Spreadsheet 0
spreadsheet_0_data = pd.read_excel('data/shipping_data_0.csv')
spreadsheet_0_data.to_sql('table_name_0', conn, if_exists='append', index=False)

# Read and combine Spreadsheet 1 and 2
spreadsheet_1_data = pd.read_excel('data/shipping_data_1.csv')
spreadsheet_2_data = pd.read_excel('data/shipping_data_2.csv')
merged_data = pd.merge(spreadsheet_1_data, spreadsheet_2_data, on='shipping_identifier')

# Iterate through merged data and insert into the database
for index, row in merged_data.iterrows():
    # Extract relevant data from the row
    shipping_identifier = row['shipping_identifier']
    product_name = row['product_name']
    quantity = row['quantity']
    origin = row['origin']
    destination = row['destination']

    # Insert data into the database
    cursor.execute('INSERT INTO table_name_1 (columns) VALUES (?, ?, ?, ?, ?)', (shipping_identifier, product_name, quantity, origin, destination))

# Commit changes and close the connection
conn.commit()
conn.close()
