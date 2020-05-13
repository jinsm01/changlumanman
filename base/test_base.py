#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/13 17:17 
# @Author :shannan
# @File : test_base.py
from selenium import webdriver


class Base:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
