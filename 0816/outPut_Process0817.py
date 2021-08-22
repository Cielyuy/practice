import re , os
import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib
import xlwings as xw

matplotlib.style.use('ggplot')

re_mat = re.compile(r'[a-z]+')
re_xiaoshu = re.compile(r'\d+\.?\d*')

l1 = []
l2 = []
l3 = []
##df.toexcel(file_path,index = False)
abs_Path = os.path.abspath('.')
file_Name = 'out_3-10000.txt'
file_Dir = os.path.join(abs_Path , file_Name)

with open(file_Dir, 'r',encoding='utf-8') as ot:
    
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
            l3.append(float((re_xiaoshu.findall(line))[2]))

# print(l1)
#read
outputFile_Name = 'result5.xlsx'
outputFile_Dir = os.path.join(abs_Path , outputFile_Name)

wb = xw.Book()  # 创建新的工作簿
# sht = wb.sheets['Sheet1']  # 实例化工作表
# sht.range('A1').value = 'Hello World!'  # 写入
# print(sht.range('A1').value)  # 读取
wb.save(outputFile_Dir)  # 保存
wb.close()



data = pd.read_excel(outputFile_Dir)
data['time-step'] = l1
data['flow'] = l2
data['Specify_V'] = l3
data['time-step'] = l2

DataFrame(data).to_excel(outputFile_Dir, sheet_name='Sheet1', index=False, header=True)


plt.plot(data['time-step'],data['Specify_V'])
# print(data.values[0][1:])
# plt.plot(data['flow'],data['Specify_V'])
# plt.pie(data.values[1][1:])
plt.show()


    