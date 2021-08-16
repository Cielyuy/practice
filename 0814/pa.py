import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')
#write
# dic1 = {'标题列1': ['wenwen','miaomiao'],
#         '标题列2': [80, 90]
# }
# df = pd.DataFrame(dic1)
# df.to_excel('1.xlsx', index = False)

#read
data = pd.read_excel('1.xlsx')
# print(data.values)

# print(data.values[1])

print(data['标题列2'].values)
# print(data(1).values)
# data.values[2] = ('binbin',20,40)

# data.loc[4] = ['binbin',20]

# data['title 4'] = [10,20]
data['title4'] = [90,50,20]

# data = data.drop([0], axis=0)

# data = data.drop('title 4',axis = 1)



l1 = np.arange(20)
# plt.plot(l1)
# plt.show()
# plt.plot(np.array([2.5, 4.1, 2.7, 8.8, 1.0]))
# plt.show()
# l2 =[2.5, 4.1, 2.7, 8.8, 1.0]
# s1 = Series(np.array(l2))
# s1.plot()
# plt.show()
# dataframe=DataFrame({'A':[9.3, 4.3, 4.1, 5.0, 7.0], 'B':[2.5, 4.1, 2.7, 8.8, 1.0]})
# dataframe.plot()
# plt.show()
plt.plot(data['标题列2'],data['title3'],data['标题列2'],data['title4'])
# plt.pie(data.values[1][1:])
plt.show()

DataFrame(data).to_excel('1.xlsx', sheet_name='Sheet1', index=False, header=True)