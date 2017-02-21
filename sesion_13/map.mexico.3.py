import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

map = Basemap(projection='cea',
    llcrnrlat=0, urcrnrlat=50,
    llcrnrlon=-120, urcrnrlon=-80)

map.drawmapboundary(fill_color="blue")

map.fillcontinents(color="red", lake_color="yellow")

import re

def latlon(coord):
    #22°21′00″N
    r = re.search("(\d+).(\d+).(\d+)..(\w)", coord)

    g = int(r.group(1))
    m = int(r.group(2))
    s = int(r.group(3))

    return g + m / 60.0 + s / 3600.0

import sci

estados = sci.load_xl("estados.xlsx", "Hoja1", "A1:E101")

for ciudad in estados:
    nombre_estado = ciudad["Estado"]
    nombre_ciudad = ciudad["Ciudad"]

    latitud = ciudad["Latitud"] 
    longitud = ciudad["Longitud"]

    lat = latlon(latitud)
    lon = -latlon(longitud)

    x, y = map(lon, lat)

    plt.plot(x, y, "ko")
    
    #plt.annotate("%s: %s" %(nombre_estado, nombre_ciudad),
    #    xy=(x, y), color="white")
    

plt.show()