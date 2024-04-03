'''这是一个随机点名程序
实现了从数据中随机抽取指定数目的数据（不会有重复数据被抽取）
由用户输入存有姓名与学号的文件，文件格式支持csv表格、dat数据文件和txt文本文件
数据的格式要求不强硬，此程序可以智能识别，并获取姓名与学号数据
程序由界面化的部分和终端部分共同组成
界面化为用户点名提供方便，终端用于记录所有的点名过程
界面化程序中，按钮绑定了一些关联的事件，使得按钮更加高级
界面由两部分组成，一个是主页面，另一个是点名页面，可以相互切换
页面的切换类似于手机滑屏，采用正弦函数产生的数据实现滑动过程更加顺滑
点名页面会显示最近的10个点名记录，从上到下，依次显示
'''

from random import choice, sample
from tkinter import *


class CallingNmaes:
    '''
    这是一个可以实现随机点名的类————CallingNmaes
    '''

    def __init__(self):
        # -------- 设置窗口的一些属性 ----------
        self.root = Tk()
        self.root.title('随机点名小程序')
        self.root.resizable(0, 0)
        self.root.geometry('300x500+500+100')

        self.fresh = False  # 设定刷新为False
        self.name_table = [' \n']*10  # 名字显示的存储

    def read_file(self, file_path):
        '''
        这个方法可以简单地判断输入的文件路径是否符合要求
        现在支持的文件格式有CSV、DAT和TXT三种
        它可以智能地读取文件
        '''
        # ------------- 文件后缀名为csv -----------
        if '.csv' in file_path:
            try:
                with open(file_path, 'r') as infile:
                    self.data = infile.readlines()
                if '学号' in self.data[0] or '姓名' in self.data[0]:
                    self.data = self.data[1:]
                self.data = [lis.strip() for lis in self.data]
                self.data = [lis.split(',') for lis in self.data]
            except:  # 文件路径有误
                raise Exception(
                    '\033[31mIncorrect file path or file is not correct\033[0m')

        # ------------- 文件后缀名为dat或txt ------------
        elif '.txt' in file_path or '.dat' in file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    self.data = infile.readlines()
                if '学号' in self.data[0] or '姓名' in self.data[0]:
                    self.data = self.data[1:]
                self.data = [lis.strip() for lis in self.data]
                self.data = [lis.split() for lis in self.data]
            except:  # 文件路径有误
                raise Exception(
                    '\033[31mIncorrect file path or file is not correct\033[0m')

        # -------- 其他文件后缀名 -------------
        else:
            error_type = file_path.split('.')[-1]
            raise Exception('\033[31mIncorrect type(.%s) of text file.\033[0m\
\nWe only support text files in \033[34mCSV, DAT and TXT\033[0m formats now' % error_type)

    def GUI_initialization(self):
        '''
        执行这个方法会初始化GUI界面
        '''
        # -------------主页面 ----------------
        self.frame_home = Frame(self.root, bg='lightyellow')
        self.frame_home.place(width=300, height=500)
        Label(self.frame_home, bg='lightyellow', fg='skyblue', text='点名小程序',
              font=('华文新魏', 40)).place(width=300, height=100, y=50)
        Label(self.frame_home, bg='lightyellow', text='请在下方输入点名人数',
              font=('华文新魏', 15)).place(width=300, height=100, y=120)
        self.input_text = Entry(self.frame_home, bg='yellow', fg='springgreen', bd=0, font=(
            '华文新魏', 20), justify='center')
        self.input_text.place(width=150, height=40, x=75, y=200)
        self.label_hint = Label(self.frame_home, bg='lightyellow', fg='red',
                                text='输入值必须在0到%s之间!' % len(self.data), font=('宋体', 12))
        self.btn = Button(self.frame_home, bd=0, bg='lightgreen', fg='orange',
                          text='开始点名', font=('华文新魏', 18), command=self.judge_inputnum)
        self.btn.place(width=100, height=40, y=350, x=100)

        # -------------------- 点名页面 ------------------
        self.frame_call = Frame(self.root, bg='lightyellow')
        self.back = Button(self.frame_call, bd=0, bg='lightgreen', fg='orange', text='返回', font=(
            '华文新魏', 15), command=lambda: self.calling_page(2))
        self.back.place(width=100, height=30, y=460, x=170)

        # ------------------- 变量显示 ------------------
        self.text_info = StringVar()
        Label(self.frame_call, bg='lightyellow', fg='orange', textvariable=self.text_info, font=(
            '华文新魏', 30)).place(width=300, height=50, y=10)
        self.name_info = StringVar()
        Label(self.frame_call, bg='green').place(
            width=244, height=104, x=28, y=68)
        Label(self.frame_call, bg='lightyellow', textvariable=self.name_info, font=(
            '华文新魏', 20)).place(width=240, height=100, x=30, y=70)
        self.leave_num = StringVar()
        Label(self.frame_call, bg='lightyellow', textvariable=self.leave_num,
              fg='blue', font=('华文新魏', 15)).place(width=300, height=30, y=175)
        Label(self.frame_call, bg='green').place(
            width=244, height=244, x=28, y=208)
        self.name_infolis = StringVar()
        self.name_infolis.set(''.join(self.name_table)[:-1])
        Label(self.frame_call, bg='lightyellow', textvariable=self.name_infolis, font=(
            '楷体', 15)).place(width=240, height=240, x=30, y=210)

        # ----------------- 按钮关联 --------------------
        self.btn.bind('<Enter>', lambda event: btn_enter(event))
        self.btn.bind('<Leave>', lambda event: btn_leave(event))
        self.back.bind('<Enter>', lambda event: btn_enter(event))
        self.back.bind('<Leave>', lambda event: btn_leave(event))

        # ------------------ 关联函数 --------------------
        def btn_enter(event):
            event.widget['bg'] = 'skyblue'
            event.widget['fg'] = 'springgreen'

        def btn_leave(event):
            event.widget['bg'] = 'lightgreen'
            event.widget['fg'] = 'orange'

    def random_name(self, num):
        '''
        这个方法会从文件中随机调用num个不同的数据
        '''
        length = len(self.data)
        if num.isdigit() and 0 < int(num) < length:
            name_lis = sample(range(len(self.data)), int(num))
            return name_lis

    def calling_page(self, mode):
        '''
        这个方法用于转换页面
        mode 1：主页面转点名页面；mode 2：点名页面转主页面
        '''
        def slide(page1, page2, counter=0, i=1, flu=[200, 130, 90, 70, 50, 35, 25, 15, 5, -5, -15, -25, -35, -40, -35, -25, -15, -5, 0]):
            page1.place(width=300, height=500, x=i*flu[counter])
            page2.place(width=300, height=500, x=i*(flu[counter]-300))
            if counter < len(flu)-1:
                self.root.after(20, slide, page1, page2, counter+1, i)
            else:
                if mode == 1:
                    self.calling_info(self.random_lis)

        self.label_hint.place_forget()

        # -------------- 页面转换时的一些附加操作 -----------
        if mode == 1:
            self.fresh = False
            self.name_table = [' \n']*10
            self.name_infolis.set(''.join(self.name_table)[:-1])
            slide(self.frame_call, self.frame_home, i=1)
        else:
            self.fresh = True
            slide(self.frame_home, self.frame_call, i=-1)

    def judge_inputnum(self):
        '''
        这个方法用于判断用户输入的点名人数是否符合要求
        '''
        self.random_lis = self.random_name(self.input_text.get())

        if self.random_lis == None:
            self.label_hint.place(width=200, height=30, y=250, x=50)
        else:
            self.calling_page(1)

    def calling_info(self, lis):
        '''
        这个是点名页面的一些文本的显示
        '''
        print()

        def next(i=0):
            self.select(lis[i], i)
            self.leave_num.set('还有%s个人要点名哦!' % (len(lis)-i-1))
            if i < len(lis)-1 and not self.fresh:
                self.root.after(3000, next, i+1)

        next(i=0)

    def select(self, num, count):
        '''
        随机名字的显示由这个方法实现
        '''
        def timer(counter=0):
            l = choice(self.data)
            if l[0].isdigit():
                l[0], l[1] = l[1], l[0]
            self.name_info.set('%s\n%s' % (l[0], l[1]))
            if counter < 50 and not self.fresh:
                self.root.after(30, timer, counter+1)
            else:
                self.text_info.set('就是你啦!')
                self.name_info.set('%s\n%s' % (real_data[0], real_data[1]))

                if count < 10:
                    self.name_table[count] = '%s %s\n' % (
                        real_data[0], real_data[1])
                    self.name_infolis.set(''.join(self.name_table)[:-1])
                else:
                    self.name_table.append('%s %s\n' %
                                           (real_data[0], real_data[1]))
                    self.name_infolis.set(''.join(self.name_table[-10:])[:-1])

                print('嘿！\033[32m%s\033[0m,就是你啦！你的学号是\033[32m%s\033[0m' % (
                    real_data[0], real_data[1]))

        self.text_info.set('随机点名中...')

        real_data = self.data[num]
        if real_data[0].isdigit():
            real_data[0], real_data[1] = real_data[1], real_data[0]

        timer(counter=0)


file_path = input('【请输入姓名学号文件路径】')  # 用户输入文件路径

object = CallingNmaes()  # 实例化对象
object.read_file(file_path)  # 读取文件
object.GUI_initialization()  # 初始化GUI界面
object.root.mainloop()  # 启动窗口

# --------------- 测试文件 ----------
# test.csv or test.txt
