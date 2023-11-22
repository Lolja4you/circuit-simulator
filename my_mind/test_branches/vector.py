import numpy as np
import matplotlib.pyplot as plt

# Данные
data = [
    # ('E1', 10.0, 0.0099888391823086),
    ('R2', 9.9888391823086,  0.0099888391823086),
    ('C3', 0.02649621886023858, 0.0099888391823086),
    ('L4', 0.03765703655163917, 0.0099888391823086)
]

# Извлечение данных
names = [d[0] for d in data]
currents = np.array([d[1] for d in data])  # Значения тока
voltages = np.array([d[2] for d in data])  # Значения напряжения

# Построение векторной диаграммы
fig, ax = plt.subplots(figsize=(8, 6))

# Векторы тока
ax.quiver(0, 0, currents, currents, angles='xy', scale_units='xy', scale=1, color='b', label='Ток')

# Векторы напряжения
ax.quiver(0, 0, voltages, voltages, angles='xy', scale_units='xy', scale=1, color='r', label='Напряжение')

# Названия элементов
for i, name in enumerate(names):
    ax.annotate(name, (currents[i], currents[i]), xytext=(5, -5), textcoords='offset points')

# Оси и легенда
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Vector Diagram of Currents and Voltages')
plt.legend()

plt.grid()
plt.show()