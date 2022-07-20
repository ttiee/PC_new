from rich import print
import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'}


def get_music_name(__song):
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(__song)
    driver = webdriver.Chrome()
    driver.set_window_rect(0, 0, 0, 0)
    driver.get(url=url)
    driver.switch_to.frame('g_iframe')

    a = driver.find_element(By.CLASS_NAME, "text").find_element(By.TAG_NAME, 'a').get_attribute('href')
    b = driver.find_element(By.CLASS_NAME, "text").find_element(By.TAG_NAME, 'a').find_element(By.TAG_NAME,
                                                                                               'b').get_attribute(
        'title')
    au = driver.find_elements(By.CLASS_NAME, 'text')[1].find_element(By.TAG_NAME, 'a').get_attribute('text')
    driver.quit()  # 关闭浏览器
    print(f'\n[bold green]音乐名称：[/bold green][magenta]{b}[/magenta]')
    print('[bold green]作者：[/bold green]' + au)
    print('[bold green]音乐链接为：[/bold green]' + a)
    print('[bold green]音乐下载链接为：[/bold green]' + 'https://music.163.com/song/media/outer/url?id={}.mp3'.format(
        a[len('https://music.163.com/song?id='):]))
    print('[bold green]歌曲id为：[/bold green]' + a[len('https://music.163.com/song?id='):])
    file = requests.get(
        url='https://music.163.com/song/media/outer/url?id={}.mp3'.format(a[len('https://music.163.com/song?id='):]),
        headers=headers).content
    # print(file)

    if 'html' not in str(file):
        if os.path.exists('music'):
            os.chdir('music')
            with open('{}.mp3'.format(b), 'wb') as f:
                f.write(file)
                print('\n[red]下载完成！')
        else:
            os.mkdir('music')
            os.chdir('music')
            with open('{}.mp3'.format(b), 'wb') as f:
                f.write(file)
                print('\n[red]下载完成！')
    else:
        print('\n[red]这首歌要付费呢')


# 勇往直前 森林狂想曲 548252595
print('[yellow]请输入想要下载的歌曲', end='')
song = input('：')
get_music_name(__song=song)
print('\n[bold pink]最好放在桌面用(也可以在其他文件夹中)\n下载的歌曲也在桌面的music文件夹中（其他文件夹则在同一级music中）[/bold pink]\n\n[italic underline]10秒后窗口自动关闭[/italic underline]')
time.sleep(10)