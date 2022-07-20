import os
import sys
import time

import cv2
import pyautogui


def prepare():
    if not os.path.exists('./pic'):
        os.mkdir('./pic')
    if not os.path.exists('./pic/chrome.png'):
        print('还没有用来匹配的谷歌浏览器的图片呢！\n请在桌面给谷歌浏览器截一个图片，命名为chrome.png，放在pic文件夹下，用于匹配')
        sys.exit()


def main():
    # 准备工作
    prepare()

    # 返回桌面
    pyautogui.hotkey('win', 'd')
    time.sleep(0.05)

    # 截图并保存
    pyautogui.screenshot().save('./pic/screenshot.png')

    # 加载截图和谷歌浏览器的图片
    screen_shot_img = cv2.imread('./pic/screenshot.png')
    chrome_img = cv2.imread('./pic/chrome.png')

    # 获得谷歌图片的大小
    chrome_shape = chrome_img.shape
    # print(chrome_shape)

    # 将两个图片进行匹配，获得匹配的左上角坐标
    result0 = cv2.matchTemplate(screen_shot_img, chrome_img, cv2.TM_SQDIFF_NORMED)
    result = cv2.minMaxLoc(result0)[2]
    # print(result)

    # 获得中心坐标
    x, y = result[0] + chrome_shape[1]/2, result[1] + chrome_shape[0]/2

    # 获取鼠标位置，完成任务后返回该坐标
    mouse_p = pyautogui.position()

    # 双击打开浏览器
    pyautogui.doubleClick(x, y)

    # 鼠标回到双击之前的位置
    pyautogui.moveTo(mouse_p)


if __name__ == '__main__':
    main()
