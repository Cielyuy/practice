import pandas as pd
from pandas import DataFrame
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

data['title 4'] = [10,20]

# data = data.drop([0], axis=0)

data = data.drop('title 4',axis = 1)


DataFrame(data).to_excel('1.xlsx', sheet_name='Sheet1', index=False, header=True)

