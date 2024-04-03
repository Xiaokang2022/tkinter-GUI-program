# 界面初始化 #
from tkinter import *

from value import value


class initialization:
    def __init__(self):
        self.board_initialization()  # 棋盘初始化
        self.peice_initialization()  # 棋子初始化
        self.face_initialization()  # 图像初始化

    def board_initialization(self, w=3, l=12):  # 棋盘初始化
        value.canvas.place(width=960, height=500)

        value.canvas.create_image(480, 250, image=value.background)  # 背景
        value.canvas.create_rectangle(
            275, 20, 685, 480, width=3, outline=value.colorlis[0])  # 外框
        value.canvas.create_rectangle(
            280, 25, 680, 475, outline=value.colorlis[0])  # 内框

        value.canvas.create_line(
            430, 25, 530, 125, fill=value.colorlis[0])  # 两个“×”
        value.canvas.create_line(430, 375, 530, 475, fill=value.colorlis[0])
        value.canvas.create_line(430, 125, 530, 25, fill=value.colorlis[0])
        value.canvas.create_line(430, 475, 530, 375, fill=value.colorlis[0])

        for y in [175, 325]:  # “十”字形
            for i in [(280, y), (380, y), (480, y), (580, y), (680, y), (330, y+50*(-1)**(y//150)), (630, y+50*(-1)**(y//150))]:
                if i[0] != 280:
                    value.canvas.create_line(
                        # 左上
                        i[0]-w, i[1]-w, i[0]-w-l, i[1]-w, width=2, fill=value.colorlis[0])
                    value.canvas.create_line(
                        i[0]-w, i[1]-w, i[0]-w, i[1]-w-l, width=2, fill=value.colorlis[0])
                    value.canvas.create_line(
                        # 左下
                        i[0]-w, i[1]+w+1, i[0]-w-l, i[1]+w+1, width=2, fill=value.colorlis[0])
                    value.canvas.create_line(
                        i[0]-w, i[1]+w+1, i[0]-w, i[1]+w+l+1, width=2, fill=value.colorlis[0])
                if i[0] != 680:
                    value.canvas.create_line(
                        # 右上
                        i[0]+w+1, i[1]-w, i[0]+w+l+1, i[1]-w, width=2, fill=value.colorlis[0])
                    value.canvas.create_line(
                        i[0]+w+1, i[1]-w, i[0]+w+1, i[1]-w-l, width=2, fill=value.colorlis[0])
                    value.canvas.create_line(
                        # 右下
                        i[0]+w+1, i[1]+w+1, i[0]+w+l+1, i[1]+w+1, width=2, fill=value.colorlis[0])
                    value.canvas.create_line(
                        i[0]+w+1, i[1]+w+1, i[0]+w+1, i[1]+w+l+1, width=2, fill=value.colorlis[0])

        for i in range(75, 425+1, 50):
            value.canvas.create_line(
                280, i, 680, i, fill=value.colorlis[0])  # 横线

        for i in range(330, 630+1, 50):  # 竖线
            value.canvas.create_line(i, 25, i, 225, fill=value.colorlis[0])
            value.canvas.create_line(i, 275, i, 475, fill=value.colorlis[0])

        value.canvas.create_text(480, 250, text='楚河 · 汉界', font=(
            '华文新魏', 35), fill=value.colorlis[0])  # “楚河 · 汉界”

    def peice_initialization(self, count=-1):  # 棋子初始化
        for ylis in value.board_lists:  # 摆子
            count += 1
            for i in ylis:
                if i != -1:
                    x, y = count, ylis.index(i)
                    s_x, s_y = x*50+25, y*50+280
                    value.peice_lists[i] = value.canvas.create_image(
                        s_y, s_x, image=value.resourcelists[i])

    def button_initialization(self):  # 按钮初始化 (allbind.py中进行)
        self.bo1 = value.canvas.create_rectangle(
            720, 315, 940, 360, width=3, outline=value.colorlis[1])  # “设置”按钮
        self.bi1 = value.canvas.create_rectangle(
            725, 320, 935, 355, outline=value.colorlis[1])
        self.bt1 = value.canvas.create_text(
            830, 338, text='设        置', font=('华文新魏', 20), fill=value.colorlis[0])

        self.bo2 = value.canvas.create_rectangle(
            720, 375, 940, 420, width=3, outline=value.colorlis[1])  # “悔棋”按钮
        self.bi2 = value.canvas.create_rectangle(
            725, 380, 935, 415, outline=value.colorlis[1])
        self.bt2 = value.canvas.create_text(
            830, 398, text='悔        棋', font=('华文新魏', 20), fill=value.colorlis[0])

        self.bo3 = value.canvas.create_rectangle(
            720, 435, 940, 480, width=3, outline=value.colorlis[1])  # “退出”按钮
        self.bi3 = value.canvas.create_rectangle(
            725, 440, 935, 475, outline=value.colorlis[1])
        self.bt3 = value.canvas.create_text(
            830, 458, text='退        出', font=('华文新魏', 20), fill=value.colorlis[0])

        self.bo4 = value.canvas.create_rectangle(
            20, 315, 240, 360, width=3, outline=value.colorlis[1])  # “帮助”按钮
        self.bi4 = value.canvas.create_rectangle(
            25, 320, 235, 355, outline=value.colorlis[1])
        self.bt4 = value.canvas.create_text(
            130, 338, text='帮        助', font=('华文新魏', 20), fill=value.colorlis[0])

        self.bo5 = value.canvas.create_rectangle(
            20, 375, 240, 420, width=3, outline=value.colorlis[1])  # “重新开始”按钮
        self.bi5 = value.canvas.create_rectangle(
            25, 380, 235, 415, outline=value.colorlis[1])
        self.bt5 = value.canvas.create_text(
            130, 398, text='重新开始', font=('华文新魏', 20), fill=value.colorlis[0])

        self.bo6 = value.canvas.create_rectangle(
            20, 435, 240, 480, width=3, outline=value.colorlis[1])  # “制作人员”按钮
        self.bi6 = value.canvas.create_rectangle(
            25, 440, 235, 475, outline=value.colorlis[1])
        self.bt6 = value.canvas.create_text(
            130, 458, text='制作人员', font=('华文新魏', 20), fill=value.colorlis[0])

        self.button_lists = [self.bo1, self.bi1, self.bt1, self.bo2, self.bi2, self.bt2, self.bo3, self.bi3, self.bt3,
                             self.bo4, self.bi4, self.bt4, self.bo5, self.bi5, self.bt5, self.bo6, self.bi6, self.bt6]

    def face_initialization(self):  # 图像初始化
        value.canvas.create_rectangle(
            720, 20, 940, 300, width=3, outline=value.colorlis[1])  # 步骤显示板
        value.canvas.create_rectangle(
            725, 25, 935, 295, outline=value.colorlis[1])
        value.canvas.create_text(830, 40, text='下棋记录', font=(
            '华文新魏', 20), fill=value.colorlis[0])

        value.canvas2.place(width=205, height=240, x=728, y=52)
        value.canvas2.create_image(480-728, 240-52, image=value.background)
        value.canvas2.create_image(100, 100, image=value.face)

        def back(event):
            if len(value.steptextlis) > 12:
                if event.delta < 0 and value.firststep > 250-len(value.steptextlis)*20:
                    for i in value.steptextlis:
                        value.canvas2.move(i, 0, -20)
                    value.firststep -= 20
                elif event.delta > 0 and value.firststep <= -10:
                    for i in value.steptextlis:
                        value.canvas2.move(i, 0, 20)
                    value.firststep += 20

        value.canvas2.bind('<MouseWheel>', back)

        value.canvas.create_rectangle(
            20, 20, 240, 300, width=3, outline=value.colorlis[1])  # 信息显示板
        value.canvas.create_rectangle(
            25, 25, 235, 295, outline=value.colorlis[1])
        value.canvas.create_image(130, 160, image=value.face)
        value.canvas.create_text(130, 40, text='游戏信息', font=(
            '华文新魏', 20), fill=value.colorlis[0])

    def buttonchange(self, n, mode):  # 按钮皮肤
        if mode == 'change1':  # 模式一:经过
            for i in self.button_lists:
                if (n-1)*3 <= self.button_lists.index(i) < n*3:
                    try:
                        value.canvas.itemconfig(i, outline=value.colorlis[5])
                    except:
                        value.canvas.itemconfig(i, fill=value.colorlis[5])

        elif mode == 'change2':  # 模式二:按下
            for i in self.button_lists:
                if (n-1)*3 <= self.button_lists.index(i) < n*3:
                    try:
                        value.canvas.itemconfig(i, outline=value.colorlis[2])
                    except:
                        value.canvas.itemconfig(i, fill=value.colorlis[2])

        else:  # 模式三:离开
            for i in self.button_lists:
                try:
                    value.canvas.itemconfig(i, outline=value.colorlis[1])
                except:
                    value.canvas.itemconfig(i, fill=value.colorlis[0])
