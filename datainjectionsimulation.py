# Step 1: Set Up the Environment

# Step 2: Define the Data Store
data_store = []

# Step 3: Define the Data Model
class Record:
    def __init__(self, record_id, name, age):
        self.id = record_id
        self.name = name
        self.age = age

# Step 4: Implement Data Injection
def insert_data(name, age):
    record_id = len(data_store) + 1
    new_record = Record(record_id, name, age)
    data_store.append(new_record)
    print(f"Inserted: {new_record.__dict__}")

# Step 5: Implement Data Update
def update_age(record_id, new_age):
    for record in data_store:
        if record.id == record_id:
            record.age = new_age
            print(f"Updated age for record {record_id} to {new_age}")

# Step 6: Display Data Store
def display_data_store():
    for record in data_store:
        print(record.__dict__)

# Step 7: Run the Simulation
if __name__ == "__main__":
    # Insert initial data
    insert_data("Alice", 25)
    insert_data("Bob", 30)

    # Display initial data
    print("Initial Data:")
    display_data_store()

    # Update age
    update_age(1, 27)

    # Display updated data
    print("\nUpdated Data:")
    display_data_store()
