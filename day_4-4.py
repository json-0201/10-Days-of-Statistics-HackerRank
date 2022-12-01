# Enter your code here. Read input from STDIN. Print output to STDOUT

# during first 5 => 1st, 2nd, 3rd, 4th, 5th

in_1 = list(map(int, input().split()))
in_2 = input()

p = in_1[0]/in_1[1]

probs = []
for i in range(1,6):
    prob = (p**1) * (1-p)**(i-1)
    probs.append(prob)

print("%.3f" %sum(probs))
