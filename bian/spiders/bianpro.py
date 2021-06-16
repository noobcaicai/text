import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BianproSpider(CrawlSpider):
    name = 'bianpro'
    allowed_domains = ['netbian.com']
    start_urls = ['https://pic.netbian.com/']

    # def start_requests(self):
    #     cookies = '__yjs_duid=1_0647d691aefa811bb7d235ae26dd248d1620311062395; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1620311065,1622514286; yjs_js_security_passport=36a8d55454b7965f625ed625588cb9b5e866ccc9_1622514454_js; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1622516161'
    #     cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split(';')}
    #     yield scrapy.Request(
    #         'https://pic.netbian.com/',
    #         callback=self.parse_item,
    #         cookies=cookies
    #     )
    rules = (
        Rule(LinkExtractor(allow=r'/index_\d+.html'), callback='parse_item',follow=True),
    )


    def parse_item(self, response):
        item = {}
        li_list=response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            li_url='https://pic.netbian.com'+li.xpath('./a/@href').extract_first()
            yield scrapy.Request(
                li_url,
                callback=self.parse_url,
                meta={'item':item}
            )
    def parse_url(self, response):
        item=response.meta['item']
        item['img']='https://pic.netbian.com'+response.xpath('//*[@id="img"]/img/@src').extract_first()
        item['name']=response.xpath('//*[@id="img"]/img/@alt').extract_first()
        yield item

