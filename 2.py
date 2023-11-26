import numpy as np

X = np.zeros((12, 3))
X[:, 0] = 1
X[:, 1] = np.random.randint(2, 14, size=12)
X[:, 2] = np.random.randint(60, 82, size=12)

Y = np.random.uniform(13.5, 18.6, (12, 1))

A = np.linalg.inv(X.T @ X) @ X.T @ Y

print("Матрица X:\n", X, "\n")
print("Вектор столбец Y:\n", Y, "\n")
print("Вектор оценок A:\n", A, "\n")
