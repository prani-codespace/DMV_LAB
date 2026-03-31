import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---- USER INPUT ----
limit = int(input("Enter axis limit (e.g., 10 for -10 to 10): "))
speed = int(input("Enter speed in ms (lower = faster, e.g., 100): "))

# Initial position
x, y = 0, 0

# Create figure
fig, ax = plt.subplots()
circle = plt.Circle((x, y), 0.5, color='blue')
ax.add_patch(circle)

# Set axis limits from user
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
def update(frame):
    circle.set_center((x, y))
    return circle,

# ---- KEYBOARD CONTROL ----
def on_key(event):
    global x, y
    
    if event.key == 'up':
        y += 1
    elif event.key == 'down':
        y -= 1
    elif event.key == 'left':
        x -= 1
    elif event.key == 'right':
        x += 1

# Connect keyboard
fig.canvas.mpl_connect('key_press_event', on_key)

# Animation with user-defined speed
ani = FuncAnimation(fig, update, interval=speed)

plt.show()