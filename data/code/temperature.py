import random
import csv
from datetime import datetime, timedelta

# Function to generate random environmental sensor data
def generate_sensor_data(timestamp, station):
    # Simulate sensor failure with 10% probability
    if random.random() < 0.1:
        temperature_min = "Sensor Failure"
        temperature_max = "Sensor Failure"
    else:
        # Generate random temperature data within reasonable ranges
        temperature_min = round(random.uniform(-20, 40), 2)
        temperature_max = round(random.uniform(temperature_min, 40), 2)
    
    return [timestamp, station, temperature_min, temperature_max]

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

# Function to generate data for a given month
def generate_month_data(year, month):
    start_date = datetime(year, month, 1)
    end_date = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1)
    current_date = start_date
    data = []
    while current_date < end_date:
        for station in stations:
            season = get_season(current_date.month)
            timestamp = current_date.strftime("%d-%m-%Y %H:%M:%S")
            sensor_data = generate_sensor_data(timestamp, station)
            data.append([season] + sensor_data)
            current_date += timedelta(minutes=1)
    return data

# Define stations
stations = ["Station A", "Station B", "Station C", "Station D"]

# Define event_id
event_id = 1

# Generate data for each month in 2023
data = []
for month in range(1, 13):
    data += generate_month_data(2023, month)

# Add event_id as the first column
for row in data:
    row.insert(0, event_id)
    event_id += 1

# Save data to CSV file
with open("temperature_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Event_ID", "Season", "Timestamp", "Station", "Temperature_Min(°C)", "Temperature_Max(°C)"])
    writer.writerows(data)

import random
import csv
from datetime import datetime, timedelta

# Function to generate random environmental sensor data
def generate_sensor_data(timestamp, station):
    # Simulate sensor failure with 10% probability
    if random.random() < 0.1:
        temperature_min = 0
        temperature_max = 0
    else:
        # Generate random temperature data within reasonable ranges
        temperature_min = round(random.uniform(-20, 40), 2)
        temperature_max = round(random.uniform(temperature_min, 40), 2)
    
    return [timestamp, station, temperature_min, temperature_max]

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

# Function to generate data for a given month
def generate_month_data(year, month):
    start_date = datetime(year, month, 1)
    end_date = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1) - timedelta(seconds=1)
    current_date = start_date
    data = []
    while current_date < end_date:
        for station in stations:
            season = get_season(current_date.month)
            timestamp = current_date.strftime("%Y-%m-%d %H:%M:%S")
            sensor_data = generate_sensor_data(timestamp, station)
            data.append([season] + sensor_data)
            current_date += timedelta(minutes=1)
    return data

# Define stations
stations = ["Station A", "Station B", "Station C", "Station D"]

# Define event_id
event_id = 1

# Generate data for each month in 2023
data = []
for month in range(1, 13):
    data += generate_month_data(2023, month)

# Add event_id as the first column
for row in data:
    row.insert(0, event_id)
    event_id += 1

# Save data to CSV file
with open("temperature_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["event_id", "season", "timestamp", "station", "temperature_min", "temperature_max"])
    writer.writerows(data)
