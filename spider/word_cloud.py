# coding=utf-8
import jieba
from Tools.scripts.objgraph import ignore
from matplotlib import pyplot
import numpy
from wordcloud import WordCloud
from PIL import Image
import pymysql

import spider.utils
from spider import utils
tableList = ['fkdt', 'zhengcwj', 'yhfc']
def getData(table,limitation='where id between 1 and 50'):
	conn,cursor=spider.utils.get_conn()
	sql=f'select content from {table} {limitation}'
	data=spider.utils.query(sql)
	return data
def wordCloud(data,imgPath):
	text=""
	for item in data:
		text=text+item[0]
	cut=jieba.cut(text)
	string=' '.join(cut)
	# 制作词云图片
	img = Image.open(imgPath)  # 遮罩图片
	img_array = numpy.array(img)
	wc = WordCloud(
		background_color='#4b0082',
		mask=img_array,
		font_path="STXINWEI.TTF"
	)
	wc.generate_from_text(string)
	# 绘制图片
	pyplot.subplots(figsize=(20, 16))
	pyplot.imshow(wc)
	pyplot.axis("off")
	pyplot.show()

if __name__ =="__main__":
	data=getData(tableList[2])
	imgPath=r'../static/img/covid3.jpg'
	wordCloud(data,imgPath)
