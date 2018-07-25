# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:57:51 2018

@author: gongyanshang1

测试turtle库
"""

import turtle
def draw_snake(rad, angle, len, neckrad):
    for _ in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.forward(rad/2)
    turtle.circle(neckrad, 180)
    turtle.forward(rad/4)
    
if "__main__" == __name__:
    turtle.setup(1500, 1400, 0, 0)
    turtle.pensize(30)
    turtle.pencolor("green")
    turtle.seth(-40)
    draw_snake(70, 80, 1, 15)

