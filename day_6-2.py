# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
from scipy.stats import norm as n

t = 250
mean = 100 * 2.4
std = 2.0 * sqrt(100)

p = n(mean, std).cdf(t)

print("%.4f" %p)
