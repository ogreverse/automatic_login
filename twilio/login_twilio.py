#! /usr/bin/env python3
#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import time

args = sys.argv
email = os.getenv('TWILIO_{0}_USERNAME'.format(args[1]))
password = os.getenv('TWILIO_{0}_PASSWORD'.format(args[1]))
timeout_sec = 15

d = webdriver.Chrome("chromedriver")
d.get('https://jp.twilio.com/login')

WebDriverWait(d, timeout_sec).until(EC.presence_of_all_elements_located)

# Emailアドレス入力
print(email)
d.find_element_by_id('email').send_keys(email)
nextBtn = d.find_element_by_xpath('//*[@id="content"]/div[2]/div/form/div[2]/button')
nextBtn.click()

# ページ遷移の待機
time.sleep(1)

# パスワード入力、ログイン
element = d.find_element_by_id('password').send_keys(password)

logInBtn = d.find_element_by_id('login')
logInBtn.click()
