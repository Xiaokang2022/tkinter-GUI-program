# 启动程序 #
from tkinter import *

from buttonbind import buttonbind
from initialization import initialization
from mouse import mouse
from play import play
from rule import rule
from value import value

initialization()  # 界面初始化
buttonbind()  # 关联处理
mouse()  # 实时显示鼠标位置
play()  # 玩家走子
rule()  # 执行规则

value.game.mainloop()  # 启动窗口


# 17行
