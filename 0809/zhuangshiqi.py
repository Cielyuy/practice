# def log(func):
#     def wrapper(*args, **kwargs):
#         print('call %s()' % func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
import functools 


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s call %s()' %(text , func.__name__) )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log("excute")
def now():
    print('2021-08-09')

print(now())
print(now.__name__)


a = '123'
print(dir(a))