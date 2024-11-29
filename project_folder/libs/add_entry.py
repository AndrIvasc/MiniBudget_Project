def add_entry(entry_type, data_list):
    print(f"Adding a new {entry_type}:")
    date = input("Enter the date (YYYY-MM-DD): ")
    name = input(f"Enter the {entry_type} name (e.g., salary, food): ")

    try:
        amount = float(input(f"Enter the {entry_type} amount: "))
        if amount <= 0:
            print("Amount must be positive. Entry not added.")
            return
    except ValueError:
        print("Invalid amount. Entry not added.")
        return

    # Append the entry as a nested list [date, name, amount]
    data_list.append([date, name, amount])
    print(f"{entry_type.capitalize()} entry added successfully!\n")
