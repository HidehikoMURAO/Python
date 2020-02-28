# coding: UTF-8

# Import Module
#---+--10|----+--20|----+--30|----+--40|----+--50|----+--60|----+--70|----+--80|
import numpy as np
import matplotlib.pyplot as plt

# Definition of Function
#---+--10|----+--20|----+--30|----+--40|----+--50|----+--60|----+--70|----+--80|
def reg1dim2(x, y):
    n = len(x)
    a = ((np.dot(x, y) - y.sum() * x.sum() / n) / 
        ((x ** 2).sum() - x.sum()**2 / n))
    b = (y.sum() - a * x.sum()) / n
    return a, b

# Data setting
#---+--10|----+--20|----+--30|----+--40|----+--50|----+--60|----+--70|----+--80|
x = np.array([1, 2, 4, 6, 7])
y = np.array([1, 3, 3, 5, 4])
a, b = reg1dim2(x, y)

# Drawing Graph
#---+--10|----+--20|----+--30|----+--40|----+--50|----+--60|----+--70|----+--80|
plt.scatter(x, y, color = "k")
xmax = x.max()
plt.plot([0, xmax], [0, a * xmax], color = "k")
plt.show()