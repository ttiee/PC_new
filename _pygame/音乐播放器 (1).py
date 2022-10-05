import threading
import time
#from turtle import color
import pygame
import tkinter as tk
from tkinter import filedialog
import os
import sys
import msvcrt
from mutagen.mp3 import MP3
from tqdm import tqdm
import colorama

def timeshow():
    while True:
        if pygame.mixer.music.get_busy()!=1:
            while True:
                if pygame.mixer.music.get_busy()==1:
                    break
        timelist=[]
        music_long=int(audio.info.length)   #获取音乐长度
        num=0
        while num<=music_long:  #创建列表
            num=num+1
            timelist.append(str(num))
        for i in tqdm(timelist): 
    #print(i)
            time.sleep(1)
            if exit_flag == True:
                return 0
            elif pause_flag == True:
                while pause_flag:
                    time.sleep(0.2)
            elif Probar_restart == True:
                break

            
         
        
'''
def manage():
    print('q=关闭，s=暂停，c=取消暂停')
    while True:
        choice = msvcrt.getch()  #读取按键，返回一字节字符串，b'x'
        if choice==b'q':
            pygame.mixer.music.fadeout(500)   #淡出
            exit_flag=True
            sys.exit(0)   #退出
        elif choice==b's':
            pygame.mixer.music.pause()  #暂停播放
        elif choice==b'c':
            pygame.mixer.music.unpause()  #取消暂停
'''
pygame.init()
colorama.init(autoreset=True)
os.system('cls')
print('音乐播放器v1.0.1')
print('\n请选择音乐文件')
a='1'
while a =='1':
    root = tk.Tk()   # 实例化
    root.withdraw()
        # 获取文件路径
    music_path = filedialog.askopenfilename()
    while music_path=='':
        print('没有检测到文件')
        os.system('pause')
        sys.exit(0)
    print(colorama.Fore.YELLOW+'\n获取的文件地址：', music_path)
    if music_path.endswith('.mp3')==True:
        print(colorama.Fore.GREEN+'格式检测成功，目标为mp3文件')
    elif music_path.endswith('.ogg')==True:
        print(colorama.Fore.GREEN+'格式检测成功，目标为ogg文件')
    else:
        print(colorama.Fore.RED+'检测失败，请检查文件格式是否为ogg或mp3')
        os.system('pause')
        sys.exit(1)
    #track = pygame.mixer.music.load(music_path)
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()
    audio = MP3(music_path)
    print('目标文件长度为'+str(int(audio.info.length)))
    #---------标识
    exit_flag=False   #退出标志
    pause_flag=False   #暂停标志
    Probar_restart=False  #进度条重启标志
    #canpause_flag=False    #取消暂停标志
    #----------
    #t1=threading.Thread(target=manage)  #开启多线程
    #t1.start()
    t2=threading.Thread(target=timeshow)
    t2.start()
    print('q=关闭，s=暂停，c=取消暂停，b=重新开始')
    while True:
        choice = msvcrt.getch()  #读取按键，返回一字节字符串，b'x'
        if choice==b'q':
            pygame.mixer.music.fadeout(10000)   #淡出
            exit_flag=True
            sys.exit(0)   #退出
        elif choice==b's':
            pygame.mixer.music.pause()  #暂停播放
            pause_flag=True
        elif choice==b'c':
            pygame.mixer.music.unpause()  #取消暂停
            pause_flag=False
        elif choice==b'b':
            pygame.mixer.music.rewind()  #重新开始
            Probar_restart=True  #重置进度条
            time.sleep(1)
            Probar_restart=False
    #a = input('按下“1”继续选择文件播放，按其他键退出')

'''
while True:
    if pygame.mixer.music.get_busy() ==1:
        pass
    else:
        break
'''
