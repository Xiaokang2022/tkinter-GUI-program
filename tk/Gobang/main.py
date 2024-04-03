from random import *
from tkinter import *

import pygame

pygame.mixer.init()

game = Tk()
game.geometry('960x480+150+100')
game.title('五子棋')
game.resizable(0,0)

background = PhotoImage(file='resources\\fivechess2.png')
pygame.mixer.music.load('resources\\fivechessbgm.mp3')
pygame.mixer.music.set_volume(0.1)

class fivechess:
    def __init__(self):#定义必要变量

        self.game7 = Frame(game)
        self.canvas = Canvas(self.game7)
        self.px,self.py = 960,480

        self.text = ''#下棋记录
        self.lists = []#棋盘存储列表
        self.cold = 0#冷却值,0白方回合,1黑方回合
        self.mode = 0#0默认为人机对战
        self.color = 'white'#默认白子先走
        self.value = 1#0为空子;1为白子;2为黑子
        self.Count = 0#步数
        self.over = 0#决定游戏是否结束
        self.buttontext = '人机模式'
        self.regretlis = []#可悔棋列表
        self.regretlisxy = []#可悔棋坐标列表

        self.T = StringVar()
        self.t = 15#初始剩余时间数
        self.ty = 150#时间标签初始纵坐标
        self.Mode = StringVar()
        self.Mode.set('人机模式')

        self.function()

    def function(self):#启动功能
        self.lists = [[0]*15 for _ in range(15)]

        self.game7.place(width=960,height=480)
        self.canvas.place(width=960,height=480)
        self.canvas.create_image(500,250,image=background)

        self.canvas.bind('<Button-1>',lambda event:self.player())
        self.canvas.bind('<Motion>',lambda event:self.position(event))

        self.modeset()
        self.initialization1()
        self.initialization2()
        self.AI_initialization()

    def initialization1(self,color='black'):#棋盘初始化

        for i in range(256,705,32):#棋盘网 (256,16)~(704,464)
            self.canvas.create_line(i,16,i,464)
            self.canvas.create_line(256,i-240,704,i-240)

        self.canvas.create_rectangle(250,10,710,470,width=3)#棋盘框

        self.canvas.create_oval(349,109,355,115,fill=color)#棋盘点
        self.canvas.create_oval(349,365,355,371,fill=color)
        self.canvas.create_oval(605,109,611,115,fill=color)
        self.canvas.create_oval(605,365,611,371,fill=color)
        self.canvas.create_oval(477,237,483,243,fill=color)

    def position(self,event,color='springgreen'):#鼠标位置
        if 240< event.x <720:
            self.px,self.py = 32*int((event.x-240)/32)+256,32*int(event.y/32)+16

            try:
                for i in [self.l1,self.l2,self.l3,self.l4,self.l5,self.l6,self.l7,self.l8]:self.canvas.delete(i)
            except:pass

            self.l1 = self.canvas.create_line(self.px-15,self.py-15,self.px-15,self.py-5,width=1,fill=color)
            self.l2 = self.canvas.create_line(self.px-15,self.py-15,self.px-5,self.py-15,width=1,fill=color)

            self.l3 = self.canvas.create_line(self.px-15,self.py+15,self.px-15,self.py+5,width=1,fill=color)
            self.l4 = self.canvas.create_line(self.px-15,self.py+15,self.px-5,self.py+15,width=1,fill=color)

            self.l5 = self.canvas.create_line(self.px+15,self.py-15,self.px+15,self.py-5,width=1,fill=color)
            self.l6 = self.canvas.create_line(self.px+15,self.py-15,self.px+5,self.py-15,width=1,fill=color)

            self.l7 = self.canvas.create_line(self.px+15,self.py+15,self.px+5,self.py+15,width=1,fill=color)
            self.l8 = self.canvas.create_line(self.px+15,self.py+15,self.px+15,self.py+5,width=1,fill=color)

    def initialization2(self):

        Label(self.game7,bg='grey',font=('consolas',30),text='白方',fg='white').place(width=200,height=200,x=20,y=20)
        Label(self.game7,bg='grey',font=('consolas',30),text='黑方',fg='white').place(width=200,height=200,x=20,y=260)

        self.f1 = Label(self.game7,bg='black')
        self.f2 = Label(self.game7,bg='black')
        self.f3 = Label(self.game7,bg='black')
        self.f4 = Label(self.game7,bg='black')

        self.f(10)

        Label(self.game7,bg='black').place(width=220,height=280,y=10,x=730)
        Label(self.game7,bg='grey').place(width=216,height=276,y=12,x=732)

        Label(self.game7,bg='grey',textvariable=self.Mode,font=('consolas',15),fg='white').place(width=216,height=26,y=12,x=732)

        countframe = Frame(self.game7,bg='grey')
        countframe.place(width=216,height=250,x=732,y=38)

        self.countlabel = Label(countframe,bg='grey',fg='white',text=self.text,font=('consolas',12),anchor='sw')
        self.timelabel = Label(self.game7,bg='grey',textvariable=self.T,fg='white',font=('consolas',30))

        self.B1 = Button(self.game7,bg='grey',bd=0,font=('consolas',20),fg='white',text='退出',command=self.game7.quit)
        self.B1.place(width=220,x=730,height=50,y=300)
        self.B2 = Button(self.game7,bg='grey',bd=0,font=('consolas',20),fg='white',text='重置',command=lambda:gameagain())
        self.B2.place(width=220,x=730,height=50,y=360)
        self.B3 = Button(self.game7,bg='grey',bd=0,font=('consolas',20),fg='white',text='悔棋',command=lambda:self.regret(),state='disabled')
        self.B3.place(width=220,x=730,height=50,y=420)

        for i in [self.B1,self.B2,self.B3]:
            i.bind('<Enter>',lambda event:enter(event))
            i.bind('<Leave>',lambda event:leave(event))

        def enter(event):event.widget['bg']='#F0F0F0';event.widget['fg']='black'
        def leave(event):event.widget['bg']='grey';event.widget['fg']='white'

        def gameagain():
            self.game7.destroy()
            fivechess()
        
    def f(self,fy):
        self.f1.place(width=5,height=220,x=10,y=fy)
        self.f2.place(width=220,height=5,x=10,y=fy)
        self.f3.place(width=220,height=5,x=10,y=fy+215)
        self.f4.place(width=5,height=220,x=225,y=fy)

    def AI_initialization(self):

        self.defense_case =[[0,0,0,0,0],#0
                            
                            [0,0,1,0,0],
                            [0,1,0,0,0],
                            [1,0,0,0,0],

                            [1,0,0,1,0],
                            [0,0,1,1,0],#5
                            [0,1,0,1,0],
                            [1,0,1,0,0],
                            [1,0,0,0,1],
                            [0,0,0,1,1],
                            
                            [1,1,0,0,1],#10
                            [0,1,1,0,1],
                            [0,1,0,1,1],
                            [1,0,1,0,1],
                            [1,1,1,0,0],
                            [0,1,1,1,0],]#15

        self.attack_case = [[0,0,0,0,0],#0
                            
                            [0,0,2,0,0],
                            [0,2,0,0,0],
                            [2,0,0,0,0],

                            [2,0,0,2,0],
                            [0,0,2,2,0],#5
                            [0,0,2,2,0],
                            [2,0,2,0,0],
                            [0,2,0,2,0],
                            [0,0,0,2,2],
                            
                            [2,2,0,0,2],#10
                            [0,2,0,2,2],
                            [0,2,2,0,2],
                            [2,0,2,0,2],
                            [2,2,2,0,0],
                            [0,2,2,2,0],]#15

    def defense(self,lis,value=0):
        if 0 in lis and lis.count(1) == 4:value = 9999999999
        elif 2 in lis and lis.count(1) == 4:value = 5000
        elif lis == [0,1,1,1,0]:value = 9999999
        elif lis in [[1,1,0,1,0],[0,1,1,0,1]] or reversed(lis) in [[1,1,0,1,0],[0,1,1,0,1]]:value = 10000
        else:
            try:value = self.defense_case.index(lis)**3
            except:
                try:value = self.defense_case.index(reversed(lis))**3
                except:pass

        return value

    def defense2(self,lis,value=0):
        if lis == [0,0,1,1,1,0] or lis == [0,1,1,1,0,0]:value = 999999999
        elif lis in [[0,1,1,1,1,2],[1,0,1,1,1,2],[1,1,0,1,1,2],[1,1,1,0,1,2],[2,1,0,1,1,1,],[2,1,1,0,1,1],[2,1,1,1,0,1],[2,1,1,1,1,0]]:value = 99999999
        elif lis in [[1,1,1,1,0,1],[1,0,1,1,1,1]]:value = 9999999

        return value

    def attack2(self,lis,value=0):
        if lis == [1,2,2,2,2,1]:value = -99999
        elif lis == [0,2,2,2,2,1] or lis == [1,2,2,2,2,1]:value = 9999
        elif lis == [0,2,2,2,2,0]:value = 9999999999
        elif lis == [0,2,2,0,2,0] or lis == [0,2,0,2,2,0]:value = 999999

        return value

    def attack(self,lis,value=0):
        if lis == [2]*5:value=9999999999
        elif 0 in lis and lis.count(2) == 4:value = 9999999
        elif 1 in lis and lis.count(2) == 4:value = -1000
        elif lis == [0,1,1,1,0]:value = -10000
        elif lis in [[2,1,1,0,2],[2,0,1,1,1],[2,1,1,1,0],[2,1,0,1,2],[2,1,1,1,2]] or reversed(lis) in [[2,1,1,0,2],[2,0,1,1,1],[2,1,1,1,0],[2,1,1,1,2]]:value = -300000
        elif lis in [[2,1,2,2,0],[2,1,2,2,2]] or reversed(lis) in [[2,1,2,2,0],[2,1,2,2,2]]:value = -30000
        elif lis in [[2,2,0,2,0],[0,2,2,0,2],[0,2,2,2,0]] or reversed(lis) in [[2,2,0,2,0],[0,2,2,0,2]]:value = 4000
        else:
            try:value = self.attack_case.index(lis)**3
            except:
                try:value = self.attack_case.index(reversed(lis))**3
                except:pass

        return value

    def regret(self):
        self.B3.config(state='disabled')
        if self.Count%2 == 0:
            self.Count -= 2
            self.text = self.text[:-40]
            self.countlabel.config(text=self.text)
            self.countlabel.place(width=216,height=20*self.Count,y=250-20*self.Count)

            for i in self.regretlis:self.canvas.delete(i)
            for i in self.regretlisxy:self.lists[i[0]][i[1]] = 0

            try:
                self.winlabel.destroy()
                pygame.mixer.music.unpause()
                self.over = 0
                self.mode = 1 if self.buttontext == '对弈' else 0
            except:pass

    def Time(self,updata=0):
        if updata == 1:
            self.timelabel.config(fg='white')
            self.t = 15
            self.ty = 150 if self.ty == 390 else 390

        self.T.set('- %s -'%self.t)
        self.timelabel.place(width=200,height=30,x=20,y=self.ty)

        if self.t == 2 and self.mode != 2:
            self.timelabel.config(fg='red')
            pygame.mixer.Sound('resources\\ring.wav').play()

        if self.t != 0 and updata == 0:
            self.t -= 1
            self.game7.after(1000,self.Time)

    def modeset(self):

        self.MS = Frame(self.game7)
        self.MS.place(width=300,height=200,y=140,x=330)

        Label(self.MS,bg='black').place(width=280,height=90,x=10,y=70)
        textlabel = Label(self.MS,bg='grey',font=('consolas',15),fg='white',text='人类与电脑之间的战斗！\n不怕死就来挑战吧！')
        textlabel.place(width=276,height=86,x=12,y=72)

        b1 = Button(self.MS,text=self.buttontext,font=('consolas',20),bd=0,command=lambda:button())
        b1.place(width=200,height=30,y=35,x=50)

        Label(self.MS,bg='grey',text='设置',font=('consolas',15)).place(width=300,height=30)
        Label(self.MS,bg='grey').place(width=300,height=30,y=170)
        Button(self.MS,text='确定',font=('consolas',15),bd=0,command=lambda:okget()).place(width=100,height=20,y=175,x=195)

        def okget():
            pygame.mixer.music.play(loops=10)
            self.MS.destroy()
            self.Time()
            if self.mode == 2:
                self.cold = 1
                self.f(500)
                self.ty = 500
                self.AI_AI()

        def button():
            if self.buttontext=='机机模式':
                self.buttontext = '人机模式'
                self.mode = 0
                self.Mode.set('人机模式')
                textlabel.config(text='人类与电脑之间的战斗！\n不怕死就来挑战吧！')

            elif self.buttontext=='人机模式':
                self.buttontext = '对弈模式'
                self.mode = 1
                self.Mode.set('对弈模式')
                textlabel.config(text='人类与人类之间的对决！\n到底谁才是王中王呢！')

            elif self.buttontext == '对弈模式':
                self.buttontext = '机机模式'
                self.mode = 2
                self.Mode.set('机机模式')
                textlabel.config(text='电脑与电脑之间的交流！\n一种神秘而牛逼的设定！')

            b1.config(text=self.buttontext)

        def enter(event):event.widget['bg']='grey';event.widget['fg']='white'
        def leave(event):event.widget['bg']='#F0F0F0';event.widget['fg']='black'

        b1.bind('<Enter>',enter)
        b1.bind('<Leave>',leave)

    def referee(self,lists,M=1):#判断输赢M为1就非AI
        AIlist = []

        #竖
        for i in range(15):
            temp_list = []
            for lis in lists:temp_list.append(lis[i])
            
            if M == 1:self.judgement(temp_list)
            else:AIlist.append(temp_list)
            
        #横
        for lis in lists:
            if M == 1:self.judgement(lis)
            else:AIlist.append(lis)

        #斜
        for i in [1,-1]:#右斜;左斜
            for x in range(15):
                y = 0
                temp_list1 = []
                temp_list2 = []
                try:
                    while x >= 0:
                        temp_list1.append(lists[x][y])
                        temp_list2.append(lists[i*(y-7)+7][i*(x-7)+7])
                        x += i
                        y += 1
                except:pass

                if M == 1:
                    self.judgement(temp_list1)
                    self.judgement(temp_list2)
                else:
                    AIlist.append(temp_list1)
                    AIlist.append(temp_list2)

        return AIlist

    def judgement(self,lis):
        try:
            for i in range(11):
                if lis[i:i+5] == [1]*5:self.gameover(1);return None
                if lis[i:i+5] == [2]*5:self.gameover(2);return None
        except:pass

    def gameover(self,winner):#winner=1则白方胜，2则黑方胜
        pygame.mixer.music.pause()
        if winner == 1:
            if self.mode == 0:pygame.mixer.Sound('resources\\victory.wav').play()
            self.winlabel = Label(self.game7,bg='grey',font=('consolas',30),fg='springgreen',text='-白方胜-')
            self.winlabel.place(width=200,height=50,x=20,y=40)
        else:
            if self.mode == 0:pygame.mixer.Sound('resources\\defeat.wav').play()
            self.winlabel = Label(self.game7,bg='grey',font=('consolas',30),fg='springgreen',text='-黑方胜-')
            self.winlabel.place(width=200,height=50,x=20,y=280)

        if self.mode == 1:pygame.mixer.Sound('resources\\victory.wav').play()

        self.over = 1#锁定玩家
        self.mode = 2#锁定AI

    def countadd(self,n,x,y):
        self.Count += 1
        player = '[白方]' if n == 1 else '[黑方]'

        self.text += '\n%s(%02d,%02d)\t  [%03d]'%(player,x+1,15-y,self.Count)
        self.countlabel.config(text=self.text)
        self.countlabel.place(width=216,height=20*self.Count,y=250-20*self.Count)

    def regretadd(self,i,x,y):
        self.regretlis.append(i)
        self.regretlisxy.append((x,y))
        if len(self.regretlis) >= 2:self.B3.config(state='active')
        if len(self.regretlis) == 3:
            del self.regretlis[0]
            del self.regretlisxy[0]

    def player(self):
        
        if self.cold+self.over == 0:

            x,y = (self.px-256)//32,(self.py-16)//32

            if self.lists[x][y] == 0:self.lists[x][y] = self.value
            else:return None
            self.countadd(self.value,x,y)

            i = self.canvas.create_oval(self.px-15,self.py-15,self.px+15,self.py+15,fill=self.color,width=0)
            self.regretadd(i,x,y)
            pygame.mixer.Sound('resources\\%s.mp3'%randint(1,4)).play()
            self.referee(self.lists)
            self.cold = 1

            if self.mode == 0:
                self.f(250)
                self.ai_execute()
                self.Time(updata=1)

            elif self.mode == 1:
                if self.color == 'black':
                    self.color = 'white'
                    self.value = 1
                    self.f(10)
                else:
                    self.color = 'black'
                    self.value = 2
                    self.f(250)
                self.cold = 0
                self.Time(updata=1)

    def ai_execute(self,color='black'):

        ai_x,ai_y = self.AI()

        if color == 'black':
            self.lists[ai_x][ai_y] = 2
            self.countadd(2,ai_x,ai_y)
        else:
            self.lists[ai_x][ai_y] = 1
            self.countadd(1,ai_x,ai_y)

        ai_x,ai_y = 32*ai_x+256,ai_y*32+16
        i = self.canvas.create_oval(ai_x-15,ai_y-15,ai_x+15,ai_y+15,fill=color,width=0)
        self.regretadd(i,(ai_x-256)//32,(ai_y-16)//32)
        pygame.mixer.Sound('resources\\%s.mp3'%randint(1,4)).play()
        if self.mode == 0:
            self.cold = 0
            self.f(10)
            self.Time(updata=1)
        self.referee(self.lists)

    def AI(self):

        xlis,ylis = [],[]
        AIdata,AIvalue = [],[]
        try:
            for lis in self.lists:
                for i in lis:
                    if i != 0:
                        xlis.append(self.lists.index(lis))
                        ylis.append(lis.index(i))

            xmax,ymax,xmin,ymin = max(xlis)+4,max(ylis)+4,min(xlis)-4,min(ylis)-4
        except:xmax,ymax,xmin,ymin = 20,20,-5,-5

        for x in range(15):
            for y in range(15):
                if self.lists[x][y] == 0 and xmin<x<xmax and ymin<y<ymax:
                    a_value,d_value = 0,0
                    self.lists[x][y] = 2

                    for lis in self.referee(self.lists,M=0):
                        for i in range(11):
                            try:
                                d_value += self.defense(lis[i:i+5])
                                d_value += self.defense2(lis[i:i+6])#强化
                            except:pass
                            try:
                                a_value += self.attack(lis[i:i+5])
                                a_value += self.attack2(lis[i:i+6])#强化
                            except:pass
                    
                    AIdata.append([x,y])
                    AIvalue.append(a_value-d_value)
                    self.lists[x][y] = 0

        keyvalue = max(AIvalue)
        N = AIvalue.count(keyvalue)
        if N == 1:return AIdata[AIvalue.index(keyvalue)]
        else:
            for i in range(len(AIvalue)):
                try:
                    value = AIvalue[i]
                    if value != keyvalue:AIdata.remove(AIdata[i])
                except:pass
            return choice(AIdata)
        
    def AI_AI(self):
        if self.over == 0:
            color = 'white' if self.Count%2 == 0 else 'black'
            self.ai_execute(color)
            self.referee(self.lists)
            self.game7.after(1000,self.AI_AI)

fivechess()
game.mainloop()