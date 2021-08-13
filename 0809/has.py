# class Gender_horse(object):
#     def seta(self, gender):
#         setattr(self, '__gender', gender)

#     def set(self, gender):
#         self.__gender = gender

#     def geta(self):
#         return getattr(self, '__gender')

#     def get(self):
#         return self.__gender


# dilu = Gender_horse()
# # 在 class 中定义私有属性
# dilu.set('Female')
# print(hasattr(dilu, '__gender'), dir(dilu))
# print('\n\n\n')
# print(getattr(dilu, '__gender', None), dilu.get())

# # 在 class 中用三个 attr 定义非私有属性
# dilu.seta('Lesbian')
# print(hasattr(dilu, '__gender'), dir(dilu))
# print(getattr(dilu, '__gender', None), dilu.get(), dilu.geta())

class MyDog(object):
    def run():
        print('dog is running')
        
    def __len__(self):
        print('length')
    
    def __init__(self,name,age,height):
        self.__age = age
        self.__name = name
        self.height = height

    def GetName(self):
        print(self.__name)

a = MyDog('wenhui',12,110)
a.GetName()

b1 = hasattr(a, 'getName')
b2 = hasattr(a, 'GetName')

print(b1)
print(b2)

b3 = getattr(a,'GetName')
b4 = getattr(a,'height')
print(b3)
print(b4)
setattr(a,'width',200)
b5 = getattr(a,'width')
print(b5)
print(b3())