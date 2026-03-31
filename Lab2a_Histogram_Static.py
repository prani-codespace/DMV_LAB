import matplotlib.pyplot as plt

# Sample data
data = [35, 42, 48, 50, 55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 95,
         30, 40, 45, 52, 58, 63, 67, 73, 77, 83, 87]

# Plotting histogram
plt.hist(data, bins=6, color='green', edgecolor='black')  

# Adding labels and title
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Static Histogram")

# Adding grid
plt.grid(True)

# Display the plot
plt.show()