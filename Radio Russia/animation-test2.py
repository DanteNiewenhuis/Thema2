from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib.animation as animation
import readMap
from matplotlib.patches import Polygon
import matplotlib.patches as mpatches
import analyse

font1 = FontProperties()
font1.set_family('monospace')
font1.set_size(14)

input_list = readMap.read_complete_animation('testanimate.txt')

my_map = Basemap(resolution = 'l', area_thresh = 1000.0,
                 projection='mill',
                 llcrnrlon=-125.5, llcrnrlat=24,
                 urcrnrlon=-66, urcrnrlat=50)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'gray')
my_map.drawmapboundary()
my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))

my_map.readshapefile('st99_d00', name='states', drawbounds=True, linewidth=1.1)
state_names = []
for shape_dict in my_map.states_info:
    state_names.append(shape_dict['NAME'])

color_dict = {'zA': 'red', 'zB': 'blue', 'zC': 'yellow', 'zD': 'green', 'zE': 'pink', 'zF': 'cyan', 'zG': 'orange'}
signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
signal_costs = {'zA':19, 'zB':20, 'zC':21, 'zD':23, 'zE':36, 'zF':37, 'zG':38}
text_list = []

def init():
    ax = plt.gca()
    for nshape, seg in enumerate(my_map.states):
        poly = Polygon(seg, facecolor='grey')
        result = ax.add_patch(poly)
    return result,

# animation function.  This is called sequentially
def animate(i):
    ax = plt.gca()
    nodes = input_list[i]
    for nshape, seg in enumerate(my_map.states):
        for state in nodes:
            if state_names[nshape] == state.name:
                color = color_dict[state.signal]
                poly = Polygon(seg, facecolor=color)
                result = ax.add_patch(poly)
                break
    freq = analyse.signal_frequentie(nodes)
    spacing = {}
    for signal in color_dict:
        if signal not in freq:
            freq[signal] = 0
        if freq[signal] > 9:
            spacing[signal] = ' €'
        else:
            spacing[signal] = '  €'
    map_costs = analyse.get_cost(freq, signal_costs)

    red_patch = mpatches.Patch(color='red', label='zA' + ' {' + str(freq['zA']) + '}' +
                                                  spacing['zA'] + str(signal_costs['zA']))
    blue_patch = mpatches.Patch(color='blue', label='zB' + ' {' + str(freq['zB']) + '}' +
                                                    spacing['zB'] + str(signal_costs['zB']))
    yellow_patch = mpatches.Patch(color='yellow', label='zC' + ' {' + str(freq['zC']) + '}' +
                                                        spacing['zC'] + str(signal_costs['zC']))
    green_patch = mpatches.Patch(color='green', label='zD' + ' {' + str(freq['zD']) + '}' +
                                                      spacing['zD'] + str(signal_costs['zD']))
    pink_patch = mpatches.Patch(color='pink', label='zE' + ' {' + str(freq['zE']) + '}' +
                                                    spacing['zE'] + str(signal_costs['zE']))
    cyan_patch = mpatches.Patch(color='cyan', label='zF' + ' {' + str(freq['zF']) + '}' +
                                                    spacing['zF'] + str(signal_costs['zF']))
    orange_patch = mpatches.Patch(color='orange', label='zG' + ' {' + str(freq['zG']) + '}' +
                                                        spacing['zG'] + str(signal_costs['zG']))

    plt.legend(handles=[red_patch, blue_patch, yellow_patch, green_patch, pink_patch, cyan_patch, orange_patch],
               loc=4, prop={'family': 'monospace'})

    for txt in text_list:
        txt.set_visible(False)
    text = plt.text(0, 0, 'costs = ' + str(map_costs) + ' iterations = ' + str(i),
             horizontalalignment='left',
             verticalalignment='bottom',
             fontsize=12,
             transform=ax.transAxes,
             backgroundcolor="white",
             fontproperties=font1)
    text_list.append(text)
    return result,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init, frames=len(input_list), interval=1, blit=False)
anim.save('animation.gif', fps=100)

plt.show()