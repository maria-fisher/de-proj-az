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
        food_id = len(data) + 1
        quantity = random.randint(10, 1000)
        price_unity = random.uniform(1.0, 10.0)
        price_total = quantity * price_unity
        data.append((food_id, food_type, station, quantity, price_unity, price_total))

# Write data to file
with open("food_data.csv", "w") as f:
    f.write("food_id,food_type,station,quantity,price_unity,price_total\n")
    for row in data:
        f.write(",".join(map(str, row)) + "\n")