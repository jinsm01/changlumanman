#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 10:21 
# @Author :labixiaoxin
# @File : base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    driver = None
    base_url = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = '127.0.0.1:9696'
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = driver

        if self.base_url != '':
            self.driver.get(self.base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)
