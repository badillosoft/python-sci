import re

m = re.search("(\d+)/(\d+)/(\d+)", "1/5/88")

print m.group(1)
print m.group(2)
print m.group(3)

