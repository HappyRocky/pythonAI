# 乘法表
N = 10
for i in range(1, N):
    for j in range(1, i + 1):
        print("{:4d}".format(i * j), end=" ")
    print()

