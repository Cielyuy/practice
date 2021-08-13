from types import MethodType

class Student(object):
    #__slots__ = ('huihui','huiTaiLang','name','age','liwen','setLiwen')

    count = 0

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('not an integer')
        if value>100 or value<0 :
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value
            

    def __init__(self, name):
        self.name = name
        #self.count = 1 + self.count
        Student.count += 1

a = Student('wenhui')
print(a.count)
b = Student('miao')
print(b.count)
a.liwen = '123'
print(a.liwen)
#print(b.liwen)
def setLiwen(self):
    print('%s liwen,haha' % self.name)
    print('liwenwenwenw')

a.setLiwen = MethodType( setLiwen, a )
a.setLiwen()
print(hasattr(a,'setLiwen'))
print(hasattr(b,'setLiwen'))
print(hasattr(Student,'setLiwen'))
Student.setLiwen = setLiwen
b.setLiwen()
print(dir(Student))
class GraduteStudent(Student):
    __slots__ = ('name1')
    pass
g = GraduteStudent('liwen')
g.huihui = 999999
print(g.huihui)

a.score = 99
print(a.score)

class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @width.setter
    def height(self,height):
        self.__height = height

    @property
    def revolution(self):
        return self.__width * self.__height


#a1 = Screen(10,20)
a1 = Screen()
a1.width = 1024
a1.height = 768
b11 = a1.revolution
print(b11)
    