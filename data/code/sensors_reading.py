import random
from datetime import datetime, timedelta

# Define station IDs
stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Define season types with associated environmental data ranges
seasons = {
    "Spring": {"temp": (10, 20), "rh": (40, 60), "co2": (300, 600), "wa": (0.1, 0.5)},
    "Summer": {"temp": (25, 35), "rh": (50, 70), "co2": (200, 500), "wa": (0.3, 0.7)},
    "Autumn": {"temp": (10, 20), "rh": (40, 60), "co2": (300, 600), "wa": (0.1, 0.5)},
    "Winter": {"temp": (-5, 5), "rh": (30, 50), "co2": (400, 700), "wa": (0.05, 0.3)}
}

# Generate data
data = []
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

while start_date <= end_date:
    for station_id in range(1, len(stations) + 1):
        season = None
        if 3 <= start_date.month <= 5:
            season = "Spring"
        elif 6 <= start_date.month <= 8:
            season = "Summer"
        elif 9 <= start_date.month <= 11:
            season = "Autumn"
        else:
            season = "Winter"

        event_id = len(data) + 1
        temp = random.uniform(seasons[season]["temp"][0], seasons[season]["temp"][1])
        rh = random.uniform(seasons[season]["rh"][0], seasons[season]["rh"][1])
        co2 = random.uniform(seasons[season]["co2"][0], seasons[season]["co2"][1])
        wa = random.uniform(seasons[season]["wa"][0], seasons[season]["wa"][1])
        station = stations[station_id - 1]
        data.append((event_id, temp, rh, co2, wa, station, start_date.strftime("%Y-%m-%d %H:%M:%S")))

    start_date += timedelta(hours=1)

# Write data to file
with open("sensors_reading_.csv", "w") as f:
    f.write("event_id,temp,rh,co2,wa,station,datetime\n")
    for row in data:
        f.write(",".join(map(str, row)) + "\n")

