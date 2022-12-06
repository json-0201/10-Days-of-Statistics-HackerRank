# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt as sq

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

mu_x = sum(x)/len(x)
mu_y = sum(y)/len(y)
sig_x = sq(sum([(x[i]-mu_x)**2 for i in range(n)])/n)
sig_y = sq(sum([(y[i]-mu_y)**2 for i in range(n)])/n)

pcc = sum([(x[i]-mu_x)*(y[i]-mu_y) for i in range(n)])/(n*sig_x*sig_y)

print("%.3f" %pcc)
