#! /usr/bin/env python3
#-*- coding: utf-8 -*-

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
service = Service(executable_path="chromedriver")
d = webdriver.Chrome(options=options, service=service)
d.get('https://{0}.signin.aws.amazon.com/console'.format(account))

WebDriverWait(d, timeout_sec).until(EC.presence_of_all_elements_located)

print(username)
d.find_element('id', 'username').send_keys(username)
d.find_element('id', 'password').send_keys(password)
signInBtn = d.find_element('id', 'signin_button')
signInBtn.click()

d.maximize_window()

