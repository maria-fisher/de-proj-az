import random

# Define stations
stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Define food types and their corresponding stations
food_types = {
    'Dried food': ['A', 'B'],
    'Dairy': ['C', 'D'],
    'Drinks': ['E', 'F'],
    'Fresh veg': ['G', 'H'],
    'Meat': ['I', 'J']
}

# Generate data
data = []

for food_type, assigned_stations in food_types.items():
    for station in assigned_stations:
        data.append((station, food_type))

# Write data to file
with open("station_food.csv", "w") as f:
    f.write("station,food_type\n")
    for row in data:
        f.write(",".join(map(str, row)) + "\n")