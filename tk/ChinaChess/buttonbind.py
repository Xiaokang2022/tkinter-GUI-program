# 关联处理 #
from tkinter import *

from buttonfunction import function
from initialization import initialization
from value import value


class buttonbind:
    def __init__(self):
        self.changelis = ['change1', 'change2', 'change3']

        value.game.bind(
            # 按下
            '<Button-1>', lambda event: self.buttonchange(event, 1, mode=2))
        value.canvas.bind('<Motion>', lambda event: self.buttonchange(
            event, 0, mode=1))  # 经过及离开
        value.canvas.bind(
            # 按下
            '<B1-Motion>', lambda event: self.buttonchange(event, 1, mode=2))
        value.canvas.bind('<ButtonRelease-1>',
                          # 松开
                          lambda event: self.buttonchange(event, 0, 0, 0))
        value.game.bind('<Any-KeyPress>', self.keypress_bind)  # 键盘响应

        self.setbind()
        initialization.button_initialization(self)  # 按钮初始化

    def buttonchange(self, event, change, mode=0, m=''):
        x, y = event.x, event.y
        change = self.changelis[change]

        if (720 <= x <= 935 and 320 <= y <= 355) or m == 's':  # 关联“设置”按钮
            initialization.buttonchange(self, 1, change)
            if m in ['s', 0]:
                function.b1_func(self)

        elif (720 <= x <= 935 and 380 <= y <= 415) or m == 'r':  # 关联“悔棋”按钮
            initialization.buttonchange(self, 2, change)
            if m in ['r', 0]:
                function.b2_func(self)

        elif (720 <= x <= 935 and 440 <= y <= 475) or m == 'q':  # 关联“退出”按钮
            initialization.buttonchange(self, 3, change)
            if m in ['q', 0]:
                function.b3_func(self)

        elif (20 <= x <= 235 and 320 <= y <= 355) or m == 'h':  # 关联“帮助”按钮
            initialization.buttonchange(self, 4, change)
            if m in ['h', 0]:
                function.b4_func(self)

        elif (20 <= x <= 235 and 380 <= y <= 415) or m == 'a':  # 关联“重新开始”按钮
            initialization.buttonchange(self, 5, change)
            if m in ['a', 0]:
                function.b5_func(self)

        elif (20 <= x <= 235 and 440 <= y <= 475) or m == 'm':  # 关联“制作人员”按钮
            initialization.buttonchange(self, 6, change)
            if m in ['m', 0]:
                function.b6_func(self)

        elif mode == 1:
            initialization.buttonchange(self, 0, 'change3')  # 关联离开按钮
        elif mode == 2:
            self.buttonchange(event, 0, mode=1)  # 按下

    def keypress_bind(self, event, count=0):  # 键盘响应
        m = event.char
        if count == 0:
            if m == 's':
                initialization.buttonchange(self, 1, 'change1')
            elif m == 'r':
                initialization.buttonchange(self, 2, 'change1')
            elif m == 'q':
                initialization.buttonchange(self, 3, 'change1')
            elif m == 'h':
                initialization.buttonchange(self, 4, 'change1')
            elif m == 'i':
                initialization.buttonchange(self, 5, 'change1')
            elif m == 'm':
                initialization.buttonchange(self, 6, 'change1')
            value.game.after(1, self.keypress_bind, event, 1)
        elif count == 1:
            self.buttonchange(event, 0, 0, m)
            value.game.after(80, self.keypress_bind, event, 2)
        else:
            self.buttonchange(event, 0, mode=1)

    def setbind(self):
        for i in value.slis+[value.sbt1, value.sbt2]:
            i.bind('<Enter>', lambda event, i=i: enter(i))
            i.bind('<Leave>', lambda event, i=i: leave(i))

        def enter(i):
            i.config(bg=value.colorlis[4])

        def leave(i):
            i.config(bg=value.colorlis[3])
