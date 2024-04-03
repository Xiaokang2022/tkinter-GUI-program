from random import *
from tkinter import *

import pygame

################################################################################################################
pygame.mixer.init()
pygame.mixer.music.load('resources\\Rise.wav')  # 加载音乐
game = Tk()  # 创建窗口
###################################### 可设置的默认变量 ######################################
# 语言变量 #
Englishfont = ['Set', 'Play', 'Quit', 'System Set', 'Select Game', 'Refresh Rate', 'Transparency', 'Font', 'Language', 'Music', 'OK', 'Cancel', 'None', 'On', 'Off', 'Help', 'Restore Default',
               'Refresh rate is the refresh rate\nof the background picture\nTransparency is the transparency\nof the game window\n\n1ms≤Refresh rate≤1000ms\n0<Transparency≤1', 'Again',
               "Press 'w' , 's' , 'a' and 'd' to move!\n4000 points win!\nGood luck!"]
Chinesefont = ['设置', '开始', '退出', '系统设置', '选择游戏', '刷新率', '透明度', '字体', '语言', '音乐', '确定', '取消', '暂无', '开', '关', '帮助', '恢复默认',
               '刷新率是背景图片的刷新速度\n透明度是游戏窗口的透明程度\n\n1ms≤刷新率≤1000ms\n0<透明度≤1', '重置',
               '按‘w’、‘s’、‘a’和‘d’进行移动！\n4000分胜利！\n祝你好运！']

language = Englishfont  # 长度为20
# 特殊变量 #
s_gif = 10  # gif图刷新速度
s_alpha = 1  # 窗口透明度
s_font = '华文新魏'  # 字体
s_language = 'English'  # 语言
s_audio = language[13]  # 声音
# 系统变量 #
(s_1 := StringVar()).set(s_gif)
(s_2 := StringVar()).set(s_alpha)
(s_3 := StringVar()).set(s_font)
(s_4 := StringVar()).set(s_language)
(s_5 := StringVar()).set(s_audio)
########################################## 通用函数 ##########################################
def enter(event): event.widget['fg'] = 'yellow'; event.widget['bg'] = 'dimgray'
def leave(event): event.widget['fg'] = 'orange'; event.widget['bg'] = 'black'
def enter2(event): event.widget['bg'] = 'grey'; event.widget['fg'] = 'orange'


def leave2(event):
    event.widget['bg'] = 'lightyellow'
    event.widget['fg'] = 'black'


def enter3(event): event.widget['bg'] = 'springgreen'
def leave3(event): event.widget['bg'] = 'lightgreen'
def shutenter(event): event.widget['fg'] = 'white'; event.widget['bg'] = 'red'
def shutleave(event): event.widget['fg'] = 'black'; event.widget['bg'] = 'grey'


def helpenter(event):
    event.widget['fg'] = 'white'
    event.widget['bg'] = 'lightgreen'


def GameQuit_MusicSet():
    global s_audio
    if s_audio == 'On' or s_audio == '开':
        s_audio = language[13]
        s_5.set(s_audio)
        pygame.mixer.music.play(loops=10)


##############################################################################################
gamelist = ['2048小游戏', '简易枪战[!]', '大鱼吃小鱼',
            '俄罗斯方块[!]', '贪吃蛇[!]', '飞机大战[!]', language[12]]
#################################################### 游戏代码区域 ####################################################
# 游戏1 #


def Game1():
    global size
    game.geometry('305x205+500+250')
    game1 = Frame(game)
    size = '305x205'
    game1.place(width=305, height=205)

    def base():
        numdict = {1: {}, 2: {}, 3: {}, 4: {}}
        for key in numdict.keys():
            numdict[key] = {1: '', 2: '', 3: '', 4: ''}
        while 1:
            x1, x2, y1, y2 = randint(1, 4), randint(
                1, 4), randint(1, 4), randint(1, 4)
            if x1 != x2 or y1 != y2:
                numdict[x1][y1], numdict[x2][y2] = 2, 2
                break

        Label(game1, bg='#BBADA0').place(width=205, height=205)
        Label(game1, bg='orange').place(width=100, height=205, x=205)
        Label(game1, bg='#FAF8EF').place(x=210, y=5, width=90, height=195)
        (score := StringVar()).set('Score\n\n0')
        (score_value := StringVar()).set('0')
        Label(game1, textvariable=score, font=(s_font, 15),
              bg='yellow').place(x=215, y=10, width=80, height=100)
        quitbutton = Button(game1, text=language[2], font=(
            s_font, 15), bd=0, bg='lightgreen', command=lambda: game1quit())
        quitbutton.place(x=215, y=160, width=80, height=30)
        playbutton = Button(game1, text=language[1], font=(
            s_font, 15), bd=0, bg='lightgreen', command=lambda: gamestart())
        playbutton.place(x=215, y=120, width=80, height=30)

        n14 = StringVar()
        n24 = StringVar()
        n34 = StringVar()
        n44 = StringVar()
        n13 = StringVar()
        n23 = StringVar()
        n33 = StringVar()
        n43 = StringVar()
        n12 = StringVar()
        n22 = StringVar()
        n32 = StringVar()
        n42 = StringVar()
        n11 = StringVar()
        n21 = StringVar()
        n31 = StringVar()
        n41 = StringVar()

        for sy in [5, 55, 105, 155]:  # 放置格子
            for sx, i in zip([5, 55, 105, 155], [n14, n24, n34, n44, n13, n23, n33, n43, n12, n22, n32, n42, n11, n21, n31, n41][4*(sy-5)//50:4*(sy+45)//50]):
                Label(game1, bg='#CDC1B4', textvariable=i, font=(
                    s_font, 15)).place(width=45, height=45, y=sy, x=sx)

        def initialization():  # 初始化
            for x in range(1, 5):
                for y, i in zip(range(1, 5), [n11, n12, n13, n14, n21, n22, n23, n24, n31, n32, n33, n34, n41, n42, n43, n44][4*(x-1):4*x]):
                    i.set(numdict[x][y])

        def gamewin(score=0):  # 游戏胜利
            for value in numdict.values():
                for i in value.values():
                    if str(i).isdigit():
                        score += int(i)
            if score >= 2048:
                frame_win = Frame(game1, bg='yellow')
                frame_win.place(width=305, height=205)
                Label(frame_win, text='You Win!', font=(s_font, 30),
                      fg='red', bg='yellow').place(width=305, height=60)
                Button(frame_win, bd=0, bg='lightgreen', font=(
                    s_font, 15), text=language[18], command=lambda: base()).place(width=80, height=30, y=150, x=45)
                Button(frame_win, bd=0, bg='lightgreen', font=(
                    s_font, 15), text=language[2], command=lambda: game1quit()).place(width=80, height=30, y=150, x=180)
                Label(frame_win, font=(s_font, 15), text='You have got to\n2048!',
                      bg='yellow').place(width=205, height=60, y=60, x=50)
            else:
                game1.after(100, gamewin)

        def gameover():  # 游戏结束
            frame_over = Frame(game1, bg='yellow')
            frame_over.place(width=305, height=205)
            Label(frame_over, text='Game Over!', font=(s_font, 30),
                  fg='red', bg='yellow').place(width=305, height=60)
            Button(frame_over, bd=0, bg='lightgreen', font=(
                s_font, 15), text=language[18], command=lambda: base()).place(width=80, height=30, y=150, x=45)
            Button(frame_over, bd=0, bg='lightgreen', font=(
                s_font, 15), text=language[2], command=lambda: game1quit()).place(width=80, height=30, y=150, x=180)
            Label(frame_over, font=(s_font, 50), textvariable=score_value,
                  bg='yellow').place(width=205, height=60, y=60, x=50)

        def move(way, count=0):  # 操作函数
            if way in ['w', 's', 'a', 'd']:  # 判断是否为正确的操作

                if way == 'w':
                    for x in range(1, 5):
                        numdict[x][5] = 0
                        for y in range(1, 5):
                            if numdict[x][y] == numdict[x][y+1] and numdict[x][y] != '':
                                numdict[x][y] = ''
                                numdict[x][y+1] *= 2
                            elif numdict[x][y] != '' and numdict[x][y+1] == '':
                                numdict[x][y], numdict[x][y +
                                                          1] = numdict[x][y+1], numdict[x][y]
                        del numdict[x][5]
                if way == 's':
                    for x in range(1, 5):
                        numdict[x][0] = 0
                        for y in range(4, 0, -1):
                            if numdict[x][y] == numdict[x][y-1] and numdict[x][y] != '':
                                numdict[x][y] = ''
                                numdict[x][y-1] *= 2
                            elif numdict[x][y] != '' and numdict[x][y-1] == '':
                                numdict[x][y], numdict[x][y -
                                                          1] = numdict[x][y-1], numdict[x][y]
                        del numdict[x][0]
                if way == 'd':
                    numdict[5] = {1: 0, 2: 0, 3: 0, 4: 0}
                    for y in range(1, 5):
                        for x in range(1, 5):
                            if numdict[x][y] == numdict[x+1][y] and numdict[x][y] != '':
                                numdict[x][y] = ''
                                numdict[x+1][y] *= 2
                            elif numdict[x][y] != '' and numdict[x+1][y] == '':
                                numdict[x][y], numdict[x +
                                                       1][y] = numdict[x+1][y], numdict[x][y]
                    del numdict[5]
                if way == 'a':
                    numdict[0] = {1: 0, 2: 0, 3: 0, 4: 0}
                    for y in range(1, 5):
                        for x in range(4, 0, -1):
                            if numdict[x][y] == numdict[x-1][y] and numdict[x][y] != '':
                                numdict[x][y] = ''
                                numdict[x-1][y] *= 2
                            elif numdict[x][y] != '' and numdict[x-1][y] == '':
                                numdict[x][y], numdict[x -
                                                       1][y] = numdict[x-1][y], numdict[x][y]
                    del numdict[0]

                for x in range(1, 5):
                    for y, i in zip(range(1, 5), [n11, n12, n13, n14, n21, n22, n23, n24, n31, n32, n33, n34, n41, n42, n43, n44][4*(x-1):4*x]):
                        i.set(numdict[x][y])
                        if numdict[x][y] == '':
                            count = 1
                if count == 0:
                    gameover()
                    return None  # 决定是否结束游戏

                while 1:  # 随机再产生一个数
                    x, y = randint(1, 4), randint(1, 4)
                    if numdict[x][y] == '':
                        numdict[x][y] = choice([2, 4])
                        break
                [n11, n12, n13, n14, n21, n22, n23, n24, n31, n32, n33,
                    n34, n41, n42, n43, n44][4*x+y-5].set(numdict[x][y])

        def scorevalue(value=0):  # 计分板
            for x in range(1, 5):
                for y in range(1, 5):
                    if numdict[x][y] != '':
                        value += numdict[x][y]
            score.set('Score\n\n%s' % value)
            score_value.set(str(value))
            game1.after(10, scorevalue)

        def gamestart():  # 游戏开始
            game.bind('<Any-KeyPress>', lambda event: move(event.char))  # 键盘关联
            initialization()  # 初始化
            scorevalue()  # 开始计分
            gamewin()  # 检测胜利

        def enter(event): event.widget['bg'] = 'springgreen'
        def leave(event): event.widget['bg'] = 'lightgreen'
        for i in [quitbutton, playbutton]:
            i.bind('<Enter>', lambda event: enter(event))
            i.bind('<Leave>', lambda event: leave(event))

        def game1quit(): global size; game.unbind('<Any-KeyPress>'); game1.destroy(
        ); size = '960x480'; game.geometry('960x480+150+100'); GameQuit_MusicSet()

    base()

# 游戏2 #


class Game2():
    pass

# 游戏3 #
###############################


class Game3:
    def __init__(self):
        self.pw, self.ph, self.px, self.py = 40, 20, 455, 250
        self.pf = 15
        self.count = 0
        self.god = False
        self.score = 0
        self.RGBcolorlist = ['0', '1', '2', '3', '4', '5',
                             '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        self.Score = IntVar()
        self.Score.set(self.score)

        self.game3 = Frame(game)
        self.game3.place(width=960, height=480)
        self.main = Frame(self.game3)
        self.main.place(width=960, height=480)
        self.player = Label(self.game3, bg='black', fg='white', font=(
            'consolas', self.pf), text='O', anchor='w')
        self.player.place(width=self.pw, height=self.ph, y=self.py, x=self.px)

        Label(self.game3, bg='lightgreen', textvariable=self.Score,
              font=(s_font, 20)).place(width=960, height=40)

        for i in range(3):
            Label(self.game3, bg='red').place(
                width=30, height=30, y=5, x=925-35*i)

        self.life = Label(self.game3, bg='lightgreen')
        self.life.place(height=40, x=845, width=0)

        Button(self.game3, bd=0, bg='orange', text=language[2], font=(
            # 退出按钮
            s_font, 15), command=lambda: self.fishquit()).place(width=100, height=30, y=5, x=5)
        Button(self.game3, bd=0, bg='orange', text=language[18], font=(
            # 重置按钮
            s_font, 15), command=lambda: self.fishagain()).place(width=100, height=30, y=5, x=110)

        self.game3start()

    def game3start(self):
        game3help = Frame(self.game3)
        game3help.place(width=600, height=360, y=60, x=180)
        Label(game3help, text=language[15], bg='grey', font=(
            s_font, 15)).place(width=600, height=30)
        Label(game3help, bg='lightgreen', font=(s_font, 20),
              text=language[19]).place(width=600, height=300, y=30)
        Label(game3help, bg='grey').place(width=600, height=30, y=330)
        Button(game3help, bg='lightgreen', text=language[10], bd=0, font=(
            s_font, 12), command=lambda: start()).place(width=80, height=20, y=335, x=510)

        def start():
            game.bind('<Any-KeyPress>',
                      lambda event: self.playmove(event.char))  # 键盘关联
            self.randomfish()
            game3help.destroy()

    def fishagain(self):
        self.pw, self.ph, self.px, self.py = 40, 20, 455, 250
        self.pf = 15
        self.count = 0
        self.score = 0
        self.game3.destroy()
        Game3()  # 重置函数

    def fishquit(self):
        global s_audio
        game.unbind('<Any-KeyPress>')
        self.game3.destroy()
        GameQuit_MusicSet()  # 退出函数

    def victory(self):  # 胜利设定
        if self.score >= 4000:
            Label(self.game3, bg='lightyellow', font=(s_font, 100),
                  text='- Victory -', fg='orange').place(width=960, height=440, y=40)
            self.main.destroy()

    def death(self):  # 死亡设定
        self.count += 1

        if self.count < 3:
            self.god = True if self.god == False else False
            self.life.place(height=40, x=845, width=self.count*40)
        else:
            self.life.place(height=40, x=845, width=120)
            self.main.destroy()
            Label(self.game3, bg='lightyellow', font=(s_font, 100),
                  text='- You Dead -', fg='orange').place(width=960, height=440, y=40)

        if self.god == True:
            self.count -= 1
            self.game3.after(1000, self.death)

    def eattest(self, fish, rw, rh, ry, rx):  # 碰撞检测
        if self.god == False:
            pxw = self.px+self.pw
            pyh = self.py+self.ph
            rxw = rx+rw
            ryh = ry+rh
            test = True if (self.px < rx < pxw or self.px < rxw < pxw or rx < self.px < rxw or rx < pxw < rxw) and (
                self.py < ry < pyh or self.py < ryh < pyh or ry < self.py < ryh or ry < pyh < ryh) else False
            if test == True:
                if self.pw*self.ph > rw*rh:
                    fish.destroy()
                    self.score += rw+rh
                    self.Score.set(self.score)
                    self.pw = self.score//40+40
                    self.ph = self.score//80+20
                    self.pf = self.score//100+15
                    self.player.config(font=('consolas', self.pf))
                    self.victory()
                else:
                    self.death()

    def fishmove(self, fish, speed, rway, rw, rh, ry, rx):  # 鱼的移动
        rx += speed if rway == 'e' else -1*speed
        fish.place(width=rw, height=rh, y=ry, x=rx)
        self.eattest(fish, rw, rh, ry, rx)

        if rx > 960 or rx+rw < 0:
            fish.destroy()
        else:
            self.main.after(10, self.fishmove, fish,
                            speed, rway, rw, rh, ry, rx)

    def randomfish(self, rcolor='#'):  # 随机刷新鱼
        for _ in range(6):
            rcolor += choice(self.RGBcolorlist)

        speed = randint(10, 100+self.score//100)*0.01
        rway = choice(['w', 'e'])
        rh = randint(self.ph//4, self.ph*2)

        while 1:
            rw = randint(self.pw//4, self.pw*2)
            if rw > 1.2*rh:
                break

        rx = -1*rw if rway == 'e' else 960
        ry = randint(40, 480-rh)
        rf = rh//2
        fish = Label(self.main, bg=rcolor, font=(
            'consolas', rf), text='O', anchor=rway)
        fish.place(width=rw, height=rh, y=ry, x=rx)

        self.fishmove(fish, speed, rway, rw, rh, ry, rx)
        self.main.after(randint(1000, 3000), self.randomfish)

    def playmove(self, way):  # 玩家移动
        if way == 'w' and self.py > 40:
            self.py -= 10
        elif way == 's' and self.py <= 470-self.ph:
            self.py += 10
        elif way == 'a' and self.px > 0:
            self.px -= 10
            self.player.config(anchor='w')
        elif way == 'd' and self.px <= 955-self.pw:
            self.px += 10
            self.player.config(anchor='e')

        self.player.place(width=self.pw, height=self.ph, y=self.py, x=self.px)


class Game4():
    pass


class Game5():
    pass


class Game6():
    pass


#####################################################################################################################
game.geometry('960x480+150+100')
game.resizable(0, 0)
game.overrideredirect(1)  # 设置窗口基本属性

f01 = Frame(game)
f01.place(width=960, height=480)  # 欢迎框架

Label(f01, text='- WELCOME -', font=(s_font, 100)
      ).place(width=960, height=400)  # 欢迎页面标签
Label(f01, bg='black').place(width=504, height=25, y=360, x=228)  # 进度条外框
Label(f01).place(width=500, height=21, y=362, x=230)  # 进度条内部

numIdx, i, frames = 40, 0, []
imagelabel = Label(game, bg='black')
barlabel = Label(f01, bg='orange')
selfx, selfy = 0, 0
size = '960x480'  # 定义一些必要变量


def update(idx):
    frame = frames[idx]
    idx += 1
    imagelabel.config(image=frame)
    game.after(s_gif, update, idx % numIdx)  # gif图片定时器函数


def load():  # 加载函数
    global i, frames
    if i < 500:
        frames += [PhotoImage(file='resources\\GIF.gif',
                              format='gif -index %i' % (i//12.5))]  # 加载每一帧图片
        barlabel.place(width=i+12.5, height=21, y=362, x=230)
        game.after(1, load)  # 进度条显示
    else:
        pygame.mixer.music.play(loops=10)  # 播放音乐
        imagelabel.place(width=960, height=480)  # gif图片放置
        game.after(0, update, 0)  # gif图片显示
        homepage()
        f01.destroy()  # 加载主页、摧毁欢迎页
    i += 12.5  # 进度条每次增加12.5


def homepage():  # 主页面
    b01 = Button(game, bg='black', bd=0, font=(s_font, 15),
                 fg='orange', text=language[0], command=setpage)
    b01.place(width=100, height=30, x=310, y=400)  # 设置按钮
    b02 = Button(game, bg='black', bd=0, font=(s_font, 15),
                 fg='orange', text=language[1], command=playselect)
    b02.place(width=100, height=30, x=430, y=400)  # 开始按钮
    b03 = Button(game, bg='black', bd=0, font=(s_font, 15),
                 fg='orange', text=language[2], command=game.quit)
    b03.place(width=100, height=30, x=550, y=400)  # 退出按钮

    for i in [b01, b02, b03]:
        i.bind('<Enter>', enter)
        i.bind('<Leave>', leave)  # 按钮关联鼠标进入事件

    def move(event):
        global selfx, selfy
        game.geometry(size+'+%s+%s' % (game.winfo_x()+event.x -
                      selfx, game.winfo_y()+event.y-selfy))  # 窗口移动函数

    def beforemove(event):
        global selfx, selfy
        selfx, selfy = event.x, event.y

    game.bind('<B1-Motion>', lambda event: move(event))  # 鼠标左键一直按下移动事件关联
    game.bind('<Button-1>', lambda event: beforemove(event))  # 鼠标左键按下移动事件关联


def setpage():  # 设置页面
    f31 = Frame(game, bg='lightyellow')
    f31.place(width=600, height=340, x=180, y=60)  # 设置页框架

    Label(f31, font=(s_font, 15), text=language[3], anchor='w', bg='grey').place(
        width=600, height=30)  # 设置页头部
    Label(f31, bg='grey').place(width=600, height=40, y=300)  # 设置页底部

    b31 = Button(f31, font=(s_font, 15), text='×',
                 bg='grey', bd=0, command=f31.destroy)
    b31.place(width=30, height=30, x=570)  # 关闭按钮
    b32 = Button(f31, font=(s_font, 15), text='?',
                 bg='grey', bd=0, command=lambda: sethelp())
    b32.place(width=30, height=30, x=540)  # 帮助按钮
    b33 = Button(f31, font=(s_font, 15), bd=0, bg='lightgreen',
                 text=language[10], command=lambda: okget())
    b33.place(width=100, height=30, y=305, x=380)  # 确定按钮
    b34 = Button(f31, font=(s_font, 15), bd=0, bg='lightgreen',
                 text=language[11], command=f31.destroy)
    b34.place(width=100, height=30, y=305, x=490)  # 取消按钮

    for i in range(5, 10):
        Label(f31, font=(s_font, 20), bg='lightyellow', text=language[i]).place(
            width=200, height=40, x=100, y=(i-4)*50)  # 各个设置项

    e31 = Entry(f31, font=(s_font, 20), bg='lightyellow',
                textvariable=s_1, bd=0, justify='center')
    e31.place(width=150, height=40, x=350, y=50)  # 刷新率文本框
    e32 = Entry(f31, font=(s_font, 20), bg='lightyellow',
                textvariable=s_2, bd=0, justify='center')
    e32.place(width=150, height=40, x=350, y=100)  # 透明度文本框
    e33 = Entry(f31, font=(s_font, 20), bg='lightyellow',
                textvariable=s_3, bd=0, justify='center')
    e33.place(width=150, height=40, x=350, y=150)  # 字体文本框
    b35 = Button(f31, font=(s_font, 20), bg='lightyellow',
                 textvariable=s_4, bd=0, command=lambda: cmd4())
    b35.place(width=150, height=40, x=350, y=200)  # 语言切换
    b36 = Button(f31, font=(s_font, 20), bg='lightyellow',
                 textvariable=s_5, bd=0, command=lambda: cmd5())
    b36.place(width=150, height=40, x=350, y=250)  # 音乐开关

    def cmd4():
        global s_language
        s_language = 'English' if s_language == '简体中文' else '简体中文'
        s_4.set(s_language)  # 语言切换函数

    def cmd5():
        global s_audio
        s_audio = 'On' if s_audio == 'Off' else 'Off' if s_audio == 'On' else '开' if s_audio == '关' else '关'
        s_5.set(s_audio)  # 音乐开关函数

    b31.bind('<Enter>', shutenter)
    b31.bind('<Leave>', shutleave)  # 按钮关联鼠标进入事件
    b32.bind('<Enter>', helpenter)
    b32.bind('<Leave>', shutleave)  # 按钮关联鼠标进入事件

    for i in [e31, e32, e33, b35, b36]:
        i.bind('<Enter>', enter2)
        i.bind('<Leave>', leave2)  # 按钮关联鼠标进入事件
    for i in [b33, b34]:
        i.bind('<Enter>', enter3)
        i.bind('<Leave>', leave3)  # 按钮关联鼠标进入事件

    def sethelp():  # 帮助页面
        fhelp = Frame(f31)
        fhelp.place(width=400, height=250, x=100, y=40)  # 帮助框架

        Label(fhelp, bg='gray', font=(s_font, 15), text=language[15]).place(
            width=400, height=30)  # 帮助页面头部
        Label(fhelp, bg='gray', font=(s_font, 15)).place(
            width=400, height=30, y=220)  # 帮助页面底部
        Label(fhelp, text=language[17], font=(s_font, 15)).place(
            width=400, height=190, y=30)  # 帮助主体内容

        b37 = Button(fhelp, text=language[10], bd=0, bg='lightgreen', font=(
            s_font, 12), command=fhelp.destroy)
        b37.place(width=80, height=20, y=225, x=315)  # 确定按钮
        b38 = Button(fhelp, text=language[16], bd=0, bg='lightgreen', font=(
            s_font, 12), command=lambda: restoredefault())
        b38.place(width=120, height=20, y=225, x=5)  # 默认设置按钮

        for i in [b37, b38]:
            i.bind('<Enter>', enter3)
            i.bind('<Leave>', leave3)  # 按钮关联鼠标进入事件

        def restoredefault():  # 默认设置函数
            global s_gif, s_alpha, s_font, s_language, s_audio, language
            s_1.set(s_gif := 10)
            s_2.set(s_alpha := 1)
            s_3.set(s_font := '华文新魏')
            s_4.set(s_language := 'English')
            language = Englishfont
            s_5.set(s_audio := language[13])
            fhelp.destroy()  # 关闭帮助页面

    def okget():  # 设置改变函数
        global s_gif, s_alpha, s_font, s_language, s_audio, language
        f31.destroy()

        if 0 < float(s_1.get()) <= 1000:
            s_gif = s_1.get()  # 设置刷新率
        else:
            s_1.set(s_gif := 10)  # 切换为默认值
        if 0 < float(s_2.get()) <= 1:
            s_alpha = s_2.get()  # 设置透明度
        else:
            s_2.set(s_alpha := 1)  # 切换为默认值

        s_font = s_3.get()  # 字体切换
        language = Englishfont if s_language == 'English' else Chinesefont  # 语言切换

        if s_audio == 'On' or s_audio == '开':
            s_5.set(s_audio := language[13])
            pygame.mixer.music.unpause()  # 音乐继续播放
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(loops=10)
        else:
            s_5.set(s_audio := language[14])
            pygame.mixer.music.pause()  # 音乐暂停

        game.wm_attributes("-alpha", s_alpha)
        homepage()  # 改变系统变量并重新加载


def playselect():  # 开始页面
    f11 = Frame(game, bg='lightyellow')
    f11.place(width=200, height=340, x=380, y=60)  # 开始页面框架

    Label(f11, font=(s_font, 15), text=language[4], anchor='w', bg='grey').place(
        width=200, height=30)  # 开始页面头部

    b11 = Button(f11, font=(s_font, 15), text='×',
                 bg='grey', bd=0, command=f11.destroy)
    b11.place(width=30, height=30, x=170)  # 关闭按钮

    for i in range(len(lis := [Button(f11)]*7)):
        lis[i] = Button(f11, bg='lightyellow', font=(
            s_font, 15), bd=0, text=gamelist[i], command=lambda arg=i: gamestart(arg+1))
        lis[i].place(width=180, height=30, x=10, y=i*40+50)

    b11.bind('<Enter>', shutenter)
    b11.bind('<Leave>', shutleave)  # 按钮关联鼠标进入事件

    for i in lis:
        i.bind('<Enter>', enter2)
        i.bind('<Leave>', leave2)  # 按钮关联鼠标进入事件

    def gamestart(n):
        pygame.mixer.music.stop()
        f11.destroy()
        if n == 1:
            Game1()
        elif n == 2:
            Game2()
        elif n == 3:
            Game3()
        elif n == 4:
            Game4()
        elif n == 5:
            Game5()
        elif n == 6:
            Game6()
        else:
            None


load()  # 启动加载函数
game.mainloop()  # 进入消息事件循环
