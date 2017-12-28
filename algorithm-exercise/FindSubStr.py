# 问题：给定两个字符串A和B，要求判断A是否包含B，如果包含返回第一次出现B的index
class FindSubStr:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        
    # 最传统的方法，双重循环，O(m*n)
    def strStr(self):
        if self.source is None or self.target is None:
            return -1
        for i in range(len(self.source) - len(self.target) + 1):
            for j in range(len(self.target)):
                if self.source[i + j] != self.target[j]:
                    break
            else: # 此else对应的是for，表示for循环没有被break过
                return i
        return -1

if __name__ == '__main__':
    S = FindSubStr('gongyanshang','yan')
    print(S.strStr())
