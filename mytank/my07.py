import pygame
import time

screen_width = 600
screen_height = 500
BG_COLOR = pygame.Color(255, 255, 0)
T_COLOR = pygame.Color(255, 0, 0)


# 主程序
class MainGame:
    window = None
    my_tank = None

    # 开始游戏
    def start_game(self):
        # 屏幕显示
        pygame.display.init()
        MainGame.window = pygame.display.set_mode(size=[screen_width, screen_height])
        pygame.display.set_caption("坦克大战1.01")
        # 初始化我防坦克
        MainGame.my_tank = MyTank(300, 250)
        while True:
            # 填充背景
            MainGame.window.fill(BG_COLOR)
            # 文字显示
            MainGame.window.blit(self.text('敌方剩余坦克数量：{}'.format(6)), dest=(200, 10))
            # 显示坦克
            MainGame.my_tank.display()
            # 获取事件
            self.get_event()
            # 坦克移动
            MainGame.my_tank.move()
            # 屏幕刷新
            pygame.display.update()
            # 防止屏幕刷新过快
            time.sleep(0.03)

    # 结束游戏
    def end_game(self):
        print('游戏结束，欢迎下次游玩')
        exit()

    # 绘制文字
    def text(self, text):
        pygame.font.init()
        fort = pygame.font.SysFont('华文仿宋', 20)
        textsurface = fort.render(text, False, T_COLOR)
        return textsurface

    def get_event(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                self.end_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    self.end_game()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    MainGame.my_tank.direction = 'L'
                    print('坦克开始向左走')
                    # 开启坦克移动开关
                    MainGame.my_tank.l_stop = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    MainGame.my_tank.direction = 'R'
                    print('坦克开始向右走')
                    # 开启坦克移动开关
                    MainGame.my_tank.r_stop = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    MainGame.my_tank.direction = 'U'
                    print('坦克开始向上走')
                    # 开启坦克移动开关
                    MainGame.my_tank.u_stop = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    MainGame.my_tank.direction = 'D'
                    print('坦克开始向下走')
                    # 开启坦克移动开关
                    MainGame.my_tank.d_stop = False
                elif event.key == pygame.K_SPACE or event.key == pygame.K_j or event.key == pygame.K_KP0:
                    MainGame.my_tank.shot()
                    print('发射子弹')

            # 让坦克停下来
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    print('坦克停止向左走')
                    # 关闭坦克移动开关
                    MainGame.my_tank.l_stop = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print('坦克停止向右走')
                    # 关闭坦克移动开关
                    MainGame.my_tank.r_stop = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    print('坦克停止向上走')
                    # 关闭坦克移动开关
                    MainGame.my_tank.u_stop = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print('坦克停止向下走')
                    # 关闭坦克移动开关
                    MainGame.my_tank.d_stop = True


class Tank:

    def __init__(self, left, right):
        pass

    def shot(self):
        pass

    def display(self):
        pass

    def move(self):
        pass


class MyTank(Tank):

    def __init__(self, left, right):
        self.images = {
            'U': pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif')
        }
        # 方向
        self.direction = 'U'
        # 根据方向选图片
        self.img = self.images[self.direction]
        self.rect = self.img.get_rect()
        self.rect.left = left
        self.rect.top = right
        # 速度
        self.speed = 4
        # 坦克移动开关
        self.l_stop = True
        self.r_stop = True
        self.u_stop = True
        self.d_stop = True

    def shot(self):
        pass

    def display(self):
        self.img = self.images[self.direction]
        MainGame.window.blit(self.img, self.rect)

    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0 and not self.l_stop:
                self.rect.left -= self.speed
        if self.direction == 'R':
            if self.rect.left+self.rect.width < screen_width and not self.r_stop:
                self.rect.left += self.speed
        if self.direction == 'U':
            if self.rect.top > 0 and not self.u_stop:
                self.rect.top -= self.speed
        if self.direction == 'D':
            if self.rect.top+self.rect.height < screen_height and not self.d_stop:
                self.rect.top += self.speed


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
    MainGame().start_game()
