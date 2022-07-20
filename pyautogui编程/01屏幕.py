import pyautogui
import time


def main1():
    print(pyautogui.size())
    while 1:
        print(pyautogui.position())
        time.sleep(1)


def main2():
    pyautogui.moveTo(1, 1, duration=0.1)
    for i in range(100):
        pyautogui.move(5, 5, 0.1)
        print(6)
        # time.sleep(1)


def main3():
    pyautogui.moveTo(1900, 400, duration=0.5)
    pyautogui.dragTo(1900, 400, button='right', duration=0.1)
    pyautogui.drag(-50, 50, button='left', duration=3)


def main4():
    p = pyautogui.position()
    pyautogui.click(1870, 150, clicks=2, button='left', interval=0)
    # pyautogui.doubleClick()
    # pyautogui.tripleClick()
    pyautogui.moveTo(p)


def main5():
    pyautogui.mouseDown(button='left')
    pyautogui.move(0, -100)
    pyautogui.mouseUp(button='left')


def main6():
    p = pyautogui.position()

    pyautogui.moveTo(1770, 250)
    pyautogui.click()
    pyautogui.scroll(-500)
    time.sleep(1)
    pyautogui.scroll(500)
    time.sleep(1)
    pyautogui.click(1206, 1052)

    pyautogui.moveTo(p)


def main7():
    p = pyautogui.position()

    pyautogui.moveTo(1133, 361)
    pyautogui.click()
    pyautogui.write('hhh')
    # pyautogui.press('enter')
    time.sleep(1)
    for i in range(3):
        pyautogui.press('backspace')

    pyautogui.moveTo(p)


def get_position():
    time.sleep(4)
    print(pyautogui.position())


if __name__ == '__main__':
    # main1()
    # main2()
    # main3()
    # main4()
    # main5()
    get_position()
    # main6()
    # main7()
