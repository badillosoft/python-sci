from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='cea',llcrnrlat=0,urcrnrlat=50,\
            llcrnrlon=-120,urcrnrlon=-80,resolution='c')

m.drawcoastlines()

m.fillcontinents(color='coral',lake_color='red')

# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,10.))
m.drawmeridians(np.arange(-180.,181.,10.))

m.drawmapboundary(fill_color='blue')

lats = [25, 25, 25, 25, 25]

lons = np.linspace(-120, -80, 5)

X, Y = m(lons, lats)

m.plot(X, Y, "k", linewidth=2.0)
m.plot(X, Y, "r*")

plt.annotate('Isla', xy=(X[1], Y[1]), xytext=(X[1] + 100000, Y[1] + 100000),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.title("Mundo")

plt.show()