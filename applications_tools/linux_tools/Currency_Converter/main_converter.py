
def currency_converter():   ## this is a test for a gpg key
    import requests
    from bs4 import BeautifulSoup
    from applications_tools.linux_tools.g_lib.general_library import users_inputs
    # well time for some explanation about what is happening here
    # this is a curency Converter and uses the https://www.unitconverters.net/ site to grab the most recent values of the USD to whatever curency it have


    def find_amount(url, replace1, replace2, replace3, replace4):
        print(url)
        response_from = requests.get(str(url))
        response_to = requests.get(str(url))

        from_result = BeautifulSoup(response_from.text, "html.parser")
        to_result = BeautifulSoup(response_to.text, "html.parser")

        replace1 = replace1 + " "  # web scraping for the amounts
        from_finder = from_result.find_all("table")[0].parent.find_all("td")[8].find_all("input")[0]['value'].replace(replace1, "").replace(replace2, "").replace("[", "").replace("]", "")
        to_finder = to_result.find_all("table")[0].parent.find_all("td")[8].find_all("input")[1]['value'].replace(replace3, "").replace(replace4, "").replace("[", "").replace("]", "")
        finder = float(from_finder) / float(to_finder)
        return finder


    while True:
        euro = False
        usd = False
        cad = False
        yen = False
        yuan = False
        gbp = False

        print("""    0-exit
            1- Europe euro
            2- United States dollar
            3- Canadian dollar
            4- Japanese yen
            5- Chinese yuan
            6- British Pound Sterling""")
        users_input = users_inputs(0, 6)

        if users_input == 0:
            break

        elif users_input == 1:
            euro = True
            main = "eur"
            replace1 = "EUR"  # replace 1 and 2 is needed for replacing some characters from the string to find the amount
            replace2 = "Euro"
        elif users_input == 2:
            usd = True
            main = "usd"
            replace1 = "USD"
            replace2 = "United States Dollar"
        elif users_input == 3:
            cad = True
            main = "cad"
            replace1 = "CAD"
            replace2 = "Canadian Dollar"
        elif users_input == 4:
            yen = True
            main = "jpy"
            replace1 = "JPY"
            replace2 = "Japanese Yen"
        elif users_input == 5:
            yuan = True
            main = "cny"
            replace1 = "CNY"
            replace2 = "Chinese Yuan"
        elif users_input == 6:
            gbp = True
            main = "gbp"
            replace1 = "GBP"
            replace2 = "British Pound Sterling"

        while True:
            num_euro = -1
            num_usd = -1
            num_cad = -1
            num_yen = -1
            num_yuan = -1
            num_gbp = -1
            i = 0

            if not euro:
                i += 1
                print("    " + str(i) + "- to convert to euro ")
                num_euro = i

            if not usd:
                i += 1
                print("    " + str(i) + "- to convert to usd ")
                num_usd = i

            if not cad:
                i += 1
                print("    " + str(i) + "- to convert to cad ")
                num_cad = i

            if not yen:
                i += 1
                print("    " + str(i) + "- to convert to yen ")
                num_yen = i

            if not yuan:
                i += 1
                print("    " + str(i) + "- to convert to yuan ")
                num_yuan = i

            if not gbp:
                i += 1
                print("    " + str(i) + "- to convert to British Pound Sterling ")
                num_gbp = i

            print("    0- exit")

            users_input = users_inputs(0, i)

            if users_input == 0:
                break
            elif users_input == num_euro:  
                url = "https://www.unitconverters.net/currency/" + str(main) + "-to-eur.htm"

                amount = find_amount(url, replace1, replace2, "EUR", "Euro")  # URL and the replace 3 and 4 values

            elif users_input == num_usd:
                url = "https://www.unitconverters.net/currency/" + str(main) + "-to-usd.htm"

                amount = find_amount(url, replace1, replace2, "USD", "United States Dollar")

            elif users_input == num_cad:
                url = "https://www.unitconverters.net/currency/" + str(main) + "-to-cad.htm"
                amount = find_amount(url, replace1, replace2, "CAD", "Canadian Dollar")

            elif users_input == num_yen:
                url = "https://www.unitconverters.net/currency/" + str(main) + "-to-jpy.htm"
                amount = find_amount(url, replace1, replace2, "JPY", "Japanese Yen")

            elif users_input == num_yuan:
                url = "https://www.unitconverters.net/currency/" + str(main) + "-to-cny.htm"
                amount = find_amount(url, replace1, replace2, "CNY", "Chinese Yuan")

            elif users_input == num_gbp:
                url = "https://www.unitconverters.net/currency/" + str(main) + "-to-gbp.htm"
                amount = find_amount(url, replace1, replace2, "GBP", "British Pound Sterling")

            amount = float(amount) * int(input("give me the amount you want to convert: "))
            print("The amount is: " + str(amount))
