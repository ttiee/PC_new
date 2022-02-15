import pygame
import time
import random

from pygame.sprite import Sprite

screen_width = 600
screen_height = 600
BG_COLOR = pygame.Color(255, 255, 0)
T_COLOR = pygame.Color(255, 0, 0)


class BaseItem(Sprite):
    pass


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
    # 存储墙
    wall_list = []
    # 储存爆炸
    blast_list = []
    # 分数
    score = 0
    # 计时器
    my_time = 30

    # 开始游戏
    def start_game(self):
        # 屏幕显示
        pygame.display.init()
        MainGame.window = pygame.display.set_mode(size=[screen_width, screen_height])
        pygame.display.set_caption("坦克大战1.01")
        # 初始化我方坦克
        MainGame.my_tank = MyTank(screen_width/2, screen_height/2)
        # 初始化敌方坦克
        self.create_enemy_tank()
        # 初始化墙壁
        self.creat_wall()
        while True:
            # 填充背景
            MainGame.window.fill(BG_COLOR)
            # 显示墙壁
            self.blit_wall()
            # 显示坦克
            if MainGame.my_tank:
                MainGame.my_tank.display()
            self.blit_enemy_tank()
            # 显示子弹
            self.blit_bullet()
            # 显示爆炸
            self.blit_blast()
            # 文字显示
            MainGame.window.blit(self.text('敌方剩余坦克数量：{0}'.format(len(MainGame.enemy_list)) + ' '*80 + '分数：{0}'.format(MainGame.score)), dest=(10, 10))
            # 获取事件
            self.get_event()
            # 坦克移动
            if MainGame.my_tank:
                MainGame.my_tank.move()
            # 屏幕刷新
            pygame.display.update()
            # 击败坦克
            self.hit_enemy()
            self.hit_me()
            # 重新生成坦克
            if len(MainGame.enemy_list) == 0:
                MainGame().create_enemy_tank()
            if not MainGame.my_tank:
                self.creat_mytank()
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
            if MainGame.my_tank:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        self.end_game()
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        MainGame.my_tank.direction = 'L'
                        print('坦克开始向左走')
                        # 开启坦克移动开关
                        MainGame.my_tank.l_stop = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        MainGame.my_tank.direction = 'R'
                        print('坦克开始向右走')
                        # 开启坦克移动开关
                        MainGame.my_tank.r_stop = False
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        MainGame.my_tank.direction = 'U'
                        print('坦克开始向上走')
                        # 开启坦克移动开关
                        MainGame.my_tank.u_stop = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        MainGame.my_tank.direction = 'D'
                        print('坦克开始向下走')
                        # 开启坦克移动开关
                        MainGame.my_tank.d_stop = False
                    if event.key == pygame.K_SPACE or event.key == pygame.K_j or event.key == pygame.K_KP0:
                        MainGame.my_tank.shot()
                        print('发射子弹')

                # 让坦克停下来
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        print('坦克停止向左走')
                        # 关闭坦克移动开关
                        MainGame.my_tank.l_stop = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        print('坦克停止向右走')
                        # 关闭坦克移动开关
                        MainGame.my_tank.r_stop = True
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        print('坦克停止向上走')
                        # 关闭坦克移动开关
                        MainGame.my_tank.u_stop = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        print('坦克停止向下走')
                        # 关闭坦克移动开关
                        MainGame.my_tank.d_stop = True

    # 初始化敌方坦克，并加到敌方列表中
    def create_enemy_tank(self):
        right = 100
        for i in range(MainGame.enemy_num):
            # 第一个为规格生成，但只能生成5个 ； 第二个为随机生成，个数不限
            # a = i*screen_width/MainGame.enemy_num
            a = random.randint(0, screen_width - 60)
            enemy = EnemyTank(a, right)
            MainGame.enemy_list.append(enemy)

    # 显示敌方坦克
    def blit_enemy_tank(self):
        for enemy in MainGame.enemy_list:
            enemy.display()
            # 随机移动
            enemy.rand_move()
            # 随机发射子弹
            enemy.rand_shot()

    # 显示子弹
    def blit_bullet(self):
        for bullet in MainGame.my_bullet:
            if bullet.live:
                bullet.display()
                # 子弹移动
                bullet.move()
            else:
                MainGame.my_bullet.remove(bullet)
        for bullet in MainGame.enemy_bullet:
            if bullet.live:
                bullet.display()
                # 子弹移动
                bullet.move()
            else:
                MainGame.enemy_bullet.remove(bullet)

    # 显示爆炸
    def blit_blast(self):
        for blast in MainGame.blast_list:
            if blast.live:
                blast.display()
            else:
                MainGame.blast_list.remove(blast)

    # 击败敌方坦克
    def hit_enemy(self):
        for bullet in MainGame.my_bullet:
            bullet.hit()

    # 击败我方坦克
    def hit_me(self):
        for bullet in MainGame.enemy_bullet:
            bullet.hit()

    # 生成我方坦克
    def creat_mytank(self):
        if MainGame.my_time == 0:
            MainGame.my_tank = MyTank(screen_width/2, screen_height/2)
            MainGame.my_time = 20
        else:
            MainGame.my_time -= 1

    # 生成墙壁
    def creat_wall(self):
        wall = Wall(0, 0)
        MainGame.wall_list.append(wall)
        wall = Wall(0, screen_height - wall.rect.height)
        MainGame.wall_list.append(wall)
        wall = Wall(screen_width - wall.rect.width, 0)
        MainGame.wall_list.append(wall)
        wall = Wall(screen_width - wall.rect.width, screen_height - wall.rect.height)
        MainGame.wall_list.append(wall)
        for i in range(10):
            wall = Wall(i*60, screen_height/2 - wall.rect.height)
            MainGame.wall_list.append(wall)

    # 显示墙壁
    def blit_wall(self):
         for wall in MainGame.wall_list:
             wall.wall_bullet()
             if wall.hp > 0:
                if wall.live:
                    wall.display()
                else:
                    MainGame.wall_list.remove(wall)
             else:
                MainGame.wall_list.remove(wall)


class Tank(BaseItem):

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
        # 生存状态
        self.live = True
        self.old_left = self.rect.left
        self.old_top = self.rect.top

    def shot(self):
        bullet = Bullet(self)
        MainGame.bullet_list.append(bullet)

    def display(self):
        self.img = self.images[self.direction]
        MainGame.window.blit(self.img, self.rect)

    def move(self):
        self.old_left = self.rect.left
        self.old_top = self.rect.top
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

    def hit_wall(self):
        for wall in MainGame.wall_list:
            if pygame.sprite.collide_rect(self, wall):
                self.stay()

    def hit_tank(self):
        # 敌方与敌方的碰撞
        # for tank in MainGame.enemy_list:
        #     if tank == self:
        #         pass
        #     elif pygame.sprite.collide_rect(self, tank):
        #         self.stay()
        if self.live:
            if MainGame.my_tank == self:
                for tank in MainGame.enemy_list:
                    if pygame.sprite.collide_rect(self, tank):
                        self.stay()
        if self == MainGame.my_tank or not MainGame.my_tank:
            pass
        elif pygame.sprite.collide_rect(self, MainGame.my_tank):
            self.stay()

    def stay(self):
        self.rect.left = self.old_left
        self.rect.top = self.old_top


class MyTank(Tank):

    def shot(self):
        if len(MainGame.my_bullet) < 10:
            bullet = My_Bullet(self)
            MainGame.my_bullet.append(bullet)
    
    def move(self):
        if not self.l_stop:
            self.direction = 'L'
        if not self.r_stop:
            self.direction = 'R'
        if not self.u_stop:
            self.direction = 'U'
        if not self.d_stop:
            self.direction = 'D'
        super(MyTank, self).move()
        self.hit_wall()
        self.hit_tank()


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
        self.speed = random.randint(1, 6)
        # 记录步数
        self.step = random.randint(10, 120)
        # 随机发射子弹
        self.shot_time = random.randint(5, 50)

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
        if self.live:
            if self.step <= 0:
                self.direction = self.rand_direction()
                self.step = random.randint(10, 120)
                self.speed = random.randint(0, 7)
            else:
                self.move()
                self.step -= 1
                self.hit_wall()
                self.hit_tank()
        else:
            MainGame.enemy_list.remove(self)

    def rand_shot(self):
        if self.shot_time <= 0:
            self.shot()
            self.shot_time = random.randint(5, 50)
        else:
            self.shot_time -= 1

    def shot(self):
        bullet = Enemy_Bullet(self)
        MainGame.enemy_bullet.append(bullet)


class Wall(BaseItem):

    def __init__(self, left, right):
        self.image = pygame.image.load('img/steels.gif')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = right
        self.live = True
        self.hp = 3

    def display(self):
        MainGame.window.blit(self.image, self.rect)

    def wall_bullet(self):
        for bullet in MainGame.enemy_bullet:
            if pygame.sprite.collide_rect(self, bullet):
                self.hp -= 1
                MainGame.enemy_bullet.remove(bullet)
        for bullet in MainGame.my_bullet:
            if pygame.sprite.collide_rect(self, bullet):
                self.hp -= 1
                MainGame.my_bullet.remove(bullet)


class Bullet(BaseItem):

    def __init__(self, tank):
        self.image = pygame.image.load('img/enemy-missile.gif')
        self.direction = tank.direction
        self.rect = self.image.get_rect()
        self.select_position(tank)
        self.speed = 8
        self.live = True

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

    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < screen_width:
                self.rect.left += self.speed
            else:
                self.live = False
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < screen_height:
                self.rect.top += self.speed
            else:
                self.live = False


class My_Bullet(Bullet):

    def hit(self):
        for enemy in MainGame.enemy_list:
            if pygame.sprite.collide_rect(self, enemy):
                enemy.live = False
                blast = Explode(enemy)
                MainGame.blast_list.append(blast)
                if self in MainGame.my_bullet:
                    self.live = False
                MainGame.score += 1


class Enemy_Bullet(Bullet):

    def hit(self):
        if MainGame.my_tank:
            if pygame.sprite.collide_rect(self, MainGame.my_tank):
                # MainGame().end_game()
                print('你死亡了，请重新开始')
                if self in MainGame.enemy_bullet:
                    self.live = False
                blast = Explode(MainGame.my_tank)
                MainGame.blast_list.append(blast)
                MainGame.my_tank.live = False
                MainGame.my_tank = None
        # 敌方坦克子弹射到敌方坦克
        # for tank in MainGame.enemy_list:
        #     if pygame.sprite.collide_rect(self, tank):
        #         self.live = False


class Music:

    def display(self):
        pass


class Explode:

    def __init__(self, tank):
        self.images = [
            pygame.image.load('img/blast0.gif'),
            pygame.image.load('img/blast1.gif'),
            pygame.image.load('img/blast2.gif'),
            pygame.image.load('img/blast3.gif'),
            pygame.image.load('img/blast4.gif')
        ]
        self.step = 0
        self.img = self.images[self.step]
        self.rect = tank.rect
        # self.rect.left -= 36
        # self.rect.top -= 24
        self.live = True

    def display(self):
        if self.step < 5:
            self.img = self.images[self.step]
            MainGame.window.blit(self.img, self.rect)
            self.step += 1
        else:
            self.step = 0
            self.live = False


def main():
    MainGame().start_game()


if __name__ == '__main__':
    main()
