import pygame
from copy import deepcopy

pygame.init()

with open('__init__.txt', 'r') as init:
    _init = eval(init.read())
    length = _init['length']
    width = _init['width']
    mode = _init['mode']
    del _init
if (not mode) and length != width:
    raise ValueError('when the boundary is not enabled, the length and width must be the same')
length_ = length // 5
width_ = width // 5
window = pygame.display.set_mode((length, width))
draw = False
drawLock = False
empty = []
for i in range(length_):
    _ = []
    for j in range(width_):
        _.append(0)
    empty.append(_)
del _
liveNow = deepcopy(empty)
liveNext = deepcopy(liveNow)
r = 0
oldColorPoint = (-1, -1)
Quit = False


class MyEvent():
    type = pygame.USEREVENT


while True:
    events = pygame.event.get()
    if not events:
        # MyEvent = MyEvent
        events.append(MyEvent)  # 无动作时使events不为空

    for event in events:
        if event.type == pygame.QUIT:
            Quit = True  # 退出游戏
            break

        elif event.type == pygame.MOUSEBUTTONDOWN:
            draw = True and not drawLock  # 开始绘制

        elif event.type == pygame.MOUSEBUTTONUP:
            draw = False and not drawLock  # 结束绘制
            oldColorPoint = (-1, -1)

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_CLEAR, pygame.K_c] and not drawLock:
                liveNow = deepcopy(empty)
                window.fill((0, 0, 0))  # 清屏

            if event.key == pygame.K_s:
                drawLock = not drawLock  # 更改锁的状态

        if not drawLock:  # 重置轮数
            pygame.display.set_caption('康威生命游戏')
            r = 0
        else:  # 计算下一代
            x = 0
            while x < length_:
                y = 0
                while y < width_:
                    add = 0
                    i = -1
                    while i < 2:
                        j = -1
                        while j < 2:
                            if not i == j == 0:
                                _x, _y = (x + i), (y + j)
                                if (-1 < _x < length_ and -1 < _y < width_) or (not mode):  # 限制细胞状态更新范围
                                    a = liveNow[_x % length_][_y % width_]
                                    add += a
                            j += 1
                        i += 1

                    if add in ([2, 3] if liveNow[x][y] == 1 else [3]):  # 渲染下一轮细胞状态
                        liveNext[x][y] = 1
                        pygame.draw.rect(window, (255, 255, 255), (x * 5, y * 5, 5, 5))
                    else:
                        liveNext[x][y] = 0
                        pygame.draw.rect(window, (0, 0, 0), (x * 5, y * 5, 5, 5))
                    y += 1
                x += 1

            liveNow = deepcopy(liveNext)
            pygame.display.set_caption(f'康威生命游戏一一第{r}轮')  # 更改标题

            continue

        ColorPoint = (pygame.mouse.get_pos()[0] // 5, pygame.mouse.get_pos()[1] // 5)
        PointColor = window.get_at(pygame.mouse.get_pos())
        if draw and oldColorPoint != ColorPoint:  # 更改细胞生死状态
            pygame.draw.rect(window, (255 - PointColor[0], 255 - PointColor[1], 255 - PointColor[2]),
                             (ColorPoint[0] * 5, ColorPoint[1] * 5, 5, 5))
            liveNow[ColorPoint[0]][ColorPoint[1]] *= -1
            liveNow[ColorPoint[0]][ColorPoint[1]] += 1
            oldColorPoint = deepcopy(ColorPoint)

        r += 1
        pygame.display.flip()

    if Quit:
        break
