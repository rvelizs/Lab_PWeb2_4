# Función de verificación
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

# Función de impresión
def impMatriz(m):
	for line in m:
		print('  '.join(map(str, line)))
	print()

# Principal

# Crear matrices
matriz1 = [[3,0,0,0],[0,3,0,0],[0,0,3,0],[0,0,0,3]] # Escalar
matriz2 = [[3,0,0,0],[0,-3,0,0],[0,0,3,0],[0,0,0,3]] # No escalar
matriz3 = [[3,0,1,0],[0,3,0,0],[0,0,3,0],[0,0,0,3]] # No escalar

# En consola
print("La matriz\n")
impMatriz(matriz1) # Podemos cambiar por matriz2 o matriz3

if esEscalar(matriz1): # Podemos cambiar por matriz2 o matriz3
	print("Es matriz escalar")
else:
	print("No es matriz escalar")

