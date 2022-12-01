# Enter your code here. Read input from STDIN. Print output to STDOUT
ratio = list(map(float, input().split()))
b = ratio[0]/sum(ratio)
g = ratio[1]/sum(ratio)

# factorial function
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

# at least 3 boys => 3, 4, 5, 6
# each case => probability * combination
probability =[]
for i in range(3,7):
    p = (b**(i))*(g**(6-i))\
    *(factorial(6)/(factorial(i)*factorial(6-i)))
    probability.append(p)

p_final = "%.3f" %sum(probability)

print(p_final)
