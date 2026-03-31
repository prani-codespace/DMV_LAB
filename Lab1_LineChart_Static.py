import matplotlib.pyplot as plt

# Sample data for x and y axis
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plotting line chart
plt.plot(x, y, marker='o',linestyle='--' , color='blue')  

# Adding labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Static Line Chart")

# Adding grid
plt.grid(True)

# Display the plot
plt.show()