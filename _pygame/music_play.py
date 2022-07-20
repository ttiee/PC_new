"""导入所需要的模块"""
import pygame, sys, re, time

from pygame.locals import *

import os

"""初始化数据"""
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('SimHei', 20)
# 设置屏幕
screen = pygame.display.set_mode((484, 710))
screen.fill((0, 0, 0))
pygame.display.set_caption("简陋的播放器")

"""创建歌词解析类"""


class LyricParse:
    def __init__(self, path):
        self.path = path  # 歌词文件路径
        self.lyrics = []  # 歌词列表，保存歌词对象

    # 加载文件
    def load(self):
        if os.path.exists(self.path):
            with open(self.path, encoding='utf-8') as fp:
                data = fp.readlines()
                # 去掉每一句后的换行符，和去掉换行符后的空行
                return [value.strip() for value in data if value.strip()]
        return False  # 如果返回False文件不存在

    def parse(self):
        data = self.load()
        lyrics = []
        if data:  # 数据存在
            for i in range(len(data) - 1, -1, -1):
                tmp = data[i].split(']')
                tmp = [value for value in tmp if value]
                if len(tmp) < 2:
                    data.pop(i)
                else:
                    data[i] = data[i].replace("[", '')
            # 解析
            for line in data:
                line = line.split(']')
                for item in line[:-1]:
                    # 把时间字符串分割成列表，并把列表元素转换为浮点数
                    second = [float(value) for value in re.split(r':|\.', item)]
                    second = second[0] * 60 + second[1] + second[2] / 100
                    # obj = Lyric(second,line[-1]) #生成歌词对象，line[-1]是歌词
                    lyrics.append([second, line[-1]])  # 添加到歌词列表
                # 排序
                lyrics.sort()
            return lyrics


def select_songs():
    # 从指定路径筛选音乐文件
    def collect_songs(fidir):
        # 建立备选列表
        musics = []
        # 遍历文件路径
        for root, dirs, files in os.walk(fidir):
            for file in files:
                tmp = []
                if file.endswith('mp3') or file.endswith('wav'):
                    # if file.endswith('mp3'):
                    file = os.path.join(root, file)
                    tmp.append(file)
                    musics.append(tmp)
        return musics

    # 指定筛选路径
    musics = collect_songs(r'D:\WorkSpace\PC\_pygame')
    # print(musics,musics[0],musics[0][0])
    return musics


def select_lyrics():
    # 从指定路径筛选歌词文件
    def collect_songs(fidir):
        # 建立备选列表
        lyrics = []
        # 遍历文件路径
        for root, dirs, files in os.walk(fidir):
            for file in files:
                tmp = []
                if file.endswith('txt'):
                    file = os.path.join(root, file)
                    tmp.append(file)
                    lyrics.append(tmp)
        return lyrics

    # 指定筛选路径
    lyrics = collect_songs(r'D:\WorkSpace\PC\_pygame')
    # print(lyrics, lyrics[0], lyrics[0][0])
    return lyrics


"""歌词匹配"""


def match_songs(musics, lyrics, judge):
    # print(musics[0][0])
    str_music = re.split(r'\\|\.', musics[i_music][0])[-2]
    print(str_music)
    str_lyric = re.split(r'\\|\.', lyrics[0][0])[-2]
    # print(str_lyric)
    f_name = re.split(r'\\|\.', musics[i_music][0])[-2]
    f_name = font.render("正在播放歌曲：" + f_name, 1, (250, 250, 249))
    screen.blit(f_name, [screen.get_width() / 2 - f_name.get_width() / 2, 280])
    if str_lyric == str_music:
        print("匹配成功")
        judge = True
    else:
        # print("匹配失败")
        judge = False
    return judge


def last_song(i_music):
    # pygame.mixer.music.pause()
    if i_music >= 0:
        pass
    else:
        i_music = -1
    pygame.mixer.music.load(str(select_songs()[i_music][0]))
    pygame.mixer.music.play(1)
    return i_music


"""播放下一首歌"""


def next_song(i_music, music_length):
    if i_music < music_length:
        pass
    else:
        i_music = 0
    pygame.mixer.music.load(str(select_songs()[i_music][0]))
    pygame.mixer.music.play(1)
    return i_music


def volume_music(volume):
    # 调节音量
    pygame.mixer.music.set_volume(volume)
    v = int(volume)


"""快进"""


def up_speed():
    speed_times = int(pygame.mixer.music.get_pos() / 1000 + 1)
    pygame.mixer.music.pause()
    pygame.mixer.music.play(start=speed_times)


"""快退"""


def down_speed():
    down_times = int(pygame.mixer.music.get_pos() / 1000 - 1)
    pygame.mixer.music.pause()
    pygame.mixer.music.play(start=down_times)


def pause_music():
    """暂停音乐"""
    pygame.mixer.music.pause()
    pause = True


def draw_kongjian(pause):
    # 画进度条
    length_music = pygame.mixer.music.get_pos()
    length_music_act = int(length_music) / 500
    # 画一条宽度为2的线，y高度为149，x从40到600,颜色为(0,100,100)
    pygame.draw.line(screen, (0, 100, 100), (0, 260), (length_music_act, 260), 6)
    # 画播放、暂停按钮
    # 先画圆边框，半径20
    pygame.draw.circle(screen, (36, 86, 239), (240, 60), 50, 10)
    # 画三角形，开始播放
    pygame.draw.line(screen, (36, 86, 239), (230, 90), (230, 30), 10)  # 竖线
    # 如果正在播放且没有暂停
    if pause:
        # 显示第二条竖线
        pygame.draw.line(screen, (36, 86, 239), (230, 90), (270, 60), 10)
        pygame.draw.line(screen, (36, 86, 239), (230, 30), (270, 60), 10)
    if pause == False:
        # 显示三角形
        pygame.draw.line(screen, (36, 86, 239), (250, 90), (250, 30), 10)
    # 画上一首按钮
    pygame.draw.line(screen, (36, 86, 239), (160, 90), (160, 30), 10)
    pygame.draw.line(screen, (36, 86, 239), (140, 80), (140, 40), 10)
    pygame.draw.line(screen, (36, 86, 239), (160, 90), (140, 60), 10)
    pygame.draw.line(screen, (36, 86, 239), (160, 30), (140, 60), 10)

    # 画下一首按钮
    pygame.draw.line(screen, (36, 86, 239), (320, 30), (320, 90), 10)
    pygame.draw.line(screen, (36, 86, 239), (340, 80), (340, 40), 10)
    pygame.draw.line(screen, (36, 86, 239), (320, 90), (340, 60), 10)
    pygame.draw.line(screen, (36, 86, 239), (320, 30), (340, 60), 10)


"""弹出歌词"""


def blit_lyric(lp, pause, judge):  # 参数为实体化歌词对象、是否暂停
    time_music = pygame.mixer.music.get_pos()  # 获取音乐播放的位置
    if pause == False:
        # 歌词解析 获取列表
        if judge == True:
            list_lp = lp.parse()
            # 遍历歌词查找歌词对应弹出位置
            for j in range(len(list_lp)):
                if int(time_music / 1000) == int(list_lp[j][0]):
                    # a = int(i // 6)
                    f_word = str(list_lp[j][1])
                    f = font.render(f_word, 1, (248, 216, 129))  # 设置歌词字体
                    if pause == False:
                        screen.blit(f, [screen.get_width() / 2 - f.get_width() / 2, 320])
                    elif pause == True:
                        pass
        else:
            f = font.render('没有找到对应歌词，请将txt歌词放在对应文件夹内', 1, (242, 3, 36))
            screen.blit(f, [screen.get_width() / 2 - f.get_width() / 2, 320])
    else:
        pass


"""制作旋转cd"""


def blit_cd(pause):
    suf = pygame.draw.circle(screen, (31, 58, 77), (242, 550), 150, 60)
    cd = pygame.image.load("wangfei.png")
    if pause == False:
        rotated_image = pygame.transform.rotate(cd, -i)
        new_rect = rotated_image.get_rect(center=(242, 550))
        screen.blit(rotated_image, new_rect.topleft)
    if pause == True:
        rotated_image = pygame.transform.rotate(cd, 0)
        new_rect = rotated_image.get_rect(center=(242, 550))
        screen.blit(rotated_image, new_rect.topleft)


"""显示当前本地时间"""


def blit_time():
    c = time.time()
    l = time.localtime(c)
    s = time.strftime("%Y-%m-%d %H:%M:%S", l)
    f_time = font.render(s, 1, (255, 140, 28))
    screen.blit(f_time, [0, 0])


"""主函数"""


def main():
    # 设置歌曲播放计数器
    global i_music
    i_music = 0
    musics = select_songs()
    lyrics = select_lyrics()
    music_length = len(musics)
    select_lyrics()
    """导入歌曲"""
    # 按当前计数器对应文件路径导入歌曲
    pygame.mixer.music.load(str(musics[i_music][0]))
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    lp = LyricParse(str(lyrics[i_music][0]))
    # print(lp.parse())
    global i
    global pause
    running = True
    pause = False
    i = 0
    list_lp = lp.parse()
    # print([value for elem in list_lp for value in elem])
    volume = pygame.mixer.music.get_volume()
    f2 = font.render("音量：" + str(100 * volume), 1, (242, 3, 18))
    global judge
    judge = True
    """while循环"""
    while running:
        # 第一步画背景
        screen.fill((0, 0, 0))  # ----------------新添加
        # 第二步添加背景图片
        background = pygame.image.load("music_ground.png")  # 加载背景图片
        screen.blit(background, (0, 0))
        clock.tick(1)
        screen.fill((255, 255, 255))  # 填充颜色
        screen.blit(background, (0, 0))  # 填入到背景
        # 显示本地时间
        blit_time()
        # 获取鼠标事件并作出反应
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # 按上键加音量
                    volume1 = pygame.mixer.music.get_volume() + 0.01
                    volume_music(volume1)
                if event.key == pygame.K_DOWN:  # 按下键减音量
                    volume = pygame.mixer.music.get_volume() - 0.01
                    volume_music(volume)
                if event.key == pygame.K_TAB:  # 按tab键暂停
                    pygame.mixer.music.pause()
                    pause = True
                if event.key == pygame.K_u:  # 按u键快进
                    up_speed()
                if event.key == pygame.K_d:  # 按d快退
                    down_speed()
                if event.key == pygame.K_l:  # 按l选择上一首
                    i_music -= 1
                    i_music = last_song(i_music)
                if event.key == pygame.K_n:  # 按n选择下一首
                    i_music += 1
                    i_music = next_song(i_music, music_length)
                if event.key == pygame.K_o:  # 按o开始
                    pygame.mixer.music.unpause()
                    pause = False

        # 弹出音量及显示条
        volume = pygame.mixer.music.get_volume()
        f2 = font.render("音量：" + str(int(100 * volume)), 1, (242, 3, 18))
        # screen.blit(f2, [screen.get_width() / 2 - f2.get_width() / 2, 260])
        screen.blit(f2, [360, 180])
        pygame.draw.line(screen, (222, 198, 225), (460, 200), (460, 200 - 180 * volume), 16)
        i = (i + 1)
        if match_songs(musics, lyrics, i_music):
            blit_lyric(lp, pause, judge)
            clock.tick(8)
        else:
            f = font.render('没有找到对应歌词，请将txt歌词放在对应文件夹内', 1, (242, 3, 36))
            screen.blit(f, [screen.get_width() / 2 - f.get_width() / 2, 320])
        blit_cd(pause)
        # 显示控件
        draw_kongjian(pause)
        f2 = font.render("歌曲进度", 1, (242, 3, 18))
        screen.blit(f2, [0, 230])
        pygame.display.flip()


if __name__ == '__main__':
    main()
