import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('shipment_database.db')
cursor = conn.cursor()

# Read and insert Spreadsheet 0 (CSV format)
spreadsheet_0_data = pd.read_csv('data/shipping_data_0.csv')
spreadsheet_0_data.to_sql('shipping_data_0', conn, if_exists='append', index=False)

# Read Spreadsheet 1 and 2 (assuming they are in CSV format)
spreadsheet_1_data = pd.read_csv('data/shipping_data_1.csv')
spreadsheet_2_data = pd.read_csv('data/shipping_data_2.csv')

# Iterate through Spreadsheet 1 and insert each row into the database
for index, row in spreadsheet_1_data.iterrows():
    shipping_identifier = row.iloc[0]  # Assuming first column is the shipping identifier
    product_name = row['product_name']
    quantity = row['quantity']

    # Insert data into the database
    cursor.execute('INSERT INTO shipping_data_1 (shipping_identifier, product_name, quantity) VALUES (?, ?, ?)',
                   (shipping_identifier, product_name, quantity))

# Iterate through Spreadsheet 2 and update destination for each shipment
for index, row in spreadsheet_2_data.iterrows():
    shipping_identifier = row.iloc[0]  # Assuming first column is the shipping identifier
    destination = row['destination']

    # Update destination in the database
    cursor.execute('UPDATE shipping_data_1 SET destination = ? WHERE shipping_identifier = ?', (destination, shipping_identifier))

# Commit changes and close the connection
conn.commit()
conn.close()
