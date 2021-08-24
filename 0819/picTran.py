import re , os
import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib

#文件夹位置
clipDir1 = os.getcwd()
clipDir = clipDir1
print(clipDir)
#字母
re_ZiMu = re.compile(r'[a-z]+')
re_XiaoShu = re.compile(r'\d+\.?\d*')
#excelName:
excelName  = '0819.xlsx'

txtDirList = [x for x in os.listdir('.') if '.txt' in x]
isFlag = True
contNum_l = 0
df = pd.DataFrame()

for i in txtDirList:
    l0 = []
    l1 = []
    # l2 = []
    d1 = os.path.join(clipDir,i)
    if isFlag:
        # print(d1)
        with open(d1,'r',encoding='utf-8') as docu :
            for line in docu.readlines():
                # print(line)
                # print(re_ZiMu.findall(line))
                if re_ZiMu.findall(line) == []:
                    # print(line)
                    l0.append((re_XiaoShu.findall(line))[0])
                    l1.append((re_XiaoShu.findall(line))[1])
                    # l2.append((re_XiaoShu.findall(line))[2])
                    # isFlag = False
                else:
                    pass
            # df['stepNum'] = l0
            df['flow'] = l0
            df[i.split(".")[0]] = l1
            isFlag = False
    else:
        with open(d1,'r',encoding='utf-8') as docu :
            for line in docu.readlines():
                
                if re_ZiMu.findall(line) == []:
                    # print(line)
                    # l0.append((re_XiaoShu.findall(line))[0])
                    # l1.append((re_XiaoShu.findall(line))[1])
                    l1.append((re_XiaoShu.findall(line))[1])
                    # isFlag = False
                else:
                    pass
            df[i.split(".")[0]] = l1

excelDir = os.path.join(clipDir,excelName)
df.to_excel(excelDir,index = False)

print(len(df.columns))
print(df.index)
# print(df[df['flow']>'1000'])
df[df.columns[0]] = df[df.columns[0]].apply(lambda x : (int(x)//100))# 把100步当作1步
for i in df.columns:
    # print(i)
    if i == df.columns[0]:
        pass
    else:
        # print(df[i])
        df[i] = df[i].apply(lambda x:round(float(x),2))  #保留两位小数
        plt.figure(i)
        # ax = plt.subplot(111)
        # plt.title('pic test!')plt.figure("huihui")
        plt.title(i)
        plt.plot(df[df.columns[0]],df[i])
        # plt.plot(df.columns[1],i,label = 'y = sin(x)')
        # ax = plt.gca()
        # xmajorLocator = plt.MultipleLocator(100)
        # xmajorFormatter = plt.FormatStrFormatter('%5.1f')
        # ymajorLocator = plt.MultipleLocator(10)
        # ymajorFormatter = plt.FormatStrFormatter('%5.1f')

        # # ax.xaxis.set_major_locator(x_major_locator)
        # ax.yaxis.set_major_locator(ymajorFormatter)
        # a = plt.xlim()[0]
        # b = plt.xlim()[1]
        # plt.xticks(np.arange(100,16000,1000))
        
        # c ,d = plt.ylim()[0],plt.ylim()[1]
        # plt.yticks(np.arange(0,100,5))
        # print(a,b,c,d)


        plt.xlabel('step')
        plt.ylabel("value")
        
        # plt.axis([0,15100,-1,1])

        # plt.legend(loc = 1)
        # plt.xticks([0,3.1416,6.2832,9.4298],['0','$\pi','2$\pi','3$\pi'])
        # plt.yticks([-1,0,1])
        plt.savefig(i+'.png')
        print("done!")
        # a1 = 1
        # b1 = 2

##指定两组数值进行画图匹配
print('指定若干组进行对比')
plt.figure('2&3')
plt.title('2&3')
# p1 = plt.plot(df[df.columns[0]],df['cirPoint2'])
# p2 = plt.plot(df[df.columns[0]],df['cirPoint3'])
plt.plot(df[df.columns[0]],df['cirPoint2'])
plt.plot(df[df.columns[0]],df['cirPoint3'])
#xy轴名称
plt.xlabel('step')
plt.ylabel("value")
#设置图例
# plt.legend([p1,p2],['p2','p3'],loc='upper left')
plt.legend(['p2','p3'],loc='upper right')
plt.savefig('cirPoint2&3'+'.png')
print("done23!")

##含有point的所有数组进行对比