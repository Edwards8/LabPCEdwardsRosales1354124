X = [[15, 2, 2  ],
     [8, 5, 8],
     [3, 8, 10]]

Y = [[5, 8, 3],
     [6, 6, 3],
     [11, 5, 7]]

suma = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        suma[i][j] = X[i][j] + Y[i][j]

print("Suma de matrices:")
for res in suma:
    print(res)

resta = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        resta[i][j] = X[i][j] - Y[i][j]

print("Resta de matrices:")
for res in resta:
    print(res)

multiplicacion = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        multiplicacion[i][j] = X[i][j] * Y[i][j]

print("Multiplicación de matrices:")1
for res in multiplicacion:
    print(res) 

print("\nElementos pares de la primera matriz:")
for i in range(len(X)):
    for j in range(len(X[0])):
        if X[i][j] % 2 == 0:
            print(f"Elemento ({i}, {j}) = {X[i][j]}")

print("\nElementos impares de la segunda matriz:")
for i in range(len(Y)):
    for j in range(len(Y[0])):
        if Y[i][j] % 2 != 0:
            print(f"Elemento ({i}, {j}) = {Y[i][j]}")