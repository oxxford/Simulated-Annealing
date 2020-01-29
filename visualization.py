import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

fig = plt.figure()
ax = plt.axes(ylim=(40, 62), xlim=(25, 140))
line, = ax.plot([], [], lw=3)

data = np.load('data.npy')
names = pd.read_csv('names.csv', encoding='utf-16', header=None)

ax.scatter(data[0][1], data[0][0])
for i in range(len(names)):
    ax.annotate(names.iloc[i][1], (data[0][1][i],  data[0][0][i]))

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = data[i][1]
    y = data[i][0]
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=len(data), interval=20, blit=True)

plt.show()