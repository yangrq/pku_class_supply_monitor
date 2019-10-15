# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import threading
import os

opts = Options()
opts.add_argument(
    "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")

pattern = re.compile(r'<span>计算概论A<\/span>[\s\S]*?(\d\d[ ]*\/[ ]*\d\d)')
num_div_num = re.compile(r'(\d\d)[ ]*\/[ ]*(\d\d)')


def alert():
    while(True):
        os.system('cmdmp3.exe radar.mp3')


def fetch_class_data():
    driver = webdriver.Chrome()
    driver.get("http://elective.pku.edu.cn")
    driver.implicitly_wait(20)
    driver.find_element_by_id("user_name").click()
    driver.find_element_by_id("user_name").clear()
    driver.find_element_by_id("user_name").send_keys("")
    driver.find_element_by_id("password").click()
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("")
    time.sleep(5)
    driver.find_element_by_id("logon_button").click()
    time.sleep(5)
    driver.execute_script(
        "window.location.href='http://elective.pku.edu.cn/elective2008/edu/pku/stu/elective/controller/supplement/SupplyCancel.do'")
    time.sleep(2)
    driver.execute_script(
        "window.location.href='http://elective.pku.edu.cn/elective2008/edu/pku/stu/elective/controller/supplement/SupplyCancel.do'")
    time.sleep(2)
    html = driver.execute_script(
        "return document.getElementsByTagName('html')[0].innerHTML")
    result = pattern.findall(html)
    found = False

    for item in result:
        obj = num_div_num.findall(item)
        if (int(obj[0][0]) > int(obj[0][1])):
            found = True

    if (found):
        alert()
    else:
        driver.close()
        driver.quit()


def construct_timer():
    try:
        fetch_class_data()
    except:
        pass
    timer = threading.Timer(300, construct_timer)
    timer.start()


timer = threading.Timer(0, construct_timer)
timer.start()
