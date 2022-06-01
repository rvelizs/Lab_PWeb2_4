def esEscalar(m):
    d = m[0][0]
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                if m[i][j] != 0:
                    print(m[i][j])
                    return False
                elif m[i][j] != d:
                    print(m[i][j])
                    return False
    return True

def esUnitaria(m):
    return m[0][0] == 1 and esEscalar(m)

def impMatriz(m):
    for line in m:
        print('  '.join(map(str, line)))
    print()

matriz1 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] # Unitaria
matriz2 = [[1,0,0,0],[0,-3,0,0],[0,0,1,0],[0,0,0,1]] # No unitaria
matriz3 = [[1,0,3,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] # No unitaria

print("La matriz\n")
impMatriz(matriz1) # Podemos cambiar por matriz2 o matriz3

if esUnitaria(matriz1): # Podemos cambiar por matriz2 o matriz3
        print("Es matriz unitaria")
else:
        print("No es matriz unitaria")