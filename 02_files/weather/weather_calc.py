import csv
from datetime import datetime


def calculate_seasonal_avg_temp(filtered_data):
    seasonal_avg_temp = {'Spring': {}, 'Summer': {}, 'Autumn': {}, 'Winter': {}}

    for data_point in filtered_data:
        year = data_point['date'].year
        month = data_point['date'].month
        mean_temp = data_point['mean_temp']

        if 3 <= month <= 5:  # Spring: March (3) to May (5)
            season = 'Spring'
        elif 6 <= month <= 8:  # Summer: June (6) to August (8)
            season = 'Summer'
        elif 9 <= month <= 11:  # Autumn: September (9) to November (11)
            season = 'Autumn'
        else:  # Winter: December (12) to February (2)
            season = 'Winter'

        if year not in seasonal_avg_temp[season]:
            seasonal_avg_temp[season][year] = {'sum': mean_temp, 'count': 1}
        else:
            seasonal_avg_temp[season][year]['sum'] += mean_temp
            seasonal_avg_temp[season][year]['count'] += 1

    result = {}
    for season, year_data in seasonal_avg_temp.items():
        season_results = {}
        for year, data in year_data.items():
            avg_temp = data['sum'] / data['count']
            season_results[year] = avg_temp
        result[season] = season_results

    return result

# Example usage with your filtered_data
filtered_data = [{'date': datetime(2009, 3, 15, 0, 0), 'mean_temp': 9.0},
                {'date': datetime(2009, 6, 15, 0, 0), 'mean_temp': 20.0},
                {'date': datetime(2009, 9, 15, 0, 0), 'mean_temp': 15.5},
                {'date': datetime(2009, 12, 15, 0, 0), 'mean_temp': 5.0},
                # Add more data points for other years and seasons...
               ]

seasonal_avg_temp = calculate_seasonal_avg_temp(filtered_data)
print(seasonal_avg_temp)




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

process_data_for_each_day()
seasonal_avg_temp = calculate_seasonal_avg_temp(filtered_data)
print(seasonal_avg_temp)