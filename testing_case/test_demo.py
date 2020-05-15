#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/15 14:01 
# @Author :labixiaoxin
# @File : test_demo.py
import pytest
import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWeiXin:

    def setup(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9696'
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def add_cookies(self):
        db = shelve.open('cookies')
        # db['cookie'] = self.driver.get_cookies()  # cookies获取
        cookies = db['cookie']
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        db.close()

    def test_weixin(self):
        # 第一步：打开要登陆的页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # 第二步：添加cookie
        self.add_cookies()
        # 第三步：登陆页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # 第四步：点击联系人
        # self.driver.find_element_by_css_selector('.frame_nav_item frame_nav_item_Curr').click()
        self.driver.find_element_by_xpath('//*[@id="menu_apps"]').click()
        sleep(5)

    # def test_weixin1(self):
    #     # 第一步：打开要登陆的页面
    #     self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    #     # 第二步：添加cookie
    #     db = shelve.open('cookies')
    #     db['cookie'] = self.driver.get_cookies()
    # cookies = db['cookie']
    # for cookie in cookies:
    #     if 'expiry' in cookie.keys():
    #         cookie.pop('expiry')
    #     self.driver.add_cookie(cookie)
    # db.close()
    # # 第三步：登陆页面
    # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    # self.driver.find_element_by_css_selector('#menu_contacts').click()

    # @pytest.mark.skip
    # def test_demo(self):
    #     # self.driver.get('https://home.testing-studio.com/')  # 复用浏览器时，无需在打开网页
    #     self.driver.find_element_by_link_text('分类').click()
