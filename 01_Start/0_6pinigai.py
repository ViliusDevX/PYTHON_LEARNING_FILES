usd_eur = 0.91
eur_usd = 1.10
rub_usd = 0.013


def convert_price(sum, currency_from, currency_to):
    if currency_from == 'EUR':
        sum *= eur_usd
    elif currency_from == 'RUB':
        sum *= rub_usd

    if currency_to == 'EUR':
        sum /= eur_usd
    elif currency_to == 'RUB':
        sum /= rub_usd

    return sum


def format_price(sum, currency):
    price = f"{sum:.2f}"
    if currency == 'EUR':
        return price + '€'
    elif currency == 'USD':
        return price + '$'
    elif currency == 'RUB':
        return price + '₽'


write_your_sum = int(input("Jūsų suma: "))
write_your_currency = input("Jūsų valiuta: ")
write_your_currency_to = input("Jūsų valiuta i kuria konvertuojat: ")


converted_price = convert_price(write_your_sum, write_your_currency, write_your_currency_to)
print(f"{format_price(write_your_sum, write_your_currency)} = {format_price(converted_price, write_your_currency_to)}")
