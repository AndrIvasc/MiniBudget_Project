def print_rows(data_list, entry_type):
    if not data_list:
        print(f"No {entry_type} entries to display.")
        return

    print(f"\n{entry_type.capitalize()} entries:")
    for entry in data_list:
        print(f"Date: {entry[0]}, Name: {entry[1]}, Amount: {entry[2]:.2f}")


def print_statistics(income_list, expense_list):
    total_income = sum(entry[2] for entry in income_list)
    total_expenses = sum(entry[2] for entry in expense_list)
    balance = total_income - total_expenses

    if expense_list:
        avg_expense = total_expenses / len(expense_list)
    else:
        avg_expense = 0.0

    print("\nStatistics:")
    print(f"Total income: {total_income:.2f}")
    print(f"Total expenses: {total_expenses:.2f}")
    print(f"Average expense: {avg_expense:.2f}")
    print(f"Balance left: {balance:.2f}")
