# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from lxml import etree
from ziroomuniversal.items import ZiroomuniversalItem


class ZiroomSpider(CrawlSpider):
	name = 'ziroom'
	allowed_domains = ['hz.ziroom.com']
	start_urls = ['http://hz.ziroom.com/z/p%s/' %n for n in range(1,51)]

	rules = (
		Rule(LinkExtractor(allow='\/\/hz.ziroom.com\/x\/\d+\.html', restrict_xpaths='//div[@class="Z_list-box"]'), callback='parse_item'),
	)

	def parse_item(self, response):
		item = ZiroomuniversalItem()
		#item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
		#item['name'] = response.xpath('//div[@id="name"]').get()
		#item['description'] = response.xpath('//div[@id="description"]').get()
		item['url'] = response.url
		item['title'] = response.xpath('//h1[@class="Z_name"]/text()').extract_first()
		item['rooms'] = response.xpath('//div[@class="Z_home_b clearfix"]/dl[3]/dd/text()').extract_first()
		item['direction'] = response.xpath('//div[@class="Z_home_b clearfix"]/dl[2]/dd/text()').extract_first()

		space = response.xpath('//div[@class="Z_home_b clearfix"]/dl[1]/dd/text()').extract_first()
		item['space_sqm'] = re.match('(.*)㎡', space).group(1)

		price = response.xpath('//div[@class="Z_price"]/i[1]/@style').extract_first()
		item['price_img_url'] = 'http:' + re.search('url\((.*)\)', price, re.S).group(1)

		background_position_list = []
		background_positions = response.xpath('//div[@class="Z_price"]/i')
		for each in background_positions:
			style = each.xpath('./@style').extract_first()
			background_position = re.search('background-position:(.*)px', style, re.S).group(1)
			background_position_list.append(background_position)
		item['background_position_list'] = background_position_list

		address = response.xpath('//div[@class="Z_container Z_bread mt60"]/a[2]/text()').extract_first()
		try:
			item['district'] = re.match('(.*区)(.*)', address).group(1)
			item['neighborhood'] = re.match('(.*区)(.*)', address).group(2)
			yield item
		except AttributeError:
			district = neighborhood = address
			yield item