import csv


def load_and_return_csv_file_info(file_path):
    with open(file_path, "r") as file:
        file_data = csv.DictReader(file, quoting=csv.QUOTE_NONNUMERIC)
        list_of_dicts = list(file_data)
        return list_of_dicts


file_name = "TOP_SPORT/data/dogs.csv"
products = load_and_return_csv_file_info(file_name)


def create_products():
    id = input("Ivesk produkto ID: ")
    name = str(input("Ivesk produkto pavadinima: "))
    qty = int(input("Ivesk produkto kieki: "))
    product = {
        "id": id,
        "name": name,
        "qty": qty
    }
    products.append(product)
    ask_add_more_products = str(input("Ar dar desi produktus? (T arba N): "))
    if ask_add_more_products == "T":
        create_products()


def delete_products(file_path, condition):
    # Read existing data from CSV file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Filter out rows based on the condition
    filtered_rows = [row for row in rows if not condition(row)]

    # Write the remaining data back to the CSV file
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filtered_rows)


# Example usage
def delete_condition(row):
    what_to_delete = input("Kelinta eilute nori istrinti?: ")
    return row[what_to_delete] == 'delete'


def add_info_to_csv_file(file_path, list_of_dicts):
    keys = list_of_dicts[0].keys()
    with open(file_path, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys, quoting = csv.QUOTE_NONNUMERIC)
        dict_writer.writeheader()
        dict_writer.writerows(list_of_dicts)


def print_all_products():
    for product in products:
        print(f"id: {product['id']}, name: {product['name']}, qty: {product['qty']}")


def call_all_functions():
    ask_to_see_products_list = str(input("Ar nori pamatyti produktu lista? (T arba N): "))
    if ask_to_see_products_list == "T":
        print_all_products()

    ask_create_products_list = str("Ar nori sukurti nauja produktu lista? (T arba N): ")
    if ask_create_products_list == "T":
        create_products()

    want_to_delete_products = str(input("Ar nori istrinti kzk produkta? (T arba N): "))
    if want_to_delete_products == "T":
        delete_products(file_name, delete_condition)

    add_info_to_csv_file(file_name, products)


#TODO : parasyti cikla per products


call_all_functions()


