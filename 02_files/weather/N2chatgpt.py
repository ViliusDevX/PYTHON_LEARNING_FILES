import csv
from datetime import datetime


def process_data_for_each_day(data):
    for row in data:
        date = datetime.strptime(row['date'], '%Y%m%d')
        mean_temp = float(row['mean_temp'])

        print(f"Date: {date.strftime('%Y-%m-%d')}")
        print(f"Mean temp: {mean_temp}")


with open('193_london_weather.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

    for month in range(1, 13):
        for year in range(1979, 2021):
            filtered_data = []
            for row in data:
                date = datetime.strptime(row['date'], '%Y%m%d')
                if date.month == month and date.year == year:
                    filtered_data.append(row)
            if filtered_data:
                print(f"Processing data for {datetime(year, month, 1).strftime('%Y-%m')}")
                process_data_for_each_day(filtered_data)


process_data_for_each_day(csv_file)
