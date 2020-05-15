#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/14 15:47 
# @Author :labixiaoxin
# @File : test_tou_act.py
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.chrome.options import Options


class TestTouchAction:
    def setup(self):
        options = Options()
        options.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_touch_scroll(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
        sleep(5)
        ele = self.driver.find_element_by_xpath('//*[@id="su"]')
        action = TouchActions(self.driver)
        sleep(3)
        action.tap(ele).perform()
        sleep(3)
        action.scroll_from_element(ele, 0, 10000).perform()

    # @pytest.mark.skip
    # def test_login(self):
    #     self.driver.get('http://www.baidu.com')
    #     self.driver.find_element_by_xpath('//*[@id="u1"]/a[2]').click()
    #     self.driver.find_element_by_css_selector('#TANGRAM__PSP_10__footerULoginBtn').click()
    #     self.driver.find_element_by_css_selector('#TANGRAM__PSP_10__userName').send_keys('eeeee')
    #     self.driver.find_element_by_css_selector('#TANGRAM__PSP_10__password').send_keys('fdfdfdf')
    #     self.driver.find_element_by_css_selector('#TANGRAM__PSP_10__memberPass').click()
    #     self.driver.find_element_by_css_selector('#TANGRAM__PSP_10__submit').click()


