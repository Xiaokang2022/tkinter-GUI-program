# 模块引用
from math import *
from time import *
from tkinter import *

from ttkbootstrap import Style  # 可能需要pip

# 常量定义
signlist = ['+', '-', '×', '÷', '^', '.']
sign = ['+', '-', '×', '÷', '^', 'mod', 'ln', 'sqrt']
varlist1 = ['+', '-', '×', '÷']
varlist2 = ['e', 'π']
varlist3 = [')', '%', '!', 'e', 'π']
varlist4 = ['.', '(', ')', 'e', '-']
varlist5 = ['ln', 'sqrt']
varlist6 = ['+', '-', '×', '÷', '^', '.', '(']
allsign = ['+', '-', '*', '/', '^', '=', '.',
           '(', ')', '!', 'e', 'c', 's', 'm', 'l', 'r', 'a']
theme_list = ['superhero', 'cosmo', 'sandstone', 'flatly', 'journal', 'darkly',
              'cyborg', 'solar', 'minty', 'lumen', 'minty', 'pulse', 'united', 'yeti']
count_theme = 0
# 基本框架
root = Tk()
root.title('小康智能计算器')
root.geometry('301x500+900+100')
root.resizable(0, 0)
Style(theme='superhero').master
root.wm_attributes("-alpha", 0.85)
# 定义标签
(line3 := StringVar()).set('')
(line2 := StringVar()).set('')
(line1 := StringVar()).set('0')
# 状态栏
time_var = StringVar()
theme_var = StringVar()
theme_var.set('蓝色')
Label(root, textvariable=time_var, font=(
    'consolas', 15)).place(width=100, height=20)


def get_time(): time_var.set(strftime('%H:%M:%S')); root.after(1000, get_time)


def theme():
    global count_theme
    count_theme += 1
    Style(theme=theme_list[count_theme]).master
    if count_theme >= 13:
        count_theme = -1


Button(root, text='Theme', font=('consolas', 15),
       command=theme).place(x=200, width=100, height=20)
# 字体大小控制函数


def size_font():
    length1 = len(line1.get())
    if length1 >= 8:
        Label(root, textvariable=line1, anchor='e', font=('consolas',
              round(40*8/length1))).place(y=145, width=300, height=80)
    else:
        Label(root, textvariable=line1, anchor='e', font=(
            'consolas', 40)).place(y=145, width=300, height=80)


def size_font_2():
    length2, length3 = len(line2.get()), len(line3.get())
    if length2 >= 12:
        Label(root, textvariable=line2, anchor='e', font=('consolas',
              round(30*12/length2))).place(y=65, width=300, height=80)
    else:
        Label(root, textvariable=line2, anchor='e', font=(
            'consolas', 30)).place(y=65, width=300, height=80)
    if length3 >= 18:
        Label(root, textvariable=line3, anchor='e', font=('consolas',
              round(20*18/length3))).place(y=20, width=300, height=45)
    else:
        Label(root, textvariable=line3, anchor='e', font=(
            'consolas', 20)).place(y=20, width=300, height=45)


# 执行基本函数
get_time()
size_font()
# 基本按钮
btnln = Button(root, font=('consolas', 17),
               text='ln',  command=lambda: func('ln'))
btnsgn = Button(root, font=('consolas', 15),
                text='+/-', command=lambda: func('+/-'))
btn0 = Button(root, font=('consolas', 20),
              text='0',   command=lambda: func('0'))
btnpoi = Button(root, font=('consolas', 20),
                text='.',   command=lambda: func('.'))
btnequ = Button(root, font=('consolas', 20),
                text='=',   command=lambda: func('='))

btnn = Button(root, font=('consolas', 17),
              text='n!',  command=lambda: func('n!'))
btn1 = Button(root, font=('consolas', 20),
              text='1',   command=lambda: func('1'))
btn2 = Button(root, font=('consolas', 20),
              text='2',   command=lambda: func('2'))
btn3 = Button(root, font=('consolas', 20),
              text='3',   command=lambda: func('3'))
btnplu = Button(root, font=('consolas', 20),
                text='+',   command=lambda: func('+'))

btnmod = Button(root, font=('consolas', 15),
                text='mod', command=lambda: func('mod'))
btn4 = Button(root, font=('consolas', 20),
              text='4',   command=lambda: func('4'))
btn5 = Button(root, font=('consolas', 20),
              text='5',   command=lambda: func('5'))
btn6 = Button(root, font=('consolas', 20),
              text='6',   command=lambda: func('6'))
btnsub = Button(root, font=('consolas', 20),
                text='-',   command=lambda: func('-'))

btnq = Button(root, font=('consolas', 17),
              text='^',   command=lambda: func('^'))
btn7 = Button(root, font=('consolas', 20),
              text='7',   command=lambda: func('7'))
btn8 = Button(root, font=('consolas', 20),
              text='8',   command=lambda: func('8'))
btn9 = Button(root, font=('consolas', 20),
              text='9',   command=lambda: func('9'))
btnmut = Button(root, font=('consolas', 20),
                text='×',   command=lambda: func('×'))

btnsqr = Button(root, font=('consolas', 13), text='sqrt',
                command=lambda: func('sqrt'))
btnac = Button(root, font=('consolas', 15),
               text='AC',  command=lambda: func('AC'))
btnc = Button(root, font=('consolas', 16),
              text='C',   command=lambda: func('C'))
btnrep = Button(root, font=('consolas', 15),
                text='rep', command=lambda: func('rep'))
btndiv = Button(root, font=('consolas', 20),
                text='÷',   command=lambda: func('÷'))

btne = Button(root, font=('consolas', 18),
              text='e',   command=lambda: func('e'))
btnpi = Button(root, font=('consolas', 18),
               text='π',   command=lambda: func('π'))
btnl = Button(root, font=('consolas', 15),
              text='(',   command=lambda: func('('))
btnr = Button(root, font=('consolas', 15), text=')',
              command=lambda: func(')'))
btnbac = Button(root, font=('consolas', 13), text='back',
                command=lambda: func('back'))
# 按钮放置
buttonlist = [btnln, btnsgn, btn0, btnpoi, btnequ, btnn, btn1, btn2, btn3, btnplu, btnmod, btn4, btn5, btn6,
              btnsub, btnq, btn7, btn8, btn9, btnmut, btnsqr, btnac, btnc, btnrep, btndiv, btne, btnpi, btnl, btnr, btnbac]
button_x, button_y = [1, 61, 121, 181, 241], [455, 410, 365, 320, 275, 230]
for b_y, k in zip(button_y, range(6)):
    for b_x, bt in zip(button_x, buttonlist[5*k:5*k+5]):
        bt.place(x=b_x, y=b_y, width=59, height=44)
# 数据分析函数


def split_num(str_num):
    for i in sign:
        str_num = ' '.join(str_num.split(i))
    return str_num.split()[-1]


def is_num(str_num):
    for i in varlist4:
        str_num = ''.join(str_num.split(i))
    return str_num.isdigit()
# 操作函数


def func(press):
    old_num = line1.get()

    if press == 'C' or press == 'c':  # 清除 [功能函数]
        line1.set('0')

    if press == 'AC' or press == 'a':  # 清空所有 [功能函数]
        line1.set('0')
        line2.set('')
        line3.set('')

    if press == 'back':  # 删减操作 [功能函数]
        if old_num == '0':
            pass
        elif old_num == 'Error':
            line1.set('0')
        elif old_num[-3:] == 'mod':
            line1.set(old_num[:-3])
        elif len(old_num) == 1 or (len(old_num) == 2 and old_num[0] == '-'):
            line1.set('0')
        else:
            line1.set(old_num[:-1])

    if press == 'rep' or press == 'r':  # 撤销 [功能函数]
        rep_value = line2.get()
        if rep_value != '':
            line1.set(rep_value)
        else:
            line1.set('0')
        size_font()

    if press == '=':  # 计算函数 [功能函数]
        line2_str = line2.get()
        line3.set(line2_str)
        line2.set(old_num)
        size_font_2()
        num = old_num
        for i in sign:
            num = ' '.join(num.split(i))
        for k in num.split():
            if '!' in k:
                fact_num = k.count('!')
                old_num = old_num.replace(
                    k, 'factorial('*fact_num+k[:-fact_num]+')'*fact_num)
        old_num = old_num.replace('×', '*')
        old_num = old_num.replace('÷', '/')
        old_num = old_num.replace('mod', '%')
        old_num = old_num.replace('ln', 'log')
        old_num = old_num.replace('π', 'pi')
        old_num = old_num.replace('^', '**')
        old_num = old_num.replace('!', '')
        try:
            result = str(eval(old_num))
            if result[-2:] == '.0':
                line1.set(result[:-2])
            else:
                line1.set(result)
        except:
            line1.set('Error')

    if press == '+/-':  # 正负号切换 [功能函数]
        if old_num[0] == '-':
            line1.set(old_num[1:])
        elif old_num != '0':
            line1.set('-'+old_num)

    if len(line1.get()) == 1:
        size_font()  # 字数检测【位置不可乱动！】
    elif len(line1.get()) >= 20:
        return None

    if press in varlist2:  # e、π常量
        if old_num[-1].isdigit() and old_num[-1] != '0' or old_num[-1] == '.':
            pass
        elif old_num == '0':
            line1.set(press)
        else:
            line1.set(old_num+press)

    if press.isdigit():  # 数字符号
        if old_num == '0':
            line1.set(press)
        else:
            line1.set(old_num+press)

    if press in varlist1 or press == '/' or press == '*':  # 加法、减法、乘法、除法
        if press == '/':
            press = '÷'
        if press == '*':
            press = '×'
        if old_num[-1] in signlist and old_num != press:
            line1.set(old_num[:-1]+press)
        elif old_num[-1] == press:
            pass
        elif old_num[-1].isdigit() or old_num[-1] == ')' or old_num[-1] == '!':
            line1.set(old_num+press)

    if press == 'mod' or press == 'm':  # 取余运算
        if old_num[-3:] == 'mod':
            pass
        elif old_num[-1].isdigit() or old_num[-1] == ')' or old_num[-1] == '!':
            line1.set(old_num+press)

    if press == '^':  # 幂(指数)运算
        if old_num[-1].isdigit() or old_num[-1] in varlist3:
            line1.set(old_num+'^')

    if press in varlist5 or press == 's' or press == 'l':  # 取自然对数、开平方
        if press == 's':
            press = 'sqrt'
        if press == 'l':
            press = 'ln'
        if old_num[-3:] == 'mod':
            pass
        elif old_num[-1] not in varlist6:
            new_num = split_num(old_num)
            line1.set(old_num.replace(new_num, '')+press+'('+new_num+')')

    if press == '.':  # 小数点
        if old_num[-1] == ')' or old_num[-1] in signlist or '.' in split_num(old_num):
            pass
        else:
            line1.set(old_num+'.')

    if press == 'n!' or press == '!':  # 阶乘
        if old_num[-1].isdigit() or old_num[-1] == ')' or old_num[-1] == '!':
            line1.set(old_num+'!')

    if press == '(':  # 左括号
        if not old_num[-1].isdigit() and old_num[-1] != '.':
            line1.set(old_num+'(')
        elif old_num == '0':
            line1.set('(')
    if press == ')':  # 右括号
        l_bracket_num, r_bracket_num = old_num.count('('), old_num.count(')')
        if l_bracket_num > r_bracket_num:
            if (old_num[-1].isdigit() or old_num[-1] == ')' or old_num[-1] in varlist2 or old_num[-1] == '!') and old_num != '0':
                line1.set(old_num+')')

    size_font()
# 关联键盘


def callback(event):
    if event.char.isdigit() or event.char in allsign:
        func(event.char)


root.bind('<Any-KeyPress>', callback)
root.bind('<BackSpace>', lambda s: func('back'))
# 事件循环
root.mainloop()
