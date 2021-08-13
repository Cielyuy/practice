def f(x):
    return x*x

l1 = list(range(10))
r  = map(f,l1,)
for i in list(r):
    print(i)