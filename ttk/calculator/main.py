import math
import tkinter
import tkinter.ttk

__author__ = '小康2022'

# NOTE: 2022/9/26 重制


# 保存临时结果
Ans = '0'


root = tkinter.Tk()  # 创建窗口
root.title('计算器')  # 设置窗口标题
root.geometry('301x500+500+100')  # 设置窗口大小及位置
root.resizable(False, False)  # 设置窗口大小不可改变
root.attributes("-alpha", 0.9)  # 设置窗口透明度为0.9
tkinter.ttk.Style(root).configure('TButton', font=('楷体', 15))  # 设置按钮字体及大小


# 第一栏变量
(line_1 := tkinter.StringVar()).set('0')
# 第二栏变量
line_2 = tkinter.StringVar()
# 第三栏变量
line_3 = tkinter.StringVar()
# 第一栏
(label_1 := tkinter.Label(root, textvariable=line_1, anchor='e',
 font=('微软雅黑', 40))).place(y=145, width=300, height=80)
# 第二栏
(label_2 := tkinter.Label(root, textvariable=line_2, anchor='e',
 font=('微软雅黑', 30))).place(y=65, width=300, height=80)
# 第三栏
(label_3 := tkinter.Label(root, textvariable=line_3, anchor='e',
 font=('微软雅黑', 20))).place(y=20, width=300, height=45)


# 各个按钮
button = [tkinter.ttk.Button(root, text='ln', command=lambda: func('ln(')),
          tkinter.ttk.Button(root, text='+/-', command=lambda: func('+/-')),
          tkinter.ttk.Button(root, text='0', command=lambda: func('0')),
          tkinter.ttk.Button(root, text='.', command=lambda: func('.')),
          tkinter.ttk.Button(root, text='=', command=lambda: func('=')),
          tkinter.ttk.Button(root, text='n!', command=lambda: func('!')),
          tkinter.ttk.Button(root, text='1', command=lambda: func('1')),
          tkinter.ttk.Button(root, text='2', command=lambda: func('2')),
          tkinter.ttk.Button(root, text='3', command=lambda: func('3')),
          tkinter.ttk.Button(root, text='+', command=lambda: func('+')),
          tkinter.ttk.Button(root, text='mod', command=lambda: func('mod')),
          tkinter.ttk.Button(root, text='4', command=lambda: func('4')),
          tkinter.ttk.Button(root, text='5', command=lambda: func('5')),
          tkinter.ttk.Button(root, text='6', command=lambda: func('6')),
          tkinter.ttk.Button(root, text='-', command=lambda: func('-')),
          tkinter.ttk.Button(root, text='^', command=lambda: func('^')),
          tkinter.ttk.Button(root, text='7', command=lambda: func('7')),
          tkinter.ttk.Button(root, text='8', command=lambda: func('8')),
          tkinter.ttk.Button(root, text='9', command=lambda: func('9')),
          tkinter.ttk.Button(root, text='×', command=lambda: func('×')),
          tkinter.ttk.Button(root, text='√', command=lambda: func('√(')),
          tkinter.ttk.Button(root, text='AC', command=lambda: func('a')),
          tkinter.ttk.Button(root, text='C', command=lambda: func('c')),
          tkinter.ttk.Button(root, text='Ans', command=lambda: func('Ans')),
          tkinter.ttk.Button(root, text='÷', command=lambda: func('÷')),
          tkinter.ttk.Button(root, text='e', command=lambda: func('e')),
          tkinter.ttk.Button(root, text='π', command=lambda: func('π')),
          tkinter.ttk.Button(root, text='(', command=lambda: func('(')),
          tkinter.ttk.Button(root, text=')', command=lambda: func(')')),
          tkinter.ttk.Button(root, text='←', command=lambda: func('BackSpace'))]


# 放置各个按钮
for y, k in zip([455, 410, 365, 320, 275, 230], range(6)):
    for x, _button in zip([1, 61, 121, 181, 241], button[5*k:5*k+5]):
        _button.place(x=x, y=y, width=59, height=44)


def wrap(func):
    """ 函数包装器，使math库函数返回值取整 """
    def wrap_function(num: int):
        key = func(num)
        if abs(key-round(key)) < 1e-6:
            return int(key)
        return key
    return wrap_function


sqrt = wrap(math.sqrt)  # 包装sqrt函数
log = wrap(math.log)  # 包装log函数
pi = math.pi  # math库的pi
e = math.e  # math库的e


def calc(string: str):
    """ 解析字符串表达式 """
    result = string.replace('Ans', Ans)
    result = result.replace('×', '*')
    result = result.replace('÷', '/')
    result = result.replace('^', '**')
    result = result.replace('mod', '%')
    result = result.replace('ln', 'log')
    result = result.replace('√', 'sqrt')
    result = result.replace('π', 'pi')
    result = result.replace('e', 'e')

    # 简写处理，如 3e 等价于 3*e
    c, temp = 0, result
    for i, v in enumerate(temp):
        if temp[i-1].isdigit() and v in '(pelsA':
            result = result[:i+c] + '*' + result[i+c:]
            c += 1

    # 阶乘处理，如 3! 等价于 math.factorial(3)
    c, temp = 0, result
    for i, v in enumerate(temp):
        if v == '!':
            key = 0
            if temp[i-1].isdigit():
                for ind in range(i):
                    if not temp[i-ind-1].isdigit():
                        key = i-ind
                        break
                result = result.replace('!', ')', 1)
                result = result[:15*c+key] + \
                    'math.factorial(' + \
                    result[15 * c+key:15*c+i] + result[15*c+i:]
            elif temp[i-1] == ')':
                k = 0
                for ind in range(i):
                    if temp[i-ind] == ')':
                        k += 1
                    elif temp[i-ind] == '(':
                        k -= 1
                    if not k:
                        if temp[i-ind-4:i-ind] == 'sqrt':
                            key = i-ind-4
                        elif temp[i-ind-3:i-ind] == 'log':
                            key = i-ind-3
                        result = result.replace('!', ')', 1)
                        result = result[:15*c+key] + \
                            'math.factorial(' + \
                            result[15*c+key:15*c+i] + result[15*c+i:]
                        break
            c += 1

    try:
        # 计算字符串表达式
        return str(eval(result))
    except:
        # 错误返回
        return 'Error'


def func(key: str):
    global Ans

    if key.isdigit() or key in 'eπ+-×÷^!.*/({[]})' or key in ('√(', 'ln(', 'mod'):
        # 输入字符
        key = '×' if key == '*' else '÷' if key == '/' else key
        key = line_1.get() + key if line_1.get() != '0' else key
        line_1.set(key)

    elif key in 'cC':
        # 清除第一栏
        line_1.set('0')

    elif key in 'aA':
        # 清空所有栏
        line_1.set('0')
        line_2.set('')
        line_3.set('')

    elif key == 'BackSpace':
        # 删减字符操作
        if line_1.get()[-3:] in ('mod', 'Ans', 'ln('):
            line_1.set(line_1.get()[:-3])
        elif line_1.get()[-5:] == 'sqrt(':
            line_1.set(line_1.get()[:-5])
        else:
            line_1.set(line_1.get()[:-1])
        if line_1.get() in ('Erro', ''):
            line_1.set('0')

    elif key == '+/-':
        # 正负号切换
        if line_1.get()[0] == '-':
            line_1.set(line_1.get()[1:])
        elif line_1.get() != '0':
            line_1.set('-'+line_1.get())

    elif key == 'Ans':
        # 上一个结果
        if line_2.get() and line_1.get() != '0':
            line_1.set(line_1.get() + 'Ans')

    elif key in '=Return':
        # 计算值
        line_3.set(line_2.get())
        line_2.set(line_1.get())
        Ans = calc(line_1.get())
        line_1.set(Ans)

    # 字体大小处理
    if len(line_1.get()) >= 8:
        label_1.configure(font=('微软雅黑', round(40*8/len(line_1.get()))))
    else:
        label_1.configure(font=('微软雅黑', 40))
    if len(line_2.get()) >= 12:
        label_2.configure(font=('微软雅黑', round(30*12/len(line_2.get()))))
    else:
        label_2.configure(font=('微软雅黑', 30))
    if len(line_3.get()) >= 18:
        label_3.configure(font=('微软雅黑', round(20*18/len(line_3.get()))))
    else:
        label_3.configure(font=('微软雅黑', 20))


# 键盘关联
root.bind('<Any-Key>',
          lambda event: func(event.char if event.char.isprintable() else event.keysym))
# 窗口循环
root.mainloop()
