import pygame
from copy import deepcopy
from datetime import datetime
from re import sub


pygame.init()

with open('__init__.txt', 'r', encoding='utf+8') as init:
    _init = eval(init.read())
    length = _init['length']
    width = _init['width']
    EnableBoundary = _init['EnableBoundary']
    del _init
if (not EnableBoundary) and length != width:
    raise ValueError('when the boundary is not enabled, the length and width must be the same')
window = pygame.display.set_mode((length * 5, width * 5))
draw = False
drawLock = False
empty = []
for i in range(length):
    _ = []
    for j in range(width):
        _.append(0)
    empty.append(_)
del _
liveNow = deepcopy(empty)

with open('__path__.txt', 'r', encoding='utf+8') as path:
    with open(path.read(), 'r', encoding='utf+8') as cellList:
        cells = eval(cellList.read())
        for cell in cells:
            liveNow[cell[0]][cell[1]] = 1
            pygame.draw.rect(window, (255, 255, 255), (cell[0] * 5, cell[1] * 5, 5, 5))

liveNext = deepcopy(liveNow)
r = 0
oldColorPoint = (-1, -1)
Quit = False


class MyEvent:
    type = pygame.USEREVENT


while True:
    events = pygame.event.get()
    if not events:
        events.append(MyEvent)

    for event in events:
        if event.type in [pygame.QUIT, pygame.K_q]:
            Quit = True
            break

        elif event.type == pygame.MOUSEBUTTONDOWN:
            draw = True and not drawLock

        elif event.type == pygame.MOUSEBUTTONUP:
            draw = False and not drawLock
            oldColorPoint = (-1, -1)

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_CLEAR, pygame.K_c] and not drawLock:
                liveNow = deepcopy(empty)
                window.fill((0, 0, 0))
            elif event.key == pygame.K_s:
                with open(sub(':', '：', str(datetime.now()))[:-7] + '.txt',
                          'w', encoding='utf+8') as cells:
                    cellList = []
                    for x in range(length):
                        for y in range(width):
                            if liveNow[x][y] == 1:
                                cellList.append([x, y])
                    cells.write(str(cellList))
            else:
                drawLock = not drawLock

        if not drawLock:
            pygame.display.set_caption('Conway Game Of Life')
            r = 0
        else:
            for x in range(length):
                for y in range(width):
                    add = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if not i == j == 0:
                                _x, _y = (x + i), (y + j)
                                if (-1 < _x < length and -1 < _y < width) or (not EnableBoundary):
                                    a = liveNow[_x % length][_y % width]
                                    add += a

                    if add in ([2, 3] if liveNow[x][y] == 1 else [3]):
                        liveNext[x][y] = 1
                        pygame.draw.rect(window, (255, 255, 255), (x * 5, y * 5, 5, 5))
                    else:
                        liveNext[x][y] = 0
                        pygame.draw.rect(window, (0, 0, 0), (x * 5, y * 5, 5, 5))
                    y += 1

            liveNow = deepcopy(liveNext)
            OrdinalSuffix = 'th' if r % 100 // 10 == 1 or r % 10 > 3 or r % 10 == 0 else (
                'st' if r % 10 == 1 else ('nd' if r % 10 == 2 else 'rd'))
            pygame.display.set_caption(f'Conway Game Of Life -- the {str(r) + OrdinalSuffix} generation of life')

        ColorPoint = (pygame.mouse.get_pos()[0] // 5, pygame.mouse.get_pos()[1] // 5)
        PointColor = window.get_at(pygame.mouse.get_pos())
        if draw and oldColorPoint != ColorPoint:
            pygame.draw.rect(window, (255 - PointColor[0], 255 - PointColor[1], 255 - PointColor[2]),
                             (ColorPoint[0] * 5, ColorPoint[1] * 5, 5, 5))
            liveNow[ColorPoint[0]][ColorPoint[1]] *= -1
            liveNow[ColorPoint[0]][ColorPoint[1]] += 1
            oldColorPoint = deepcopy(ColorPoint)
        r += 1

    pygame.display.flip()

    if Quit:
        break
