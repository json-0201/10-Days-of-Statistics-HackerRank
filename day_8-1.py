# Enter your code here. Read input from STDIN. Print output to STDOUT
x, y = [], []

for i in range(5):
    n,m = map(int, input().split())
    x.append(n)
    y.append(m)

sum_x, sum_y = sum(x), sum(y)
mu_x, mu_y = sum_x/len(x), sum_y/len(y)
sum_x2 = sum([e**2 for e in x])
sum_xy = sum([e1*e2 for e1, e2 in zip(x,y)])

b = ((5*sum_xy) - (sum_x*sum_y)) / ((5*sum_x2)-(sum_x**2))
a = mu_y - (b*mu_x)

# y = ax + b
ans = a+b*80
print("%.3f" %ans)
