import os

l1 = list(range(1,12))
l2 = []
for i in range(1,10):
    l2.append(i)

l3 = [x*x for x in range(1,10)]
l4 = [x + x for x in range(1,4)]
l5 = [2*x for x in range(2,4)]

l6 = [x*x  for x in range(1,10) if x % 2 ==0]
l7 = [x + y for x in "abc" for y in "xyz"]
l8 = [x + x if x % 2 !=0 else x for x in range(1,10)]

l9 = [d for d in os.listdir(".")]
print ("hah")
d1 = {'x':'A','y':'B','Z':'C'}
for k , v in d1.items():
    print(k, " = " , v)

d2 = {'x':'A','y':'B','Z':'C'}
l10 = [k+ '='+v for k,v in d2.items()]

print("h")

L = ['Hello', 'World', 18, 'Apple', None]
L1 = [x for x in L if isinstance(x,str)]
print("hello world!")

