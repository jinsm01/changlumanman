#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/13 17:23 
# @Author :labixiaoxin
# @File : test_wait.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://home.testing-studio.com/latest')
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element_by_xpath('//*[@title="归入各种类别的所有主题"]').click()
        # 显示等待
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="table-heading"]')))
        self.driver.find_element_by_xpath('//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()



         # def wait(x):
         #    return len(self.driver.find_element_by_xpath('//*[@class="table-heading"]and[@aria-role="heading"]')) == 1
