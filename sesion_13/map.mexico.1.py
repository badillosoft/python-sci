import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

map = Basemap(projection='cea',
    llcrnrlat=0, urcrnrlat=50,
    llcrnrlon=-120, urcrnrlon=-80)

map.drawmapboundary(fill_color="blue")

map.fillcontinents(color="red", lake_color="yellow")

lat = 22.35
lon = -102.4

x, y = map(lon, lat)

plt.plot(x, y, "ko")

plt.show()