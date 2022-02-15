'''
坦克大战游戏的需求
1.项目中有哪些类
2.每个类中有哪些方法

1.坦克类（我方坦克、敌方坦克）
  射击
  移动类
  显示坦克的方法
2.子弹类
   移动
   显示子弹的方法
3.墙壁类
   属性：是否可以通过
4.爆炸效果类
  展示爆炸效果
5.音效类
  播放音乐
6.主类
  开始游戏
  结束游戏
'''
class MainGame():
    def __init__(self):
        pass
    #开始游戏
    def startGame(self):
        pass
    #结束游戏
    def endGame(self):
        pass

class Tank():
    def __init__(self):
        pass
    #移动
    def move(self):
        pass

    #射击
    def shot(self):
        pass
    #展示坦克的方法
    def displayTank(self):
        pass
#我方坦克
class MyTank(Tank):
    def __init__(self):
        pass

#敌方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass

#子弹类
class Bullet():
    def __init__(self):
        pass
    #移动
    def move(self):
        pass
    #展示子弹的方法
    def displayBullet(self):
        pass
class Wall():
    def __init__(self):
        pass
    #展示墙壁的方法
    def displayWall(self):
        pass
class Explode():
    def __init__(self):
        pass
    #展示爆炸效果的方法
    def displayExplode(self):
        pass
class Music():
    def __init__(self):
        pass
    #播放音乐
    def play(self):
        pass
