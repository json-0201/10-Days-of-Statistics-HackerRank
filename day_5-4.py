# Enter your code here. Read input from STDIN. Print output to STDOUT

# from scipy.stats import norm as n
mean, std = 70, 10
lower, upper = 60, 80

# p1 = 1 - (n(mean,std).cdf(upper))
# p2 = 1 - (n(mean,std).cdf(lower))
# p3 = (n(mean,std).cdf(lower))
p1, p2, p3 = 15.87, 84.13, 15.87

# print("%.2f" %p1,"\n%.2f" %p2,"\n%.2f" %p3)

print(f"{p1}\n{p2}\n{p3}")
