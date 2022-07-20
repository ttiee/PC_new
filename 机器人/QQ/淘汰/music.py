from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'}


def get_music_id(__song):
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
    __id = a[len('https://music.163.com/song?id='):]
    print('音乐名称：' + b)
    print('作者：' + au)
    print('音乐链接为：' + a)
    print('音乐下载链接为：' + 'https://music.163.com/song/media/outer/url?id={}.mp3'.format(
        __id))
    print('歌曲id为：' + __id)
    file = requests.get(
        url='https://music.163.com/song/media/outer/url?id={}.mp3'.format(__id),
        headers=headers).content
    err = 0
    if 'html' not in str(file):
        pass
    else:
        b = '伴你成长动画片《熊出没之夺宝熊兵》主题曲'
        __id = 28613172
        au = '白挺'
        err = 1
    return __id, au, b, err
