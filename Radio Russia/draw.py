import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import matplotlib.patches as mpatches
import analyse
import numpy as np

def draw_america(input, signal_costs):
    font1 = FontProperties()
    font1.set_family('monospace')
    font1.set_size(14)
    map = Basemap(resolution='i',  # c, l, i, h, f or None
                projection='mill',
                llcrnrlon = -125.5, llcrnrlat = 24,
                urcrnrlon = -66, urcrnrlat = 50)

    map.drawmapboundary(fill_color='#46bcec')
    map.drawcountries(linewidth=1)
    map.fillcontinents(color='white')

    map.readshapefile('st99_d00', name='states', drawbounds=True)
    state_names = []
    for shape_dict in map.states_info:
        state_names.append(shape_dict['NAME'])

    ax = plt.gca() # get current axes instance

    color_dict = {'zA':'red', 'zB':'blue', 'zC':'yellow', 'zD':'green', 'zE':'pink', 'zF':'cyan', 'zG':'orange'}
    for nshape, seg in enumerate(map.states):
        for state in input:
            if state_names[nshape] == state.name:
                color = color_dict[state.signal]
                poly = Polygon(seg, facecolor=color)
                ax.add_patch(poly)
                break

    freq = analyse.signal_frequentie(input)
    spacing = {}
    for signal in color_dict:
        if signal not in freq:
            freq[signal] = 0
        if freq[signal] > 9:
            spacing[signal] = ' €'
        else:
            spacing[signal] = '  €'
    map_costs = analyse.get_cost(freq, signal_costs)
    print(map_costs)

    red_patch = mpatches.Patch(color='red', label='zA'+ ' {' + str(freq['zA']) + '}' +
                                                  spacing['zA'] + str(signal_costs['zA']))
    blue_patch = mpatches.Patch(color='blue', label='zB'+ ' {' + str(freq['zB']) + '}' +
                                                    spacing['zB'] + str(signal_costs['zB']))
    yellow_patch = mpatches.Patch(color='yellow', label='zC'+ ' {' + str(freq['zC']) + '}' +
                                                        spacing['zC'] + str(signal_costs['zC']))
    green_patch = mpatches.Patch(color='green', label='zD'+ ' {' + str(freq['zD']) + '}' +
                                                      spacing['zD'] + str(signal_costs['zD']))
    pink_patch = mpatches.Patch(color='pink', label='zE'+ ' {' + str(freq['zE']) + '}' +
                                                    spacing['zE'] + str(signal_costs['zE']))
    cyan_patch = mpatches.Patch(color='cyan', label='zF'+ ' {' + str(freq['zF']) + '}' +
                                                    spacing['zF'] + str(signal_costs['zF']))
    orange_patch = mpatches.Patch(color='orange', label='zG'+ ' {' + str(freq['zG']) + '}' +
                                                        spacing['zG'] + str(signal_costs['zG']))

    plt.legend(handles=[red_patch, blue_patch, yellow_patch, green_patch, pink_patch, cyan_patch, orange_patch],
               loc=4, prop={'family': 'monospace'})

    plt.text(0, 0, 'costs = ' + str(map_costs),
            horizontalalignment='left',
            verticalalignment='bottom',
            fontsize=12,
            transform=ax.transAxes,
            backgroundcolor="white",
            fontproperties=font1)
    plt.show()

#based on https://pythonspot.com/en/matplotlib-bar-chart/
def bar_plot(dict, title, x_label, y_label):
    objects = (dict.keys())
    y_pos = np.arange(len(objects))
    performance = [dict[x] for x in objects]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title, fontsize=20)

    plt.show()