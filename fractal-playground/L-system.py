# L-System(Lindenmayer system)是一种用字符串替代产生分形图形的算法
from math import sin, cos, pi
from matplotlib import pyplot as pl
from matplotlib import collections

class L_System(object):
    def __init__(self, rule):
        info = rule['S']
        for i in range(rule['iter']): # 迭代次数
            ninfo = [] # 按顺序存放新一轮迭代之后的字符
            for c in info: # info为本轮迭代的输入字符串，遍历它
                if c in rule: # 如果一个字符具有迭代公式
                    ninfo.append(rule[c]) # 根据迭代公式，将此字符换为对应字符串
                else:
                    ninfo.append(c) # 没有迭代公式，保留此字符
            info = "".join(ninfo) # 将字符数组连接为字符串
        self.rule = rule # 保存参数rule
        self.info = info # 迭代过后最终的字符串
        
    def get_lines(self):
        # 此函数返回一个数组，每个元素是一个元组，包含两个子元组，一个是起始点，一个是终点，表示一条线段。
        d = self.rule['direct'] # 方向初始值
        a = self.rule['angle'] # 每次旋转的角度
        p = (0.0,0.0) # 起点
        l = 1.0 # 运行F时向前走的长度
        lines = [] # 存放结果
        stack = [] # 栈，用于执行[和]
        for c in self.info:
            if c in "Ff": # 根据当前角度，向前画一条线段
                r = d * pi / 180
                t = p[0] + l * cos(r), p[1] + l * sin(r)
                lines.append(((p[0],p[1]),(t[0],t[1])))
                p = t
            elif c == "+": # 旋转角度
                d += a
            elif c == "-": # 旋转角度
                d -= a
            elif c == "[": # 将当前的位置记录到栈中
                stack.append((p,d))
            elif c == "]":
                p, d = stack[-1] # 取出栈中顶层数值，相当于坐标p和方向d回退到了之前某次迭代之后的位置。这说明图形在此位置将要分叉。
                del stack[-1]
        return lines

rules = [ # 定义6个图案的规则
    {
        "F":"F+F--F+F", "S":"F",
        "direct":180,
        "angle":60,
        "iter":5,
        "title":"Koch"
    },
    {
        "X":"X+YF+", "Y":"-FX-Y", "S":"FX",
        "direct":0,
        "angle":90,
        "iter":13,
        "title":"Dragon"
    },
    {
        "f":"F-f-F", "F":"f+F+f", "S":"f",
        "direct":0,
        "angle":60,
        "iter":7,
        "title":"Triangle"
    },
    {
        "X":"F-[[X]+X]+F[+FX]-X", "F":"FF", "S":"X",
        "direct":-45,
        "angle":25,
        "iter":6,
        "title":"Plant"
    },
    {
        "S":"X", "X":"-YF+XFX+FY-", "Y":"+XF-YFY-FX+",
        "direct":0,
        "angle":90,
        "iter":6,
        "title":"Hilbert"
    },
    {
        "S":"L--F--L--F", "L":"+R-F-R+", "R":"-L+F+L-",
        "direct":0,
        "angle":45,
        "iter":10,
        "title":"Sierpinski"
    } 
]

def draw(ax, rule, iter=None):
    # 此方法输入一个规则，输出一个figure
    if iter != None:
        rule["iter"] = iter
    lines = L_System(rule).get_lines();
    lineCollections = collections.LineCollection(lines)
    ax.add_collection(lineCollections, autolim=True)
    ax.axis("equal")
    ax.set_axis_off()
    ax.set_xlim(ax.dataLim.xmin, ax.dataLim.xmax)
    ax.invert_yaxis()

fig = pl.figure(figsize=(7,4.5))
fig.patch.set_facecolor("w")

for i in range(len(rules)): # 依次按照规则生成图案
    ax = fig.add_subplot(231 + i)
    draw(ax, rules[i])

fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
pl.show()