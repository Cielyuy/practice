
# g = (x * x for x in range(10))

# print(next(g))
# print(next(g))
# print(next(g))


# for n in g:
#     print(n)


# def triangles(int num):
#     n = 0 , a = 0 , b = 0 
#     while n < num:
#         a , b = a+b, b 

def triangles(num):
    L =[1]
    for j in range(num):
        #while True:
        yield L[:]
        L.append(0)
        L=[L[i]+L[i-1] for i in range(len(L))]

g1 = triangles(1)
g2 = triangles(10)

for i in g2:
    print(i)
for i in g1:
    print(i)


l1 = [1,3]
l2 = l1[:]
#print(hello)
# def triangles():    L=[1]    while True:        yield L[:]        L.append(1)        if len(L) > 2:            for i in range(1,len(L)-1)[::-1]:                L[i] += L[i-1]