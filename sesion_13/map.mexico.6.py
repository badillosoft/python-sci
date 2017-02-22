# -*- coding: utf-8 -*-

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

lats = sci.data_map(rutas, lambda ruta: latlon(ruta["Latitud"]))
lons = sci.data_map(rutas, lambda ruta: -latlon(ruta["Longitud"]))

latlons = zip(lats, lons)

XY = sci.data_map(latlons, lambda (lat, lon): map(lon, lat))

X = sci.data_map(XY, lambda (x, y): x)
Y = sci.data_map(XY, lambda (x, y): y)

plt.plot(X, Y)
plt.plot(X, Y, "ro")

plt.show()