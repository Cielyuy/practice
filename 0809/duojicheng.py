class Animal(object):
    pass

class Male(Animal):
    pass

class peopleMixIn(object):
    pass

class Student(object):
    def __init__(self,name,age):#,a=0,b=1
        # self.a = a
        # self.b = b
        self.__age = age
        self.__name = name
    
    def __call__(self):
        print('My name is %s.' %self.__name)

    def __str__(self):
        return 'Student object (name：%s)' % self.__name

    __repr__ = __str__

    def __getattr__(self,attr):
        if attr == 'dahui':
            #print('dahuihuihui')
            return lambda:77
    # def __iter__(self):
    #     pass
    # def __next__(self):
    #     self.a , self.b = self.b ,self.a + self.b
    #     if self.a >10000:
    #         raise StopIteration()
    #     return self.a




s1 = Student('huihui',18)
t1 = s1.__str__()
t2 = str(s1)
#print(t2)
print(s1)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)

print(Fib())

class Fib1(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f2 = Fib1()
print(f2[2:10])

s2 = Student('miao',18)

print(s2.dahui())
print(s2.huihui)

s2()
#print(s2())

