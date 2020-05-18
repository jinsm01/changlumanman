#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 7:53 
# @Author :labixiaoxin
# @File : test_add_members.py
from time import sleep

from weixin_main.page.main_page import MainPage


class TestAddMembers:
    def setup(self):
        self.mainpage = MainPage()

    def test_addmembers(self):
        add_members = self.mainpage.goto_add_members()
        add_members.add_members()
        add_members.get_members()
        sleep(2)
        assert 'SE' in add_members.get_members()

