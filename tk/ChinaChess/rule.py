# 制定规则 #
from copy import deepcopy
from tkinter import *

from AI import AI
from value import value


class rule:
    def __init__(self):
        self.gameinfo()

    def stepinfo(self, dy, now_x):  # 棋谱记录
        v = value.play_tampvalue
        before_x = value.play_tamp_x

        try:
            if len(value.steptextlis) > 12:
                for i in value.steptextlis:
                    value.canvas2.move(
                        i, 0, 250-len(value.steptextlis)*20-value.firststep)
                value.firststep = 250-len(value.steptextlis)*20
        except:
            pass

        if 16 <= v <= 31:  # “红方”情况
            player = '红方' if value.mode in ['对弈', '网络', '机机'] else '玩家'
            way = '进' if dy < 0 else '退' if dy > 0 else '平'
            num = value.number[-before_x-1]
            if way == '平':
                dis = value.number[-now_x-1]
            else:
                if value.peices[v] in ['马', '相', '仕']:
                    dis = value.number[-now_x-1]
                else:
                    dis = value.number[abs(dy)//50-1]

        if 0 <= v <= 15:  # “黑方”情况
            player = '黑方' if value.mode in ['对弈', '网络', '机机'] else '电脑'
            way = '进' if dy > 0 else '退' if dy < 0 else '平'
            num = value.number[before_x]
            if way == '平':
                dis = value.number[now_x]
            else:
                if value.peices[v] in ['马', '象', '士']:
                    dis = value.number[now_x]
                else:
                    dis = value.number[abs(dy)//50-1]

        steptext = '[%s]%s  [%03d]' % (
            player, value.peices[v]+num+way+dis, value.step)
        s = value.canvas2.create_text(
            102, 250, text=steptext, font=('楷体', 15), fill=value.colorlis[0])
        value.steptextlis.append(s)
        for i in value.steptextlis:
            value.canvas2.move(i, 0, -20)
        value.firststep -= 20

    def gameinfo(self):  # 信息显示
        try:
            value.canvas.delete(value.gameinfo_temp)
        except:
            pass

        gamecontent = '\n游戏模式: '+value.mode+'模式'\
                                + '\n人机难度: '+value.level\
                                + '\n闯关关数: '+value.challenge\
                                + '\n'\
                                + '\n先手方:   '+value.first\
                                + '\n当前方:   '+value.player\
                                + '\n'\
                                + '\n红方让子: '+value.r_please\
                                + '\n黑方让子: '+value.b_please\
                                + '\n'\
                                + '\n悔棋记录:  '+str(value.regret)+' 次'

        value.gameinfo_temp = value.canvas.create_text(
            130, 160, text=gamecontent, font=('楷体', 15), fill=value.colorlis[0])

    def pleaseprocess(self):  # 让子操作
        lis1 = [value.p_r, value.p_b]
        lis2 = [value.r_please, value.b_please]

        for i in [0, 1]:  # 文字显示
            c = lis1[i][0]+lis1[i][1]
            p = lis1[i][2]+lis1[i][3]
            m = lis1[i][4]+lis1[i][5]

            if c+p+m == 0:
                lis2[i] = '无'
            else:
                lis2[i] = ''
                for a, b in zip([c, p, m], ['车', '炮', '马']):
                    lis2[i] += b if a != 0 else ''
                if c//2+p//2+m//2 != 0:
                    lis2[i] += '双'
                    for x, y in zip([c, p, m], ['车', '炮', '马']):
                        if x == 2:
                            lis2[i] = lis2[i].replace(y, '')
                            lis2[i] += y

        value.r_please, value.b_please = lis2

        for i, y, v in zip([0, 1], [[-1, -1, -3, -3, -1, -1], [0, 0, 2, 2, 0, 0]], [[23, 24, 25, 26, 21, 22], [7, 8, 9, 10, 5, 6]]):  # 实际操作

            if lis1[i][0] == 1 and value.board_lists[y[0]][0] != -1:  # 左车让子
                value.canvas.move(
                    value.peice_lists[value.board_lists[y[0]][0]], 0, 600)
                value.regretuselis[0][y[0]][0] = -1
                value.board_lists[y[0]][0] = -1
            if lis1[i][0] == 0 and value.board_lists[y[0]][0] == -1:  # 左车恢复
                value.regretuselis[0][y[0]][0] = v[0]
                value.board_lists[y[0]][0] = v[0]
                value.canvas.move(
                    value.peice_lists[value.board_lists[y[0]][0]], 0, -600)

            if lis1[i][1] == 1 and value.board_lists[y[1]][-1] != -1:  # 右车让子
                value.canvas.move(
                    value.peice_lists[value.board_lists[y[1]][-1]], 0, 600)
                value.regretuselis[0][y[1]][-1] = -1
                value.board_lists[y[1]][-1] = -1
            if lis1[i][1] == 0 and value.board_lists[y[1]][-1] == -1:  # 右车恢复
                value.regretuselis[0][y[1]][-1] = v[1]
                value.board_lists[y[1]][-1] = v[1]
                value.canvas.move(
                    value.peice_lists[value.board_lists[y[1]][-1]], 0, -600)

            if lis1[i][2] == 1 and value.board_lists[y[2]][1] != -1:  # 左炮让子
                value.canvas.move(
                    value.peice_lists[value.board_lists[y[2]][1]], 0, 600)
                value.regretuselis[0][y[2]][1] = -1
                value.board_lists[y[2]][1] = -1
            if lis1[i][2] == 0 and value.board_lists[y[2]][1] == -1:  # 左炮恢复
                value.regretuselis[0][y[2]][1] = v[2]
                value.board_lists[y[2]][1] = v[2]
                value.canvas.move(
                    value.peice_lists[value.board_lists[y[2]][1]], 0, -600)

            if lis1[i][3] == 1 and value.board_lists[y[3]][-2] != -1:  # 右炮让子
                value.canvas.move(
                    value.peice_lists[value.board_lists[y[3]][-2]], 0, 600)
                value.regretuselis[0][y[3]][-2] = -1
                value.board_lists[y[3]][-2] = -1
            if lis1[i][3] == 0 and value.board_lists[y[3]][-2] == -1:  # 右炮恢复
                value.regretuselis[0][y[3]][-2] = v[3]
                value.board_lists[y[3]][-2] = v[3]
                value.canvas.move(
                    value.peice_lists[value.board_lists[y[3]][-2]], 0, -600)

            if lis1[i][4] == 1 and value.board_lists[y[4]][1] != -1:  # 左马让子
                value.canvas.move(
                    value.peice_lists[value.board_lists[y[4]][1]], 0, 600)
                value.regretuselis[0][y[4]][1] = -1
                value.board_lists[y[4]][1] = -1
            if lis1[i][4] == 0 and value.board_lists[y[4]][1] == -1:  # 左马恢复
                value.regretuselis[0][y[4]][1] = v[4]
                value.board_lists[y[4]][1] = v[4]
                value.canvas.move(
                    value.peice_lists[value.board_lists[y[4]][1]], 0, -600)

            if lis1[i][5] == 1 and value.board_lists[y[5]][-2] != -1:  # 右马让子
                value.canvas.move(
                    value.peice_lists[value.board_lists[y[5]][-2]], 0, 600)
                value.regretuselis[0][y[5]][-2] = -1
                value.board_lists[y[5]][-2] = -1
            if lis1[i][5] == 0 and value.board_lists[y[5]][-2] == -1:  # 右马恢复
                value.regretuselis[0][y[5]][-2] = v[5]
                value.board_lists[y[5]][-2] = v[5]
                value.canvas.move(
                    value.peice_lists[value.board_lists[y[5]][-2]], 0, -600)

    def AIprocess(self):
        '''
        if value.mode in ['对弈','网络']:side = None
        elif value.mode in ['人机','闯关']:side = 'b' if value.player == '黑方' else None
        else:side = 'b' if value.player == '黑方' else 'r'
        '''

        def fluent(k, dx, dy, flu=0, lis=[0.02, 0.02, 0.06, 0.1, 0.18, 0.3, 0.18, 0.1, 0.06, 0.02, 0.02, -0.06]):
            value.canvas.move(value.peice_lists[k], lis[flu]*dx, lis[flu]*dy)
            if flu < 11:
                value.canvas.after(10, fluent, k, dx, dy, flu+1)

        def AImove():
            lis = AI(deepcopy(value.board_lists)).search('Red', 10)
            y, x, sy, sx = lis[0], lis[1], lis[2], lis[3]
            if value.board_lists[sy][sx] != -1:
                value.canvas.move(
                    value.peice_lists[value.board_lists[sy][sx]], 0, 600)
            value.board_lists[sy][sx] = value.board_lists[y][x]
            k = value.board_lists[y][x]
            dx, dy = (sx-x)*50, (sy-y)*50
            fluent(k, dx, dy)
            value.board_lists[y][x] = -1

            rule.Dead(self)
            value.step += 1
            rule.stepinfo(self, dy, sx)
            rule.Modes(self)
            rule.gameinfo(self)
            value.regretuselis.append(eval(str(value.board_lists)))
            # rule.AIprocess(self)

        if value.mode in ['人机', '机机']:
            AImove()

    def Modes(self):
        if value.mode in ['人机', '闯关']:  # 人机模式、闯关模式
            if value.player == '黑方':
                value.player = '红方'
                value.team = value.r_team
            else:
                value.player = '黑方'
                value.team = []

        elif value.mode == '机机':
            value.team = []  # 机机模式

        else:  # 对弈模式、网络模式
            if value.player == '黑方':
                value.player = '红方'
                value.team = value.r_team
            else:
                value.player = '黑方'
                value.team = value.b_team

    def Gank(self):  # “将军”
        pass

    def Dead(self, j=0):  # “绝杀”
        def func(c=0):
            if c == 1:
                value.canvas.delete(self.dead)
            else:
                value.canvas.after(1000, func, 1)

        for i in value.board_lists:
            if 0 in i:
                j += 1
            if 16 in i:
                j += 1
        if j != 2:
            self.dead = value.canvas.create_image(480, 250, image=value.dead)
            value.DEAD = 1
            func()
