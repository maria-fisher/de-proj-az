import random
import csv
from datetime import datetime, timedelta

# Function to generate random environmental sensor data for CO2 levels
def generate_co2_data(timestamp, station):
    # Simulate sensor failure with 10% probability
    if random.random() < 0.1:
        co2_min = 0
        co2_max = 0
    else:
        # Generate random CO2 data within reasonable ranges
        co2_min = round(random.uniform(300, 1500), 2)
        co2_max = round(random.uniform(co2_min, 2000), 2)
    
    return [timestamp, station, co2_min, co2_max]

# Function to determine season based on month
def get_season(month):
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Autumn"
    else:
        return "Winter"

# Function to generate data for CO2 levels for a given month
def generate_month_co2_data(year, month):
    start_date = datetime(year, month, 1)
    end_date = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1) - timedelta(seconds=1)
    current_date = start_date
    data = []
    while current_date < end_date:
        for station in stations:
            season = get_season(current_date.month)
            timestamp = current_date.strftime("%Y-%m-%d %H:%M:%S")
            co2_data = generate_co2_data(timestamp, station)
            data.append([season] + co2_data)
            current_date += timedelta(minutes=1)
    return data

# Define stations
stations = ["Station A", "Station B", "Station C", "Station D"]

# Generate data for CO2 levels for each month in 2023
co2_data = []
for month in range(1, 13):
    co2_data += generate_month_co2_data(2023, month)

# Add event_id as the first column
event_id = 1
for row in co2_data:
    row.insert(0, event_id)
    event_id += 1


# Save CO2 data to CSV file
with open("co2_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["event_id", "season", "timestamp", "station", "co2_min", "co2_max"])
    writer.writerows(co2_data)
