import sci

data = [
    { "x": 10, "y": 8 },
    { "x": 1, "y": 2 },
    { "x": 5, "y": 3 },
    { "x": 7, "y": 1 },
]

data2 = sci.data_map(data, lambda dic: dic["x"] if dic["x"] > 5 else None)

print data2