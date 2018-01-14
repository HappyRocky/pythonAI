# matplotlib工具类
import matplotlib
from matplotlib.font_manager import FontProperties

def getKaiFront():
    # 获取matplotlib中文楷体字体
    zhFront = FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
    return zhFront
    
if __name__ == '__main__':
    print(getKaiFront())