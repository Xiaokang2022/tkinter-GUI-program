# 人机AI #
from copy import deepcopy


class AI:
    def __init__(self, data):
        self.data = data

    def search(self, side, depth, data=[]):
        if depth == 0 or len(data) == 1:
            from pprint import pprint
            pprint(data[0])
            return data[0]

        side = 'Black' if side == 'Red' else 'Red'

        if data == []:
            tree = []
            lis = self.data
            for i in range(10):
                for j in range(9):
                    if 0 <= lis[i][j] <= 15:
                        for x in range(10):
                            for y in range(9):
                                if self.Isstep(lis, 'Black', i, j, x, y):
                                    temp = deepcopy(lis)
                                    temp[x][y] = -1
                                    temp[x][y], temp[i][j] = temp[i][j], temp[x][y]
                                    tree.append(
                                        [i, j, x, y, temp, self.scores(temp)])

            data = tree

        else:
            for ind, l in enumerate(data):
                lis = l[4]
                scorelist = []

                for i in range(10):
                    for j in range(9):
                        if (side == 'Red' and 16 <= lis[i][j] <= 31) or (side == 'Black' and 0 <= lis[i][j] <= 15):
                            for x in range(10):
                                for y in range(9):
                                    if self.Isstep(lis, side, i, j, x, y):
                                        temp = deepcopy(lis)
                                        temp[x][y] = -1
                                        temp[x][y], temp[i][j] = temp[i][j], temp[x][y]
                                        scorelist.append(self.scores(temp))

                tot, length = 0, 0
                for i in scorelist:
                    if i != 0:
                        tot += i
                        length += 1

                if length:
                    data[ind][-1] += tot/length
                else:
                    data[ind][-1] += 0
                '''

                k = 1 if side == 'Black' else -1
                scorelist = [k*i for i in scorelist]

                key = abs(min(scorelist))
                tot = 0
                for i in scorelist:
                    tot += (i+key)**2
                
                ans = 0
                for i in scorelist:
                    try:
                        ans += i*((i+key)**2/tot)
                    except:
                        continue

                data[ind][-1] += ans*k
                '''

        # [1:round(0.618*len(data))]
        return self.search(side, depth-1, sorted(data, key=lambda x: -x[-1])[0:round(0.618*len(data))])

    def scores(self, data):  # 计算棋面得分
        lib = (99999, 1500, 1500, 1000, 1000, 4000, 4000,
               6000, 6000, 4000, 4000, 100, 300, 500, 300, 100)
        Black, Red = 0, 0

        for i in data:
            for j in i:
                if 0 <= j <= 15:
                    Black += lib[j]
                if 16 <= j <= 31:
                    Red += lib[j-16]

        # return Black-Red

        if Black-Red > 0:
            return Black-Red*0.618
        else:
            return 0.618*Black-Red

    def Isstep(self, data, side, x, y, tx, ty):  # 判断是否可以走子
        i = data[x][y]

        if i != -1:

            if side == 'Black':
                lib = list(range(16, 32))
            else:
                lib = list(range(16))

            if i in [0, 16]:  # 将帅
                for sx, sy in zip([x+1, x-1, x, x], [y, y, y+1, y-1]):
                    if 0+7*(i//16) <= sx <= 2+7*(i//16) and 3 <= sy <= 5:
                        if [tx, ty] == [sx, sy] and data[sx][sy] in [-1]+lib:
                            return True

            if i in [1, 2, 17, 18]:  # 士仕
                for sx, sy in zip([x+1, x-1, x+1, x-1], [y+1, y-1, y-1, y+1]):
                    if 0+7*(i//17) <= sx <= 2+7*(i//17) and 3 <= sy <= 5:
                        if [tx, ty] == [sx, sy] and data[sx][sy] in [-1]+lib:
                            return True

            elif i in [3, 4, 19, 20]:  # 象相(撇腿)
                for sx, sy in zip([x+2, x-2, x+2, x-2], [y+2, y-2, y-2, y+2]):
                    if 0+5*(i//19) <= sx <= 4+5*(i//19) and 0 <= sy <= 8 and data[(sx+x)//2][(sy+y)//2] == -1:
                        if [tx, ty] == [sx, sy] and data[sx][sy] in [-1]+lib:
                            return True

            elif i in [5, 6, 21, 22]:  # 马(撇腿)
                for sx, sy in zip([x+2, x+2, x-2, x-2, x+1, x+1, x-1, x-1], [y+1, y-1, y+1, y-1, y+2, y-2, y+2, y-2]):
                    if 0 <= sx <= 9 and 0 <= sy <= 8 and data[round((sx+2*x)/3)][round((sy+2*y)/3)] == -1:
                        if [tx, ty] == [sx, sy] and data[sx][sy] in [-1]+lib:
                            return True

            elif i in [7, 8, 23, 24]:  # 车
                for lis in [range(1, 10), range(-1, -10, -1)]:

                    for d in lis:
                        if 9 >= x+d >= 0:
                            if data[x+d][y] != -1:
                                if [tx, ty] != [x+d, y]:
                                    break
                            if data[x+d][y] in [-1]+lib:
                                if [tx, ty] == [x+d, y]:
                                    return True
                            else:
                                break

                    for d in lis:
                        if 8 >= y+d >= 0:
                            if data[x][y+d] != -1:
                                if [tx, ty] != [x, y+d]:
                                    break
                            if data[x][y+d] in [-1]+lib:
                                if [tx, ty] == [x, y+d]:
                                    return True
                            else:
                                break

            elif i in [9, 10, 25, 26]:  # 炮
                for lis in [range(1, 10), range(-1, -10, -1)]:

                    pao_c = 0
                    for d in lis:
                        if 9 >= x+d >= 0:
                            if data[x+d][y] == -1 and pao_c == 0:
                                if [tx, ty] == [x+d, y]:
                                    return True
                            elif data[x+d][y] != -1:
                                pao_c += 1
                            if pao_c == 2:
                                if [tx, ty] == [x+d, y] and data[x+d][y] in lib:
                                    return True

                    pao_c = 0
                    for d in lis:
                        if 8 >= y+d >= 0:
                            if data[x][y+d] == -1 and pao_c == 0:
                                if [tx, ty] == [x, y+d]:
                                    return True
                            elif data[x][y+d] != -1:
                                pao_c += 1
                            if pao_c == 2:
                                if [tx, ty] == [x, y+d] and data[x][y+d] in lib:
                                    return True

            elif i in [11, 12, 13, 14, 15, 27, 28, 29, 30, 31]:  # 卒兵
                if (x < 5 and i//27 == 0) or (4 < x and i//27 == 1):  # 未过河
                    sx = x+(-1)**(i//27)
                    if [tx, ty] == [sx, y] and data[sx][y] in [-1]+lib:
                        return True

                elif ((5 <= x <= 9 and i//27 == 0) or (0 <= x <= 4 and i//27 == 1)) and 0 <= y <= 8:  # 已过河
                    dx = x+(-1)**(i//27)
                    for sx, sy in zip([x, dx, x], [y-1, y, y+1]):
                        if [tx, ty] == [sx, sy] and data[sx][sy] in [-1]+lib:
                            return True

        return False
