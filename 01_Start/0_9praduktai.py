products = {
    {
        "GR01":
            {"product name": "grietine",
             "price": 3.99
             }},
    {
        "JO01":
            {"product name": "jogurt",
             "price": 2.49
             }},
    {
        "SUR01": {
            "product name": "surelis",
            "price": 0.59
        }}
}

shopping_bag = [
    {
        "product id": "GR01",
        "quantity": 4
    },
    {
        "product id": "JO01",
        "quantity": 2
    }
]


def add_cart_item(product_id, quantity):
    shopping_bag.append({"product id": product_id,
                  "quantity": quantity})


def get_cart_item(cart_item_index):
    get_bag_item = shopping_bag[cart_item_index]
    get = get_bag_item.get("product id")
    product_xujne_kazkokia_naxui = products[get]
    product_qty = get_bag_item["quantity"]
    total_price = product_qty * product_xujne_kazkokia_naxui["price"]

get_cart_item(1)
exit()
