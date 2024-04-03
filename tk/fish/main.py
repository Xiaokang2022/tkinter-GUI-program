from random import *
from tkinter import *

game = Tk()
game.geometry('960x480+150+100')
game.resizable(0, 0)


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
              font=('华文新魏', 20)).place(width=960, height=40)

        for i in range(3):
            Label(self.game3, bg='red').place(
                width=30, height=30, y=5, x=925-35*i)

        self.life = Label(self.game3, bg='lightgreen')
        self.life.place(height=40, x=845, width=0)

        Button(self.game3, bd=0, bg='orange', text='退出', font=('华文新魏', 15),
               command=lambda: self.fishquit()).place(width=100, height=30, y=5, x=5)  # 退出按钮
        Button(self.game3, bd=0, bg='orange', text='重置', font=('华文新魏', 15),
               command=lambda: self.fishagain()).place(width=100, height=30, y=5, x=110)  # 重置按钮

        self.game3start()

        game.mainloop()

    def game3start(self):
        game3help = Frame(self.game3)
        game3help.place(width=600, height=360, y=60, x=180)
        Label(game3help, text='帮助', bg='grey', font=(
            '华文新魏', 15)).place(width=600, height=30)
        Label(game3help, bg='lightgreen', font=('华文新魏', 20),
              text='按‘w’、‘s’、‘a’和‘d’进行移动！\n4000分胜利！\n祝你好运！').place(width=600, height=300, y=30)
        Label(game3help, bg='grey').place(width=600, height=30, y=330)
        Button(game3help, bg='lightgreen', text='确定', bd=0, font=(
            '华文新魏', 12), command=lambda: start()).place(width=80, height=20, y=335, x=510)

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

    def fishquit(self): game.quit()

    def victory(self):  # 胜利设定
        if self.score >= 4000:
            Label(self.game3, bg='lightyellow', font=('华文新魏', 100),
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
            Label(self.game3, bg='lightyellow', font=('华文新魏', 100),
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


Game3()
