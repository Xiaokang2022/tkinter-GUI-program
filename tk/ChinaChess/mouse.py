# 鼠标位置显示 #
from tkinter import *

from value import value


class mouse:
    def __init__(self):
        self.tempx, self.tempy = 0, 0  # 初始化鼠标位置
        value.game.bind('<Motion>', self.callback)  # 关联鼠标移动事件

    def callback(self, event, color=value.colorlis[-1], dv1=25, dv2=10, w=2):
        if 250 < event.x < 705:  # 判断是否越界
            event.x, event.y = 50*int((event.x-255)/50) + \
                280, 50*int(event.y/50)+25  # 处理鼠标位置
            if (event.x, event.y) != (self.tempx, self.tempy):  # 显示框
                self.tempx, self.tempy = event.x, event.y

                try:  # 删除之前的位置
                    for i in [self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7, self.l8]:
                        value.canvas.delete(i)
                except:
                    pass

                self.l1 = value.canvas.create_line(
                    event.x-dv1, event.y-dv1, event.x-dv1, event.y-dv2, width=w, fill=color)  # 左上
                self.l2 = value.canvas.create_line(
                    event.x-dv1, event.y-dv1, event.x-dv2, event.y-dv1, width=w, fill=color)

                self.l3 = value.canvas.create_line(
                    event.x-dv1, event.y+dv1, event.x-dv1, event.y+dv2, width=w, fill=color)  # 左下
                self.l4 = value.canvas.create_line(
                    event.x-dv1, event.y+dv1, event.x-dv2, event.y+dv1, width=w, fill=color)

                self.l5 = value.canvas.create_line(
                    event.x+dv1, event.y-dv1, event.x+dv1, event.y-dv2, width=w, fill=color)  # 右上
                self.l6 = value.canvas.create_line(
                    event.x+dv1, event.y-dv1, event.x+dv2, event.y-dv1, width=w, fill=color)

                self.l7 = value.canvas.create_line(
                    event.x+dv1, event.y+dv1, event.x+dv2, event.y+dv1, width=w, fill=color)  # 右下
                self.l8 = value.canvas.create_line(
                    event.x+dv1, event.y+dv1, event.x+dv1, event.y+dv2, width=w, fill=color)
