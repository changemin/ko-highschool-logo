# Phase 2
# crawl-logo.py
# 이미지를 크롤링 해보자

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import pandas as pd
import os # 경로 생성
 
def make_city_path(df):
    city_df = df['시도'].groupby(df['시도']).describe()
    for index, row in city_df.iterrows():
        os.makedirs(f"result/{row.name}", exist_ok = True)

def crawl_image(driver, city, school_name):
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(f"{school_name} 로고")
    elem.send_keys(Keys.RETURN)
    
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

    images[0].click()
    time.sleep(0.6)
    try:
        img_url = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
        urllib.request.urlretrieve(img_url, f"result/{city}/{school_name}.jpg")
    except: 
        raise NameError(f'error in {school_name}')
    
if __name__ == '__main__':
    file_path = "data/highschool-extracted.xlsx"
    df = pd.read_excel(file_path)

    make_city_path(df)
    driver = webdriver.Chrome('chromedriver')
    for index, row in df.iterrows():
        
        try:
            crawl_image(driver, row['시도'], row['학교명'])
        except:
            print(f"error in {index} : {row['학교명']}")
            pass
        
    driver.close()
    

