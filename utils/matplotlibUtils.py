# matplotlib工具类
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import math
import numpy

def getKaiFront():
    # 获取matplotlib中文楷体字体
    zhFront = FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
    return zhFront

def plot_function_and_derivative(fun, x_limits, figure_name, point_num = 100):
    '''
    画出fun的函数曲线和导数曲线
    fun:一个函数名
    x_limits:x轴的范围,[low, upper]
    point_num:x轴的采样点数
    '''
    
    gap = (x_limits[1] - x_limits[0]) / point_num # 点的间隔
    
    # 计算出x和y的list
    x_list = list(numpy.linspace(x_limits[0], x_limits[1], point_num+1))
    y_list = []
    for x in x_list:
        y_list.append(fun(x))
        
    # 计算出导数的list
    y2_list = []
    for i in range(len(x_list)):
        if i == 0:
            y2_list.append((y_list[0]-fun(x_list[0]-gap))/gap)
        else:
            y2_list.append((y_list[i]-y_list[i-1])/gap)
        
    # 画出函数图
    fig = plt.figure()
    
    ax1 = fig.add_subplot(111)
    ax1.plot(x_list, y_list, 'b')
    ax1.set_ylabel('function values (blue)')
    ax1.set_title(figure_name + ' (blue) and its derivative (red)')

    ax2 = ax1.twinx()
    ax2.plot(x_list, y2_list, 'r')
    ax2.set_xlim(x_limits)
    ax2.set_ylabel('derivative values (red)')
    plt.grid(True)
    plt.show()
if __name__ == '__main__':
    '''
    plot_function_and_derivative(lambda x : 1/(1+math.exp(-x)), [-10, 10], "sigmoid")
    plot_function_and_derivative(lambda x : math.tanh(x), [-10, 10], "tanh")
    plot_function_and_derivative(lambda x : x if x > 0 else 0, [-10, 10], "ReLU")
    '''
    plot_function_and_derivative(lambda x : 0.5*math.log((1-x)/x), [0.01, 0.99], "AdaBoost")
