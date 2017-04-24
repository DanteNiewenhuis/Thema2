import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import matplotlib.patches as mpatches
import analyse

def draw_america(input, map_costs):
    map = Basemap(resolution='c',  # c, l, i, h, f or None
                projection='mill',
                llcrnrlon = -125.5, llcrnrlat = 24,
                urcrnrlon = -66, urcrnrlat = 50)

    map.drawmapboundary(fill_color='#46bcec')
    map.drawcountries(linewidth=1)
    map.fillcontinents(color='white')
    #map.drawcoastlines()

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
    for signal in color_dict:
        if signal not in freq:
            freq[signal] = 0

    red_patch = mpatches.Patch(color='red', label='zA'+ ' {' + str(freq['zA']) + '}')
    blue_patch = mpatches.Patch(color='blue', label='zB'+ ' {' + str(freq['zB']) + '}')
    yellow_patch = mpatches.Patch(color='yellow', label='zC'+ ' {' + str(freq['zC']) + '}')
    green_patch = mpatches.Patch(color='green', label='zD'+ ' {' + str(freq['zD']) + '}')
    pink_patch = mpatches.Patch(color='pink', label='zE'+ ' {' + str(freq['zE']) + '}')
    cyan_patch = mpatches.Patch(color='cyan', label='zF'+ ' {' + str(freq['zF']) + '}')
    orange_patch = mpatches.Patch(color='orange', label='zG'+ ' {' + str(freq['zG']) + '}')

    plt.legend(handles=[red_patch, blue_patch, yellow_patch, green_patch, pink_patch, cyan_patch, orange_patch],
               loc=4)

    plt.text(0, 0, 'costs = ' + str(map_costs),
            horizontalalignment='left',
            verticalalignment='bottom',
            fontsize=12,
            transform=ax.transAxes,
            backgroundcolor="white" )
    plt.show()