#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 7:41 
# @Author :labixiaoxin
# @File : add_members.py
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMembers:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_members(self):
        sleep(2)
        self.driver.find_element(By.ID, 'username').send_keys('测试1')
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('1111111')
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('11111111111')
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(5)
        return True

