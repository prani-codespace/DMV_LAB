# Question 6: Complete Graph using Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Take input
n = int(input("Enter number of vertices (>3): "))

if n <= 3:
    print("Enter number greater than 3")
else:
    # Create circular points
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta)
    y = np.sin(theta)

    plt.figure()
    
    # Plot vertices
    plt.scatter(x, y, color='blue')

    # Connect every vertex to every other vertex
    for i in range(n):
        for j in range(i+1, n):
            plt.plot([x[i], x[j]], [y[i], y[j]], color='black')

    plt.title("Complete Graph")
    plt.show()
