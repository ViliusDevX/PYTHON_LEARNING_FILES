import csv


csv_file = "309_currency.csv"
currency_data = {}


def load_csv():
    global currency_data
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            code, symbol, name = row
            currency_data[code] = {"Symbol": symbol, "Name": name}


def ask_check_user_input():
    user_input = input("Ivesk valiutos kodas (pvz.: USD, EUR): ").strip().upper()
    if user_input in currency_data:
        currency_info = currency_data[user_input]
        print(f"Valiutos kodas: {user_input}")
        print(f"Symbolis: {currency_info['Symbol']}")
        print(f"Pavadinimas: {currency_info['Name']}")
    else:
        print("Valiuta nerasta")


load_csv()
ask_check_user_input()
