import re

re_tel = re.compile(r'\d+\.?\d*')
# re_tel = re.compile(r'^\d\.$')
# re_tel = re.compile((r'\d+\.?\d*$'))
# re_tel = re.compile(r'(^(-?\d+)(\.\d+)?N$))
l1 = []

with open(r'C:\Users\48231\Desktop\pythonPratice\0813\qiangzai.txt', 'r',encoding='utf-8') as qz:
    
    for line in qz.readlines():
        print(line)
        if re_tel.findall(line):
            l1.append(re_tel.findall(line))

print(l1)

print(re_tel.findall(r'Time of solve this question is : CPU :13.2: User : 13.4'))