import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

f = lambda x: np.arctan(x)
h = np.logspace(-1, -10, num=50, endpoint=True, base=10.0)
x = sqrt(2)

twopoint = (f(x+h) - f(x))/h
threepoint = (f(x+h) - f(x-h))/(2*h)
exact = 1.0/3

plt.loglog(h,abs(twopoint-exact), "-c")
plt.show()
plt.loglog(h, abs(threepoint-exact), "-k")
plt.show()
