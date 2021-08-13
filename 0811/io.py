# try:
#     f = open('C:/Users/48231/Desktop/pythonPratice/0811/wenhui1.txt', 'r')
#     con = f.read()
#     print (con)
# finally:
#     if f:
#         f.close()

a = '\nhuihuihuihui'
with open('C:/Users/48231/Desktop/pythonPratice/0811/wenhui2.txt', 'rb') as f:
    # f.write(a)

    for line in f.readlines():
        print(line)