#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 6:42 
# @Author :labixiaoxin
# @File : Index.py

from selenium import webdriver

from weixin_login.page.Register import Register
from weixin_login.page.login import Login


class Index:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')

    def go_to_login(self):
        self.driver.find_element_by_css_selector('.index_top_operation_loginBtn').click()
        return Login(self.driver)     # 避免初始化所以传进来

    def go_to_register(self):
        self.driver.find_element_by_css_selector('.index_head_info_pCDownloadBtn').click()
        return Register(self.driver)      # 避免初始化所以传进来

