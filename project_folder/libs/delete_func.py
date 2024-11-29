def delete_entry(entry_type, data_list):
    if not data_list:
        print(f"No {entry_type} entries to delete.")
        return

    print(f"Select the index of the {entry_type} entry to delete:")
    for i, entry in enumerate(data_list):
        print(f"{i}: Date: {entry[0]}, Name: {entry[1]}, Amount: {entry[2]:.2f}")

    try:
        index = int(input(f"Enter the index of the {entry_type} entry to delete: "))
        if 0 <= index < len(data_list):
            del data_list[index]
            print(f"{entry_type.capitalize()} entry deleted successfully.")
        else:
            print("Invalid index. No entry deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")