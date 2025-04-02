def ask_product_list():
    product_list = []
    ask = input("ar krausi dar prekes i krepsi?")
    if ask == "T":
        type_product_name = input("ivesk prekes pavadinima")
        product_list.append({type_product_name})
        ask_product_list()
    else:
        print(product_list)

ask_product_list()