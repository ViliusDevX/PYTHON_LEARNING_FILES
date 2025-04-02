usd_eur = 0.91
eur_usd = 1.10
rub_usd = 0.013


def convert_price(amount, currency_from, currency_to):
    if currency_from == 'EUR':
        amount *= eur_usd
    elif currency_from == 'RUB':
        amount *= rub_usd

    if currency_to == 'EUR':
        amount /= eur_usd
    elif currency_to == 'RUB':
        amount /= rub_usd

    return amount


def format_price(amount, currency):
    price = f"{amount:.2f}"
    if currency == 'EUR':
        return price + '€'
    elif currency == 'USD':
        return price + '$'
    elif currency == 'RUB':
        return price + '₽'


rub_to_eur = convert_price(250, 'RUB', 'EUR')
print(f"{format_price(250, 'RUB')} = {format_price(rub_to_eur, 'EUR')}")

eur_to_rub = convert_price(300, 'EUR', 'RUB')
print(f"{format_price(300, 'EUR')} = {format_price(eur_to_rub, 'RUB')}")

usd_to_eur = convert_price(400, 'USD', 'EUR')
print(f"{format_price(400, 'USD')} = {format_price(usd_to_eur, 'EUR')}")