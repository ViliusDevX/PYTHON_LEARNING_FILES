currency_usd = "$"
currency_eur = "€"
currency_rub = "₽"

def format_price(amount, currency):
    price = f"{amount:.2f}"
    if currency == 'EUR':
        return price + '€'
    elif currency == 'USD':
        return price + '$'
    elif currency == 'RUB':
        return price + '₽'

    return


print(format_price(154, 'USD'))