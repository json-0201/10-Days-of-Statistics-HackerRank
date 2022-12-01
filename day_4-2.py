# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = list(map(int, input().split()))

p = inp[0]/100
n = inp[1]

def factorial(num):
    return 1 if num<=1 else num*factorial(num-1)

probs_1, probs_2 = [], []

# no more than 2 rejects => 0, 1, 2 rejects
for i in range(0,3):
    prob = ((p**i)*((1-p)**(n-i))) * (factorial(n)/(factorial(i)*factorial(n-i)))
    probs_1.append(prob)
    
# at least 2 rejects => at most 8 accepts
for i in range(0,9):
    prob = (p**(n-i))*((1-p)**i) * (factorial(n)/(factorial(n-i)*factorial(i)))
    probs_2.append(prob)

print("%.3f" %sum(probs_1))
print("%.3f" %sum(probs_2))
