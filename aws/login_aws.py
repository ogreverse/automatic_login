#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
import sys

args = sys.argv
account = os.getenv('AWS_{0}_ACCOUNT'.format(args[1]))
username = os.getenv('AWS_{0}_USERNAME'.format(args[1]))
password = os.getenv('AWS_{0}_PASSWORD'.format(args[1]))
timeout_sec = 15

options = Options()
options.add_experimental_option('detach', True)

# `chromedriver` のパスを指定
chromedriver_path = "/opt/homebrew/bin/chromedriver"
service = Service(executable_path=chromedriver_path)

d = webdriver.Chrome(options=options, service=service)
d.get('https://{0}.signin.aws.amazon.com/console'.format(account))

WebDriverWait(d, timeout_sec).until(EC.presence_of_all_elements_located)

print(username)
# ユーザー名フィールドが表示されるまで待機
WebDriverWait(d, timeout_sec).until(EC.presence_of_element_located(('id', 'username')))
d.find_element('id', 'username').send_keys(username)

# パスワードフィールドが表示されるまで待機
WebDriverWait(d, timeout_sec).until(EC.presence_of_element_located(('id', 'password')))
d.find_element('id', 'password').send_keys(password)

# サインインボタンが表示されるまで待機
WebDriverWait(d, timeout_sec).until(EC.element_to_be_clickable(('id', 'signin_button')))
signInBtn = d.find_element('id', 'signin_button')

signInBtn.click()

d.maximize_window()
