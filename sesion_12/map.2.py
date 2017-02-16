from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='cea',llcrnrlat=-50,urcrnrlat=50,\
            llcrnrlon=-120,urcrnrlon=60,resolution='c')

m.drawcoastlines()

m.fillcontinents(color='coral',lake_color='red')

# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,10.))
m.drawmeridians(np.arange(-180.,181.,10.))

m.drawmapboundary(fill_color='blue')

plt.title("Mundo")

plt.show()