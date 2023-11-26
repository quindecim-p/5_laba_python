import numpy as np
import matplotlib.pyplot as plt


def f(x, a):
    return (1 / np.tan(x))**3 + 2.24 * a * x


a_min = 3.5
a_max = 25.5
delta_a = 0.75

x_const = 3.567

a_values = np.arange(a_min, a_max, delta_a)

result_array = [f(x_const, a) for a in a_values]

for a, result in zip(a_values, result_array):
    print(f"a = {a}: f(x) = {result}")

max_value = np.max(result_array)
min_value = np.min(result_array)
average_value = np.mean(result_array)

array_size = len(result_array)

sorted_array = np.sort(result_array)[::-1]

print(f"\nНаибольшее значение: {max_value}")
print(f"Наименьшее значение: {min_value}")
print(f"Среднее значение: {average_value}")
print(f"Количество элементов в массиве: {array_size}")

print("\nОтсортированный массив по убыванию:")
for result in sorted_array:
    print(result)

plt.axhline(average_value, color="red", linestyle="--", label="Среднее значение f(x)")

plt.plot(a_values, result_array, label="f(x)")

plt.title("График функции f(x)")
plt.xlabel("Значение параметра a")
plt.ylabel("Значение функции f(x)")

plt.axvline(0, color="black", linewidth=0.5)
plt.axhline(0, color="black", linewidth=0.5)

plt.grid(color="gray", linestyle="--", linewidth=0.5)

plt.legend()
plt.show()
