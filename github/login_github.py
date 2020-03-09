#! /usr/bin/env python3
#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

args = sys.argv
username = os.getenv('GITHUB_{0}_USERNAME'.format(args[1]))
password = os.getenv('GITHUB_{0}_PASSWORD'.format(args[1]))
timeout_sec = 15

d = webdriver.Chrome("chromedriver")
d.get('https://github.com/login')

WebDriverWait(d, timeout_sec).until(EC.presence_of_all_elements_located)

print(username)
d.find_element_by_id('login_field').send_keys(username)
d.find_element_by_id('password').send_keys(password)
signInBtn = d.find_element_by_name('commit')
signInBtn.click()

d.maximize_window()
