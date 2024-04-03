# 初始化变量 #
from tkinter import *


class value:
    # 窗口变量 #
    game = Tk()  # 创建窗口
    game.title('中国象棋')  # 窗口标题
    game.geometry('960x500+150+100')  # 窗口大小及位置
    game.resizable(0, 0)  # 窗口大小固定
    game.iconbitmap('resources\\icon.ico')  # 窗口图标
    canvas = Canvas(game, highlightthickness=0)  # 创建画布
    canvas2 = Canvas(canvas, highlightthickness=0)

    # 基本变量 #
    modelis = ['人机', '对弈', '机机', '网络', '闯关']  # 游戏模式
    mode = modelis[1]  # 默认模式
    levellis = ['暂无数据', '简单', '普通', '困难']  # 人机难度
    level = levellis[0]  # 默认难度
    playerlis = ['红方', '黑方']  # 玩家列表
    player = '红方'  # 当前玩家
    first = playerlis[0]  # 先下棋方
    challenge = '暂无数据'  # 闯关关数
    r_please = '无'  # 红方让子
    b_please = '无'  # 黑方让子
    regret = 0  # 悔棋次数
    alpha = 1  # 窗口透明
    max_depth = 3  # 搜索深度

    colorlis1 = ['black', 'black', 'white', 'lightyellow', 'lightgreen',
                 'springgreen', 'orange', 'yellow', 'red', 'white', 'springgreen']
    colorlis2 = ['black', 'black', 'white', 'white', 'grey',
                 'black', 'grey', 'grey', 'black', 'white', 'white']
    colorlis3 = ['blue', 'deepskyblue', 'skyblue', 'skyblue', 'deepskyblue',
                 'blue', 'white', 'deepskyblue', 'blue', 'skyblue', 'cyan']
    colorlis4 = ['darkgreen', 'green', 'white', 'lightgreen', 'yellowgreen',
                 'springgreen', 'white', 'green', 'darkgreen', 'lightgreen', 'springgreen']
    colorlis5 = ['purple', 'purple', 'white', 'pink', 'hotpink',
                 'fuchsia', 'red', 'pink', 'red', 'plum', 'plum']
    # 字体颜色[0] 框架颜色[1] 按钮框按下[2] 浅背景[3] 深按钮背景[4] 高亮按钮框[5] 高亮文本[6] 路径色[7] 敌人标记[8] 自己标记[9] 鼠标位置显示[10]
    colorlists = [colorlis1, colorlis2, colorlis3, colorlis4, colorlis5]

    with open('resources\\cache.txt', 'r') as infile:
        data = infile.readline()

    theme = int(data)

    colorlis = colorlists[theme-1]

    # 游戏变量 #
    flulis = [0.01, 0.03, 0.07, 0.14, 0.24, 0.39, 0.67,
              0.82, 0.92, 0.99, 1.03, 1.05, 1.06, 1.04, 1]

    info_lists = [[0]*9 for _ in range(10)]

    b_j, b_s1, b_s2, b_x1, b_x2, b_m1, b_m2, b_c1, b_c2, b_p1, b_p2, b_z1, b_z2, b_z3, b_z4, b_z5 = [
        0]*16
    r_j, r_s1, r_s2, r_x1, r_x2, r_m1, r_m2, r_c1, r_c2, r_p1, r_p2, r_z1, r_z2, r_z3, r_z4, r_z5 = [
        0]*16

    peice_lists = [b_j, b_s1, b_s2, b_x1, b_x2, b_m1, b_m2, b_c1, b_c2, b_p1, b_p2, b_z1, b_z2, b_z3, b_z4, b_z5,
                   r_j, r_s1, r_s2, r_x1, r_x2, r_m1, r_m2, r_c1, r_c2, r_p1, r_p2, r_z1, r_z2, r_z3, r_z4, r_z5]

    board_lists = [[7, 5, 3, 1, 0, 2, 4, 6, 8],  # 初始棋子摆法
                   [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                   [-1, 9, -1, -1, -1, -1, -1, 10, -1],
                   [11, -1, 12, -1, 13, -1, 14, -1, 15],
                   [-1, -1, -1, -1, -1, -1, -1, -1, -1],

                   [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                   [27, -1, 28, -1, 29, -1, 30, -1, 31],
                   [-1, 25, -1, -1, -1, -1, -1, 26, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                   [23, 21, 19, 17, 16, 18, 20, 22, 24]]

    peices = ['将', '士', '士', '象', '象', '马', '马', '车', '车', '炮', '炮', '卒', '卒', '卒', '卒', '卒',
              '帅', '仕', '仕', '相', '相', '马', '马', '车', '车', '炮', '炮', '兵', '兵', '兵', '兵', '兵']

    number = ['一', '二', '三', '四', '五', '六', '七', '八', '九']

    b_team = range(16)
    r_team = range(16, 32)
    team = r_team
    step = 0
    stepcontent = ''

    templists = []
    play_count = 0
    play_temp_x, play_temp_y = -2, -2
    play_tempvalue = -2

    DEAD = 0
    steptextlis = []
    firststep = 250

    gameinfo_temp = None

    p_rc1, p_rc2, p_rp1, p_rp2, p_rm1, p_rm2 = [0, 0, 0, 0, 0, 0]
    p_bc1, p_bc2, p_bp1, p_bp2, p_bm1, p_bm2 = [0, 0, 0, 0, 0, 0]

    p_r = [p_rc1, p_rc2, p_rp1, p_rp2, p_rm1, p_rm2]  # 让子列表
    p_b = [p_bc1, p_bc2, p_bp1, p_bp2, p_bm1, p_bm2]

    regretuselis = [eval(str(board_lists))]

    # 图片资源 #
    background = PhotoImage(file='resources\\background.png')
    victory = PhotoImage(file='resources\\victory.png')
    defeat = PhotoImage(file='resources\\defeat.png')
    dead = PhotoImage(file='resources\\dead.png')
    gank = PhotoImage(file='resources\\gank.png')
    face = PhotoImage(file='resources\\face.png')
    bigface = PhotoImage(file='resources\\bigface.png')
    makebg = PhotoImage(file='resources\\makebg.png')
    helpbg = PhotoImage(file='resources\\helpbg.png')

    bglis = []  # 图片列表

    image_b_j = PhotoImage(file='resources\\peices\\b_j.png')
    image_b_s1 = PhotoImage(file='resources\\peices\\b_s.png')
    image_b_s2 = PhotoImage(file='resources\\peices\\b_s.png')
    image_b_x1 = PhotoImage(file='resources\\peices\\b_x.png')
    image_b_x2 = PhotoImage(file='resources\\peices\\b_x.png')
    image_b_m1 = PhotoImage(file='resources\\peices\\b_m.png')
    image_b_m2 = PhotoImage(file='resources\\peices\\b_m.png')
    image_b_c1 = PhotoImage(file='resources\\peices\\b_c.png')
    image_b_c2 = PhotoImage(file='resources\\peices\\b_c.png')
    image_b_p1 = PhotoImage(file='resources\\peices\\b_p.png')
    image_b_p2 = PhotoImage(file='resources\\peices\\b_p.png')
    image_b_z1 = PhotoImage(file='resources\\peices\\b_z.png')
    image_b_z2 = PhotoImage(file='resources\\peices\\b_z.png')
    image_b_z3 = PhotoImage(file='resources\\peices\\b_z.png')
    image_b_z4 = PhotoImage(file='resources\\peices\\b_z.png')
    image_b_z5 = PhotoImage(file='resources\\peices\\b_z.png')

    image_r_j = PhotoImage(file='resources\\peices\\r_j.png')
    image_r_s1 = PhotoImage(file='resources\\peices\\r_s.png')
    image_r_s2 = PhotoImage(file='resources\\peices\\r_s.png')
    image_r_x1 = PhotoImage(file='resources\\peices\\r_x.png')
    image_r_x2 = PhotoImage(file='resources\\peices\\r_x.png')
    image_r_m1 = PhotoImage(file='resources\\peices\\r_m.png')
    image_r_m2 = PhotoImage(file='resources\\peices\\r_m.png')
    image_r_c1 = PhotoImage(file='resources\\peices\\r_c.png')
    image_r_c2 = PhotoImage(file='resources\\peices\\r_c.png')
    image_r_p1 = PhotoImage(file='resources\\peices\\r_p.png')
    image_r_p2 = PhotoImage(file='resources\\peices\\r_p.png')
    image_r_z1 = PhotoImage(file='resources\\peices\\r_z.png')
    image_r_z2 = PhotoImage(file='resources\\peices\\r_z.png')
    image_r_z3 = PhotoImage(file='resources\\peices\\r_z.png')
    image_r_z4 = PhotoImage(file='resources\\peices\\r_z.png')
    image_r_z5 = PhotoImage(file='resources\\peices\\r_z.png')

    resourcelists = [image_b_j, image_b_s1, image_b_s2, image_b_x1, image_b_x2, image_b_m1, image_b_m2, image_b_c1,
                     image_b_c2, image_b_p1, image_b_p2, image_b_z1, image_b_z2, image_b_z3, image_b_z4, image_b_z5,
                     image_r_j, image_r_s1, image_r_s2, image_r_x1, image_r_x2, image_r_m1, image_r_m2, image_r_c1,
                     image_r_c2, image_r_p1, image_r_p2, image_r_z1, image_r_z2, image_r_z3, image_r_z4, image_r_z5]

    # 文本变量 #
    helptext = '- 游戏说明 -\n白框标识棋为当前选中棋\n黄框标识位为当前棋可走路径\n红框标识棋为当前棋可吃棋\n\
              \n- 游戏规则 -\n马走日；相走田；士走斜\n将、帅和士不可出九宫格\n车和炮直走，炮隔着吃子\n河前兵往前，河后左右前\n\
              \n- 快捷键 -\n设置(s)、悔棋(r)、退出(q)\n帮助(h)、重置(a)、制作人员(m)'

    maketext = '《中国象棋》\n\n\n作者:小康\n版本：1.0\n\
              \n- 开发说明 -\n\n语言:Python\n开发工具:Visual Studio\n代码量:约72KB\n启动文件:Luncher.py\n\
              \n- 更新时间 -\n\n2022/07/14\n\
              \n- 特别说明 -\n\n图片均来源于互联网\n\
              \n- 免责声明 -\n\n若有侵权，请联系我\n\
              \n- 联系邮箱 -\n\n392126563@qq.com\n\
              \n\n\n感谢您体验这款游戏!'

    # 界面变量 #
    help_canvas = Canvas(game, highlightthickness=0)  # 帮助界面 #
    help_canvas.create_image(480, 250, image=helpbg)

    help_canvas.create_text(482, 62, text='游戏帮助',
                            font=('华文新魏', 60), fill='grey')
    help_canvas.create_text(480, 60, text='游戏帮助',
                            font=('华文新魏', 60), fill='orange')
    help_canvas.create_text(481, 291, text=helptext,
                            font=('华文新魏', 20), justify='center')
    help_canvas.create_text(480, 290, text=helptext, font=(
        '华文新魏', 20), fill='white', justify='center')

    make_canvas = Canvas(game, highlightthickness=0)  # 制作人员界面 #
    make_canvas.create_image(480, 250, image=makebg)
    make_canvas.create_image(680, 150, image=bigface)

    make_canvas2 = Canvas(make_canvas, highlightthickness=0)
    make_canvas2.place(width=300, height=150, x=420, y=260)
    make_canvas2.create_image(480-420, 250-260, image=makebg)

    textspeed = -1  # 文本滚动速度

    set_canvas = Canvas(game, highlightthickness=0, bg=colorlis[3])  # 设置界面 #
    set_canvas.create_rectangle(10, 50, 950, 490, width=3, outline=colorlis[1])
    set_canvas.create_rectangle(15, 55, 945, 485, outline=colorlis[1])
    set_canvas.create_line(230, 70, 230, 470, fill=colorlis[1])

    set_canvas.create_rectangle(799, 9, 950, 40, outline=colorlis[1])
    sbt1 = Button(set_canvas, text='返回', font=(
        '华文新魏', 17), bd=0, bg=colorlis[3])
    sbt1.place(width=150, height=30, x=800, y=10)

    set_canvas.create_rectangle(639, 9, 790, 40, outline=colorlis[1])
    sbt2 = Button(set_canvas, text='重置', font=(
        '华文新魏', 17), bd=0, bg=colorlis[3])
    sbt2.place(width=150, height=30, x=640, y=10)

    text_canvas = Canvas(set_canvas, bg=colorlis[3], highlightthickness=0)
    text_canvas.place(width=700, height=400, x=231, y=70)

    s1 = Button(set_canvas, bd=0, bg=colorlis[3], font=(
        '华文新魏', 20), text='模式设置')
    s2 = Button(set_canvas, bd=0, bg=colorlis[3], font=(
        '华文新魏', 20), text='棋局设置')
    s3 = Button(set_canvas, bd=0, bg=colorlis[3], font=(
        '华文新魏', 20), text='闯关设置')
    s4 = Button(set_canvas, bd=0, bg=colorlis[3], font=(
        '华文新魏', 20), text='主题设置')
    s5 = Button(set_canvas, bd=0, bg=colorlis[3], font=(
        '华文新魏', 20), text='音效设置')
    s6 = Button(set_canvas, bd=0, bg=colorlis[3], font=(
        '华文新魏', 20), text='窗口设置')
    s7 = Button(set_canvas, bd=0, bg=colorlis[3], font=(
        '华文新魏', 20), text='系统说明')
    s8 = Button(set_canvas, bd=0, bg=colorlis[3], font=(
        '华文新魏', 20), text='暂无设置')

    slis = [s1, s2, s3, s4, s5, s6, s7, s8]

    s1_, s2_, s3_, s4_, s5_, s6_, s7_, s8_ = [], [], [], [], [], [], [], []
