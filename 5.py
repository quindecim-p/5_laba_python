import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-30, 30, 50)  # заполняем массив 50 точками
y = np.linspace(-30, 30, 50)  # заполняем массив 50 точкам
X, Y = np.meshgrid(x, y)  # создаем двумерные массивы, которые представляют собой сетку координат

# Вычисляем значения функций в каждой точке
Z1 = X**(1/4) + Y**(1/4)
Z2 = X**2 - Y**2
Z3 = 2*X + 3*Y
Z4 = X**2 + Y**2
Z5 = 2 + 2*X + 2*Y - X**2 - Y**2

functions = [Z1, Z2, Z3, Z4, Z5]
titles = ["z=x^0.25+y^0.25", "z=x^2-y^2", "z=2x+3y", "z=x^2+y^2", "z=2+2x+2y-x^2-y^2"]

for Z, title in zip(functions, titles):
    fig = plt.figure()  # создаем новое окно графика
    ax = fig.add_subplot(111, projection="3d")  # создаем 3-х мерный подграфик (111- 1x1 сетка графиков и текущий будет первым)
    ax.plot_surface(X, Y, Z, cmap="viridis")  # строим 3-х мерный график (цвета viridis)
    ax.set_xlabel("X")  # подписываем ось X
    ax.set_ylabel("Y")  # подписываем ось Y
    ax.set_zlabel(title)  # подписываем ось Z
    ax.set_title(f"График функции {title}")  # подписываем график

plt.show()  # отображаем все графики на экране
