def compare_datasets(old_data, new_data):
    added_records = [record for record in new_data if record not in old_data]
    updated_records = [record for record in new_data if record in old_data]
    deleted_records = [record for record in old_data if record not in new_data]

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
