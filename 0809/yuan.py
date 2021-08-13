class Hello(object):
    def hello(self,name = 'world'):
        print('hello , %s' % name)
    
h = Hello()
print(type(Hello))
print(type(h))

def fn(self , name = 'world'):
    print('hello, %s' % name)

Hello2= type('Hello1',(object,),dict(hello2 = fn))
h2 = Hello2()
print(type(h2))

