import re
re_xiaoshu = re.compile(r'\d+\.?\d*')
# print(re_xiaoshu.findall("100 0.1 2.8795065980378"))
# print(float(2))

re_mat = re.compile(r'[a-z]+')
a = "Convergence history of Velocity Magnitude on miao37 (in SI units)"

print(re_mat.findall(a))