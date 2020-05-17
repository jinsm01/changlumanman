#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 6:43 
# @Author :labixiaoxin
# @File : test_register.py
from weixin_login.page.Index import Index


class TestRegister:
    def setup(self):
        self.index = Index()

    def test_register(self):
        # self.index.go_to_login().go_to_register().register()
        self.index.go_to_register().register()
