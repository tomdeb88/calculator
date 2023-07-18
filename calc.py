import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")



def calculating():

    operation=input("Podaj dzialanie, poslugujac sie odpowiednia liczba: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie \n")
    if operation=='1':
        numbers=input("Podaj liczby oddzielajac je spacja\n").split(' ')
        end_number=0
        logs_info=""
        for number in numbers:
            end_number+= float(number)
            logs_info=logs_info + " "+ number
        logging.info(f"Dodaje liczby{logs_info}")
        print(f"Wynik to {end_number}")
    elif operation=='2':
        number_1=float(input("Podaj skladnik 1 \n"))
        number_2=float(input("Podaj skladnik 2 \n"))
        logging.info(f"Odejmuje liczbe {number_1} od  {number_2}")
        result= number_1 - number_2
        print(f"Wynik to: {result} ")
    elif operation=='3':
        numbers=input("Podaj liczby oddzielajac je spacja\n").split(' ')
        end_number=1
        logs_info=""
        for number in numbers:
            end_number*= float(number)
            logs_info=logs_info + " "+ number
        logging.info(f"Mnoze liczby{logs_info}")
        print(f"Wynik to: {end_number}")
    elif operation=="4":
        number_1=float(input("Podaj skladnik 1\n"))
        number_2=float(input("Podaj skladnik 2\n"))
        logging.info(f"Dziele liczbe {number_1} przez  {number_2}")
        print(f"Wynik to: {number_1/number_2}")



calculating()