import pandas as pd
import csv

# Step 1: Create a Sample CSV File
sample_data = [
    ["Product", "Price", "Quantity"],
    ["Product A", 10.99, 50],
    ["Product B", 5.99, 30],
    ["Product C", 7.49, 20],
]

with open("sales_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sample_data)

print("Sample CSV file 'sales_data.csv' created.")

# Step 2: Load Data into a Pandas DataFrame
df = pd.read_csv("sales_data.csv")

# Display the data
print("Step 2: Loaded Data into a Pandas DataFrame")
print(df)

# Step 3: Perform Data Processing
df["Total Sales"] = df["Price"] * df["Quantity"]

# Display the updated DataFrame
print("\nStep 3: Calculated Total Sales")
print(df)

# Step 4: Save Processed Data to a New CSV File
df.to_csv("processed_sales_data.csv", index=False)

print("\nStep 4: Processed data saved to 'processed_sales_data.csv'.")
