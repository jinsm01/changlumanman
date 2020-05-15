#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/15 17:56 
# @Author :labixiaoxin
# @File : test_po3.py
from studay_sele.test_po import Main


class Test_a_b:
    def setup(self):
        main = Main()
        main.click_first_link().title()