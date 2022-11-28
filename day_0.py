# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import mean, median, mode

n = int(input())
arr = [int(num) for num in str(input()).split()]

print("%.1f" % mean(arr))
print("%.1f" % median(arr))
print(mode(sorted(arr)))
