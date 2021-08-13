# import logging
# logging.basicConfig(level=logging.INFO)

def foo(s):
    n = int(s)
    #print('>>> n = %s' % n)
    #assert n !=0,'n is zero'
    # logging.info('n = %s' %n)
    return 10 / n

def main():
    foo('0')

main()