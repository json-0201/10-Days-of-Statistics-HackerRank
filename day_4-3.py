# Enter your code here. Read input from STDIN. Print output to STDOUT
in_1 = list(map(int, input().split()))
in_2 = int(input())

p = in_1[0]/in_1[1]

result = p
for i in range(in_2-1):
    result *= (1-p)

print("%.3f" %result)
