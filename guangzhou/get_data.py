import re
import requests
import json
import time
import pymysql
from selenium import webdriver
from selenium.webdriver import Edge, EdgeOptions
import traceback
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from spider import utils
from spider.utils import get_conn, query

url_element = [r'http://wjw.gz.gov.cn/ztzl/xxfyyqfk/yqtb/index', '.html']


# 获取疫情通告页面相应的url
def get_base_url(page=1):
	if page == 1:
		base_url = url_element[0] + url_element[1]
	else:
		base_url = url_element[0] + '_' + str(page) + url_element[1]
	return base_url


# 新增本土确诊 新增本土无症状 新增境外输入确诊 新增境外输入无症状
#----------------------发布时间10.23及之后-----------------------------
p1_add_pattern_list = {'confirm_add_local_pattern': '新增本土确诊病例.*?例', 'noInfect_add_local_pattern': '新增本土无症状感染者.*?例',
                       'confirm_add_imported_pattern': '新增境外输入确诊病例.*?例',
                       'noInfect_add_imported_pattern': '境外输入无症状感染者.*?例'}
#-----------------------发布时间10.23之前-------------------------------------------
p1_add_pattern2_list = {'confirm_add_local_pattern': '\d*例本土确诊病例', 'noInfect_add_local_pattern': '\d*例本土无症状感染者',
                       'confirm_add_imported_pattern': '新增境外输入确诊病例.*?例',
                       'noInfect_add_imported_pattern': '境外输入无症状感染者.*?例'}
p1_add_element_list = ['confirm_add_local', 'noInfect_add_local', 'confirm_add_imported', 'noInfect_add_imported']
# 累计所有阳性感染者=本土+境外输入   总共确诊 总共无症状 本土(确诊+无症状) 境外(确诊+无症状) 在院治疗  在院观察
p2_history_pattern_list = {'confirm_all_pattern': '新冠肺炎阳性感染者.*?例', 'confirm_pattern': '确诊病例.*?例',
                           'noInfect_pattern': '无症状感染者.*?例', 'local_pattern': '本土.?例', 'imported_pattern': '境外输入.?例',
                           'treatment_hospital_pattern': '治疗.*?例', 'observation_hospital_pattern': '观察.*?例'}

p2_history_list = ['confirm_all', 'confirm', 'confirm_local', 'noInfect', 'noInfect_local', 'confirm_imported',
                   'noInfect_imported', 'treatment_hospital', 'observation_hospital']

# 获取累计数据
def get_oneday_history_data(url):
	browser = webdriver.Edge()
	browser.get(url)
	# 累计数据  有的在第一段,有的在第2段
	p2 = browser.find_elements(By.CSS_SELECTOR, '.zoom_box > p:nth-child(2)')[0].text
	history_data = {}  # 累计数据
	# --------------------------累计数据---------------------------------
	# 累计阳性=确诊+无症状
	confirm_all = "".join(
		list(filter(str.isdigit, re.search(p2_history_pattern_list['confirm_all_pattern'], p2).group())))
	# 确诊
	confirm = "".join(list(filter(str.isdigit, re.search(p2_history_pattern_list['confirm_pattern'], p2).group())))
	# 在院治疗
	treatment_hospital = "".join(
		list(filter(str.isdigit, re.search(p2_history_pattern_list['treatment_hospital_pattern'], p2).group())))
	# 在院观察
	observation_hospital = "".join(
		list(filter(str.isdigit, re.search(p2_history_pattern_list['observation_hospital_pattern'], p2).group())))
	# 无症状
	noInfect = "".join(list(filter(str.isdigit, re.search(p2_history_pattern_list['noInfect_pattern'], p2).group())))
	# ---------------------------------本土 境外---------------------------------
	local = re.findall('本土.*?例', p2)
	imported = re.findall('境外输入.*?例', p2)
	# 本土确诊
	confirm_local = "".join(list(filter(str.isdigit, local[0])))
	# 本土无症状
	noInfect_local = "".join(list(filter(str.isdigit, local[1])))
	# 境外输入确诊
	confirm_imported = "".join(list(filter(str.isdigit, imported[0])))
	# 境外输入无症状
	noInfect_imported = "".join(list(filter(str.isdigit, imported[1])))
	history_data = {'confirm_all': int(confirm_all), 'confirm': int(confirm), 'confirm_imported': int(confirm_imported),
	                'confirm_local': int(confirm_local), 'treatment_hospital': int(treatment_hospital),
	                'noInfect': int(noInfect), 'noInfect_imported': int(noInfect_imported),
	                'noInfect_local': int(noInfect_local),
	                'observation_hospital': int(observation_hospital)
	                }
	return history_data


# 将累计数据插入数据库
def insert_gz_history_p2():
	cursor = None
	conn = None
	# 获取时间和url
	href_dt_list = get_href_dt()
	try:
		conn, cursor = get_conn()
		print(f"{time.asctime()}开始更新广州疫情数据")
		for item in href_dt_list:
			dt = item['dt']  # 时间数据
			url = item['url']  # 网页url
			history = get_oneday_history_data(url)
			sql_history = "insert into gz_p2_history (" \
			              "dt,confirm_all,confirm,confirm_imported," \
			              "confirm_local,treatment_hospital,noInfect," \
			              "noInfect_imported,noInfect_local,observation_hospital)" \
			              "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			cursor.execute(sql_history, (dt, history['confirm_all'], history['confirm'], history['confirm_imported'],
			                             history['confirm_local'], history['treatment_hospital'], history['noInfect'],
			                             history['noInfect_imported'], history['noInfect_local'],
			                             history['observation_hospital']))
			conn.commit()  # 提交事务保存数据
			print(f"{item['dt']}数据更新完毕")
	except:
		traceback.print_exc()
	finally:
		cursor.close()
		conn.close()


# 获取新增数据
def get_oneday_add_data(url):
	browser = webdriver.Edge()
	browser.get(url)
	# 新增数据
	p1 = browser.find_elements(By.CSS_SELECTOR, '.zoom_box > p:nth-child(1)')[0].text
	add_data = {}  # 新增数据
	# --------------------------新增数据---------------------------------
	# 本土新增确诊
	confirm_add_local = "".join(
		list(filter(str.isdigit, re.search(p1_add_pattern2_list['confirm_add_local_pattern'], p1).group())))
	# 本土新增无症状
	noInfect_add_local = "".join(
		list(filter(str.isdigit, re.search(p1_add_pattern2_list['noInfect_add_local_pattern'], p1).group())))
	add_data = {'confirm_add_local': int(confirm_add_local), 'noInfect_add_local': int(noInfect_add_local)}
	return add_data


# 将新增数据插入数据库
def insert_gz_add_p1():
	cursor = None
	conn = None
	# 获取时间和url
	href_dt_list = get_href_dt()
	try:
		conn, cursor = get_conn()
		print(f"{time.asctime()}开始更新广州疫情数据")
		#做到36
		for item in href_dt_list[37:43]:
			dt = item['dt']  # 时间数据
			url = item['url']  # 网页url
			add = get_oneday_add_data(url)
			sql_add = "insert into gz_p1_add (dt,confirm_add_local,noInfect_add_local" \
			          ") values (%s,%s,%s)"
			cursor.execute(sql_add, (dt, add['confirm_add_local'], add['noInfect_add_local']))

			conn.commit()  # 提交事务保存数据
			print(f"{item['dt']}数据更新完毕")
	except:
		traceback.print_exc()
	finally:
		cursor.close()
		conn.close()


# 获取疫情通报的链接 标题 发布时间
def get_href_list(base_url):
	href_list = []
	option = EdgeOptions()  # 创建谷歌浏览器实例
	browser = webdriver.Edge()
	browser.implicitly_wait(3)
	browser.get(base_url)
	li_list = browser.find_elements(By.CSS_SELECTOR, '.cont_list > ul:nth-child(1) > li')
	length = len(li_list)
	for index in range(2, length + 1):
		href = {}
		a_path = f'.cont_list > ul:nth-child(1) > li:nth-child({index}) > div:nth-child(1) > a:nth-child(1)'
		time_path = f'.cont_list > ul:nth-child(1) > li:nth-child({index}) > div:nth-child(2)'
		a = browser.find_element(By.CSS_SELECTOR, a_path)
		dt = browser.find_element(By.CSS_SELECTOR, time_path).text
		title = a.get_attribute('title')
		url = a.get_attribute('href')
		href = {'dt': dt, 'title': title, 'url': url}
		href_list.append(href)
	browser.close()
	return href_list


# 将上述信息存储到数据库
def update_yqtb_url(page=1):
	conn, cursor = get_conn()
	try:
		base_url = get_base_url(page)
		href_list = get_href_list(base_url)
		print(f"{time.asctime()}开始更新广州疫情通报数据")
		sql = f"insert into gz_yqtb_href (dt,title,href) values(%s,%s,%s)"
		for href in href_list:
			cursor.execute(sql, (href['dt'], href['title'], href['url']))
		conn.commit()  # 提交事务保存数据
		print(f"{time.asctime()}数据更新完毕")
	except:
		traceback.print_exc()
	finally:
		cursor.close()
		conn.close()


# 从链接表中获取url列表
def get_href_data():
	url_list = []
	sql = "select href from gz_yqtb_href"
	res = query(sql)
	for href in res:
		url = href[0]
		url_list.append(url)
	return url_list


# 从链接table获取发布时间和url
def get_href_dt():
	href_dt_list = []
	sql = "select dt,href from gz_yqtb_href"
	res = query(sql)
	for item in res:
		href_dt = {}
		dt = item[0]
		url = item[1]
		href_dt = {'dt': dt, 'url': url}
		href_dt_list.append(href_dt)
	return href_dt_list


# 11月8日发布的数据有问题,数据日期为11月7日[6]    10-29有问题  index=16
def dbtest():
	cursor = None
	conn = None
	# 获取时间和url
	href_dt_list = get_href_dt()
	try:
		conn, cursor = get_conn()
		print(f"{time.asctime()}开始更新广州疫情数据")
		for item in href_dt_list[66:]:
			dt = item['dt']  # 时间数据
			url = item['url']  # 网页url
			history = get_oneday_history_data(url)
			# sql_add = "insert into gz_p1_add (dt,confirm_add_local,noInfect_add_local," \
			#           "confirm_add_imported,noInfect_add_imported) values (%s,%s,%s,%s,%s)"
			sql_history = "insert into gz_p2_history (" \
			              "dt,confirm_all,confirm,confirm_imported," \
			              "confirm_local,treatment_hospital,noInfect," \
			              "noInfect_imported,noInfect_local,observation_hospital)" \
			              "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			# cursor.execute(sql_add, (dt, add['confirm_add_local'], add['noInfect_add_local'],
			#                          add['confirm_add_imported'], add['noInfect_add_imported']))
			cursor.execute(sql_history, (dt, history['confirm_all'], history['confirm'], history['confirm_imported'],
			                             history['confirm_local'], history['treatment_hospital'], history['noInfect'],
			                             history['noInfect_imported'], history['noInfect_local'],
			                             history['observation_hospital']))
			conn.commit()  # 提交事务保存数据
			print(f"{item['dt']}数据更新完毕")


	except:
		traceback.print_exc()
	finally:
		cursor.close()
		conn.close()


if __name__ == "__main__":
	# 爬到第4页,8.30-11.14
	# for page in range(2,5):
	# href_list = get_href_data()
	# add, history = get_oneday_data(href_list[5])
	# print(add)
	# print(history)
	# href_dt_list=get_href_dt()
	# for item in href_dt_list[:2]:
	# 	print(item['dt'])
	# 	print(item['url'])
	insert_gz_add_p1()

