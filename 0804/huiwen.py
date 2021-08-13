# from functools import reduce

# def _daoshu(n):
#     l = []
#     while True:
#         if (n//10 or n%10) != 0 :
#             l.append(n%10)
#             n = n//10
#         else:
#             break
#     return l
# #l1 = _dret
# # D = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# # def char2Int(c):
# #     return D[c]

# # l = _daoshu(123456)
# # for i in l:
# #     print(i)

# def isHuiWen(nu):
#     if int(reduce(lambda x,y: 10*x+y , _daoshu(nu)))== nu :
#         return True
#     else:
#         return False

# output = filter(isHuiWen,range(1,1000))
# print (list(output))

def ISHUIWEN(n):
    return str(n) == str(n)[::-1]

output = filter(ISHUIWEN,range(1,1000))
print (list(output))