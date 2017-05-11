import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

y = []
with open('testding.txt','r') as text:
    for line in text:
        line_split = line.split(",")
        for cost in line_split:
            if cost is not '':
                y.append(int(cost))
print(len(y))
x = np.arange(len(y))

fig, ax = plt.subplots()
line, = ax.plot(x, y, color='k')

def update(num, x, y, line):
    print('animate')
    line.set_data(x[:num], y[:num])
    line.axes.axis([0, x[num], 900, 1350])
    return line,

ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line],
                              interval=0.01, blit=True)
#ani.save('test.gif')
plt.show()