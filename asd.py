# Sample list of daily movements
daily_movements = [35, 22, 46, 12, 75,]  # Replace '...' with your actual values

# Specify the goal distance (in cm)
goal_distance = 1000  # Replace with your actual goal distance

total_distance = 0
days = 0

# Iterate through the list of daily movements until the total distance reaches the goal
for movement in daily_movements:
    total_distance += movement
    days += 1

    if total_distance >= goal_distance:
        break

# Print the results
print("Total Distance:", total_distance, "cm")
print("Days to Reach Goal:", days, "days")
