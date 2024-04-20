import pandas as pd
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
        month = current_date.month
        season = get_season(month)
        for station in stations:
            if season == "Winter":
                co2 = random.uniform(300, 500)  # Adjust CO2 range for winter
            elif season == "Spring":
                co2 = random.uniform(400, 600)  # Adjust CO2 range for spring
            elif season == "Summer":
                co2 = random.uniform(300, 500)  # Adjust CO2 range for summer
            else:  # Fall
                co2 = random.uniform(400, 600)  # Adjust CO2 range for fall
            
            # Append data
            data.append([current_date, station, co2, month])
        
        current_date += timedelta(hours=1)
    
    return data

# Define stations and corresponding food
stations = ["Station A", "Station B", "Station C", "Station D", "Station E",
            "Station F", "Station G", "Station H", "Station I", "Station J"]

# Generate data
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31, 23)

# Generate data for the entire year
data = generate_data(start_date, end_date)

# Create DataFrame
df = pd.DataFrame(data, columns=["Timestamp", "Station", "CO2 (ppm)", "Month"])

# Add event_id
df.insert(0, "Event ID", range(1, 1 + len(df)))

# Save to CSV
df.to_csv("food_storage_co2_levels.csv", index=False)
