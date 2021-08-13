L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def _bysort(t):
    return t[0]

l1 = sorted(L, key=_bysort)
for i in l1:
    print(i)