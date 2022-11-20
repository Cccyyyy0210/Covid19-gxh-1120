import requests
import json
import time
import pymysql
from selenium import webdriver
from selenium.webdriver import Edge, EdgeOptions
import traceback
import sys

from selenium.webdriver.common.by import By
import random
from bs4 import BeautifulSoup

# 疫情关键词爬取自卫健委宣传司
# web是爬取的板块
from utils import get_conn

webList = ['fkdt', 'zhengcwj', 'yhfc']


def get_url(web, page=1):  # web=fkdt zhengcwj yhfc
	if page == 1:
		url = f'http://www.nhc.gov.cn/xcs/{web}/list_gzbd.shtml'
	else:
		url = f'http://www.nhc.gov.cn/xcs/{web}/list_gzbd_{page}.shtml'
	return url


def get_hotsearch(web, page=1):
	contents = []
	url = get_url(web, page)
	option = EdgeOptions()  # 创建谷歌浏览器实例
	option.add_argument("--headless")  # 隐藏浏览器
	browser = webdriver.Edge(options=option)
	browser.get(url)
	infos = browser.find_elements(By.CSS_SELECTOR, '.zxxx_list li')
	for li in infos:
		title = li.find_element(By.TAG_NAME, 'a').get_attribute('title')
		dt = li.find_element(By.TAG_NAME, 'span').text
		content = {}
		content['title'] = title
		content['dt'] = dt
		contents.append(content)
	browser.close()
	return contents


def update_hotsearch(web, page=1):
	conn, cursor = get_conn()
	try:
		contents = get_hotsearch(web, page)
		print(f"{time.asctime()}开始更新热搜数据")
		sql = f"insert into {web}(dt,content) values(%s,%s)"
		for content in contents:
			cursor.execute(sql, (content['dt'], content['title']))
		conn.commit()  # 提交事务保存数据
		print(f"{time.asctime()}数据更新完毕")
	except:
		traceback.print_exc()
	finally:
		cursor.close()
		conn.close()


def hotsearch_crawler(web, beginPage, endPage):
	for page in range(beginPage, endPage + 1):
		update_hotsearch(web, page)


def main():
	#hotsearch_crawler(webList[2], 1, 20)
	 #hotsearch_crawler(webList[0], 5, 20)
	hotsearch_crawler(webList[2], 21, 22)

if __name__ =="__main__":
	main()
