from libs.add_entry import add_entry
from libs.res_rep import print_rows, print_statistics
from libs.search_func import search_biggest_spendings
# Main program and menu selection

# Vartotojui leidžiam įvesti tokius duomenis - data(datetime arba tiesiog stringas), pajamų ar išlaidų pavadinimas(pvz. pajamose - avansas, atlyginimas, stipendija ar pan, išlaidose - maistas,
# įvairūs pirkiniai, būsto išlaidos ir tt) ir suma. Duomenis saugom listuose. Turime 2 pagrindinius listus - pajamos, islaidos, juose saugom vidinius listus(kaip paskaitose pavyzdys su listu darbuotojai).
#
# Programą kuriam naujame Pycharm projekte, iniciavę git repositoriją ir kodą rašom etapais, darydami commit po kiekvieno etapo, pvz sukuriam vartotojo meniu, toliau vystom funkcionalumą kiekvienam meniu punktui.
# Reikėtų panaudoti bent vieną savo parašytą funkciją iškeltą į kitą failą ir importuojamą į pagrindinę programą.
#
# Padarę šį, pradinį variantą, prijungiam trynimo funkciją ir paieškos funkciją, loginimą. Trinti per indeksą, pradžioje išvedus turimus duomenis su indekso numeriu,
# tam galime panaudoti enumerate. Pabandykim bent dalį veiksmų kelti į funkcijas.

# PAPILDYMAS: Kažkuriam etape prijungiam duomenų išsaugojimą į pickle failą.



income_list = []
expense_list = []

while True:

    print("1. Enter income\n"
          "2. Enter expenses\n"
          "3. Print income rows\n"
          "4. Print expense rows\n"
          "5. Print statistics\n"
          "6. Search for the biggest spendings over given ammount\n"
          "7. Add data to a pickle file\n"
          "8. Delete selected entry from income\n"
          "9. Delete selected entry from expeces\n"
          "q - Exit programm\n"
          "Enter your choice:")

    user_input = input("> ")

    if user_input == '1':
        add_entry("income", income_list)
        input("Press enter to continue...")
    elif user_input == '2':
        add_entry("expense", expense_list)
        input("Press enter to continue...")
    elif user_input == '3':
        print_rows(income_list, "income")
        input("Press enter to continue...")
    elif user_input == '4':
        print_rows(expense_list, "expense")
        input("Press enter to continue...")
    elif user_input == '5':
        print_statistics(income_list, expense_list)
        input("Press enter to continue...")
    elif user_input == '6':
        user_search_amount = int(input("What amount over to you want to see your spendings? -> "))
        search_biggest_spendings(expense_list, user_search_amount)
        input("Press enter to continue...")
    elif user_input == '7':

        input("Press enter to continue...")
    elif user_input == '8':

        input("Press enter to continue...")
    elif user_input == '9':

        input("Press enter to continue...")
    elif user_input == 'q':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
