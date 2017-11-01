a, b = 0, 1
N = 10
while(N > 0):
    print(b, end=" ")
    a, b = b, a + b
    N -= 1
