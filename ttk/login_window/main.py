import random
import tkinter
import tkinter.messagebox
import tkinter.ttk

__author__ = '小康2022'

# NOTE: 2022/9/25 重制

root = tkinter.Tk()  # 创建主窗口
root.title('主窗口')  # 主窗口标题
root.geometry('0x0')  # 设置主窗口大小为 0
root.overrideredirect(True)  # 暂时隐藏主窗口外框

login = tkinter.Toplevel()  # 创建登录窗口
login.title('用户登录')  # 登录窗口的标题
login.geometry('250x200+500+250')  # 登录窗口的大小及位置
login.resizable(False, False)  # 设置登录窗口的大小不可改变

image = tkinter.PhotoImage(file='res\\风景%s.png' %
                           random.randint(0, 6))  # 随机选取一个图片
tkinter.Label(login, image=image, bd=0, text='登录窗口\n由Tkinter设计', compound='center', font=(
    '华文行楷', 25), fg='yellow').place(width=250, height=100)  # 创建一个图片标签
tkinter.Label(login, text='用户').place(
    width=50, height=25, x=20, y=105)  # “用户”文字标签
tkinter.Label(login, text='密码').place(
    width=50, height=25, x=20, y=135)  # “密码”文字标签
(account := tkinter.ttk.Entry(login)).place(
    width=160, height=25, x=70, y=105)  # 用户名输入框
(password := tkinter.ttk.Entry(login, show='●')).place(
    width=160, height=25, x=70, y=135)  # 密码输入框
tkinter.ttk.Button(login, text='注册', command=lambda: toplevel_register()).place(
    width=100, height=28, x=20, y=166)  # 注册按钮
tkinter.ttk.Button(login, text='登录', command=lambda: test_for_password()).place(
    width=100, height=28, x=130, y=166)  # 登录按钮


def load_data():
    with open('res/data.csv', 'r') as infile:  # 打开文件
        return map(str.strip, infile.readlines())  # 返回处理后数据


def toplevel_register() -> None:
    register = tkinter.Toplevel(login)  # 创建注册窗口
    register.title('用户注册')  # 注册窗口标题
    register.geometry('250x125+500+300')  # 注册窗口大小及位置
    register.resizable(False, False)  # 设定注册窗口大小不可改变

    tkinter.Label(register, text='用户名').place(
        width=50, height=25, x=25, y=5)  # “用户名”文字标签
    tkinter.Label(register, text='新密码').place(
        width=50, height=25, x=25, y=35)  # “新密码”文字标签
    tkinter.Label(register, text='新密码').place(
        width=50, height=25, x=25, y=65)  # “重复新密码”文字标签
    (account := tkinter.ttk.Entry(register)).place(
        width=150, height=25, x=80, y=5)  # 新用户名输入框
    (password := tkinter.ttk.Entry(register, show='●')).place(
        width=150, height=25, x=80, y=35)  # 新密码输入框
    (password_ := tkinter.ttk.Entry(register, show='●')).place(
        width=150, height=25, x=80, y=65)  # 重复密码输入框
    tkinter.ttk.Button(register, text='注册', command=lambda: register_account()).place(
        width=100, height=27, x=20, y=94)  # 注册按钮
    tkinter.ttk.Button(register, text='取消', command=register.destroy).place(
        width=100, height=27, x=130, y=94)  # 登录按钮

    def register_account() -> None:
        if not (account.get() and password.get()):  # 用户名或密码为空
            tkinter.messagebox.showwarning('注册提示', '用户名或密码不可为空！')
        elif password.get() != password_.get():  # 两次密码不一致
            tkinter.messagebox.showwarning('注册提示', '两次密码不一致！')
        elif account.get() in [line.split(',')[0] for line in load_data()]:  # 用户名已被注册
            tkinter.messagebox.showerror('注册提示', '用户名已被注册！')
        else:  # 注册成功
            with open('res/data.csv', 'a') as infile:  # 打开文件
                infile.write('%s,%s\n' %
                             (account.get(), password.get()))  # 写入信息
            tkinter.messagebox.showinfo('注册提示', '注册成功！')
            register.destroy()  # 关闭注册窗口


def test_for_password(count: list[int] = [0]) -> None:
    if not (account.get() and password.get()):  # 用户名或密码为空
        tkinter.messagebox.showwarning('登录提示', '用户名或密码不可为空！')
    elif account.get()+','+password.get() in load_data():  # 登录成功
        tkinter.messagebox.showinfo('登录提示', '登录成功！')
        login.destroy()  # 摧毁登录窗口
        root.overrideredirect(False)  # 显示主窗口外框
        root.geometry('960x540')  # 重新设置主窗口大小及位置
    else:  # 用户名或密码错误
        count[0] += 1  # 错误计数
        if count[0] < 5:  # 错误适量
            tkinter.messagebox.showerror('登录提示', '用户名或密码错误！')
        else:  # 错误过多
            tkinter.messagebox.showerror('登录提示', '已连续错误5次！\n请稍后再试！')
            root.quit()  # 退出窗口


root.mainloop()  # 窗口循环
