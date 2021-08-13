from io import  StringIO
f = StringIO('hello!\nHi\n')
# f.write('hello')
while True:
    s = f.readline()
    if s == '':
        break
    # print(s.strip())
    print(s)



# print(f.getvalue())