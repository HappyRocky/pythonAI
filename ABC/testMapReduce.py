# 使用map
print(list(map(lambda x:x*2, range(5))))
print([x*2 for x in range(5)])

print(list(map(lambda x,y:x*y, range(5), range(5))))
print([x*y for x,y in [(x,x) for x in range(5)]])

# 使用reduce
from functools import reduce
print(reduce(lambda x,y:x+y,range(5)))

# 使用filter
def sushu(x):
    plist = [0,0] + list(range(2,x+1))
    for i in range(2,x):
        if plist[i]:
            plist[i+1::i] = [0]*len(plist[i+1::i])
    return filter(None, plist)
print(list(sushu(50)))
