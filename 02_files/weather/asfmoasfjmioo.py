import csv
from datetime import datetime

filtered_data = []



# def abc():
#     temps = {}
#     for row in filtered_data:
#         index = row['date'].year
#         mean_temp = row["mean_temp"]
#         if temps.get(index) is not None:
#             temps[index].append(mean_temp)
#         else:
#             temps[index] = [mean_temp]
#     for year, temperatures in temps.items():
#         summed_temps = sum(temperatures)
#         len_temps = len(temperatures)
#         avg_yearly_temp = summed_temps /  len_temps
#         print(year, avg_yearly_temp)
#     # print(temps)


def calculate_average_seasonal_temp(data):
    total_mean_temp = 0
    num_days = len(data)

    for row in data:
        mean_temp = float(row['mean_temp'])
        total_mean_temp += mean_temp

    if num_days > 0:
        avg_mean_temp = total_mean_temp / num_days
        return avg_mean_temp
    else:
        return None


def load_and_clean_info():
    global filtered_data
    with open('193_london_weather.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

        for row in data:
            if row['mean_temp'] != "":
                row['date'] = datetime.strptime(row['date'], '%Y%m%d')
                row['mean_temp'] = float(row['mean_temp'])
                filtered_data.append(row)


load_and_clean_info()
print(filtered_data)
# abc()

# average_temp = calculate_average_seasonal_temp(filtered_data)
# if average_temp is not None:
#     print(f"Average seasonal temperature: {average_temp:.2f}")
# else:
#     print("No data to calculate average.")

