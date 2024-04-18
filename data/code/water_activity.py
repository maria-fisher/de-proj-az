import random
import csv
from datetime import datetime, timedelta

# Function to generate random environmental sensor data for water activity
def generate_water_activity_data(timestamp, station):
    # Simulate sensor failure with 10% probability
    if random.random() < 0.1:
        water_activity_min = 0
        water_activity_max = 0
    else:
        # Generate random water activity data within reasonable ranges
        water_activity_min = round(random.uniform(0.9, 1), 2)
        water_activity_max = round(random.uniform(water_activity_min, 1), 2)
    
    return [timestamp, station, water_activity_min, water_activity_max]

# Function to generate data for water activity for a given month
def generate_month_water_activity_data(year, month):
    start_date = datetime(year, month, 1)
    end_date = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1) - timedelta(seconds=1)
    current_date = start_date
    data = []
    while current_date < end_date:
        for station in stations:
            season = get_season(current_date.month)
            timestamp = current_date.strftime("%Y-%m-%d %H:%M:%S")
            water_activity_data = generate_water_activity_data(timestamp, station)
            data.append([season] + water_activity_data)
            current_date += timedelta(minutes=1)
    return data

# Define stations
stations = ["Station A", "Station B", "Station C", "Station D"]

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

# Generate data for water activity for each month in 2023
water_activity_data = []
for month in range(1, 13):
    water_activity_data += generate_month_water_activity_data(2023, month)

# Add event_id as the first column
event_id = 1
for row in water_activity_data:
    row.insert(0, event_id)
    event_id += 1

# Save water activity data to CSV file
with open("water_activity_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["event_id", "season", "timestamp", "station", "wa_min", "wa_max"])
    writer.writerows(water_activity_data)
