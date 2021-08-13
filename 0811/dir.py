import os, shutil
print(os.name)
print(os.path.abspath('.'))

newDir = os.path.join(os.path.abspath('.'),'testDir')
# os.mkdir(newDir)

sp = os.path.split(r'C:\Users\48231\Desktop\pythonPratice')
print(sp)
st = os.path.splitext('/path/to/file.txt')
print(st)

# os.rename(r'C:\Users\48231\Desktop\pythonPratice\0811\wenhui.txt',r'C:\Users\48231\Desktop\pythonPratice\0811\miaomiao.txt')
# os.rename('wenhui1.txt','mmm.txt')
# os.remove('miaomiao.txt')
shutil.copyfile('mmm.txt','www.txt')
ld = [x for x in os.listdir('.') if os.path.isfile(x)]
print(ld)

ld1 = [1,2,3]
print(ld1)
