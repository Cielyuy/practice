from functools import reduce
import math

def split1(str1):
    s1=[]
    s2=[]
    isFlag = True
    for i in str1:
        if i == '.':
            isFlag = False
        
        if isFlag:
            s1.append(i)
        
        else:
            if i != '.':   
                s2.append(i)
    return s1,s2

l1 = split1('123.456')
for i in l1:
    print(i)

print ('hello')

D = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char2Int(c):
    return D[c]

def Int2Whole(x,y):
    return x*10+y

def str2Int(str):
    s1 = list(split1(str)[0])    
    s2 = list(split1(str)[1])    
    r1 = reduce(Int2Whole, map(char2Int,s1))
    r2 = reduce(Int2Whole, map(char2Int,s2))
    return r1 + r2/ (pow(10,len(s2)))
    
l22 = str2Int('123.456')
print(l22)