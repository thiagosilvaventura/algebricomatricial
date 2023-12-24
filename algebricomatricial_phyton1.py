import numpy as np

def calcular_linha_resultante(matriz, razao):
    linha_resultante = np.array([matriz[i, -1] - (matriz[i, -2] - (matriz[i, -3] - (matriz[i, -4] - (matriz[i, -5] - matriz[i, -6])))) for i in range(matriz.shape[0])])
    return linha_resultante

# Razão n+1
matriz_2x3 = np.array([[1, 2, 3], [4, 5, 6]])
linha_resultante_2x3 = calcular_linha_resultante(matriz_2x3, 1)
print("Matriz 2x3:")
print(matriz_2x3)
print("Linha Resultante 2x3:", linha_resultante_2x3)

matriz_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
linha_resultante_3x3 = calcular_linha_resultante(matriz_3x3, 1)
print("\nMatriz 3x3:")
print(matriz_3x3)
print("Linha Resultante 3x3:", linha_resultante_3x3)

matriz_4x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
linha_resultante_4x3 = calcular_linha_resultante(matriz_4x3, 1)
print("\nMatriz 4x3:")
print(matriz_4x3)
print("Linha Resultante 4x3:", linha_resultante_4x3)

# Razão n+2
matriz_2x3_r2 = np.array([[1, 3, 5], [4, 6, 8]])
linha_resultante_2x3_r2 = calcular_linha_resultante(matriz_2x3_r2, 2)
print("\nMatriz 2x3 (Razão n+2):")
print(matriz_2x3_r2)
print("Linha Resultante 2x3 (Razão n+2):", linha_resultante_2x3_r2)

matriz_3x3_r2 = np.array([[1, 3, 5], [4, 6, 8], [7, 9, 11]])
linha_resultante_3x3_r2 = calcular_linha_resultante(matriz_3x3_r2, 2)
print("\nMatriz 3x3 (Razão n+2):")
print(matriz_3x3_r2)
print("Linha Resultante 3x3 (Razão n+2):", linha_resultante_3x3_r2)

matriz_4x3_r2 = np.array([[1, 3, 5], [4, 6, 8], [7, 9, 11], [10, 12, 14]])
linha_resultante_4x3_r2 = calcular_linha_resultante(matriz_4x3_r2, 2)
print("\nMatriz 4x3 (Razão n+2):")
print(matriz_4x3_r2)
print("Linha Resultante 4x3 (Razão n+2):", linha_resultante_4x3_r2)

# Fórmula para X e Y
def calcular_X_Y(numero_de_colunas):
    X = 1 if numero_de_colunas == 3 else 0
    Y = 1 if numero_de_colunas >= 5 else 0
    return X, Y

# Teste com diferentes quantidades de linhas e colunas
matriz_teste_3x3 = np.random.randint(1, 10, size=(3, 3))
X, Y = calcular_X_Y(matriz_teste_3x3.shape[1])
print("\nMatriz Teste 3x3:")
print(matriz_teste_3x3)
print(f"X: {X}, Y: {Y}")

matriz_teste_4x3 = np.random.randint(1, 10, size=(3, 4))
X, Y = calcular_X_Y(matriz_teste_4x3.shape[1])
print("\nMatriz Teste 4x3:")
print(matriz_teste_4x3)
print(f"X: {X}, Y: {Y}")

matriz_teste_5x3 = np.random.randint(1, 10, size=(3, 5))
X, Y = calcular_X_Y(matriz_teste_5x3.shape[1])
print("\nMatriz Teste 5x3:")
print(matriz_teste_5x3)
print(f"X: {X}, Y: {Y}")

matriz_teste_3x5 = np.random.randint(1, 10, size=(5, 3))
X, Y = calcular_X_Y(matriz_teste_3x5.shape[1])
print("\nMatriz Teste 3x5:")
print(matriz_teste_3x5)
print(f"X: {X}, Y: {Y}")

matriz_teste_3x7 = np.random.randint(1, 10, size=(7, 3))
X, Y = calcular_X_Y(matriz_teste_3x7.shape[1])
print("\nMatriz Teste 3x7:")
print(matriz_teste_3x7)
print(f"X: {X}, Y: {Y}")

matriz_teste_4x7 = np.random.randint(1, 10, size=(7, 4))
X, Y = calcular_X_Y(matriz_teste_4x7.shape[1])
print("\nMatriz Teste 4x7:")
print(matriz_teste_4x7)
print(f"X: {X}, Y: {Y}")
