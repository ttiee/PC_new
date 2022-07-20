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
    print('音乐名称：' + b)
    print('作者：' + au)
    print('音乐链接为：' + a)
    print('音乐下载链接为：' + 'https://music.163.com/song/media/outer/url?id={}.mp3'.format(
        a[len('https://music.163.com/song?id='):]))
    print('歌曲id为：' + a[len('https://music.163.com/song?id='):])
    file = requests.get(
        url='https://music.163.com/song/media/outer/url?id={}.mp3'.format(a[len('https://music.163.com/song?id='):]),
        headers=headers).content
    # print(file)

    if 'html' not in str(file):
        if os.path.exists('music'):
            os.chdir('music')
            with open('{}.mp3'.format(b), 'wb') as f:
                f.write(file)
                print('\n下载完成！')
        else:
            os.mkdir('music')
            os.chdir('music')
            with open('{}.mp3'.format(b), 'wb') as f:
                f.write(file)
                print('\n下载完成！')
    else:
        print('\n这首歌要付费呢')


# 勇往直前 森林狂想曲 548252595
song = input('请输入想要下载的歌曲：')
get_music_name(__song=song)
print('\n最好放在桌面用(也可以在其他文件夹中)\n下载的歌曲也在桌面的music文件夹中（其他文件夹则在同一级music中）\n\n10秒后窗口自动关闭')
time.sleep(10)