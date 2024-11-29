def search_biggest_spendings(expense_list, user_search_amount):
    big_spendings = [entry for entry in expense_list if entry[2] > user_search_amount]

    if not big_spendings:
        print("No expenses over 100 found.")
        return

    print("\nBiggest spendings over 100:")
    for entry in big_spendings:
        print(f"Date: {entry[0]}, Name: {entry[1]}, Amount: {entry[2]:.2f}")