#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 15:52 
# @Author :labixiaoxin
# @File : main_page.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from weixin_main.page.contacts import AddMembers


class Main_page:
    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9696'
        self.driver = webdriver.Chrome(options=options)

    def goto_add_members(self):
        # click contacts

        # click add members
        return AddMembers(self.driver)
