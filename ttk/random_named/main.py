import random
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.ttk
import webbrowser

__author__ = '小康2022'

# NOTE: 2022/10/16 重制


root = tkinter.Tk()  # 创建窗口
root.title('点名小程序')
root.geometry('300x500+500+100')
root.resizable(False, False)

flag = True  # 点名是否正在进行的标志
TIP = '温馨提示：\n支持的文件格式有txt和csv\n点击“解析文件”可再次加载文件\n文件格式如下：\n张三, 10001\n李四, 10002'

(_cb1 := tkinter.IntVar()).set(1)  # 复选按钮1的值
(_cb2 := tkinter.IntVar()).set(0)  # 复选按钮2的值
(_cb3 := tkinter.IntVar()).set(1)  # 复选按钮3的值
(info := tkinter.StringVar()).set('开始点名吧!')  # 开始点名按钮的显示值
path = tkinter.StringVar()  # 文件路径

tkinter.ttk.Button(root, text='选项设置', command=lambda: slide(-1)
                   ).place(width=135, height=30, x=155, y=460)
launch = tkinter.ttk.Button(root, text='开始点名', command=lambda: start())
launch.place(width=135, height=30, x=10, y=460)

canvas = tkinter.Canvas(root, bg='white', highlightthickness=0)
canvas.create_text(152, 37, text='点名小程序', font=('方正舒体', 40), fill='#BBB')
canvas.create_text(150, 35, text='点名小程序', font=('方正舒体', 40))
canvas.place(width=300, height=450)

_canvas = tkinter.Canvas(root, bg='white', highlightthickness=0)
_canvas.create_rectangle(0, 450, 270, 500, fill='#EEE', width=0)
_canvas.create_rectangle(10, 45, 260, 115, fill='#EEE', width=0)
_canvas.create_rectangle(10, 330, 260, 440, fill='#EEE', width=0)
_canvas.create_text(10, 10, anchor='nw', font=('楷体', 15), text='选项设置')
_canvas.create_text(20, 340, anchor='nw', font=('楷体', 11), text=TIP)
_canvas.create_line(0, 35, 270, 35, fill='grey')
_canvas.create_line(0, 0, 0, 500, fill='grey')
_canvas.place(width=270, height=500, x=300)

tkinter.Label(canvas, textvariable=info, font=('楷体', 12)
              ).place(width=280, height=30, x=10, y=80)

text = tkinter.scrolledtext.ScrolledText(canvas, bd=0, font=('楷体', 13), state='disabled',
                                         highlightthickness=1,
                                         highlightcolor='#4A9EE0',
                                         highlightbackground='#C0C0C0')
text.place(width=280, height=200, x=10, y=240)

c1 = tkinter.Canvas(canvas, highlightbackground='#C0C0C0',
                    highlightthickness=1)
c2 = tkinter.Canvas(canvas, highlightbackground='#C0C0C0',
                    highlightthickness=1)
c1.place(width=280, height=50, x=10, y=120)
c2.place(width=280, height=50, x=10, y=180)
t1 = c1.create_text(140, 25, font=('华文行楷', 20))
t2 = c2.create_text(140, 25, font=('华文行楷', 20))

tkinter.ttk.Checkbutton(_canvas, text='重复点名', variable=_cb1).place(
    width=70, height=30, x=20, y=50)
tkinter.ttk.Checkbutton(_canvas, text='随机点名', variable=_cb2).place(
    width=70, height=30, x=150, y=50)
tkinter.ttk.Checkbutton(_canvas, text='显示序号', variable=_cb3).place(
    width=70, height=30, x=20, y=80)

combobox = tkinter.ttk.Combobox(_canvas, textvariable=path)
combobox.place(width=250, height=25, x=10, y=125)

tkinter.ttk.Button(_canvas, text='选择文件', command=lambda: openfile()).place(
    width=120, height=30, x=10, y=160)
tkinter.ttk.Button(_canvas, text='解析文件', command=lambda: analysis()).place(
    width=120, height=30, x=140, y=160)

_text = tkinter.Text(_canvas, bd=0, font=('楷体', 13), state='disabled',
                     highlightthickness=1,
                     highlightcolor='#4A9EE0',
                     highlightbackground='#C0C0C0')
_text.place(width=250, height=120, x=10, y=200)

tkinter.ttk.Button(_canvas, text='返回', command=lambda: slide(
    1)).place(width=120, height=30, x=10, y=460)
tkinter.ttk.Button(_canvas, text='点赞支持',
                   command=lambda: webbrowser.open(
                       'https://xiaokang2022.blog.csdn.net/article/details/123600462')
                   ).place(width=120, height=30, x=140, y=460)


def openfile():
    """ 打开文件 """
    _path = tkinter.filedialog.askopenfilename(
        filetypes=[('All Files', ['*.txt', '*.csv'])])
    if _path:
        path.set(_path)  # 显示文件路径


def start():
    """ 开始点名 """
    if path.get():
        if not _text.get(1.).isspace() or analysis():
            launch.configure(text='停止', command=stop)
            info.set('会选中谁呢?')
            call()
    else:
        tkinter.messagebox.showinfo('温馨提示', '点名文件尚未添加！\n请单击“选项设置”以添加文件')


def stop():
    """ 停止点名 """
    global flag
    flag = False
    launch.configure(text='继续点名', command=start)


def analysis():
    """ 解析文件 """
    global data
    if not path.get():
        tkinter.messagebox.showinfo('温馨提示', '未选择文件！\n请单击“选择文件”以解析')
        return

    try:
        with open(path.get(), 'r') as file:
            data = [line.strip() for line in file.readlines() if line]
        if len(data[0].split(',')) != 2:
            tkinter.messagebox.showerror(
                '解析失败', '文件路径错误或文件格式不正确！\n请重新检查文件是否正确！')
            return
        result = '文件名称：' + path.get().split('/')[-1] + '\n'
        result += '点名人数：%d\n文件预览(前5项)：\n--------------------\n' % len(data)
        result += '\n'.join(data[:5])
        _text.configure(state='normal')
        _text.delete(1., 'end')
        _text.insert(1., result)
        _text.configure(state='disabled')
        data = [line.split(',') for line in data]
        if type(combobox['value']) == str:
            combobox['value'] = (path.get(),)
        elif path.get() not in combobox['value']:
            combobox['value'] = list(combobox['value']) + [path.get()]
        return True
    except:
        tkinter.messagebox.showerror('解析失败', '文件路径错误或文件格式不正确！\n请重新检查文件是否正确！')


def call(ind: list = [0, 0]):
    """ 点名滚动 """
    global flag
    if ind[0] == len(data):
        ind[0] = 0
    try:
        c1.itemconfigure(t1, text=data[ind[0]][0])
        c2.itemconfigure(t2, text=data[ind[0]][1])
    except:
        tkinter.messagebox.showinfo(
            '点名完毕', '当前为不重复点名模式！\n文件内所有名字均已点过！\n请点击“解析文件”以重新加载文件')
        stop()
        flag = True
        return
    if flag:
        if _cb2.get():
            ind[0] = random.randint(0, len(data) - 1)
        else:
            ind[0] += 1
        root.after(30, call)
    else:
        ind[1] += 1
        text.configure(state='normal')
        if _cb3.get():
            text.insert('end', '[%03d] %s %s\n' %
                        (ind[1], data[ind[0]][1], data[ind[0]][0]))
        else:
            text.insert('end', '%s %s\n' % (data[ind[0]][1], data[ind[0]][0]))
        text.configure(state='disabled')
        if not _cb1.get():
            del data[ind[0]]
        info.set('就是你啦!')
        flag = True


def slide(key: int, ind=0):
    """ 设置页滑动 """
    lib = [1, 2, 2, 3, 3, 5, 6, 7, 9, 12, 12, 9, 7, 6, 5, 3, 3, 2, 2, 1]
    _canvas.place(x=int(_canvas.place_info()['x']) + int(lib[ind] * key * 2.8))
    if ind < 19:
        root.after(5, slide, key, ind + 1)
    else:
        launch.configure(state='normal' if key == 1 else 'disabled')


root.mainloop()
