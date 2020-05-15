#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/14 17:58 
# @Author :labixiaoxin
# @File : test_windows.py
from time import sleep

from selenium import webdriver


class TestWindowns:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_windows(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="u1"]/a[2]').click()  # denglu
        print(self.driver.current_window_handle)
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()  # zhuce
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_css_selector('#TANGRAM__PSP_4__phone').send_keys(11111111)
        self.driver.switch_to.window(windows[0])
        sleep(5)


