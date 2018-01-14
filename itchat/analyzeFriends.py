import itchat
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def getFriendsInfo():
    # 爬取好友信息，返回json
    friends = itchat.get_friends(update=True)[0:]
    return friends

# 男女比例统计
def analyzeSexRatio(friends):
    male = female = other = 0
    for i in friends[1:]:
        sex = i["Sex"]
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1
    return (male, female, other)
    
itchat.login()
    
# 输出男女比例
friends = getFriendsInfo()
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