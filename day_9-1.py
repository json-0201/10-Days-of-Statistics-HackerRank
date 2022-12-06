from sklearn import linear_model

m, n = map(int, input().split())

X = []
Y = []
for i in range(n):
    xy = input().split()
    X.append([float(xy[j]) for j in range(m)])
    Y.append(float(xy[-1]))
    
lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_
coefs = [b[k] for k in range(m)]

r = int(input())
for i in range(r):
    x1x2 = input().split()
    y = a
    for j in range(m):
        y += coefs[j]*float(x1x2[j])
    print("%.2f" %y)
