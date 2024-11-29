def delete_entry(entry_type: str, data_list: list):
    """
    Delete given entry from the list
    :param entry_type: str
    :param data_list: list
    :return:
    """
    if not data_list:
        print(f"No {entry_type} entries to delete.")
        return

    print(f"Select the index of the {entry_type} entry to delete:")
    for i, entry in enumerate(data_list):
        print(f"{i + 1}: Date: {entry[0]}, Name: {entry[1]}, Amount: {entry[2]:.2f}")

    try:
        index = int(input(f"Enter the index of the {entry_type} entry to delete: "))
        if 0 <= index < len(data_list):
            del data_list[index]
            print(f"{entry_type.capitalize()} entry deleted successfully.")
        else:
            print("Invalid index. No entry deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")