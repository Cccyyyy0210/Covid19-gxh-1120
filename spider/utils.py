import time
import pymysql


def get_time():
	time_str = time.strftime("%Y{}%m{}%d{} %X")
	return time_str.format("年", "月", "日")  # 用format来识别中文


# return: 连接数据库，返回游标
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


def query(sql, *args):
	conn, cursor = get_conn()
	cursor.execute(sql, args)
	res = cursor.fetchall()
	close_conn(conn, cursor)
	return res


def get_c1_data():
	"""
	:return: 返回前端页面div id=c1 的数据
	"""
	# 因为会更新多次数据，取timestamp最新的那组数据
	sql = "select sum(confirm),sum(suspect),sum(heal),sum(dead) from province"
	res = query(sql)
	return res[0]


# 返回各省数据
def get_c2_data():
	# 因为会更新多次数据，取timestamp最新的那组数据
	sql = "select provinceName,nowConfirm from province"
	res = query(sql)
	return res


# 历史数据:累计确诊 现有确诊 累计治愈 累计死亡
def get_l1_data():
	sql = "select ds,confirm,nowConfirm,heal,dead from history"
	res = query(sql)
	return res


# 现有确诊 现有无症状
def get_l2_data():
	sql = "select ds,nowConfirm,noInfectH5 from history"
	res = query(sql)
	return res


# 返回城市确诊人数前5名
def get_r1_data():
	sql = 'SELECT city,confirm FROM details WHERE city NOT IN ("地区待确认","境外输入") ORDER BY confirm DESC LIMIT 5'
	res = query(sql)
	return res


# 返回最近的20条热搜
def get_r2_data():
	sql = 'select content from yhfc order by id desc limit 20'
	res = query(sql)
	return res

if __name__ == "__main__":
 	print(get_c2_data())
