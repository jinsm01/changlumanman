#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 7:41 
# @Author :labixiaoxin
# @File : add_members.py
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from weixin_main.page.base_page import BasePage


class AddMembers(BasePage):

    def add_members(self):
        sleep(2)
        self.find(By.ID, 'username').send_keys('sryy78e')
        self.find(By.ID, 'memberAdd_acctid').send_keys('ayrysycc')
        self.find(By.ID, 'memberAdd_phone').send_keys('13828328222')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(5)

    def get_members(self):
        elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        return [element.get_attribute('title')for element in elements]


    # list = []
    # for element in elements:
    #     list.append(element.get_attribute('title'))
    # return list
