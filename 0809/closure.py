def createCounter():
    l1 = []
    def counter():
        l1.append(1)
        
        return len(l1)
    return counter

c1 = createCounter()
print(c1())
print(c1())
print(c1())
print(c1())
print(c1())

L = list(filter(lambda x: x% 2 == 1 , range(1,20)))
for i in L:
    print(i)