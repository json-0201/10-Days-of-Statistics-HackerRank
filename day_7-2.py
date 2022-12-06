# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
x=list(map(float, input().split()))
y=list(map(float, input().split()))

r_x = [sorted(x).index(num) for num in x]
r_y = [sorted(y).index(num) for num in y]

d_i = [xx-yy for xx,yy in zip(r_x,r_y)]
d_i = [num**2 for num in d_i]

srcc = 1 - (6*sum(d_i))/(n*(n**2-1))
print("%.3f" %srcc)
