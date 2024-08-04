import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Обчислення інтегралу методом Монте-Карло
N = 100000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
integral_mc = (b - a) * np.mean(y_rand)

# Аналітичне обчислення інтегралу
integral_analytic = (b**3 / 3) - (a**3 / 3)

# Обчислення інтегралу за допомогою функції quad
integral_quad, error = spi.quad(f, a, b)

# Порівняння результатів
print(f"Інтеграл методом Монте-Карло: {integral_mc}")
print(f"Аналітичний інтеграл: {integral_analytic}")
print(f"Інтеграл за допомогою quad: {integral_quad} (помилка: {error})")

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
