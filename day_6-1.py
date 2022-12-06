from math import sqrt
from scipy.stats import norm as n

max_load = 9800
mean = 205 * 49
std = 15 * sqrt(49)

p = n(mean, std).cdf(max_load)

print("%.4f" %p)
