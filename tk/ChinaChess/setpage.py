# 设置页面 #
from tkinter import *

from value import value


class setpage:

    def set_button(self, n):
        try:  # 切换时删除之前的
            value.text_canvas.unbind('<Button-1>')
            value.text_canvas.unbind('<B1-Motion>')
            value.text_canvas.unbind('<Motion>')
            value.text_canvas.unbind('<ButtonRelease-1>')
            for i in value.s1_+value.s2_+value.s3_+value.s4_+value.s5_+value.s6_+value.s7_+value.s8_:
                value.text_canvas.delete(i)
        except:
            pass

        if n == 1:  # 模式设置
            a = value.text_canvas.create_text(
                100, 25, text='模式设置', font=('华文新魏', 25))
            b = value.text_canvas.create_line(
                30, 50, 680, 50, fill=value.colorlis[0])

            c = value.text_canvas.create_rectangle(
                30, 60, 130, 90, outline=value.colorlis[1])
            d = value.text_canvas.create_text(
                80, 75, text='人机模式', font=('华文新魏', 15))
            e = value.text_canvas.create_rectangle(
                150, 60, 250, 90, outline=value.colorlis[1])
            f = value.text_canvas.create_text(
                200, 75, text='对弈模式', font=('华文新魏', 15))
            g = value.text_canvas.create_rectangle(
                270, 60, 370, 90, outline=value.colorlis[1])
            h = value.text_canvas.create_text(
                320, 75, text='机机模式', font=('华文新魏', 15))
            i = value.text_canvas.create_rectangle(
                390, 60, 490, 90, outline=value.colorlis[1])
            j = value.text_canvas.create_text(
                440, 75, text='网络模式', font=('华文新魏', 15))
            k = value.text_canvas.create_rectangle(
                510, 60, 610, 90, outline=value.colorlis[1])
            l = value.text_canvas.create_text(
                560, 75, text='闯关模式', font=('华文新魏', 15))

            m = value.text_canvas.create_rectangle(
                30, 100, 680, 200, outline=value.colorlis[1])  # 描述框

            n = value.text_canvas.create_text(
                180, 220, text='（只有未下棋时才可设置该选项！）', font=('华文新魏', 15))

            text1 = '人类与电脑之间的决斗！\n你以为你能战胜电脑吗？不！你错了！\n真正的答案是：我也不知道！'
            text2 = '人与人之间的对决！\n不会吧，不会吧，居然有人认为有和棋？\n这只是场你死我活的战斗！'
            text3 = '电脑和电脑战斗！\n有些人啊，就喜欢坐在那儿看戏！\n这明明不关你的事，这只是个烧电脑的实验罢了！'
            text4 = '想和网上的朋友玩，那就来这里吧！\n通过局域网的方式，你将和对面的那个傻子对局！\n啊对对对，对面也在和傻子(你)对局！'
            text5 = '接手残局，勇闯鬼门关！\n你今天要是走不出鬼门关，就别回来了！\n因为你回不来了！'

            text = [text1, text2, text3, text4, text5]

            value.text_canvas.itemconfig(
                [d, f, h, j, l][value.modelis.index(value.mode)], fill=value.colorlis[6])
            txt = value.text_canvas.create_text(355, 150, text=text[value.modelis.index(
                value.mode)], font=('华文新魏', 15), justify='center')

            value.s1_ = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, txt]

            def callback11(event):
                for s, t in zip(range(30, 511, 120), [d, f, h, j, l]):
                    if s <= event.x <= s+100 and 60 <= event.y <= 90 and value.step == 0:
                        for z in [d, f, h, j, l]:
                            value.text_canvas.itemconfig(z, fill='black')
                        value.text_canvas.itemconfig(t, fill=value.colorlis[6])
                        value.text_canvas.itemconfig(
                            txt, text=text[(s-30)//120])
                        value.mode = value.modelis[(s-30)//120]

            def callback12(event):
                if 30 <= event.x < 130 and 60 <= event.y <= 90:
                    value.text_canvas.itemconfig(c, fill=value.colorlis[4])
                elif 150 <= event.x < 250 and 60 <= event.y <= 90:
                    value.text_canvas.itemconfig(e, fill=value.colorlis[4])
                elif 270 <= event.x < 370 and 60 <= event.y <= 90:
                    value.text_canvas.itemconfig(g, fill=value.colorlis[4])
                elif 390 <= event.x < 490 and 60 <= event.y <= 90:
                    value.text_canvas.itemconfig(i, fill=value.colorlis[4])
                elif 510 <= event.x < 610 and 60 <= event.y <= 90:
                    value.text_canvas.itemconfig(k, fill=value.colorlis[4])
                else:
                    for z in [c, e, g, i, k]:
                        value.text_canvas.itemconfig(z, fill=value.colorlis[3])

            value.text_canvas.bind('<ButtonRelease-1>', callback11)
            value.text_canvas.bind('<Motion>', callback12)

        elif n == 2:  # 棋局设置
            a = value.text_canvas.create_text(
                100, 25, text='棋局设置', font=('华文新魏', 25))
            b = value.text_canvas.create_line(
                30, 50, 680, 50, fill=value.colorlis[0])
            c = value.text_canvas.create_text(
                70, 75, text='先下棋方', font=('华文新魏', 15))

            d = value.text_canvas.create_rectangle(
                30, 100, 130, 130, outline=value.colorlis[0])
            e = value.text_canvas.create_text(
                80, 115, text='红方', font=('华文新魏', 15))
            f = value.text_canvas.create_rectangle(
                150, 100, 250, 130, outline=value.colorlis[0])
            g = value.text_canvas.create_text(
                200, 115, text='黑方', font=('华文新魏', 15))

            h = value.text_canvas.create_text(
                180, 360, text='（只有未下棋时才可设置该选项！）', font=('华文新魏', 15))

            i = value.text_canvas.create_text(
                70, 160, text='让子设置', font=('华文新魏', 15))

            j = value.text_canvas.create_text(
                50, 200, text='黑方', font=('华文新魏', 15))

            k = value.text_canvas.create_text(
                50, 270, text='红方', font=('华文新魏', 15))

            j1 = value.text_canvas.create_rectangle(
                30, 220, 130, 250, outline=value.colorlis[0])
            j2 = value.text_canvas.create_rectangle(
                140, 220, 240, 250, outline=value.colorlis[0])
            j3 = value.text_canvas.create_rectangle(
                250, 220, 350, 250, outline=value.colorlis[0])
            j4 = value.text_canvas.create_rectangle(
                360, 220, 460, 250, outline=value.colorlis[0])
            j5 = value.text_canvas.create_rectangle(
                470, 220, 570, 250, outline=value.colorlis[0])
            j6 = value.text_canvas.create_rectangle(
                580, 220, 680, 250, outline=value.colorlis[0])

            k1 = value.text_canvas.create_rectangle(
                30, 290, 130, 320, outline=value.colorlis[0])
            k2 = value.text_canvas.create_rectangle(
                140, 290, 240, 320, outline=value.colorlis[0])
            k3 = value.text_canvas.create_rectangle(
                250, 290, 350, 320, outline=value.colorlis[0])
            k4 = value.text_canvas.create_rectangle(
                360, 290, 460, 320, outline=value.colorlis[0])
            k5 = value.text_canvas.create_rectangle(
                470, 290, 570, 320, outline=value.colorlis[0])
            k6 = value.text_canvas.create_rectangle(
                580, 290, 680, 320, outline=value.colorlis[0])

            l1 = value.text_canvas.create_text(
                80, 235, text='左车', font=('华文新魏', 15))
            l2 = value.text_canvas.create_text(
                190, 235, text='右车', font=('华文新魏', 15))
            l3 = value.text_canvas.create_text(
                300, 235, text='左炮', font=('华文新魏', 15))
            l4 = value.text_canvas.create_text(
                410, 235, text='右炮', font=('华文新魏', 15))
            l5 = value.text_canvas.create_text(
                520, 235, text='左马', font=('华文新魏', 15))
            l6 = value.text_canvas.create_text(
                630, 235, text='右马', font=('华文新魏', 15))

            m1 = value.text_canvas.create_text(
                80, 305, text='左车', font=('华文新魏', 15))
            m2 = value.text_canvas.create_text(
                190, 305, text='右车', font=('华文新魏', 15))
            m3 = value.text_canvas.create_text(
                300, 305, text='左炮', font=('华文新魏', 15))
            m4 = value.text_canvas.create_text(
                410, 305, text='右炮', font=('华文新魏', 15))
            m5 = value.text_canvas.create_text(
                520, 305, text='左马', font=('华文新魏', 15))
            m6 = value.text_canvas.create_text(
                630, 305, text='右马', font=('华文新魏', 15))

            value.s2_ = [a, b, c, d, e, f, g, h, i, j, k, j1, j2, j3, j4, j5, j6,
                         k1, k2, k3, k4, k5, k6, l1, l2, l3, l4, l5, l6, m1, m2, m3, m4, m5, m6]

            value.text_canvas.itemconfig(
                [e, g][value.playerlis.index(value.first)//1], fill=value.colorlis[6])

            for x, y, k in zip(value.p_r, value.p_b, range(6)):
                if x == 1:
                    value.text_canvas.itemconfig(
                        [m1, m2, m3, m4, m5, m6][k], fill=value.colorlis[6])
                if y == 1:
                    value.text_canvas.itemconfig(
                        [l1, l2, l3, l4, l5, l6][k], fill=value.colorlis[6])

            def please(w, n, m):  # w哪一方;n第几个;m修改值
                if w == 'r':
                    value.p_r[n] = m
                if w == 'b':
                    value.p_b[n] = m

            def callback21(event):
                if value.step == 0 and value.mode not in ['网络', '闯关']:
                    for s, t in zip([30, 150], [e, g]):
                        if s <= event.x <= s+100 and 100 <= event.y <= 130:
                            for z in [e, g]:
                                value.text_canvas.itemconfig(z, fill='black')
                            value.text_canvas.itemconfig(
                                t, fill=value.colorlis[6])
                            value.first = value.playerlis[(s-30)//120]
                            value.player = value.first

                            if value.mode in ['对弈', '网络']:
                                if value.player == '红方':
                                    value.team = value.r_team
                                else:
                                    value.team = value.b_team
                            elif value.mode == '机机':
                                value.team = []
                            else:
                                if value.player == '红方':
                                    value.team = value.r_team
                                else:
                                    value.team = []

                    for s, t1, t2 in zip(range(30, 581, 110), [l1, l2, l3, l4, l5, l6], [m1, m2, m3, m4, m5, m6]):
                        if s <= event.x <= s+100 and 220 <= event.y <= 250:
                            if value.text_canvas.itemcget(t1, 'fill') == 'black':
                                value.text_canvas.itemconfig(
                                    t1, fill=value.colorlis[6])
                                please('b', (s-30)//110, 1)
                            else:
                                value.text_canvas.itemconfig(t1, fill='black')
                                please('b', (s-30)//110, 0)

                        if s <= event.x <= s+100 and 290 <= event.y <= 320:
                            if value.text_canvas.itemcget(t2, 'fill') == 'black':
                                value.text_canvas.itemconfig(
                                    t2, fill=value.colorlis[6])
                                please('r', (s-30)//110, 1)
                            else:
                                value.text_canvas.itemconfig(t2, fill='black')
                                please('r', (s-30)//110, 0)

            def callback22(event):
                if 30 <= event.x <= 130 and 100 <= event.y <= 130:
                    value.text_canvas.itemconfig(d, fill=value.colorlis[4])
                elif 150 <= event.x <= 250 and 100 <= event.y <= 130:
                    value.text_canvas.itemconfig(f, fill=value.colorlis[4])

                elif 30 <= event.x <= 130 and 220 <= event.y <= 250:
                    value.text_canvas.itemconfig(j1, fill=value.colorlis[4])
                elif 140 <= event.x <= 240 and 220 <= event.y <= 250:
                    value.text_canvas.itemconfig(j2, fill=value.colorlis[4])
                elif 250 <= event.x <= 350 and 220 <= event.y <= 250:
                    value.text_canvas.itemconfig(j3, fill=value.colorlis[4])
                elif 360 <= event.x <= 460 and 220 <= event.y <= 250:
                    value.text_canvas.itemconfig(j4, fill=value.colorlis[4])
                elif 470 <= event.x <= 570 and 220 <= event.y <= 250:
                    value.text_canvas.itemconfig(j5, fill=value.colorlis[4])
                elif 580 <= event.x <= 680 and 220 <= event.y <= 250:
                    value.text_canvas.itemconfig(j6, fill=value.colorlis[4])

                elif 30 <= event.x <= 130 and 290 <= event.y <= 320:
                    value.text_canvas.itemconfig(k1, fill=value.colorlis[4])
                elif 140 <= event.x <= 240 and 290 <= event.y <= 320:
                    value.text_canvas.itemconfig(k2, fill=value.colorlis[4])
                elif 250 <= event.x <= 350 and 290 <= event.y <= 320:
                    value.text_canvas.itemconfig(k3, fill=value.colorlis[4])
                elif 360 <= event.x <= 460 and 290 <= event.y <= 320:
                    value.text_canvas.itemconfig(k4, fill=value.colorlis[4])
                elif 470 <= event.x <= 570 and 290 <= event.y <= 320:
                    value.text_canvas.itemconfig(k5, fill=value.colorlis[4])
                elif 580 <= event.x <= 680 and 290 <= event.y <= 320:
                    value.text_canvas.itemconfig(k6, fill=value.colorlis[4])

                else:
                    for z in [d, f, j1, j2, j3, j4, j5, j6, k1, k2, k3, k4, k5, k6]:
                        value.text_canvas.itemconfig(z, fill=value.colorlis[3])

            value.text_canvas.bind('<ButtonRelease-1>', callback21)
            value.text_canvas.bind('<Motion>', callback22)

        elif n == 3:  # 闯关设置
            a = value.text_canvas.create_text(
                100, 25, text='闯关设置', font=('华文新魏', 25))
            b = value.text_canvas.create_line(30, 50, 680, 50)
            value.s3_ = [a, b]

        elif n == 4:  # 主题设置
            a = value.text_canvas.create_text(
                100, 25, text='主题设置', font=('华文新魏', 25))
            b = value.text_canvas.create_line(
                30, 50, 680, 50, fill=value.colorlis[0])
            c = value.text_canvas.create_text(
                70, 75, text='颜色主题', font=('华文新魏', 15))

            d = value.text_canvas.create_rectangle(
                30, 100, 130, 130, outline=value.colorlis[0])
            e = value.text_canvas.create_rectangle(
                140, 100, 240, 130, outline=value.colorlis[0])
            f = value.text_canvas.create_rectangle(
                250, 100, 350, 130, outline=value.colorlis[0])
            g = value.text_canvas.create_rectangle(
                360, 100, 460, 130, outline=value.colorlis[0])
            h = value.text_canvas.create_rectangle(
                470, 100, 570, 130, outline=value.colorlis[0])

            i = value.text_canvas.create_text(
                80, 115, text='系统默认', font=('华文新魏', 15))
            j = value.text_canvas.create_text(
                190, 115, text='黑白灰', font=('华文新魏', 15))
            k = value.text_canvas.create_text(
                300, 115, text='梦幻蓝', font=('华文新魏', 15))
            l = value.text_canvas.create_text(
                410, 115, text='和谐绿', font=('华文新魏', 15))
            m = value.text_canvas.create_text(
                520, 115, text='典雅粉', font=('华文新魏', 15))

            n = value.text_canvas.create_text(
                120, 155, text='效果展示（一部分）', font=('华文新魏', 15))
            o = value.text_canvas.create_text(
                170, 330, text='（该设置项将在游戏重启后生效）', font=('华文新魏', 15))
            p = value.text_canvas.create_rectangle(
                30, 180, 680, 300, fill=value.colorlis[3], outline=value.colorlis[1])
            q = value.text_canvas.create_rectangle(
                280, 210, 430, 270, outline=value.colorlis[5], fill=value.colorlis[4], width=3)
            r = value.text_canvas.create_text(
                335, 240, text='中国', font=('华文新魏', 15))
            s = value.text_canvas.create_text(
                375, 240, text='象棋', font=('华文新魏', 15), fill=value.colorlis[6])

            value.s4_ = [a, b, c, d, e, f, g, h,
                         i, j, k, l, m, n, o, p, q, r, s]

            value.text_canvas.itemconfig(
                [i, j, k, l, m][value.theme-1], fill=value.colorlis[6])

            def callback41(event):
                if 30 <= event.x <= 130 and 100 <= event.y <= 130:
                    value.text_canvas.itemconfig(d, fill=value.colorlis[4])
                elif 140 <= event.x <= 240 and 100 <= event.y <= 130:
                    value.text_canvas.itemconfig(e, fill=value.colorlis[4])
                elif 250 <= event.x <= 350 and 100 <= event.y <= 130:
                    value.text_canvas.itemconfig(f, fill=value.colorlis[4])
                elif 360 <= event.x <= 460 and 100 <= event.y <= 130:
                    value.text_canvas.itemconfig(g, fill=value.colorlis[4])
                elif 470 <= event.x <= 570 and 100 <= event.y <= 130:
                    value.text_canvas.itemconfig(h, fill=value.colorlis[4])
                else:
                    for z in [d, e, f, g, h]:
                        value.text_canvas.itemconfig(z, fill=value.colorlis[3])

            def callback42(event):
                for x in range(30, 471, 110):
                    if x <= event.x <= x+100 and 100 <= event.y <= 130:
                        for z in [i, j, k, l, m]:
                            value.text_canvas.itemconfig(z, fill='black')
                        value.text_canvas.itemconfig(
                            [i, j, k, l, m][(x-30)//110], fill=value.colorlis[6])
                        value.theme = (x-30)//110+1
                        with open('resources\\cache.txt', 'w') as infile:
                            infile.write(str(value.theme))
                        themeprocess(value.theme)

            def themeprocess(n):
                value.text_canvas.itemconfig(
                    p, fill=value.colorlists[n-1][3], outline=value.colorlists[n-1][1])
                value.text_canvas.itemconfig(
                    q, fill=value.colorlists[n-1][4], outline=value.colorlists[n-1][5])
                value.text_canvas.itemconfig(s, fill=value.colorlists[n-1][6])

            value.text_canvas.bind('<Motion>', callback41)
            value.text_canvas.bind('<ButtonRelease-1>', callback42)

        elif n == 5:  # 音效设置
            a = value.text_canvas.create_text(
                100, 25, text='音效设置', font=('华文新魏', 25))
            b = value.text_canvas.create_line(30, 50, 680, 50)
            value.s5_ = [a, b]

        elif n == 6:  # 窗口设置
            self.x = int((1-value.alpha)*500+59)
            text1 = '设置范围为0~100，0为不透明，100为完全透明，默认为0（不透明）'
            a = value.text_canvas.create_text(
                100, 25, text='窗口设置', font=('华文新魏', 25))
            b = value.text_canvas.create_line(
                30, 50, 680, 50, fill=value.colorlis[0])
            c = value.text_canvas.create_text(
                100, 75, text='设置窗口透明度', font=('华文新魏', 15))
            d = value.text_canvas.create_rectangle(
                30, 100, 680, 150, outline=value.colorlis[0])
            e = value.text_canvas.create_line(
                60, 125, 590, 125, fill=value.colorlis[0])
            f = value.text_canvas.create_rectangle(
                self.x, 115, self.x+30, 135, fill=value.colorlis[6])
            g = value.text_canvas.create_text(
                340, 180, text=text1, font=('华文新魏', 15))
            h = value.text_canvas.create_text(
                45, 125, text='0', font=('华文新魏', 15))
            i = value.text_canvas.create_text(
                610, 125, text='100', font=('华文新魏', 15))
            j = value.text_canvas.create_line(
                630, 110, 630, 140, fill=value.colorlis[0])
            k = value.text_canvas.create_text(655, 125, text=str(
                (self.x-59)//5), font=('华文新魏', 15), fill=value.colorlis[6])
            value.s7_ = [a, b, c, d, e, f, g, h, i, j, k]

            value.text_canvas.bind(
                '<Button-1>', lambda event: callback61(event))
            value.text_canvas.bind(
                '<B1-Motion>', lambda event: callback62(event))

            def callback61(event):
                self.temp_x = event.x

            def callback62(event):
                if 100 <= event.y <= 150 and 60 <= event.x <= 590:
                    if (event.x-self.temp_x > 0 and self.x <= 560) or (event.x-self.temp_x < 0 and self.x >= 60):
                        value.text_canvas.move(f, event.x-self.temp_x, 0)
                        self.x += event.x-self.temp_x
                        self.temp_x = event.x
                        v = (self.x-59)//5
                        value.text_canvas.itemconfig(k, text=str(v))
                        value.alpha = 1-v/100
                        value.game.wm_attributes('-alpha', value.alpha)

        elif n == 7:  # 系统说明
            text1 = '游戏名称：中国象棋\n游戏版本：1.0\n人机内核：垃圾测试内核\n发布日期：2022/07/14\n运行内存：30MB左右\n占用空间：暂无数据'
            text2 = '更多详细信息：\n\nhttps://blog.csdn.net/weixin_62651706'
            text3 = '版权声明：\n\n        本游戏完全由小康独立开发，为该游戏的版权所有者，\n如盗窃程序内部资源，必究哦！'
            a = value.text_canvas.create_text(
                100, 25, text='系统说明', font=('华文新魏', 25))
            b = value.text_canvas.create_line(
                30, 50, 680, 50, fill=value.colorlis[0])
            c = value.text_canvas.create_text(
                125, 125, text=text1, font=('华文新魏', 15))
            d = value.text_canvas.create_text(
                200, 250, text=text2, font=('华文新魏', 15))
            e = value.text_canvas.create_text(
                300, 350, text=text3, font=('华文新魏', 15))
            value.s7_ = [a, b, c, d, e]

        elif n == 8:  # 暂无设置
            a = value.text_canvas.create_text(
                100, 25, text='暂无设置', font=('华文新魏', 25))
            b = value.text_canvas.create_line(
                30, 50, 680, 50, fill=value.colorlis[0])
            value.s8_ = [a, b]
