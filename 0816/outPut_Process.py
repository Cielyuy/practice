import re
import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

re_mat = re.compile(r'[a-z]+')
re_xiaoshu = re.compile(r'\d+\.?\d*')

l1 = []
l2 = []
l3 = []

with open(r'C:\Users\48231\Desktop\demo\0816\out1.txt', 'r',encoding='utf-8') as ot:
    
    for line in ot.readlines():
        # print()
        # print(line)
        a = re_mat.findall(line)
        if a:
            pass
        else:
            # print(line)
            l1.append(float((re_xiaoshu.findall(line))[0]))
            # print(int((re_mat.findAll(line))[0]))
            l2.append(float((re_xiaoshu.findall(line))[1]))
            # l3.append(float((re_xiaoshu.findall(line))[2]))

# print(l1)
#read
data = pd.read_excel('result1.xlsx')
data['time-step'] = l1
data['flow'] = l2
# data['Specify_V'] = l3

DataFrame(data).to_excel(r'C:\Users\48231\Desktop\demo\0816\result1.xlsx', sheet_name='Sheet1', index=False, header=True)


# plt.plot(data['time-step'],data['Specify_V'],data['flow'],data['Specify_V'])
# print(data.values[0][1:])
plt.plot(data['time-step'],data['flow'])
# plt.pie(data.values[1][1:])
plt.show()


    