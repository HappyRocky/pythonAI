import itchat
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pandas import DataFrame
import csv

def getFriendsInfo():
    # 爬取好友信息，返回json
    friends = itchat.get_friends(update=True)[0:]
    return friends

def getInfo(friends, key):
    # 从friends信息中获取key的值
    variable = []
    for i in friends:
        value = i[key]
        variable.append(value)
    return variable

# 男女比例统计
def analyzeSexRatio(friends):
    values = getInfo(friends[1:], 'Sex')
    male = values.count(1)
    female = values.count(2)
    other = len(values) - male - female
    return (male, female, other)

# 保存各种数据
def saveData(friends):
    NickName = getInfo(friends, 'NickName')
    Sex = getInfo(friends, 'Sex')
    Province = getInfo(friends, 'Province')
    City = getInfo(friends, 'City')
    Signature = getInfo(friends, 'Signature')
    data = {'NickName':NickName,'Sex':Sex, 'Province':Province, 'City':City, 'Signature':Signature}
    frame = DataFrame(data)
    frame.to_csv('data.csv', index=True)

def printSexRatio(friends):
    # 输出男女比例
    (male, female, other) = analyzeSexRatio(friends)
    total = male + female + other
    kaiti = FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
    print('男女比例：')
    print('男生：%.2f%%' % (float(male)/total * 100))
    print('女生：%.2f%%' % (float(female)/total * 100))
    print('性别不明：%.2f%%' % (float(other)/total * 100))
    labels = ['男','女','不明']
    X = [male, female, other]
    fig = plt.figure()
    pie = plt.pie(X, labels = labels, autopct='%1.2f%%')
    for font in pie[1]:
        font.set_fontproperties(kaiti)
    plt.title('男女比例分析',fontproperties=kaiti)
    plt.legend(prop=kaiti)
    plt.show()
    plt.savefig("SexRatioPie.jpg")
    
def plotArea():
    # 读取data.csv，分析区域分布
    area = []
    with open('data.csv','r',encoding='utf-8') as csvfile:
        read = csv.reader(csvfile,)
        for i in read:
            area.append(i[3])
    area = area[1:]
    area_dict = {k:area.count(k) for k in set(area)}
    area_dict = sorted(area_dict.items(),key=lambda item : item[1],reverse=True)
    print(area_dict)
    x = []
    y = []
    for area in area_dict:
        if area[0] == '':
            x.append('不明')
        else:
            x.append(area[0])
        y.append(area[1])
    kaiti = FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
    n = 10
    plt.bar(np.arange(n), np.array(y[:n]), 0.9)
    plt.xticks(np.arange(n),np.array(x[:n]), fontproperties=kaiti)
    plt.xlabel('区域', fontproperties=kaiti)
    plt.ylabel('人数', fontproperties=kaiti)
    plt.title('区域统计', fontproperties=kaiti)
    for xx,yy in zip(np.arange(n),y[:n]):
        plt.text(xx + 0.05, yy + 4, str(yy), ha='center',va='top')
    plt.show()

#itchat.login()
#friends = getFriendsInfo()
#printSexRatio(friends) # 输出男女比例
#saveData(friends) # 保存到data.csv中
plotArea()