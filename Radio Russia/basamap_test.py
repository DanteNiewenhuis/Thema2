import matplotlib.pyplot as plt
import matplotlib.cm

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

# Ukraine
m = Basemap(resolution='c',
            projection='mill')

m.readshapefile('/home/alexander/PycharmProjects/Thema 2/ukraineshapefiles/Ukraine', 'ukraine')
#m.drawcountries(linewidth=1)
m.drawcoastlines(linewidth=0.1)
#m.drawrivers(color='blue')
#m.drawmapboundary(fill_color='blue')


plt.show()



