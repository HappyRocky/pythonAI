# 问题：给定两个字符串A和B，要求判断A是否包含B，如果包含返回第一次出现B的index
class FindSubStr:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        
    # 最传统的方法，双重循环，O(m*n)
    def findByCommon(self):
        if self.source is None or self.target is None:
            return -1
        for i in range(len(self.source) - len(self.target) + 1):
            for j in range(len(self.target)):
                if self.source[i + j] != self.target[j]:
                    break
            else: # 此else对应的是for，表示for循环没有被break过
                return i
        return -1
    
    # 新的方法，O(m) + O(n)
    def findByDict(self):
        if self.source is None or self.target is None:
            return -1
        '''
        根据target构造字典
        如 target = 'Wor'，则构造出的字典为：
        {'W': [{'o': [{'r': [{}, '1']}, '0']}, '0']}
        每一个value是一个二维数组，存放着一个字典和0/1，字典内容是下一个字符，0/1表示当前字符是否是最后一个字符
        '''
        dic = dict()
        top = dic
        for i in range(len(self.target)):
            if i == len(self.target) - 1: # 到达最后一个字符
                s = '1'
            else:
                s = '0'
            dic[self.target[i]] = [dict(), s] # 将字符作为key放入到dict中，对应的value是一个二维数组
            dic = dic[self.target[i]][0] # 将dic深入一层，便于存放下一个字符
        # 开始搜索
        dic = top
        idx = -1 # 匹配到第一个字符的索引
        i = 0
        while i < len(self.source):
            char = self.source[i]
            if char in dic: # 字符在字典中
                # 更新idx
                if idx == -1:
                    idx = i                
                # 判断是不是最后一个字符
                if dic[char][1] == '1':
                    return idx
                # 将字典深入一层
                l = dic[char]
                dic = l[0]
            else: # 字符没有在字典中，初始化
                dic = top
                if idx != -1: # 上次循环还在字典中
                    i -= 1 # 下一次循环重新扫描这个字符
                    idx = -1
            i += 1
        return -1
            
if __name__ == '__main__':
    S = FindSubStr('HelloWoWWorld','Wor')
    print(S.findByCommon())
    print(S.findByDict())
