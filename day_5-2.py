# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = list(map(float, input().split()))
avg_a = inp[0]
avg_b = inp[1]

cost_a = 160 + 40*(avg_a+(avg_a*avg_a))
cost_b = 128 + 40*(avg_b+(avg_b*avg_b))

print("%.3f" %cost_a)
print("%.3f" %cost_b)
