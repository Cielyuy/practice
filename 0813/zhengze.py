'''
\d  一个数字
\w  一个字母或者数字
.   匹配任意字符串
变长：
*  任意个字符（包括0）
+  至少一个字符
?  0或1个字符


[0-9a-zA-Z\_]  任意一个数字、字母、下划线
[0-9a-zA-Z\_]+  至少一个由上述成分组成的字符串
[a-zA-Z\_][0-9a-zA-Z]*
[a-zA-Z\_][0-9a-zA-Z]{0,19}
A|B  :   (P|p)ython
^    ^\d
$     \d$

'''

import re

a = re.match(r'^\d{3}\-\d{3,8}$','010-12345')
print(a)

a1 = 'a  b  c  '.split(' ')
print(a1)
a2 = re.split(r'\s+','a   b   c')
print(a2)

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
b1 = m.group(0)
b2 = m.group(1)
b3 = m.group(2)
print(m.groups())

t = '19:05:30'
m1 = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m1.groups())
print(re.match(r'^(\d+?)(0*)$', '1010100').groups())

re_tel = re.compile((r'^(\d{3})-(\d{3,8})$'))

print(re_tel.match('010-12345').groups())