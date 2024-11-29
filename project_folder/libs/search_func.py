def search_biggest_spendings(expense_list: list, user_search_amount: int):
    """
    Give an amount to search for higher spendings list
    :param expense_list: list
    :param user_search_amount: int
    :return:
    """
    big_spendings = [entry for entry in expense_list if entry[2] > user_search_amount]

    if not big_spendings:
        print("No expenses over 100 found.")
        return

    print("\nBiggest spendings over 100:")
    for entry in big_spendings:
        print(f"Date: {entry[0]}, Name: {entry[1]}, Amount: {entry[2]:.2f}")
