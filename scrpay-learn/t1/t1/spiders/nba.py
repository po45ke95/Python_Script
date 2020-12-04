# -*- coding: utf-8 -*-
from t1.items import nbaItem
import scrapy
import time

class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['www.ptt.cc/bbs/NBA']
    start_urls = ['https://www.ptt.cc/bbs/NBA/index.html']

    def parse(self, response):
        items = nbaItem()
        items['author'] = response.xpath('//*[@id="main-container"]/div[2]/div[3]/div[3]/div[1]/text()').extract_first()
        items['title'] = response.xpath('//*[@id="main-container"]/div[2]/div[3]/div[2]/a/text()').extract_first()
        items['time'] = response.xpath('//*[@id="main-container"]/div[2]/div[3]/div[3]/div[3]/text()').extract_first()
        items['num'] = response.xpath('//*[@id="main-container"]/div[2]/div[3]/div[1]/span/text()').extract_first()
        yield items
