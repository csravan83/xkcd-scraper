import requests
from bs4 import BeautifulSoup
import csv
from flask import send_file
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os.path import basename
#
# def striphtml(data):
#     p = re.compile(r'<.*?>')
#     return p.sub('', data)
#

def scrape():
    driver = webdriver.Chrome(r'/home/sravan/Desktop/chromedriver_linux64/chromedriver')
    driver.get("https:/www.xkcd.com/")
    time.sleep(3)
    xp = '//*[@id="middleContainer"]/ul[2]/li[2]/a'


    elem = driver.find_element_by_xpath(xp).get_attribute("href")
    driver.get(elem)


    req = requests.get(elem)
    soup = BeautifulSoup(req.content, "lxml")

    sel = "http:"+ soup.select("img")[1].attrs['src']
    return sel
