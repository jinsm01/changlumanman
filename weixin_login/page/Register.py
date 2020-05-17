#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 6:43 
# @Author :labixiaoxin
# @File : Register.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver):   # 避免初始化所以传进来
        self.driver = driver

    def register(self):
        self.driver.find_element_by_css_selector('#corp_name').send_keys('测试1')
        self.driver.find_element_by_css_selector('#manager_name').send_keys('admin1')
        sleep(5)
        self.driver.quit()
