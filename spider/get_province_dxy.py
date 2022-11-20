import json
import re
import time
import pymysql
import requests
from selenium import webdriver
from selenium.webdriver import Edge, EdgeOptions
import traceback
import sys
from selenium.webdriver.common.by import By
import random
from bs4 import BeautifulSoup
import logging
import pymysql

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


def get_conn():
	# 创建连接
	conn = pymysql.connect(host="localhost",
	                       user="root",
	                       password="root",
	                       db="covid19",
	                       charset="utf8")
	# 创建游标
	cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
	return conn, cursor


def close_conn(conn, cursor):
	cursor.close()
	conn.close()

def fetch_crawler():
	url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"
	headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0'
	}
	r = requests.get(url, headers)
	soup = BeautifulSoup(r.content, 'lxml')
	fetch_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getAreaStat'})))
	if fetch_information:
		#provinces=fetch_parser(fetch_information=fetch_information)
		provinces = json.loads(fetch_information.group(0))
		for province in provinces:
			try:
				province.pop('provinceShortName')
				province.pop('comment')
				province.pop('locationId')
				province.pop('statisticsData')
				province.pop('cities')
				province.pop('dangerAreas')
				province.pop('detectOrgCount')
				province.pop('vaccinationOrgCount')
			except KeyError:
				pass
		return provinces
		logger.info('province_information successfully crawled.')
		return provinces
	else:
		return 0


def insert_province():
	cursor = None
	conn = None
	try:
		li = fetch_crawler()  # 1是当日详细数据
		conn, cursor = get_conn()
		print(f"{time.asctime()}开始更新省份数据")
		sql = "insert into province (provinceName,nowConfirm,confirm,suspect,heal,dead,highRisk,midRisk) values(%s,%s,%s,%s,%s,%s,%s,%s)"
		for p in li:
			cursor.execute(sql, (
			p['provinceName'], p['currentConfirmedCount'], p['confirmedCount'], p['suspectedCount'], p['curedCount'], p['deadCount'], p['highDangerCount'],
			p['midDangerCount']))
		conn.commit()  # 提交事务保存数据
		print(f"{time.asctime()}数据更新完毕")
	except:
		traceback.print_exc()
	finally:
		cursor.close()
		conn.close()
if __name__ =="__main__":
	insert_province()
