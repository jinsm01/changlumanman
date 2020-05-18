#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 15:52 
# @Author :labixiaoxin
# @File : main_page.py
from time import sleep
from selenium.webdriver.common.by import By
from weixin_main.page.add_members import AddMembers
from weixin_main.page.base_page import BasePage


class MainPage(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_members(self):
        # self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        sleep(2)
        self.find(By.ID, 'menu_contacts').click()
        sleep(2)
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return AddMembers(self.driver)
