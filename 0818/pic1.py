import re , os
import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib


x = np.linspace(0,10,100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure("huihui")
plt.title('pic test!')
plt.plot(x,y1,label = 'y = sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0,10,-1,1])
plt.legend(loc = 1)
plt.xticks([0,3.1416,6.2832,9.4298],['0','$\pi','2$\pi','3$\pi'])
plt.yticks([-1,0,1])
plt.savefig('huihui.png')
# plt.grid()
plt.figure("miaomiao")
plt.plot(x,y2, label = 'y = cos(x)')
plt.figure("huihui")
plt.title('pic test!')
plt.plot(x,y1,label = 'y = sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0,10,-1,1])
plt.legend(loc = 1)
plt.xticks([0,3.1416,6.2832,9.4298],['0','$\pi','2$\pi','3$\pi'])
plt.yticks([-1,0,1])
# plt.show()
plt.savefig('miaomiao.png')

#huimiao
plt.figure("huimiaomiao")
plt.plot(x,y2, label = 'y = cos(x)')
plt.figure("huihui")
plt.title('pic test!')
plt.plot(x,y1,label = 'y = sin(x)')
plt.plot(x,y2,label = 'y = cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0,10,-1,1])
plt.legend(loc = 1)
plt.xticks([0,3.1416,6.2832,9.4298],['0','$\pi','2$\pi','3$\pi'])
plt.yticks([-1,0,1])
# plt.show()
plt.savefig('huimiaomiao.png')