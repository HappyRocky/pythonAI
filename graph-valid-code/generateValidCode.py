# 生成随机图形验证码
import random
from PIL import Image,ImageDraw,ImageFont

# 创建图片
width = 400
height = 100
img1 = Image.new(mode="RGB",size=(width,height),color=(255,255,255))

# 创建画笔
draw1 = ImageDraw.Draw(img1, mode="RGB")

# 定义要使用的字体
font1 = ImageFont.truetype('simsun.ttc',98)
code = [0]*5 # 长度为5的数组，初始值为0
for i in range(5):
    # 随机从a~z或者0~9中抽取一个字母或数字。char()表示将ASCII码转为字符
    char1 = random.choice([chr(random.randint(65,90)),str(random.randint(0,9))])
    code[i] = char1

    # 随机生成颜色
    color1 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    # 把生成的字母或数字添加到图片上
    draw1.text([i*(400/5),0],char1,color1,font=font1)
    
    # 生随机生成10个点,随机生成10条线
    radio = random.randint(3,8) # 圆点的半径
    for j in range(10):
        c1,c2 = (random.randint(radio,width-radio),random.randint(radio,height-radio)) # 圆心位置
        draw1.ellipse((c1-radio,c2-radio,c1+radio,c2+radio), fill = color1, outline =color1)
        draw1.line((random.randint(0,400),random.randint(0,100),random.randint(0,400),random.randint(0,100)),fill=color1)

# 验证码输出
print("验证码为",code)

# 保存
with open("pic.png","wb") as f:
    img1.save(f,format="png")

# 显示图片
img1.show()