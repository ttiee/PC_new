import time
import pyautogui


def press_button(path):
    time.sleep(0.5)

    p = pyautogui.locateOnScreen(path)
    if p is None:
        print(f'没有找到目标{path}')
        return None
    x, y = pyautogui.center(p)
    p0 = pyautogui.position()
    pyautogui.click(x, y)
    pyautogui.moveTo(p0)


def get_position():
    press_button('./pic/hide_pycharm.png')
    time.sleep(4)
    print(pyautogui.position())
    press_button('./pic/un_hide_pycharm.png')


if __name__ == '__main__':
    get_position()
