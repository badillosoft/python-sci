from sci import data_map

a = [1, 2, 3, 4, 5, 9, 18]

def f(num):
    if num % 2 == 0:
        return num + 1
    else:
        return num

b = data_map(a, f)

print b