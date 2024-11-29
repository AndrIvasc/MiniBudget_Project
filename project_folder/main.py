# Main program and menu selection

while True:

    print("1. Enter income\n"
          "2. Enter expenses\n"
          "3. Print income rows\n"
          "4. Print expense rows\n"
          "5. Print statistics\n"
          "q - Exit programm\n"
          "Enter your choice:")

    user_input = input("> ")

    if user_input == '1':
        input("Press enter to continue...")
    elif user_input == '2':
        input("Press enter to continue...")
    elif user_input == '3':
        input("Press enter to continue...")
    elif user_input == '4':
        input("Press enter to continue...")
    elif user_input == '5':
        input("Press enter to continue...")
    elif user_input == 'q':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")