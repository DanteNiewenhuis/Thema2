import matplotlib.pyplot as plt
import matplotlib.cm

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize


map = Basemap(resolution='l',  # c, l, i, h, f or None
            projection='mill',
            llcrnrlon = -125.5, llcrnrlat = 24,
            urcrnrlon = -66, urcrnrlat = 50)

map.drawmapboundary(fill_color='#46bcec')
map.drawcountries(linewidth=1.5)
map.fillcontinents(color='white')
map.drawcoastlines()

map.readshapefile('st99_d00', name='states', drawbounds=True)
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])

ax = plt.gca() # get current axes instance

# get Texas and draw the filled polygon
seg = map.states[state_names.index('Connecticut')]
poly = Polygon(seg, facecolor='red',edgecolor='red')
ax.add_patch(poly)

plt.show()


