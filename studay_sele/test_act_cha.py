#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/14 11:18 
# @Author :labixiaoxin
# @File : test_act_cha.py
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # def teardown(self):
    #     self.driver.quit()

    def test_ationchains_click(self):
        self.driver.get('http://www.baidu.com')

        ele1 = self.driver.find_element_by_css_selector('#kw')
        ele2 = self.driver.find_element_by_css_selector('#su')
        ele3 = self.driver.find_element_by_css_selector('#s-top-left>div>a')

        action = ActionChains(self.driver)
        # # 单击 右键 双击
        # action.click(ele1)
        # action.context_click(ele2)
        # action.double_click(ele2)
        action.move_to_element(ele3)
        action.perform()
        sleep(5)

