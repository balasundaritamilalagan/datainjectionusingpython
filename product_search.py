import sqlite3

def create_database():
    try:
        # Connect to the database (if it doesn't exist, it will be created)
        connection = sqlite3.connect("products.db")
        cursor = connection.cursor()

        # Create the "products" table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL
            )
        ''')

        # Insert some sample data for testing
        sample_data = [
            ('grocery', 10.99),
            ('cloths', 15.49),
            ('stationary', 5.99)
        ]
        cursor.executemany('INSERT INTO products (name, price) VALUES (?, ?)', sample_data)

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

    except sqlite3.Error as e:
        print("Database error:", e)

# Function to search for products based on user input
def search_product_by_name(connection, product_name):
    try:
        # Validate user input to prevent SQL injection
        if not product_name or not product_name.isalnum():
            raise ValueError("Invalid product name")

        # Perform the SQL query
        cursor = connection.cursor()
        query = f"SELECT * FROM products WHERE name LIKE ?"
        cursor.execute(query, ('%' + product_name + '%',))

        # Fetch and print the results
        results = cursor.fetchall()
        if not results:
            print("No products found.")
        else:
            print("Products found:")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Price: ${row[2]}")

    except ValueError as ve:
        print("Error:", ve)
    except sqlite3.Error as e:
        print("Database error:", e)

# Main function
def main():
    try:
        # Create the database and insert sample data
        create_database()

        # Connect to the existing database
        connection = sqlite3.connect("products.db")

        # Take user input for product name
        product_name = input("Enter the product name to search for: ")

        # Search for products by name
        search_product_by_name(connection, product_name)

    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        # Close the database connection
        if connection:
            connection.close()

if __name__ == "__main__":
    main()
