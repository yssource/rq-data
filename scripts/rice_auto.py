# encoding: UTF-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from passwd import *
from rqdata.mongo.mongo_server import run_server
from rqdata.rpc.server import RpcHandler
import threading
import sys


def run_auto():
    driver = webdriver.Chrome()
    driver.get("https://www.ricequant.com/login")
    time.sleep(2)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="page-register"]/main/div[2]/form[4]/div[2]/input'))
        )
    finally:
        if user_name == '':
            raise Exception('place configure user name in scripts/passwd.py')
        element.send_keys(user_name)
    element = driver.find_element_by_xpath('//*[@id="page-register"]/main/div[2]/form[4]/div[4]/input')
    if passwd == '':
        raise Exception('please configure passwd in scritps/passwd.py')
    element.send_keys(passwd)
    element = driver.find_element_by_xpath('//div/input[@value="登录"]')
    element.click()
    try:
        element = WebDriverWait(driver, 10).until(
            lambda _: u"策略列表" in driver.page_source
        )
    finally:
        pass
    driver.get("https://www.ricequant.com/research/user/user_310960/notebooks/future.ipynb")
    driver.get("https://www.ricequant.com/research/user/user_310960/notebooks/future.ipynb")
    time.sleep(2)
    element = driver.find_element_by_xpath('//button[@title="run cell, select below"]')
    element.click()
    while not stop:
        pass
    driver.close()


stop = False


def stop_all():
    global stop
    stop = True


if __name__ == '__main__':
    RpcHandler.register(stop_all)
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    t1 = threading.Thread(target=run_auto, daemon=True)
    t1.start()

    while not stop:
        pass
