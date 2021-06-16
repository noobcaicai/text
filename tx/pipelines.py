# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

import requests
import scrapy
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from copy import deepcopy
from scrapy.pipelines.images import ImagesPipeline
class TXPipeline:

    def process_item(self, item, spider):
        # print(item['images_url'])
        return item
class TxdoloadPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['images_url'], meta={'item':deepcopy(item)})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        # 设置图片的路径为  类型名称/url地址
        # 这是一个图片的url: http://pics.sc.chinaz.com/Files/pic/icons128/7065/z1.png
        # 这句代码的意思是先取出图片的url，[0]表示从列表转成字符串
        # split分割再取最后一个值，这样写是让图片名字看起来更好看一点
        image_name =item['tiltet']+'.jpg'
        return image_name