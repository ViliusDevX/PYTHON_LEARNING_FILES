import csv


class CSV_Helper:

    @staticmethod
    def save(filename, list_of_dicts):
        if not list_of_dicts:
            return

        with open(filename, 'w', newline='') as csvfile:
            fieldnames = list_of_dicts[0].keys()

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in list_of_dicts:
                writer.writerow(
                    {key: f"{value}" if isinstance(value, (int, float)) else value for key, value in row.items()})

    @staticmethod
    def read(filename):
        data = []

        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = {}
                for key, value in row.items():
                    try:
                        float_value = float(value)
                        if float_value.is_integer():
                            item[key] = int(float_value)
                        else:
                            item[key] = float_value
                    except ValueError:
                        item[key] = value

                data.append(item)

        return data


random_list = [
    {'name': 'Apple', 'value': 42.4, 'category': 'Fruit'},
    {'name': 'Carrot', 'value': 75.12367, 'category': 'Vegetable'},
    {'name': 'Laptop', 'value': 1200, 'category': 'Electronics'},
    {'name': 'Book', 'value': 15, 'category': 'Stationery'},
    {'name': 'Sunglasses', 'value': 50, 'category': 'Fashion'}
]

file_name = 'my_data.csv'

CSV_Helper.save(file_name, random_list)
CSV_Helper.read(file_name)

for item in random_list:
    print(item)
