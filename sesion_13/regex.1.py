import re

r = re.search("(\d+)°(\d+)′(\d+)″(\w)", "102°24′00″W")

# ".*@.*\..*"

g = int(r.group(1))
m = int(r.group(2))
s = int(r.group(3))
d = r.group(4)

lat = g + m / 60.0 + s / 3600.0

print lat, d
