# 按钮功能 #
from tkinter import *

from initialization import initialization
from rule import rule
from setpage import setpage
from value import value


class function:

    def b1_func(self):  # “设置”按钮
        for i in value.slis:
            i.place(width=200, height=50, x=30, y=value.slis.index(i)*50+70)
        for i in value.slis:
            i.config(command=lambda i=i: setpage.set_button(
                self, value.slis.index(i)+1))

        value.sbt1.config(command=lambda: func(2))
        value.sbt2.config(command=lambda: reset())

        def func(m, c=0, flulis=value.flulis):  # 页面切换
            if m == 1:
                x1, x2 = -960*flulis[c], 960*(1-flulis[c])
            elif m == 2:
                x1, x2 = 960*(flulis[c]-1), 960*flulis[c]
            value.canvas.place(width=960, height=500, x=x1)
            value.set_canvas.place(width=960, height=500, x=x2)

            if c == 7 and value.step == 0:
                rule.pleaseprocess(self)
                rule.gameinfo(self)

            if c < 14:
                value.game.after(30, func, m, c+1)

        def reset(): pass

        func(1)

    def b2_func(self):  # “悔棋”按钮
        if len(value.steptextlis) > 1:
            try:
                if len(value.steptextlis) > 12:
                    for i in value.steptextlis:
                        value.canvas2.move(
                            i, 0, 250-len(value.steptextlis)*20-value.firststep)
                    value.firststep = 250-len(value.steptextlis)*20
            except:
                pass

            for i in value.steptextlis:
                value.canvas2.move(i, 0, 40)
            value.canvas2.delete(value.steptextlis[-1])
            value.canvas2.delete(value.steptextlis[-2])
            value.steptextlis = value.steptextlis[:-2]
            value.firststep += 40
            value.step -= 2

            for i in value.peice_lists:
                value.canvas.delete(i)

            value.board_lists = eval(str(value.regretuselis[-3]))
            initialization.peice_initialization(self)

            value.regretuselis = value.regretuselis[:-2]

            value.info_lists = [[0]*9 for _ in range(10)]

            for i in value.templists:
                value.canvas.delete(i)

            value.templists = []
            value.play_count = 0
            value.play_temp_x, value.play_temp_y = -2, -2
            value.play_tempvalue = -2

            value.DEAD = 0
            value.regret += 1
            rule.gameinfo(self)

    def b3_func(self):  # “退出”按钮
        value.game.quit()

    def b4_func(self):  # “帮助”按钮
        value.help_canvas.bind('<Button-1>', lambda event: func(2))

        def func(m, c=0, flulis=value.flulis):  # 页面切换
            if m == 1:
                x1, x2 = 960*flulis[c], 960*(flulis[c]-1)
            elif m == 2:
                x1, x2 = 960*(1-flulis[c]), -960*flulis[c]
            value.canvas.place(width=960, height=500, x=x1)
            value.help_canvas.place(width=960, height=500, x=x2)
            if c < 14:
                value.game.after(30, func, m, c+1)

        func(1)

    def b5_func(self):  # “重新开始”按钮
        value.board_lists = [[7, 5, 3, 1, 0, 2, 4, 6, 8],
                             [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                             [-1, 9, -1, -1, -1, -1, -1, 10, -1],
                             [11, -1, 12, -1, 13, -1, 14, -1, 15],
                             [-1, -1, -1, -1, -1, -1, -1, -1, -1],

                             [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                             [27, -1, 28, -1, 29, -
                              1, 30, -1, 31],
                             [-1, 25, -1, -1, -
                              1, -1, -1, 26, -1],
                             [-1, -1, -1, -1, -
                              1, -1, -1, -1, -1],
                             [23, 21, 19, 17, 16, 18, 20, 22, 24]]

        value.info_lists = [[0]*9 for _ in range(10)]

        for i in value.peice_lists:
            value.canvas.delete(i)
        for i in value.templists:
            value.canvas.delete(i)

        initialization.peice_initialization(self)

        value.templists = []
        value.play_count = 0
        value.play_temp_x, value.play_temp_y = -2, -2
        value.play_tempvalue = -2
        value.DEAD = 0

        for i in value.steptextlis:
            value.canvas2.delete(i)

        value.steptextlis = []
        value.firststep = 250
        value.step = 0

        value.r_please, value.b_please = '无', '无'

        for i in range(6):
            value.p_r[i] == 0
            value.p_b[i] == 0

        value.regret = 0
        value.regretuselis = [eval(str(value.board_lists))]

        value.player = '红方' if value.first == '黑方' else '黑方'
        rule.Modes(self)
        rule.gameinfo(self)

    def b6_func(self):  # “制作人员”按钮
        text = value.make_canvas2.create_text(150, 580, text=value.maketext, font=(
            '华文新魏', 20), fill='yellow', justify='center')

        value.make_canvas.bind('<Button-1>', lambda event: func(2))
        value.make_canvas2.bind('<Button-1>', lambda event: func(2))
        value.make_canvas2.bind('<Enter>', lambda event: speed(0))
        value.make_canvas2.bind('<Leave>', lambda event: speed(1))

        def speed(n):
            value.textspeed = 0 if n == 0 else -1

        def makefunc(i=580):
            value.make_canvas2.move(text, 0, value.textspeed)
            if i > -360:
                value.make_canvas2.after(60, makefunc, i-1)

        def func(m, c=0, flulis=value.flulis):  # 页面切换
            if m == 1:
                x1, x2 = 960*flulis[c], 960*(flulis[c]-1)
            elif m == 2:
                x1, x2 = 960*(1-flulis[c]), -960*flulis[c]
                if c == 14:
                    value.make_canvas2.delete(text)
            value.canvas.place(width=960, height=500, x=x1)
            value.make_canvas.place(width=960, height=500, x=x2)
            if c < 14:
                value.game.after(30, func, m, c+1)
            else:
                makefunc()

        func(1)
