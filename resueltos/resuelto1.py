# Función de verificación
import imp


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
	for i in range(len(m)):
		for j in range(len(m)):
			print(m[i][j] + "")
		print("\n")

# Principal

# Crear matrices
matriz1 = [[3,0,0,0],[0,3,0,0],[0,0,3,0],[0,0,0,3]]
matriz2 = [[3,0,0,0],[0,-3,0,0],[0,0,3,0],[0,0,0,3]]
matriz3 = [[3,0,1,0],[0,3,0,0],[0,0,3,0],[0,0,0,3]]

# En consola
impMatriz("La matriz\n" + matriz1)

if esEscalar(matriz1):
	print("Es matriz escalar")
else:
	print("No es matriz escalar")

