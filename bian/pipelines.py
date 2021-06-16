# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline

class BianPipeline:
    def process_item(self, item, spider):
        return item
class bianimgPipeeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img'])
    def file_path(self, request, response=None, info=None, *, item=None):
        file_name=item['name']+'.jpg'
        return file_name