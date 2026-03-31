import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ax.set_xlim(0, 12)
ax.set_ylim(0, 30)

x_data = []
y_data = []

line, = ax.step([], [], where='post', color='blue', marker='o')

# Proper step-like values
y_values = [10, 10, 10,
            20, 20, 20,
            15, 15,
            25, 25, 25,
            18, 18]

def update(frame):
    x_data.append(frame)
    y_data.append(y_values[frame])
    
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update, frames=len(y_values), interval=500, repeat=False)

plt.title("Animated Stair Chart (Real Step Values)")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()