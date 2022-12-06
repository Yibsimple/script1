import json
import scrapy
from ..items import DouyuItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['douyu.com']
    url = 'https://m.douyu.com/api/room/list?page={}&type=yz'
    page = 1
    start_urls = [url.format(page)]

    def parse(self, response):
        datas = json.loads(response.text)['data']['list']
        for data in datas:
            item = DouyuItem()
            item['nickname'] = data['nickname']
            item['verticalSrc'] = data['verticalSrc']

            yield item

        self.page += 1

        yield scrapy.Request(self.url.format(self.page), callback=self.parse)
