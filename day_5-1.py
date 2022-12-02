# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

average = float(input())
actual = float(input())

p = ((average**actual)*(math.exp(-average)))\
    / (math.factorial(actual))

print("%.3f" %p)
