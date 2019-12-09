# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
import re

class ImagePipeline(ImagesPipeline):
	def get_media_requests(self, item, info):
		yield Request(item['price_img_url'])

	def file_path(self, request, response=None, info=None):
		url = request.url
		file_path = url.split('/')[-1]
		return file_path

	def item_completed(self, results, item, info):
		img_paths = [data['path'] for ok, data in results if ok]
		if not img_paths:
			raise DropItem('Failed to Get price for item' + item['url'])
		return item

class GetPricesPipeline():
	def __init__(self, img_number_map, digit_px_list):
		self.img_number_map = img_number_map
		self.digit_px_list = digit_px_list

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			img_number_map = crawler.settings.get('IMG_NUMBER_MAP'),
			digit_px_list = crawler.settings.get('DIGIT_PX_LIST')
			)

	def open_spider(self, spider):
		pass

	def close_spider(self, spider):
		pass

	def process_item(self, item, spider):
		price_img_url = item['price_img_url']
		image = re.search('price\/(.*\.png)', price_img_url, re.S).group(1)
		number = self.img_number_map.get(image)
		background_position_list = item['background_position_list']
		digit_list = []
		for each in background_position_list:
			index = self.digit_px_list.index(each)
			digit = number[index]
			digit_list.append(digit)
		price = ''.join(digit_list)
		if price:
			item['monthly_rent_by_season'] = price
			
			space_sqm = item['space_sqm']
			monthly_rent_per_sqm_by_season = float('%.2f' %(float(price)/float(space_sqm)))
			item['monthly_rent_per_sqm_by_season'] = monthly_rent_per_sqm_by_season
		return item

class MySQLPipeline(object):
	def __init__(self, host, user, password, database, port, table):
		self.host = host
		self.user =user
		self.password = password
		self.database = database
		self.port = port
		self.table = table

	@classmethod	
	def from_crawler(cls, crawler):
		return cls(
			host = crawler.settings.get('MYSQL_HOST'),
			user = crawler.settings.get('MYSQL_USER'),
			password = crawler.settings.get('MYSQL_PASSWORD'),
			database = crawler.settings.get('MYSQL_DATEBASE'),
			port = crawler.settings.get('MYSQL_PORT'),
			table = crawler.settings.get('MYSQL_TABLE')
		)

	def open_spider(self, spider):
		self.db = pymysql.connect(self.host, self.user, self.password, self.database, self.port)
		self.cursor = self.db.cursor()

	def close_spider(self, spider):
		self.db.close()

	def process_item(self, item, spider):
		data = dict(item)
		data.pop('price_img_url')
		data.pop('background_position_list')
		keys = ','.join(data.keys())
		values = ','.join(['%s'] * len(data))
		sql = 'insert into %s (%s) values (%s)' %(self.table, keys, values)
		self.cursor.execute(sql, tuple(data.values()))
		self.db.commit()
		return item