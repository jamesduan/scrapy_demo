# -*- coding: utf-8 -*-
import scrapy

from crawler.dmoz.dmoz.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoztools.net']
    start_urls = ['http://dmoztools.net/Computers/Programming/Languages/Python/Books/']

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        print "########################start########################"
        print
        for item in response.xpath('//*[starts-with(@class,"site-item ")]/div[@class="title-and-desc"]'):
            dmoz = DmozItem()
            dmoz['link'] = item.xpath('a/@href').extract()[0]
            dmoz['title'] = item.xpath('a/div/text()').extract()[0]
            yield dmoz
        print
        print "########################end########################"
