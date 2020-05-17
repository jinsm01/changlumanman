#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 6:43 
# @Author :labixiaoxin
# @File : login.py

from selenium.webdriver.remote.webdriver import WebDriver

from weixin_login.page.Register import Register


class Login:
    def __init__(self, driver: WebDriver):    # 避免初始化所以传进来
        self.driver = driver

    def scan(self):
        pass

    def go_to_register(self):
        self.driver.find_element_by_css_selector('.login_registerBar_link').click()
        return Register(self.driver)

