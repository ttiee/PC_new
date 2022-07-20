import pyautogui
import time


# Point(x=644, y=757)
# Point(x=847, y=757)
# Point(x=1062, y=757)
# Point(x=1250, y=757)

def main():
    pyautogui.click(1097, 1048)
    # time.sleep(0.5)
    # print(pyautogui.screenshot().getpixel((1062, 757)))
    while 1:
        # time.sleep(0.05)
        # if pyautogui.pixelMatchesColor(1250, 757, (236, 70, 81)):
        #     pyautogui.click(1250, 757)
        if pyautogui.pixelMatchesColor(1062, 757, (247, 64, 86)):
            pyautogui.click(1062, 757)
        elif pyautogui.pixelMatchesColor(847, 757, (234, 68, 80)):
            pyautogui.click(847, 757)
        elif pyautogui.pixelMatchesColor(644, 757, (234, 67, 84)):
            pyautogui.click(644, 757)
        else:
            break


if __name__ == '__main__':
    main()
