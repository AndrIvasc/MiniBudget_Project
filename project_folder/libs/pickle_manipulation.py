import pickle


def save_data_to_pickle(income_list: list, expense_list: list, pickle_name: str):
    """
    Save data from two lists to a custom pickle file
    :param income_list:
    :param expense_list:
    :param pickle_name:
    :return:
    """
    try:
        with open(pickle_name, 'wb') as file:
            pickle.dump((income_list, expense_list), file)
        print(f"Data saved to '{pickle_name}' successfully!")
    except Exception as e:
        print(f"Error with seving to pickle file: {e}")
