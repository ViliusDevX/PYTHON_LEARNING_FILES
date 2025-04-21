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


def delete_product_by_id(product_id):
    global products
    products = [product for product in products if product["id"] != product_id]


def add_info_to_csv_file(file_path, list_of_dicts):
    keys = list_of_dicts[0].keys()
    with open(file_path, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys, quoting = csv.QUOTE_NONNUMERIC)
        dict_writer.writeheader()
        dict_writer.writerows(list_of_dicts)


def print_all_products():
    for product in products:
        print(f"id: {product['id']}, name: {product['name']}, qty: {product['qty']}")


def menu():
    print_all_products()
    what_to_do = input("Irasyk 0 kad prideti produkta prie listo, irasyk 1 jeigu nori istrinti produkta is listo arba "
                       "irasyk 2 kad --test-- : ")
    if what_to_do == "0":
        create_products()
    elif what_to_do == "1":
        what_to_delete = input("Koki produkta nori istrinti (pagal ID): ")
        delete_product_by_id(what_to_delete)
    elif what_to_do == "2":
        print("Sveikinu, tu sekmingai --test--")
    else:
        raise Exception("Blogai ivedei skaiciu (pasirinkima)")
    more_menu = input("Ar nori dar karta pasinaudoti menu? (T arba N): ")
    if more_menu == "T":
        menu()


menu()

