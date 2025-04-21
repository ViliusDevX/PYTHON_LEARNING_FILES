import csv
from datetime import datetime


def calculate_seasonal_avg_temp(filtered_data):
    seasonal_avg_temp = {}

    for data_point in filtered_data:
        year = data_point['date'].year
        month = data_point['date'].month
        mean_temp = data_point['mean_temp']

        if year not in seasonal_avg_temp:
            seasonal_avg_temp[year] = {'Spring': [], 'Summer': [], 'Autumn': [], 'Winter': []}

        if 3 <= month <= 5:  # Spring: March (3) to May (5)
            season = 'Spring'
        elif 6 <= month <= 8:  # Summer: June (6) to August (8)
            season = 'Summer'
        elif 9 <= month <= 11:  # Autumn: September (9) to November (11)
            season = 'Autumn'
        else:  # Winter: December (12) to February (2)
            season = 'Winter'

        seasonal_avg_temp[year][season].append(mean_temp)

    for year in seasonal_avg_temp:
        for season in seasonal_avg_temp[year]:
            avg_temp = sum(seasonal_avg_temp[year][season]) / len(seasonal_avg_temp[year][season])
            seasonal_avg_temp[year][season] = avg_temp

    return seasonal_avg_temp


def load_and_clean_csv_file(file_name):
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)
        filtered_rows = []

        for row in data:
            if row['mean_temp'] != "":
                row['date'] = datetime.strptime(row['date'], '%Y%m%d')
                row['mean_temp'] = float(row['mean_temp'])
                filtered_rows.append(row)

    return filtered_rows


filtered_csv = load_and_clean_csv_file('193_london_weather.csv')
seasonal_avg_temp = calculate_seasonal_avg_temp(filtered_csv)
print(seasonal_avg_temp)
