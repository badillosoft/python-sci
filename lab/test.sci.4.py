import sci

data = [
	{"x": "a", "y": "m"},
	{"x": "b", "y": "n"},
	{"x": "a", "y": "o"},
	{"x": "b", "y": "m"}
]

X, Y = sci.data_analize(data, ["x", "y"], ["x", "y"])

print X
print Y

cat_sets = sci.cat_set_build(data, ["x", "y"])

print cat_sets

Xp = sci.cat_transform(X, cat_sets)
Yp = sci.cat_transform(Y, cat_sets)

print Xp
print Yp