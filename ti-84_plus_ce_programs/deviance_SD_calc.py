import math

# Prompt the user for the number of trials
num_trials = int(input("Enter the number of trials: "))

# Prompt the user for the values of each data point in the trials
data_points = []
for i in range(num_trials):
    data_point = float(input(f"Enter the value for data point {i+1}: "))
    data_points.append(data_point)

# Calculate the mean
mean = sum(data_points) / num_trials

# Calculate the sum of squared differences from the mean
sum_squared_diff = sum((x - mean) ** 2 for x in data_points)

# Calculate the variance
variance = sum_squared_diff / num_trials

# Calculate the standard deviation
standard_deviation = math.sqrt(variance)

# Calculate the deviance
deviance = math.sqrt(sum_squared_diff)

# Display the result to the user
print(f"Deviance: {deviance}")
print(f"Standard Deviation: {standard_deviation}")
