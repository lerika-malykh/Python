# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на которых f < 0
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

ax.grid()
ax.set_title('Уравнение')
ax.set_xlabel('x')
ax.set_ylabel('y')

x = np.linspace(-20, 20, 1000)
y = - 12 * x ** 4 * np.sin(np.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
# y = np.exp(x)
ax.plot(x, y)
plt.show()
