import pygame

screen_width = 500
screen_height = 300
BG_COLOR = pygame.Color(250, 0, 0)


# 主程序
class MainGame:
    window = None

    # 开始游戏
    def start(self):
        pygame.display.init()
        MainGame.window = pygame.display.set_mode(size=[screen_width, screen_height])
        pygame.display.set_caption("坦克大战1.01")
        MainGame.window.fill(BG_COLOR)
        while True:
            pygame.display.update()

    # 结束游戏
    def end(self):
        pass


class Tank:

    def __init__(self):
        pass

    def shot(self):
        pass

    def display(self):
        pass

    def move(self):
        pass


class MyTank(Tank):

    def shot(self):
        pass

    def display(self):
        pass

    def move(self):
        pass


class ETank(Tank):

    def shot(self):
        pass

    def display(self):
        pass

    def move(self):
        pass


class Wall:

    def __init__(self):
        pass

    def display(self):
        pass


class B:

    def display(self):
        pass


class MyB:
    pass


class EB:
    pass


class Music:

    def play(self):
        pass


class Photo():

    def display(self):
        pass


if __name__ == '__main__':
    MainGame().start()
