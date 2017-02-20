# -*- coding: utf-8 -*-

import re

m = re.search("(\d+)º(\d+)'(\d+)''(\w)", "28º13'00''N")

grados = int(m.group(1))
minutos = int(m.group(2))
segundos = int(m.group(3))

lat = grados + minutos / 60.0 + segundos / 3600.0

print lat, grados, minutos, segundos