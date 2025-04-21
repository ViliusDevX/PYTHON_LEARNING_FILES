import csv
import datetime

# Open the CSV file
with open('193_london_weather.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Define the current date
    current_date = datetime.date.today()

    # Define the start and end date of the current month
    start_date = current_date.replace(day=1)
    if current_date.month == 12:
        end_date = current_date.replace(year=current_date.year + 1, month=1, day=1)
    else:
        end_date = current_date.replace(month=current_date.month + 1, day=1)

    # Iterate through the CSV file
    for row in csv_reader:
        # Parse the date from the CSV row
        row_date = datetime.datetime.strptime(row['date'], '%Y%m%d').date()

        # Check if the date is within the current month
        if start_date <= row_date < end_date:
            # Process the row for the current day
            print(f"Processing data for {row_date}:")
            print(f"Cloud Cover: {row['cloud_cover']}")
            print(f"Sunshine: {row['sunshine']}")
            # Add more processing as needed
