# 玩家移动模块 #
from tkinter import *

from rule import rule
from value import value


class play():
    def __init__(self):
        value.canvas.bind('<Button-1>', self.move)

    def move(self, event):  # 移动操作
        if 250 < event.x < 705:
            value.play_count = 1 if value.play_count == 0 else 0
            x, y = int((event.x-255)/50), int(event.y/50)

            # 选中棋子
            if value.play_count == 1 and value.board_lists[y][x] in value.team and value.DEAD == 0:
                self.peice_info(x, y, 1)
                value.play_tampvalue = value.board_lists[y][x]
                value.play_tamp_x, value.play_tamp_y = x, y
                value.board_lists[y][x] = -1

            elif value.play_count == 0 and value.info_lists[y][x] != 0:  # 移动棋子
                self.peice_info(x, y, 0)
                if value.board_lists[y][x] != -1:
                    value.canvas.move(
                        value.peice_lists[value.board_lists[y][x]], 0, 600)
                value.board_lists[y][x] = value.play_tampvalue
                if [value.play_tamp_x, value.play_tamp_y] != [x, y]:
                    dx, dy = (x-value.play_tamp_x)*50, (y-value.play_tamp_y)*50
                    self.fluent(dx, dy)

                    rule.Dead(self)
                    value.step += 1
                    rule.stepinfo(self, dy, x)
                    rule.Modes(self)
                    rule.gameinfo(self)
                    value.regretuselis.append(eval(str(value.board_lists)))
                    rule.AIprocess(self)

            elif value.play_count == 0 and value.info_lists[y][x] == 0:  # 换选棋子
                value.board_lists[value.play_tamp_y][value.play_tamp_x] = value.play_tampvalue
                self.peice_info(x, y, 0)

                if value.board_lists[y][x] in value.team and [value.play_tamp_x, value.play_tamp_y] != [x, y]:
                    self.peice_info(x, y, 1)
                    value.play_tampvalue = value.board_lists[y][x]
                    value.play_tamp_x, value.play_tamp_y = x, y
                    value.board_lists[y][x] = -1
                    value.play_count = 1

            else:
                value.play_count = 1 if value.play_count == 0 else 0  # 清除操作

    def fluent(self, dx, dy, flu=0, lis=[0.02, 0.02, 0.06, 0.1, 0.18, 0.3, 0.18, 0.1, 0.06, 0.02, 0.02, -0.06]):  # 移动流畅函数
        value.canvas.move(
            value.peice_lists[value.play_tampvalue], lis[flu]*dx, lis[flu]*dy)
        if flu < 11:
            value.canvas.after(10, self.fluent, dx, dy, flu+1)

    def peice_info(self, x, y, count):  # 路径计算
        if count == 1:
            i = value.board_lists[y][x]

            if i in [0, 16]:  # 将帅
                self.info(x, y, M=2)
                for sx, sy in zip([x+1, x-1, x, x], [y, y, y+1, y-1]):
                    if 0+7*(i//16) <= sy <= 2+7*(i//16) and 3 <= sx <= 5:
                        try:
                            if value.board_lists[sy][sx] == -1:
                                self.info(sx, sy)
                            else:
                                self.info(sx, sy, M=1, i=i)
                        except:
                            pass

                start_y = y+(-1)**(i//16)  # “白脸将” #
                key_y = 7*(1-(i//16))
                for sy in range(start_y, start_y+9*(-1)**(i//16), (-1)**(i//16)):
                    if key_y <= sy <= key_y+2:
                        if value.board_lists[sy][x] in [0, 16]:
                            self.info(x, sy, M=1, i=i)
                    else:
                        try:
                            if value.board_lists[sy][x] != -1:
                                break
                        except:
                            break

            if i in [1, 2, 17, 18]:  # 士仕
                self.info(x, y, M=2)
                for sx, sy in zip([x+1, x-1, x+1, x-1], [y+1, y-1, y-1, y+1]):
                    if 0+7*(i//17) <= sy <= 2+7*(i//17) and 3 <= sx <= 5:
                        try:
                            if value.board_lists[sy][sx] == -1:
                                self.info(sx, sy)
                            else:
                                self.info(sx, sy, M=1, i=i)
                        except:
                            pass

            elif i in [3, 4, 19, 20]:  # 象相(撇腿)
                self.info(x, y, M=2)
                for sx, sy in zip([x+2, x-2, x+2, x-2], [y+2, y-2, y-2, y+2]):
                    if 0+5*(i//19) <= sy <= 4+5*(i//19) and 0 <= sx <= 8 and value.board_lists[(sy+y)//2][(sx+x)//2] == -1:
                        try:
                            if value.board_lists[sy][sx] == -1:
                                self.info(sx, sy)
                            else:
                                self.info(sx, sy, M=1, i=i)
                        except:
                            pass

            elif i in [5, 6, 21, 22]:  # 马(撇腿)
                self.info(x, y, M=2)
                for sx, sy in zip([x+2, x+2, x-2, x-2, x+1, x+1, x-1, x-1], [y+1, y-1, y+1, y-1, y+2, y-2, y+2, y-2]):
                    if 0 <= sy <= 9 and 0 <= sx <= 8 and value.board_lists[round((sy+2*y)/3)][round((sx+2*x)/3)] == -1:
                        try:
                            if value.board_lists[sy][sx] == -1:
                                self.info(sx, sy)
                            else:
                                self.info(sx, sy, M=1, i=i)
                        except:
                            pass

            elif i in [7, 8, 23, 24]:  # 车
                self.info(x, y, M=2)
                for lis in [range(1, 10), range(-1, -10, -1)]:

                    for d in lis:
                        try:
                            if x+d >= 0:
                                if value.board_lists[y][x+d] == -1:
                                    self.info(x+d, y)
                                else:
                                    self.info(x+d, y, M=1, i=i)
                                    break
                            else:
                                break
                        except:
                            pass

                    for d in lis:
                        try:
                            if y+d >= 0:
                                if value.board_lists[y+d][x] == -1:
                                    self.info(x, y+d)
                                else:
                                    self.info(x, y+d, M=1, i=i)
                                    break
                            else:
                                break
                        except:
                            pass

            elif i in [9, 10, 25, 26]:  # 炮
                self.info(x, y, M=2)
                for lis in [range(1, 10), range(-1, -10, -1)]:

                    self.pao_c = 0
                    for d in lis:
                        try:
                            if x+d >= 0:
                                if value.board_lists[y][x+d] == -1 and self.pao_c == 0:
                                    self.info(x+d, y)
                                elif value.board_lists[y][x+d] != -1:
                                    self.pao_c += 1
                                if self.pao_c == 2:
                                    self.info(x+d, y, M=1, i=i)
                                    break
                            else:
                                break
                        except:
                            pass

                    self.pao_c = 0
                    for d in lis:
                        try:
                            if y+d >= 0:
                                if value.board_lists[y+d][x] == -1 and self.pao_c == 0:
                                    self.info(x, y+d)
                                elif value.board_lists[y+d][x] != -1:
                                    self.pao_c += 1
                                if self.pao_c == 2:
                                    self.info(x, y+d, M=1, i=i)
                                    break
                            else:
                                break
                        except:
                            pass

            elif i in [11, 12, 13, 14, 15, 27, 28, 29, 30, 31]:  # 卒兵
                self.info(x, y, M=2)
                if (y < 5 and i//27 == 0) or (4 < y and i//27 == 1):
                    sy = y+(-1)**(i//27)
                    try:
                        if value.board_lists[sy][x] == -1:
                            self.info(x, sy)
                        else:
                            self.info(x, sy, M=1, i=i)
                    except:
                        pass

                elif ((5 <= y <= 9 and i//27 == 0) or (0 <= y <= 4 and i//27 == 1)) and 0 <= x <= 8:
                    dy = y+(-1)**(i//27)
                    for sx, sy in zip([x-1, x, x+1], [y, dy, y]):
                        try:
                            if value.board_lists[sy][sx] == -1:
                                self.info(sx, sy)
                            else:
                                self.info(sx, sy, M=1, i=i)
                        except:
                            pass

        else:  # 删除显示
            for i in value.templists:
                value.canvas.delete(i)

            value.info_lists = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],

                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def info(self, sx, sy, M=0, i=None):  # 路径显示
        if M == 0:  # 路径
            value.info_lists[sy][sx] = 1
            s_x, s_y = sx*50+280, sy*50+25
            value.play_tampvalue = value.canvas.create_rectangle(
                s_x-10, s_y-10, s_x+10, s_y+10, outline=value.colorlis[7], width=2)

        elif M == 1:  # 敌人
            if (0 <= i <= 15 and value.board_lists[sy][sx] > 15) or (i > 15 and 0 <= value.board_lists[sy][sx] <= 15):
                value.info_lists[sy][sx] = 2
                s_x, s_y = sx*50+280, sy*50+25
                value.play_tampvalue = value.canvas.create_rectangle(
                    s_x-25, s_y-25, s_x+25, s_y+25, outline=value.colorlis[8], width=2)

        elif M == 2:  # 自己
            s_x, s_y = sx*50+280, sy*50+25
            value.play_tampvalue = value.canvas.create_rectangle(
                s_x-25, s_y-25, s_x+25, s_y+25, outline=value.colorlis[9], width=2)

        value.templists.append(value.play_tampvalue)
