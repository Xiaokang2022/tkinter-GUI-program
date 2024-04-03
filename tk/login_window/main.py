import tkinter as tk
import tkinter.messagebox as tk_mb
from random import choice

from ttkbootstrap import Style

window = tk.Tk()
window.title('主体')
window.geometry('0x0')
window.overrideredirect(1)
login = tk.Toplevel()
Style(theme='cosmo').master
login.title('用户登录')
login.geometry('250x200+500+250')
login.resizable(0, 0)
canvas = tk.Canvas(login, width=300, height=220)
image_list = range(7)
image_num = choice(image_list)
image_file = tk.PhotoImage(file='resources\\风景%s.png' % image_num)
canvas.create_image(130, 40, image=image_file)
canvas.place(x=-10, y=-10)
# login.overrideredirect(1)                 # 去除窗口边框
login.wm_attributes("-alpha", 0.9)        # 透明度(0.0~1.0)
# login.wm_attributes("-toolwindow",True)  # 置为工具窗口(没有最大最小按钮)
with open('login_data.csv', 'a'):
    pass
'''
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar,tearoff=0)
editmenu = tk.Menu(menubar,tearoff=0)
filemenu1 = tk.Menu(filemenu,tearoff=0)
menubar.add_cascade(label='设置(S)',menu=filemenu)
filemenu.add_cascade(label='语言',menu=filemenu1)
filemenu1.add_cascade(label='简体中文')
'''
tk.Label(login, text='用户:').place(x=25, y=115)
tk.Label(login, text='密码:').place(x=25, y=140)
entry1 = tk.Entry(login)
entry1.place(x=70, y=115)
entry2 = tk.Entry(login, show='*')
entry2.place(x=70, y=140)
tk.Button(login, text='注册', width=10,
          command=lambda: toplevel_register()).place(x=25, y=168)
tk.Button(login, text='登录', width=10,
          command=lambda: test_for_password()).place(x=140, y=168)


def toplevel_register():
    Toplevel_register = tk.Toplevel(login)
    Toplevel_register.title('用户注册')
    Toplevel_register.geometry('250x115+500+300')
    Toplevel_register.resizable(0, 0)
    tk.Canvas(Toplevel_register, width=300, height=125).place(x=-10, y=-10)

    label_text_list, label_y_list = ['用户名:', '新密码:', '新密码:'], [5, 30, 55]
    for lis_text, lis_y in zip(label_text_list, label_y_list):
        tk.Label(Toplevel_register, text=lis_text).place(x=20, y=lis_y)
    entry3 = tk.Entry(Toplevel_register)
    entry3.place(x=80, y=5)
    entry4 = tk.Entry(Toplevel_register, show='*')
    entry4.place(x=80, y=30)
    entry5 = tk.Entry(Toplevel_register, show='*')
    entry5.place(x=80, y=55)
    tk.Button(Toplevel_register, text='注册', width=10,
              command=lambda: register_account()).place(x=20, y=83)
    tk.Button(Toplevel_register, text='取消', width=10,
              command=lambda: Toplevel_register_quit()).place(x=150, y=83)

    def register_account():
        e3, e4, e5, account = entry3.get(), entry4.get(), entry5.get(), []
        for line in load_data():
            account.append(line.split(',')[0])
        if e3 == '' or e4 == '':
            tk_mb.showwarning(title='注册提示', message='用户名或密码不可为空！')
        elif e4 != e5:
            tk_mb.showwarning(title='注册提示', message='两次密码不一致！')
        elif e3 in account:
            tk_mb.showerror(title='注册提示', message='用户名已被注册！')
        else:
            with open('login_data.csv', 'a') as infile:
                infile.write('\n'+e3+','+e4)
            tk_mb.showinfo(title='注册提示', message='注册成功！')
            Toplevel_register.destroy()

    def Toplevel_register_quit(): Toplevel_register.destroy()


def load_data():
    with open('login_data.csv', 'r') as infile:
        indata = infile.readlines()
    for line in indata:
        indata[indata.index(line)] = line.strip()
    return indata


def mainwindow():
    window.overrideredirect(0)
    window.geometry('720x480+300+100')
    window.resizable(0, 0)
    tk.Frame(window, bg='lightyellow').place(width=100, height=480)


count = 0


def test_for_password():
    global count
    e1, e2 = entry1.get(), entry2.get()
    if e1 == '' or e2 == '':
        tk_mb.showwarning(title='登录提示', message='用户名或密码不可为空！')
    elif e1+','+e2 in load_data():
        tk_mb.showinfo(title='登录提示', message='登录成功！')
        login.destroy()
        mainwindow()
    else:
        count += 1
        if count < 5:
            tk_mb.showerror(title='登录提示', message='用户名或密码错误！')
        else:
            tk_mb.showerror(title='登录提示', message='已连续错误5次！请稍后再试！')
            login.destroy()
            window.quit()


# window.config(menu=menubar)
window.mainloop()
