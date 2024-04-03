from random import *
from tkinter import *
from tkinter.messagebox import *

game = Tk()  # 基本框架
game.title('Game-2048')
game.geometry('305x205+500+250')
game.resizable(0, 0)


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

    frame = Frame(game, bg='#BBADA0').place(width=205, height=205)
    frame2 = Frame(game, bg='orange').place(width=100, height=205, x=205)
    frame3 = Frame(frame2, bg='#FAF8EF').place(
        x=210, y=5, width=90, height=195)
    (score := StringVar()).set('Score\n\n0')
    (score_value := StringVar()).set('0')
    Label(frame3, textvariable=score, font=('consolas', 15),
          bg='yellow').place(x=215, y=10, width=80, height=100)
    helpbutton = Button(frame2, text='Help', font=(
        'consolas', 15), bd=0, bg='lightgreen', command=lambda: gamehelp())
    helpbutton.place(x=215, y=160, width=80, height=30)
    playbutton = Button(frame2, text='Play', font=(
        'consolas', 15), bd=0, bg='lightgreen', command=lambda: gamestart())
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
            Label(frame, bg='#CDC1B4', textvariable=i, font=(
                'consolas', 15)).place(width=45, height=45, y=sy, x=sx)

    def initialization():  # 初始化
        for x in range(1, 5):
            for y, i in zip(range(1, 5), [n11, n12, n13, n14, n21, n22, n23, n24, n31, n32, n33, n34, n41, n42, n43, n44][4*(x-1):4*x]):
                i.set(numdict[x][y])

    def gamewin():  # 游戏胜利
        for value in numdict.values():
            if 2048 in value:
                frame_win = Frame(game, bg='yellow').place(
                    width=305, height=205)
                Label(frame_win, text='You Win!', font=('consolas', 30),
                      fg='red', bg='yellow').place(width=305, height=60)
                Button(frame_win, bd=0, bg='lightgreen', font=('consolas', 15), text='Again!',
                       command=lambda: base()).place(width=80, height=30, y=150, x=45)
                Button(frame_win, bd=0, bg='lightgreen', font=('consolas', 15), text='Quit!',
                       command=lambda: quit()).place(width=80, height=30, y=150, x=180)
                Label(frame, font=('consolas', 15), text='You have got to\n2048!',
                      bg='yellow').place(width=205, height=60, y=60, x=50)
        game.after(100, gamewin)

    def gameover():  # 游戏结束
        frame_over = Frame(game, bg='yellow').place(width=305, height=205)
        Label(frame_over, text='Game Over!', font=('consolas', 30),
              fg='red', bg='yellow').place(width=305, height=60)
        Button(frame_over, bd=0, bg='lightgreen', font=('consolas', 15), text='Again!',
               command=lambda: base()).place(width=80, height=30, y=150, x=45)
        Button(frame_over, bd=0, bg='lightgreen', font=('consolas', 15), text='Quit!',
               command=lambda: quit()).place(width=80, height=30, y=150, x=180)
        Label(frame, font=('consolas', 50), textvariable=score_value,
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

    def gamehelp(): showinfo(title='Help of 2048',
                             message='Press "w" to up!\nPress "s"  to down!\nPress "d" to right!\nPress "a"  to left!')  # 游戏帮助

    def scorevalue(value=0):  # 计分板
        for x in range(1, 5):
            for y in range(1, 5):
                if numdict[x][y] != '':
                    value += numdict[x][y]
        score.set('Score\n\n%s' % value)
        score_value.set(str(value))
        game.after(10, scorevalue)

    def gamestart():  # 游戏开始
        game.bind_all('<Any-KeyPress>', lambda event: move(event.char))  # 键盘关联
        initialization()  # 初始化
        scorevalue()  # 开始计分
        gamewin()  # 检测胜利

    def enter(event): event.widget['bg'] = 'springgreen'
    def leave(event): event.widget['bg'] = 'lightgreen'
    for i in [helpbutton, playbutton]:
        i.bind('<Enter>', lambda event: enter(event))
        i.bind('<Leave>', lambda event: leave(event))


base()
game.mainloop()
