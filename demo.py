import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# toast
desired_caps['automationName'] = 'Uiautomator2'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def scroll_page_one_time(direction="up"):
    """
    滑动一次屏幕
    :param direction: 方向
        "up"：从下往上
        "down"：从上往下
        "right"：从左往右
        "left"：从右往左
    :return:
    """
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]

    center_x = width / 2
    center_y = height / 2

    left_x = width / 4 * 1
    left_y = center_y
    right_x = width / 4 * 3
    right_y = center_y

    top_x = center_x
    top_y = height / 4 * 1
    bottom_x = center_x
    bottom_y = height / 4 * 3

    if direction == "up":
        driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
    elif direction == "down":
        driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
    elif direction == "left":
        driver.swipe(right_x, right_y, left_x, left_y, 3000)
    elif direction == "right":
        driver.swipe(left_x, left_y, right_x, right_y, 3000)
    else:
        raise Exception("请检查参数是否正确，up/down/left/right")


def find_element_with_scroll(feature, direction="up"):
    """
    边滑边找 某个元素的特征，并且点击
    :param feature: 元素的特征
    :param direction: 方向
        "up"：从下往上
        "down"：从上往下
        "right"：从左往右
        "left"：从右往左
    :return:
    """
    page_source = ""
    while True:
        try:
            return driver.find_element(*feature)
        except Exception:

            scroll_page_one_time(direction)

            if driver.page_source == page_source:
                print("到底了")
                break
            page_source = driver.page_source


find_element_with_scroll((By.XPATH, "//*[@text='关于手机']")).click()
