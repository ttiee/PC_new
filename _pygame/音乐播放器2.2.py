import os
import sys
import pygame
from rich import print


class Music:
    __instance = None

    # 单例实例对象
    def __new__(cls, *args, **kwargs):
        if Music.__instance is None:
            bb1 = object.__new__(cls)
            Music.__instance = bb1

        return Music.__instance

    def __init__(self, file):
        self.filename = file
        # 加载音乐
        pygame.mixer.music.load(self.filename)

    # 获得音乐名
    @classmethod
    def get_filename(cls):
        if cls.__instance is not None:
            return cls.__instance.filename
        else:
            return None

    # 播放音乐
    @staticmethod
    def display(loops=1):
        pygame.mixer.music.play(loops=loops)

    # 暂停和取消暂停
    @staticmethod
    def pause():
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            Music.unpause()

    # 取消暂停
    @staticmethod
    def unpause():
        pygame.mixer.music.unpause()

    # 重新播放
    @staticmethod
    def rewind():
        pygame.mixer.music.rewind()

    # 停止（没啥用）
    @staticmethod
    def stop():
        pygame.mixer.music.stop()

    # 获得音量
    @staticmethod
    def get_volume():
        return pygame.mixer.music.get_volume()

    # 设置音量（范围0~1）
    @staticmethod
    def set_volume(num):
        pygame.mixer.music.set_volume(num)

    # 获得是否正在播放音乐
    @staticmethod
    def get_busy() -> bool:
        return pygame.mixer.music.get_busy()


class MainMusicPlayer:
    __instance = None

    music = None

    color_num = 'bold'    # 音乐序号颜色
    color_music_name = 'normal'    # 音乐颜色
    color_quit = 'red'    # 退出颜色
    color_events = '#FFFAFA'   # 指令颜色
    volume = 100   # 记录音量

    play_methods = 0   # 0普通播放 1单曲循环 2随机播放
    loops = 1  # 音乐循环次数，0为单曲循环

    # 单例实例对象
    def __new__(cls, *args, **kwargs):
        if MainMusicPlayer.__instance is None:
            MainMusicPlayer.__instance = object.__new__(cls)
        return MainMusicPlayer.__instance

    # 播放
    def play(self):
        if self.loops == 0:
            if not Music.get_busy():
                Music.display(loops=self.loops)
        elif self.loops == 1:
            if not Music.get_busy():
                Music.display(loops=self.loops)

    def set_volume(self):
        volume = input('请输入0~100的数：')
        try:
            Music.set_volume(num=float(volume) / 100)
            self.volume = int(volume)
            print('调节成功')
            # print(id(self.volume))
            # print(id(MainMusicPlayer.__instance))# 实例id
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('请输入合适的数！')
            return self.set_volume()

    @staticmethod
    def prepare():
        pygame.mixer.init()

        files_name = os.listdir('.')
        musics_name = [file for file in files_name if
                       os.path.splitext(file)[1] == '.mp3' or os.path.splitext(file)[1] == '.wav']

        music_dic = {i + 1: music_name_ for i, music_name_ in enumerate(musics_name)}

        return music_dic

    def choose(self, music_dic, color_num='bold', color_music_name='normal', color_quit='red', color_events='#FFFAFA'):

        str_key = '[{0}]{1}[/{0}]'
        str_music_name = '[{0}]{1}[/{0}]'
        str_quit = f'\n[{color_quit}]0\t退出[/{color_quit}]'
        str_events = f'[{color_events}]\np\t暂停\nr\t重新播放\nv\t调节音量[/{color_events}]'

        print()
        for key, music in music_dic.items():
            print(str_key.format(color_num, key) + '\t' + str_music_name.format(color_music_name, music))
        print(str_quit + str_events)

        # print(id(self.volume))
        # print(id(MainMusicPlayer.__instance))
        print(f'当前音量为：{self.volume}\t当前音乐为：{self.music}')

        order = input('\n请输入数字或字母：')
        os.system('cls' if os.name == 'nt' else 'clear')

        return order

    def play_events(self, music_dic):
        # self.music = Music.get_filename()    # 取消注释可以正常显示音乐名
        # self.volume = int(Music.get_volume() * 100)   # 取消注释可以正常显示音量

        order = self.choose(
            music_dic=music_dic,
            color_num=self.color_num,
            color_music_name=self.color_music_name,
            color_events=self.color_events,
            color_quit=self.color_quit
        )

        if order == '0':
            print('\n退出成功')
            sys.exit()
        elif order == 'p' or order == 'P':
            Music.pause()
        elif order == 'r' or order == 'R':
            Music.rewind()
        elif order == 'v' or order == 'V':
            self.set_volume()
        else:
            try:
                order = int(order)
                print(f'选定的音乐为\t{music_dic[order]}')
                music_path = music_dic[order]
                if os.path.exists(music_path):
                    print(f'找到了{os.path.basename(os.path.splitext(music_path)[0])}')
                    bb1 = Music(music_path)
                    bb1.filename = music_path

                    self.music = music_dic[order]
                else:
                    print('没有找到该音乐')
                    raise ConnectionError

            except ConnectionError:
                del music_dic[order]
                print('该音乐已被删除')
            except KeyError:
                print('\n没有该音乐')
            except ValueError:
                print('请输入适当的指令！')
            try:
                self.play()
            except pygame.error:
                print('还没点音乐呢！')

    @staticmethod
    def main_play():

        while True:
            music_dic = MainMusicPlayer.prepare()
            if not music_dic:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n当前文件夹没有音乐呢！')
                answer = input('准备好音乐后请输入任意字符确认(或输入q退出)：')
                if answer == 'q' or answer == 'Q':
                    sys.exit()
                return MainMusicPlayer.main_play()

            # bb1 = Music(music_dic[1])
            # self.volume = bb1.get_volume()
            MainMusicPlayer().play_events(music_dic=music_dic)


if __name__ == '__main__':
    MainMusicPlayer().main_play()
