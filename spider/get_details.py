#爬取新冠疫情实时数据1109
import random
import traceback
import pymysql
import requests
import json
import time

from userAgent import user_agent_list


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
def get_details():
	url1 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
	headers = {
		'user-agent': random.choice(user_agent_list)
	}
	r1 = requests.get(url1, headers)

	# json字符串转字典
	res1 = json.loads(r1.text)
	data1 = res1["data"]
	mudanjiang = r',{"name":"牡丹江","adcode":"231000","date":"2022/11/09","today":{"confirm":0,"confirmCuts":0,"isUpdated":true,"wzz_add":"0","local_confirm_add":0},"total":'
	data1 = data1.replace(mudanjiang, r']}]}]}')
	data_all1 = json.loads(data1)
	# 当日详细数据
	details = []
	update_time = data_all1["lastUpdateTime"]
	data_country = data_all1["areaTree"]  # list 25个国家
	data_province = data_country[0]["children"]  # 中国各省
	for pro_infos in data_province:
		province = pro_infos["name"]  # 省名
		for city_infos in pro_infos["children"]:
			city = city_infos["name"]
			confirm = city_infos["total"]["confirm"]
			confirm_add = city_infos["today"]["confirm"]
			heal = city_infos["total"]["heal"]
			dead = city_infos["total"]["dead"]
			details.append([update_time, province, city, confirm, confirm_add, heal, dead])
	return details
# 插入实时疫情数据信息details
def update_details():
	cursor = None
	conn = None
	try:
		li = get_details() # 1是当日详细数据
		conn, cursor = get_conn()
		sql = "insert into details(update_time,province,city,confirm,confirm_add,heal,dead) values(%s,%s,%s,%s,%s,%s,%s)"
		sql_query = "select %s=(select update_time from details order by id desc limit 1)"  # 对比当前最大时间戳
		# 对比当前最大时间戳
		cursor.execute(sql_query, li[0][0])
		if not cursor.fetchone()[0]:
			print(f"{time.asctime()}开始更新数据")
			for item in li:
				cursor.execute(sql, item)
			conn.commit()
			print(f"{time.asctime()}更新到最新数据")
		else:
			print(f"{time.asctime()}已是最新数据！")
	except:
		traceback.print_exc()
	finally:
		cursor.close()
		conn.close()
if __name__ =="__main__":
	update_details()