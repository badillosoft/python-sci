import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

map = Basemap(projection='cea',
    llcrnrlat=0, urcrnrlat=50,
    llcrnrlon=-120, urcrnrlon=-80)

map.drawmapboundary(fill_color="blue")

map.fillcontinents(color="coral", lake_color="yellow")

import re

def latlon(coord):
    #22°21′00″N
    r = re.search("(\d+).(\d+).(\d+)..(\w)", coord)

    g = int(r.group(1))
    m = int(r.group(2))
    s = int(r.group(3))

    return g + m / 60.0 + s / 3600.0

import sci

rutas = sci.load_xl("estados.xlsx", "Hoja2", "A1:C9")

X = []
Y = []

for ruta in rutas:
    latitud = ruta["Latitud"] 
    longitud = ruta["Longitud"]

    lat = latlon(latitud)
    lon = -latlon(longitud)

    x, y = map(lon, lat)

    X.append(x)
    Y.append(y)

    plt.plot(x, y, "ro")
    
    #plt.annotate("%s: %s" %(nombre_estado, nombre_ciudad),
    #    xy=(x, y), color="white")
    
plt.plot(X, Y, color="yellow", linewidth=3.0)

plt.show()