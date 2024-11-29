from libs.add_entry import add_entry
# Main program and menu selection

# Vartotojui leidžiam įvesti tokius duomenis - data(datetime arba tiesiog stringas), pajamų ar išlaidų pavadinimas(pvz. pajamose - avansas, atlyginimas, stipendija ar pan, išlaidose - maistas,
# įvairūs pirkiniai, būsto išlaidos ir tt) ir suma. Duomenis saugom listuose. Turime 2 pagrindinius listus - pajamos, islaidos, juose saugom vidinius listus(kaip paskaitose pavyzdys su listu darbuotojai).
#
# Programą kuriam naujame Pycharm projekte, iniciavę git repositoriją ir kodą rašom etapais, darydami commit po kiekvieno etapo, pvz sukuriam vartotojo meniu, toliau vystom funkcionalumą kiekvienam meniu punktui.
# Reikėtų panaudoti bent vieną savo parašytą funkciją iškeltą į kitą failą ir importuojamą į pagrindinę programą.
#
# Padarę šį, pradinį variantą, prijungiam trynimo funkciją ir paieškos funkciją, loginimą. Trinti per indeksą, pradžioje išvedus turimus duomenis su indekso numeriu,
# tam galime panaudoti enumerate. Pabandykim bent dalį veiksmų kelti į funkcijas.

income_list = []
expense_list = []

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
        add_entry("income", income_list)
        input("Press enter to continue...")
    elif user_input == '2':
        add_entry("expense", expense_list)
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
