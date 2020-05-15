#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/14 19:06 
# @Author :labixiaoxin
# @File : test_file_loading.py

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
        self.driver.find_element_by_xpath('//*[@id="form"]/span[1]/span[1]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input').send_keys(r'C:\Users\jsm\Desktop\1589450453(1).png')
        sleep(5)