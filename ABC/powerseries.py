# 计算幂级数： e^x = 1 + x + x^2/2! + ... + x^n/n! (0 < x < 1, n -> 去穷大)
import math
x = float(input("Input x(0 < x < 1):"))
N = int(input("Input N:"))
result = 1
unit = 1
for i in range(1, N):
    unit = unit * x / i
    result += unit
print("result:{}".format(result))
print("accurate e^x = {}".format(math.exp(x)))
