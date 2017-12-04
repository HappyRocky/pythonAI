# 生成随机图形验证码
import random
from PIL import Image,ImageDraw,ImageFont

# 创建图片，400x100 px，RGB=(255,255,255)
img1 = Image.new(mode="RGB",size=(400,100),color=(255,255,255))

# 创建画笔
draw1 = ImageDraw.Draw(img1, mode="RGB")

# 定义要使用的字体
font1 = ImageFont.truetype('simsun.ttc',98)

for i in range(5):
    # 随机从a~z或者0~9中抽取一个字母或数字。char()表示将ASCII码转为字符
    char1 = random.choice([chr(random.randint(65,90)),str(random.randint(0,9))])

    # 随机生成颜色
    color1 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    # 把生成的字母或数字添加到图片上
    draw1.text([i*80,0],char1,color1,font=font1)
    
    # 生成一个红点一个黑点
    draw1.point([100,100],fill="red")
    draw1.point([80,80],fill=(0,0,0))
    
    # 画两条线，前两个数是开始坐标，后两个数是结束坐标
    draw1.line((100,50,300,50),fill="red")
    draw1.line((100,60,200,10),fill="blue")

# 保存
with open("pic.png","wb") as f:
    img1.save(f,format="png")

# 显示图片
img1.show()