# Question 4: Moving Circle Animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()

# Set limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create a circle
circle = plt.Circle((0, 5), 0.5, color='blue')
ax.add_patch(circle)

# Animation function
def update(frame):
    circle.center = (frame, 5)  # Move circle horizontally
    return circle,

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), interval=50)

plt.show()
