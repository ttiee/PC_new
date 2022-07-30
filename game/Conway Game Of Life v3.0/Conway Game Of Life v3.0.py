import pygame
from copy import deepcopy
from datetime import datetime
from re import sub
from time import time, sleep
from decimal import Decimal

pygame.init()

with open('__init__.txt', 'r', encoding='utf+8') as init:
    _init = eval(init.read())
    length = _init['length']
    width = _init['width']
    EnableBoundary = _init['EnableBoundary']
    FPSLimit = _init['FPSLimit']
if (not EnableBoundary) and length != width:
    raise ValueError('when the boundary is not enabled, the length and width must be the same')
window = pygame.display.set_mode((length * 5, width * 5))
draw = False
drawLock = False


def GetReloadCells(Cells):
    global length, width, EnableBoundary
    reload_cell_list = []
    for X, Y in Cells:
        for I in range(-1, 2):
            for J in range(-1, 2):
                _X = X + I
                _Y = Y + J
                if (0 <= _X < length and 0 <= _Y < width) or (not EnableBoundary):
                    P = [_X % length, _Y % width]
                    if P not in reload_cell_list:
                        reload_cell_list.append(P)
    return reload_cell_list


with open('__path__.txt', 'r', encoding='utf+8') as path:
    with open(path.read(), 'r', encoding='utf+8') as cellList:
        LiveCells = eval(cellList.read())
        ReloadCells = GetReloadCells(LiveCells)
        for cell in LiveCells:
            pygame.draw.rect(window, (255, 255, 255), (cell[0] * 5, cell[1] * 5, 5, 5))

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
        if event.type == pygame.QUIT:
            Quit = True
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True and not drawLock

        if event.type == pygame.MOUSEBUTTONUP:
            draw = False and not drawLock
            oldColorPoint = (-1, -1)

        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_CLEAR, pygame.K_c] and not drawLock:
                LiveCells = []
                ReloadCells = []
                window.fill((0, 0, 0))
            elif event.key == pygame.K_s:
                with open(sub(':', '：', str(datetime.now()))[:-7] + '.txt',
                          'w', encoding='utf+8') as cells:
                    cells.write(str(LiveCells))
            else:
                drawLock = not drawLock

        if not drawLock:
            pygame.display.set_caption('Conway Game Of Life')
            r = 0
        else:
            t1 = time()

            ReloadCells = GetReloadCells(LiveCells)
            nextLiveCells = []
            for x, y in ReloadCells:
                add = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        _x, _y = x + i, y + j
                        if (0 <= _x < length and 0 <= _y < width) or (not EnableBoundary):
                            add += [_x % length, _y % width] in LiveCells
                p = [x, y]
                inLC = p in LiveCells
                if add in [3] + ([4] if inLC else []):
                    nextLiveCells.append(p)
                    pygame.draw.rect(window, (255, 255, 255), (x * 5, y * 5, 5, 5))
                else:
                    pygame.draw.rect(window, (0, 0, 0), (x * 5, y * 5, 5, 5))

            LiveCells = deepcopy(nextLiveCells)
            ReloadCells = GetReloadCells(LiveCells)

            OrdinalSuffix = 'th' if r % 100 // 10 == 1 or r % 10 > 3 or r % 10 == 0 else (
                'st' if r % 10 == 1 else ('nd' if r % 10 == 2 else 'rd'))
            pygame.display.set_caption(f'Conway Game Of Life -- the {str(r) + OrdinalSuffix} generation of life')

            t2 = time()
            sleep((1 / FPSLimit - (t2 - t1)) if 1 / FPSLimit > t2 - t1 else 0)

        ColorPoint = [pygame.mouse.get_pos()[0] // 5, pygame.mouse.get_pos()[1] // 5]
        PointColor = window.get_at(pygame.mouse.get_pos())
        if draw and oldColorPoint != ColorPoint:
            pygame.draw.rect(window, (255 - PointColor[0], 255 - PointColor[1], 255 - PointColor[2]),
                             (ColorPoint[0] * 5, ColorPoint[1] * 5, 5, 5))
            oldColorPoint = deepcopy(ColorPoint)
            LiveCells.append(ColorPoint) if ColorPoint not in LiveCells else LiveCells.remove(ColorPoint)
        r += 1

    pygame.display.flip()

    if Quit:
        break
