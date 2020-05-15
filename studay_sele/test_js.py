#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/15 18:08 
# @Author :labixiaoxin
# @File : test_js.py
from time import sleep

import pytest
from selenium import webdriver


class TestJs:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_js(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('nihao')
        self.driver.execute_script('return document.getElementById("su")').click()
        # ele = self.driver.execute_script('document.getElementById("su")')  必须有返回
        sleep(3)
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/a[10]').click()
        sleep(3)

        for data in ['return document.title', 'return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(data))


    def test_train(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script('a = document.getElementById("train_date");a.removeAttribute("readonly")')
        sleep(5)
        self.driver.execute_script('document.getElementById("train_date").value = "2020-12-30"')
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
        sleep(5)
