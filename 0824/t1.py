import re

re_txt = re.compile(r'\"\S*txt\"')  #|S表示匹配任意字符

a = re_txt.findall(r'/solve/monitors/surface/set-monitor cirPoint1  "Sum" velocity-magnitude cirPoint1 () n n y "miao_V_huan_4.txt" 100')
print(a)