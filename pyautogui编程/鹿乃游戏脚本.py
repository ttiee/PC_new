import os
import sys

import cv2
import pyautogui


# https://xingye.me/game/eatkano/index.php  游戏网址


def get_p(img_path):
    # 截图并保存
    pyautogui.screenshot().save('./pic1/screenshot.png')

    # 加载截图和谷歌浏览器的图片
    screen_shot_img = cv2.imread('./pic1/screenshot.png')
    lunai_img = cv2.imread(img_path)

    # 获得谷歌图片的大小
    lunai_shape = lunai_img.shape
    # print(chrome_shape)

    # 将两个图片进行匹配，获得匹配的左上角坐标
    result0 = cv2.matchTemplate(screen_shot_img, lunai_img, cv2.TM_SQDIFF_NORMED)
    result = cv2.minMaxLoc(result0)[2]
    # print(result)

    # 获得中心坐标
    x, y = result[0] + lunai_shape[1] / 2, result[1] + lunai_shape[0] * 3 / 2


def main():

    # 截图并保存
    pyautogui.screenshot().save('./pic1/screenshot.png')

    # 加载截图和谷歌浏览器的图片
    screen_shot_img = cv2.imread('./pic1/screenshot.png')
    lunai_img = cv2.imread('./pic1/lunai.png')

    # 获得谷歌图片的大小
    lunai_shape = lunai_img.shape
    # print(chrome_shape)

    # 将两个图片进行匹配，获得匹配的左上角坐标
    result0 = cv2.matchTemplate(screen_shot_img, lunai_img, cv2.TM_SQDIFF_NORMED)
    result = cv2.minMaxLoc(result0)[2]
    # print(result)

    # 获得中心坐标
    x, y = result[0] + lunai_shape[1]/2, result[1] + lunai_shape[0]*3/2
    pyautogui.click(x, y)


if __name__ == '__main__':
    pyautogui.click(1069, 1049)
    while 1:
        main()
