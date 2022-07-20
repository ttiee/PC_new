import pyautogui
import time


# Point(x=644, y=757)
# Point(x=847, y=757)
# Point(x=1062, y=757)
# Point(x=1250, y=757)

# 792 882

def main():
    pyautogui.click(1097, 1048)
    time.sleep(0.5)
    print(pyautogui.screenshot().getpixel((792, 882)))
    while 1:
        # time.sleep(0.05)
        # if pyautogui.pixelMatchesColor(792, 882, (108, 117, 125)):
        #     break
        if not pyautogui.pixelMatchesColor(1250, 653, (255, 255, 255)):
            pyautogui.click(1250, 757)
        elif not pyautogui.pixelMatchesColor(1062, 653, (255, 255, 255)):
            pyautogui.click(1062, 757)
        elif not pyautogui.pixelMatchesColor(847, 653, (255, 255, 255)):
            pyautogui.click(847, 757)
        elif not pyautogui.pixelMatchesColor(644, 653, (255, 255, 255)):
            pyautogui.click(644, 757)
        else:
            break


if __name__ == '__main__':
    main()
