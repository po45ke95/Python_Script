# -*- coding: utf-8 -*-
from t1.items import nbaItem
import scrapy
import time

class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['www.ptt.cc/bbs/NBA']
    start_urls = ['https://www.ptt.cc/bbs/NBA/M.1603265110.A.F66.html']

    def parse(self, response):
        items = nbaItem()
        items['author'] = response.xpath('//*[@id="main-content"]/div[1]/span[2]/text()').extract_first()
        items['title'] = response.xpath('//*[@id="main-content"]/div[3]/span[2]/text()').extract_first()
        items['time'] = response.xpath('//*[@id="main-content"]/div[4]/span[2]/text()').extract_first()
        items['text'] = response.xpath('//*[@id="main-content"]/a/text()').extract_first()
        yield items
