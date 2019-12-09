# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ZiroomuniversalItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    rooms = Field()
    space_sqm = Field()
    direction = Field()
    district = Field()
    neighborhood = Field()
    url = Field()
    monthly_rent_by_season = Field()
    monthly_rent_per_sqm_by_season = Field()

    price_img_url = Field()
    background_position_list = Field()