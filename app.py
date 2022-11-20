from flask import Flask
from flask import render_template
from flask import jsonify
from jieba.analyse import extract_tags
import string

import spider.utils
from spider import utils

app = Flask(__name__)


# 首页
@app.route('/')
def default():
	return render_template('index.html')
@app.route('/index')
def index():
	return render_template('index.html')
#数据分析
@app.route('/analysis')
def analysis():
	return render_template('data_analysis.html')


# 疫情数据可视化大屏部分
@app.route('/main')
def main():
	return render_template('main.html')


# 累计疫情数据 累计确诊 累计疑似 累计死亡 累计治愈
@app.route('/c1')
def get_c1_data():
	data = spider.utils.get_c1_data()
	return jsonify({"confirm": data[0],"suspect":data[1],"heal": data[2], "dead": data[3]})


# 返回各省数据
@app.route('/c2')
def get_c2_data():
	#data = spider.utils.get_c2_data()
	res = []
	for tup in spider.utils.get_c2_data():
		res.append({"name": tup[0], "value": int(tup[1])})
	return jsonify({"data": res})


# 累计数据
@app.route("/l1")
def get_l1_data():
	data = spider.utils.get_l1_data()
	day, confirm, confirm_add, heal, dead = [], [], [], [], []
	for a, b, c, d, e in data:  # 很多卫健委网站前7天都是没有数据的，所以把前7天砍掉了
		day.append(a.strftime("%m-%d"))  # a是datatime类型
		confirm.append(b)
		confirm_add.append(c)
		heal.append(d)
		dead.append(e)
	return jsonify({"day": day, "confirm": confirm, "confirm_add": confirm_add, "heal": heal, "dead": dead})


# 现有确诊及 无症状
@app.route("/l2")
def get_l2_data():
	data = spider.utils.get_l2_data()
	day, nowConfirm, noInfectH5 = [], [], []
	for a, b, c in data:
		day.append(a.strftime("%m-%d"))  # a是datatime类型
		nowConfirm.append(b)
		noInfectH5.append(c)
	return jsonify({"day": day, "nowConfirm": nowConfirm, "noInfectH5": noInfectH5})


# 现有确诊城市地区top5
@app.route("/r1")
def get_r1_data():
	data = spider.utils.get_r1_data()
	city = []
	confirm = []
	for k, v in data:
		city.append(k)
		confirm.append(int(v))
	return jsonify({"city": city, "confirm": confirm})


# 词云图
@app.route("/r2")
def get_r2_data():
	data = spider.utils.get_r2_data()
	d = []
	for i in data:
		k = i[0].rstrip(string.digits)  # 移除热搜数字
		v = i[0][len(k):]  # 获取热搜数字
		ks = extract_tags(k)  # 使用jieba 提取关键字
		for j in ks:
			if not j.isdigit():
				d.append({"name": j, "value": v})
	return jsonify({"kws": d})


# 时间
@app.route('/time')
def gettime():
	return spider.utils.get_time()


# ajax
@app.route('/ajax', methods=["get", "post"])
def ajax():
	return '10000'


if __name__ == '__main__':
	app.run()
