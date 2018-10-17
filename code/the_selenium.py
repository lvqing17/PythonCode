#!/user/bin/env python
# -*-coding:utf-8-*-
# @time       : 16/11/8 12:09
# @Author     : Zhangxy
# @File       : 001baiduSearch.py
# @Software   : PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.tmall.com/")
driver.find_element_by_id('mq').send_keys('selenium')
# driver.find_element_by_id('').click()