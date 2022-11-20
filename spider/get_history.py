
import random
import traceback

import requests
import json
import time

from userAgent import user_agent_list
from utils import get_conn


def get_history():
	url2 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
	headers = {
		'user-agent': random.choice(user_agent_list)
	}
	r2 = requests.get(url2, headers)
	res2 = json.loads(r2.text)
	data_all2 = json.loads(res2["data"])
	# print(data_all2)

	history = {}
	for i in data_all2["chinaDayList"]:
		ds = "2022." + i["date"]
		tup = time.strptime(ds, "%Y.%m.%d")
		ds = time.strftime("%Y-%m-%d", tup)
		confirm = i["confirm"]
		heal = i["heal"]
		dead = i["dead"]
		nowConfirm = i["nowConfirm"]
		noInfectH5 = i["noInfectH5"]
		nowSevere = i["nowSevere"]
		localConfirm = i["localConfirm"]
		importedCase = i["importedCase"]
		deadRate = i["deadRate"]
		healRate = i["healRate"]
		history[ds] = {"confirm": confirm, "heal": heal, "dead": dead, "nowConfirm": nowConfirm,
		               "noInfectH5": noInfectH5, "nowSevere": nowSevere, "localConfirm": localConfirm,
		               "importedCase": importedCase, "deadRate": deadRate, "healRate": healRate}
	return history



def insert_history():
	conn, cursor = get_conn()
	try:
		dic = get_history()
		print(f"{time.asctime()}开始插入历史数据")
		# conn, cursor = get_conn()
		sql = "insert into history values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		for k, v in dic.items():
			cursor.execute(sql, [k, v.get("confirm"),v.get("heal"),v.get("dead"),v.get("nowConfirm"),v.get("noInfectH5"),v.get("nowSevere"),v.get("localConfirm"), v.get("importedCase"), v.get("deadRate"),v.get("healRate")])
		conn.commit()
		print(f"{time.asctime()}插入历史数据完毕")
	except:
		traceback.print_exc()
	finally:
		cursor.close()
		conn.close()



def update_history():
	conn, cursor = get_conn()
	try:
		dic = get_history()
		print(f"{time.asctime()}开始更新历史数据")
		# conn, cursor = get_conn()
		sql = "insert into history values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		sql_query = "select confirm from history where ds=%s"
		for k, v in dic.items():
			if not cursor.execute(sql_query, k):
				cursor.execute(sql, [k, v.get("confirm"),v.get("heal"),v.get("dead"),
			                     v.get("nowConfirm"),v.get("noInfectH5"),v.get("nowSevere"),
			                     v.get("localConfirm"), v.get("importedCase"), v.get("deadRate"),v.get("healRate")])
		conn.commit()
		print(f"{time.asctime()}历史数据更新完毕")
	except:
		traceback.print_exc()
	finally:
		cursor.close()
		conn.close()


# if __name__ == "__main__":

