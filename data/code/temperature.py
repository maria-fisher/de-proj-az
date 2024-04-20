import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate seasonal variation
def get_season(month):
    if month in [12, 1, 2]:  # Winter
        return "Winter"
    elif month in [3, 4, 5]:  # Spring
        return "Spring"
    elif month in [6, 7, 8]:  # Summer
        return "Summer"
    else:  # Fall
        return "Fall"

# Function to generate environmental data
def generate_data(start_date, end_date):
    data = []
    current_date = start_date
    while current_date <= end_date:
        hour = current_date.hour
        month = current_date.month
        season = get_season(month)
        for station in stations:
            if season == "Winter":
                temperature = random.uniform(-5, 5)  # Adjust temperature range for winter
            elif season == "Spring":
                temperature = random.uniform(5, 20)  # Adjust temperature range for spring
            elif season == "Summer":
                temperature = random.uniform(20, 35)  # Adjust temperature range for summer
            else:  # Fall
                temperature = random.uniform(10, 25)  # Adjust temperature range for fall
            
            # Append data
            data.append([current_date, station, temperature, month])
        
        current_date += timedelta(hours=1)
    
    return data

# Define stations and corresponding food
stations = ["Station A", "Station B", "Station C", "Station D", "Station E",
            "Station F", "Station G", "Station H", "Station I", "Station J"]
foods = ["Fresh Vegetables", "Dried Food", "Drinks", "Dairy", "Meat", "Seafood", "Canned Goods"]

# Generate data
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31, 23)

# Generate data for the entire year
data = generate_data(start_date, end_date)

# Create DataFrame
df = pd.DataFrame(data, columns=["Timestamp", "Station", "Temperature (°C)", "Month"])

# Add food type
food_types = []
for _ in range(len(df)):
    if random.random() < 0.7:  # 70% chance of dried food or drinks
        food_types.append(random.choice(["Dried Food", "Drinks"]))
    else:
        food_types.append(random.choice(["Fresh Vegetables", "Dairy", "Meat", "Seafood", "Canned Goods"]))
df["Food Type"] = food_types

# Add event_id
df.insert(0, "Event ID", range(1, 1 + len(df)))

# Save to CSV
df.to_csv("food_storage_temperature.csv", index=False)
