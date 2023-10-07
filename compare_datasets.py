def compare_datasets(old_data, new_data):
    # Initialize lists to store differences
    added_records = []
    updated_records = []
    deleted_records = []

    # Convert old_data and new_data to sets for efficient comparison
    old_data_set = {tuple(d.items()) for d in old_data}
    new_data_set = {tuple(d.items()) for d in new_data}

    # Find added and updated records
    added_records = [dict(item) for item in new_data_set - old_data_set]
    updated_records = [dict(item) for item in new_data_set.intersection(old_data_set)]

    # Find deleted records (present in old_data but not in new_data)
    deleted_records = [dict(item) for item in old_data_set - new_data_set]

    return added_records, updated_records, deleted_records

# Sample data for demonstration
old_dataset = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Alice"},
    {"id": 3, "name": "Bob"},
]

new_dataset = [
    {"id": 1, "name": "John"},
    {"id": 3, "name": "Charlie"},
    {"id": 4, "name": "Eve"},
]

# Compare the datasets
added_records, updated_records, deleted_records = compare_datasets(old_dataset, new_dataset)

# Display the differences
print("Added Records:")
print(added_records)

print("\nUpdated Records:")
print(updated_records)

print("\nDeleted Records:")
print(deleted_records)
