import os
import time

import requests
import scrapy
import json
from tx.items import TxItem
from copy import deepcopy

url=[]
class Tx1Spider(scrapy.Spider):
    name = 'tx1'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js']

    def parse(self, response):
        rs = json.loads(response.text)
        # print(rs)
        data1=rs['hero']
        item = TxItem()
        for i in data1:
            item['heroId']=i['heroId']
            item['name']=i['name']
            # url.append(item['heroId'])

            next_url=f"https://game.gtimg.cn/images/lol/act/img/js/hero/{item['heroId']}.js"
            # print(next_url)

            yield scrapy.Request(
                next_url,
                callback=self.parse_dei,
                meta={'item':deepcopy(item)}
            )

    def parse_dei(self,response):
        item=response.meta['item']
        rs1 =json.loads(response.text)
        # print(rs1)
        img1=rs1['skins']
        for i in img1:
            # print(i['mainImg'])
            if i['mainImg']=='':
                continue
            else:
                item['images_url']=(i['mainImg'])

                # print(item)
                yield item


