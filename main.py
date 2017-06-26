#coding:utf-8

import time
import sys
import re
from selenium import webdriver
from bs4 import BeautifulSoup

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    driver = webdriver.PhantomJS()
    driver.get('http://music.163.com/#/song?id=112064')
    driver.switch_to.frame('contentFrame')
    # time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    print(soup.select('div[id="comment-box"] span[class="sub s-fc3"] span[class="j-flag"]')[0].get_text())

if __name__ == '__main__':
    main()