from datetime import datetime


def validate_date(date_input: datetime):
    """
    Validating date format
    :param date_input: datetime
    :return:
    """
    try:
        valid_date = datetime.strptime(date_input, "%Y-%m-%d").date()
        return str(valid_date)
    except ValueError:
        return None


def add_entry(entry_type: str, data_list: list):
    """
    Add entry to the given list
    :param entry_type: str
    :param data_list: list
    :return:
    """
    print(f"Adding a new {entry_type}:")

    date_input = input("Enter the date (YYYY-MM-DD): ")

    date = validate_date(date_input)
    if not date:
        print("Invalid date format. Please use YYYY-MM-DD. Entry not added.")
        return

    name = input(f"Enter the {entry_type} name (e.g., salary, food): ")

    try:
        amount = float(input(f"Enter the {entry_type} amount: "))
        if amount <= 0:
            print("Amount must be positive. Entry not added.")
            return
    except ValueError:
        print("Invalid amount. Entry not added.")
        return

    data_list.append([date, name, amount])
    print(f"{entry_type.capitalize()} entry added successfully!\n")
