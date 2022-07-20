import time

import pyautogui


def double_press_button(path):
    # pyautogui.hotkey('win', 'd')
    time.sleep(0.5)

    p = pyautogui.locateOnScreen(path)
    if p is None:
        print(f'没有找到目标{path}')
        # pyautogui.hotkey('win', 'd')
        return None
    x, y = pyautogui.center(p)
    p0 = pyautogui.position()
    pyautogui.doubleClick(x, y)
    pyautogui.moveTo(p0)


def press_button(path):
    # pyautogui.hotkey('win', 'd')
    time.sleep(0.5)

    p = pyautogui.locateOnScreen(path)
    if p is None:
        print(f'没有找到目标{path}')
        # pyautogui.hotkey('win', 'd')
        return None
    x, y = pyautogui.center(p)
    p0 = pyautogui.position()
    pyautogui.click(x, y)
    pyautogui.moveTo(p0)


def main():
    press_button('./pic/hide_pycharm.png')
    double_press_button('./pic/chrome.png')
    press_button('./pic/bilibili_chrome.png')
    # pyautogui.click(955, 569)
    press_button('./pic/un_hide_pycharm.png')


if __name__ == '__main__':
    main()
