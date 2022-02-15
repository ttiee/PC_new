import pygame

screen_width = 500
screen_height = 300
BG_COLOR = pygame.Color(250, 250, 0)


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
            self.getEvent()

    # 结束游戏
    def end(self):
        print('游戏结束，欢迎下次游玩')
        exit()

    def getEvent(self):
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == pygame.QUIT:
                self.end()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP0:
                    self.end()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    print('坦克开始向左走')
                    MyTank().move()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print('坦克开始向右走')
                    MyTank().move()
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    print('坦克开始向上走')
                    MyTank().move()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print('坦克开始向下走')
                    MyTank().move()


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
