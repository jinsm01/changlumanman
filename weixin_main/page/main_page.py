#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 15:52 
# @Author :labixiaoxin
# @File : main_page.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from weixin_main.page.add_members import AddMembers


class MainPage:
    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9696'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

    def goto_add_members(self):
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMembers(self.driver)
