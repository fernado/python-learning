import time
import os
import re
import requests
from selenium import webdriver


video_path = "video/"


def create_path(param_path: str):
    if not os.path.exists(param_path):
        os.makedirs(param_path)


def change_time(title: str):
    pattern = re.compile(r'[\/\\\:\*\?\"\<\>\|]')
    new_title = re.sub(pattern, ' ', title)
    return new_title


def drop_down():
    """
    scroll down page
    """
    # 1, 3, 5, 7, 9 height of page will update
    for i in range(1, 100, 4):
        time.sleep(1)
        # 1/9, 3/9, 5/9, 9/9
        j = i / 9
        # scroll bar's location
        # document.documentElement.scrollTop
        # page max height
        # document.documentElement.scrollHeight

        js = 'document.documentElement.scrollTop=document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)



create_path(video_path)

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
time.sleep(2)

drop_down()

lst = driver.find_elements_by_css_selector('div.yt-lockup-content')

for item in lst:
    url_href = item.find_element_by_tag_name('a').get_attribute('href')
    print(url_href)

