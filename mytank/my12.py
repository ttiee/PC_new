import pygame
import time
import random

screen_width = 700
screen_height = 600
BG_COLOR = pygame.Color(255, 255, 0)
T_COLOR = pygame.Color(255, 0, 0)


# 主程序
class MainGame:
    window = None
    my_tank = None
    # 存储敌方坦克的列表
    enemy_list = []
    # 子弹列表
    bullet_list = []
    # 敌方坦克数量
    enemy_num = 5
    # 存储子弹
    my_bullet = []
    enemy_bullet = []

    # 开始游戏
    def start_game(self):
        # 屏幕显示
        pygame.display.init()
        MainGame.window = pygame.display.set_mode(size=[screen_width, screen_height])
        pygame.display.set_caption("坦克大战1.01")
        # 初始化我方坦克
        MainGame.my_tank = MyTank(300, 250)
        # 初始化敌方坦克
        self.create_enemy_tank()
        while True:
            # 填充背景
            MainGame.window.fill(BG_COLOR)
            # 文字显示
            MainGame.window.blit(self.text('敌方剩余坦克数量：{}'.format(len(MainGame.enemy_list))), dest=(200, 10))
            # 显示坦克
            MainGame.my_tank.display()
            self.blit_enemy_tank()
            # 显示子弹
            self.blit_bullet()
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

    # 判断事件
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

    # 初始化敌方坦克，并加到敌方列表中
    def create_enemy_tank(self):
        right = 100
        for i in range(MainGame.enemy_num):
            left = random.randint(50, 550)
            enemy = EnemyTank(left, right)
            MainGame.enemy_list.append(enemy)

    # 显示敌方坦克
    def blit_enemy_tank(self):
        for enemy in MainGame.enemy_list:
            enemy.display()
            # 随机移动
            enemy.rand_move()
            # 随机发射子弹
            enemy.rand_shot()

    def blit_bullet(self):
        for bullet in MainGame.my_bullet:
            bullet.display()
            # 子弹移动
            bullet.move(MainGame.my_bullet)
        for bullet in MainGame.enemy_bullet:
            bullet.display()
            # 子弹移动
            bullet.move(MainGame.enemy_bullet)


class Tank:

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
        self.speed = 3
        # 坦克移动开关
        self.l_stop = True
        self.r_stop = True
        self.u_stop = True
        self.d_stop = True

    def shot(self):
        bullet = Bullet(self)
        MainGame.bullet_list.append(bullet)

    def display(self):
        self.img = self.images[self.direction]
        MainGame.window.blit(self.img, self.rect)

    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0 and not self.l_stop:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < screen_width and not self.r_stop:
                self.rect.left += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0 and not self.u_stop:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < screen_height and not self.d_stop:
                self.rect.top += self.speed


class MyTank(Tank):

    def shot(self):
        if len(MainGame.my_bullet) < 3:
            bullet = My_Bullet(self)
            MainGame.my_bullet.append(bullet)


class EnemyTank(Tank):

    def __init__(self, left, right):
        super().__init__(left, right)
        self.images = {
            'U': pygame.image.load('img/enemy1U.gif'),
            'D': pygame.image.load('img/enemy1D.gif'),
            'L': pygame.image.load('img/enemy1L.gif'),
            'R': pygame.image.load('img/enemy1R.gif')
        }
        # 随机方向
        self.direction = self.rand_direction()
        # 移动开关打开
        self.l_stop = False
        self.r_stop = False
        self.u_stop = False
        self.d_stop = False
        # 随机速度
        self.speed = random.randint(1, 5)
        # 记录步数
        self.step = random.randint(80, 150)
        # 随机发射子弹
        self.shot_time = random.randint(10, 50)

    def rand_direction(self):
        direction = random.randint(1, 4)
        if direction == 1:
            return 'U'
        elif direction == 2:
            return 'D'
        elif direction == 3:
            return 'L'
        elif direction == 4:
            return 'R'

    def rand_move(self):
        if self.step <= 0:
            self.direction = self.rand_direction()
            self.step = random.randint(80, 150)
            self.speed = random.randint(1, 5)
        else:
            self.move()
            self.step -= 1

    def rand_shot(self):
        if self.shot_time <= 0:
            self.shot()
            self.shot_time = random.randint(10, 50)
        else:
            self.shot_time -= 1

    def shot(self):
        bullet = Enemy_Bullet(self)
        MainGame.enemy_bullet.append(bullet)


class Wall:

    def __init__(self):
        pass

    def display(self):
        pass


class Bullet:

    def __init__(self, tank):
        self.image = pygame.image.load('img/enemy-missile.gif')
        self.direction = tank.direction
        self.rect = self.image.get_rect()
        self.select_position(tank)
        self.speed = 6

    def select_position(self, tank):
        if tank.direction == 'U':
            self.rect.left = tank.rect.left + (tank.rect.width - self.rect.width)/2
            self.rect.top = tank.rect.top - self.rect.height
        elif tank.direction == 'D':
            self.rect.left = tank.rect.left + (tank.rect.width - self.rect.width)/2
            self.rect.top = tank.rect.top + tank.rect.height + self.rect.height
        elif tank.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width
            self.rect.top = tank.rect.top + (tank.rect.height - self.rect.height)/2
        elif tank.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width - self.rect.width
            self.rect.top = tank.rect.top + (tank.rect.height - self.rect.height) / 2

    def display(self):
        MainGame.window.blit(self.image, self.rect)

    def move(self, list):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                list.remove(self)
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < screen_width:
                self.rect.left += self.speed
            else:
                list.remove(self)
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                list.remove(self)
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < screen_height:
                self.rect.top += self.speed
            else:
                list.remove(self)


class My_Bullet(Bullet):
    pass


class Enemy_Bullet(Bullet):
    pass


class Music:

    def play(self):
        pass


if __name__ == '__main__':
    MainGame().start_game()
