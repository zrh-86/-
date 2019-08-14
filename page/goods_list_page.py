import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class GoodListPage(BaseAction):

    # 商品列表 按钮
    goods_button = By.ID, "com.yunmall.lc:id/iv_element_1"

    # 随机点击 商品列表
    @allure.step(title='商品列表 随机点击 商品')
    def click_goods(self):
        goods = self.find_elements(self.goods_button)
        goods_count = len(goods)
        goods_index = random.randint(0, goods_count - 1)
        goods[goods_index].click()
