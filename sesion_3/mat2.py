def crear_mat(n, m):
    mat = []

    for i in range(0, n):
        row = []

        for j in range(0, m):
            row.append(i * m + j)

        mat.append(row)

    return mat

print crear_mat(3, 6)