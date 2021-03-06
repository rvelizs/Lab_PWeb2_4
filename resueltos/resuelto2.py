# Función de verificación Escalar
def esEscalar(m):
    d = m[0][0]
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                if m[i][j] != 0:
                    return False
            elif m[i][j] != d:
                return False
    return True

# Función de verificación Unitaria
def esUnitaria(m):
    return m[0][0] == 1 and esEscalar(m)

# Función de impresión
def impMatriz(m):
    for line in m:
        print('  '.join(map(str, line)))
    print()

# Principal

# Crear matrices
matriz1 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] # Unitaria
matriz2 = [[1,0,0,0],[0,-3,0,0],[0,0,1,0],[0,0,0,1]] # No unitaria
matriz3 = [[1,0,3,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] # No unitaria

# Imprime la matriz
print("La matriz\n")
impMatriz(matriz1)

if esUnitaria(matriz1): # Podemos cambiar por matriz2 o matriz3
    print("Es matriz unitaria")
else:
    print("No es matriz unitaria")