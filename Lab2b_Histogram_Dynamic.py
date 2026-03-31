import matplotlib.pyplot as plt

# Take number of data points from user
n = int(input("Enter number of values: "))

data = []

# Take each value from the user
for i in range(n):
    value = int(input(f"Enter value {i+1}: "))
    data.append(value)

# Take number of bins from user
bins = int(input("Enter number of bins: "))

# Plot histogram with user input data
plt.hist(data, bins=bins, color='yellow', edgecolor='black')

# Add labels and title
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram using User Input")

# Add grid
plt.grid(True)

# Display the plot
plt.show()
