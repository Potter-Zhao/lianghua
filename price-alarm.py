#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Team   ：FUND
Author ：Sandy
Date   ：2021/6/30 14:03
Remark ：
"""

from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import requests
import time
EDGE = {
    "browserName": "MicrosoftEdge",
    "version": "",
    "platform": "WINDOWS",
    # 无头关键
    "ms:edgeOptions": {
        'extensions': [],
        'args': [
            '--headless',
            '--disable-gpu',
            '--remote-debugging-port=9222',
        ]}
}
options = EdgeOptions()
options.use_chromium = True
options.add_argument('headless')
browser = webdriver.Edge('F:\edgedriver_win64\edgedriver_win64\MicrosoftWebDriver.exe')# capabilities=EDGE

browser.get('https://bzz.exchange/')
time.sleep(10)
apath = """//*[@id="root"]/div/div[1]/nav/div[2]/div[1]/div/span[1]"""
# xpath = """//*[@id="root"]/div/div[1]/nav/div[2]/div[1]"""
bpath = """//*[@id="root"]/div/div[1]/nav/div[2]/div[1]/div/span[2]"""

while True:
    print("正在获取Bzz的价格")
    bzz_price = browser.find_element_by_xpath(xpath=apath)
    bzz_name = browser.find_element_by_xpath(xpath=bpath)

    if bzz_name.text == "DAI / 1 BZZ":
        print("bzz的价格是：", bzz_price.text)
        try:
            response = requests.get("https://www.okex.com/api/v5/market/ticker?instId=BZZ-USDT", timeout=5).json()
            print("正在获取Okex的价格")
            ok = response['data'][0]['last']
            print("ok的价格是：", ok)
        except Exception:
            print("获取okex的数据失败")
    time.sleep(10)
